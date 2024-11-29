from pkg_resources import require

from odoo import fields,models

class Movements(models.Model):
    _name = "grupo4.movements"
    _description = 'Guarda los movimientos'

    transactionId = fields.Char(string="Id of Transaction")
    transactionDate = fields.Datetime(string="Transaction Date")
    ammount = fields.Float(string="Ammount of money")
    typeOfMoney = fields.Char(string="Type Of money")
