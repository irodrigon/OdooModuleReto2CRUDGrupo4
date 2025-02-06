from odoo import api, fields, models
from datetime import date
import re
from odoo.exceptions import ValidationError


class Account(models.Model):
    _name = "grupo4.account"
    _inherit="grupo4.product"
    _description = "guarda las cuentas de los usuarios"

    # campos simples
    balance = fields.Float(string="The ammount of money in the account")
    accountNumber = fields.Char(string="The accounts number")

    # campos calculados
    total_days_open =fields.Integer(string="Days Since Open", compute="_totalDays", store=True)

    @api.onchange('creationDate')
    def _check_creation_date(self):
        if self.creationDate and self.creationDate > date.today():
            return {
                "warning": {
                    "title": "Invalid Date",
                    "message": "The Creation Date cannot be in the future.",
                }
            }
    @api.depends("creationDate")
    def _totalDays(self):
        for record in self:
            if record.creationDate:
                record.total_days_open = (date.today() - record.creationDate).days
            else:
                record.total_days_open = 0
    #Restricciones


    @api.constrains("accountNumber")
    def _check_account_number_format(self):
        pattern = r"^\d{4}-\d{4}-\d{4}-\d{4}-\d{4}$"
        for record in self:
            if record.accountNumber and not re.match(pattern, record.accountNumber):
                raise ValidationError("Account Number must be in the format XXXX-XXXX-XXXX-XXXX-XXXX (digits only).")

    #campos relacionales
    credit_cards = fields.One2many(comodel_name="grupo4.creditcard", inverse_name="accountNumber", string="Credit Card")
    account_ids= fields.Many2many(comodel_name="grupo4.account", string="Transfer", relation="account_account_rel",column1="account_id",column2="related_account_id")

    customer_product_ids = fields.Many2many(
        'grupo4.product',
        'product_account_rel', 'account_id', 'product_id',
        string='Customer Products'
    )