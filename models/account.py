from odoo import fields, models

class Account(models.Model):
    _name = "grupo4.account"
    _description = "guarda las cuentas de los usuarios"

    # campos simples
    accountNumber = fields.Char(string="The number of the account")
    balance = fields.Float(string="The ammount of money in the account")
