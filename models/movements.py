
from odoo import fields,models, api
from datetime import date

class Movements(models.Model):
    _name = "grupo4.movements"
    _description = 'Guarda los movimientos'

    transactionId = fields.Char(string="Id of Transaction")
    transactionDate = fields.Date(string="Transaction Date")
    ammount = fields.Float(string="Ammount of money")
    typeOfMoney = fields.Char(string="Type Of money")

    @api.onchange('transactionDate')
    def _check_creation_date(self):
        if self.transactionDate and self.transactionDate > date.today():
            return {
                "warning": {
                    "title": "Invalid Date",
                    "message": "The Creation Date cannot be in the future.",
                }
            }

    @api.depends("transactionDate")
    def _totalDays(self):
        for record in self:
            if record.TransferDate:
                record.total_days_open = (date.today() - record.transactionDate).days
            else:
                record.total_days_open = 0


    creditCard = fields.Many2one(comodel_name="grupo4.creditcard", string="Credit Card", required=True, ondelete="cascade")

