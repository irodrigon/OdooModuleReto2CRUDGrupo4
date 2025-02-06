from odoo import api,fields,models
from odoo.exceptions import ValidationError
from datetime import date

class CreditCard(models.Model):
    _name = "grupo4.creditcard"
    _inherit="grupo4.product"
    _description = "saves credit cards"

    #simple fields
    creditCardNumber = fields.Char(string="Credit card number")
    expirationDate = fields.Date(string="Expiration date")
    cvv = fields.Char(string="CVV")
    pin =fields.Char(string="PIN")

    days_until_expiration = fields.Integer(string='Days Until Expiration', compute='_compute_days_until_expiration')

    @api.depends('expirationDate')
    def _compute_days_until_expiration(self):
        for record in self:
            if record.expirationDate:
                expirationDate = fields.Date.from_string(record.expirationDate)
                today = fields.Date.from_string(fields.Date.today())
                record.days_until_expiration = (expirationDate - today).days
            else:
                record.days_until_expiration = 0

    @api.constrains('creditCardNumber')
    def _check_credit_card_number(self):
        for record in self:
            if not record.creditCardNumber.isdigit() or len(record.creditCardNumber) != 16:
                raise ValidationError("Credit card number must be exactly 16 digits long")

    @api.onchange('expirationDate')
    def _check_expiration_date(self):
        if self.expirationDate and self.expirationDate < date.today():
            return {
                "warning": {
                    "title": "Invalid Date",
                    "message": "The expiration Date cannot be in the past.",
                }
            }



    #relational fields
    accountNumber = fields.Many2one(comodel_name="grupo4.account", string="Account", required=True, ondelete="cascade")
    creditCardMovement = fields.One2many(comodel_name="grupo4.movements", inverse_name="creditCard", string="Movements", required=True)

    customer_product_ids = fields.Many2many(
        'grupo4.product',
        'product_creditcard_rel', 'creditcard_id', 'product_id',
        string='Customer Products'
    )