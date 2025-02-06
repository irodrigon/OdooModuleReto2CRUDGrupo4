from odoo import models, fields, api
from datetime import date, timedelta


class Loan(models.Model):
    _name = 'grupo4.loan'
    _description = 'Loan Model'

    loan_id = fields.Char(string='Loan ID')
    creation_date = fields.Date(string='Creation Date', default=fields.Date.today)
    interest = fields.Float(string='Interest (%)', required=True)
    start_date = fields.Date(string='Start Date', required=True)
    end_date = fields.Date(string='End Date', required=True)
    amount = fields.Float(string='Total Amount', required=True)
    period = fields.Integer(string='Period (Days)', required=True, help='Each how many days payment is due')
    remaining_amount = fields.Float(string='Remaining Amount', compute='_compute_remaining_amount', store=True)

    @api.depends('start_date', 'end_date', 'interest', 'amount', 'period')
    def _compute_remaining_amount(self):
        today = date.today()
        for loan in self:
            if not loan.start_date or not loan.end_date or loan.amount <= 0 or loan.period <= 0:
                loan.remaining_amount = loan.amount
                continue

            # Calculate total amount to pay with interest
            total_days = (loan.end_date - loan.start_date).days
            num_payments = total_days // loan.period
            total_to_pay = loan.amount * (1 + (loan.interest / 100))
            payment_per_period = total_to_pay / num_payments if num_payments > 0 else total_to_pay

            # Calculate how many payments should have been made
            elapsed_days = (today - loan.start_date).days if today >= loan.start_date else 0
            payments_made = elapsed_days // loan.period

            # Calculate remaining amount
            loan.remaining_amount = max(0, total_to_pay - (payments_made * payment_per_period))

    @api.constrains('amount')
    def _check_amount(self):
        for loan in self:
            if loan.amount <= 0:
                raise models.ValidationError("The total amount must be a positive number.")


@api.model
def create(self, vals):
    """Sobrecarga el método create para asignar la fecha actual si no se proporciona una fecha."""
    if 'start_date' not in vals or not vals.get('start_date'):
        vals['start_date'] = date.today()
    if 'end_date' not in vals or not vals.get('end_date'):
        vals['end_date'] = date.today()
    return super(Loan, self).create(vals)


@api.model
def copy(self, default=None):
    """Sobrecarga copy para agregar '(1)' al final del loan_id al duplicar"""
    default = dict(default or {})
    if self.loan_id:
        default['loan_id'] = f"{self.loan_id} (1)"
    return super(Loan, self).copy(default)