from pkg_resources import require

from odoo import fields,models

class Movements(models.Model):
    _name = "grupo4.movements"
    _description = 'Guarda los movimientos'

    #simple fields
    transactionId = fields.Char(string="Id of Transaction")
    transactionDate = fields.Datetime(string="Transaction Date")
    amount = fields.Float(string="Amount of money")
    typeOfMoney = fields.Char(string="Type Of money")

    #relational fields
    cardId = fields.Many2one(comodel_name="grupo4.creditcard", string="Credit Card", required=True, ondelete="cascade")