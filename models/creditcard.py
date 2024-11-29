from odoo import fields,models

class CreditCard(models.Model):
    _name = "grupo4.creditcard"
    _description = "saves credit cards"

    #simple fields
    creditCardNumber = fields.Char(string="Credit card number")
    expirationDate = fields.Date(string="Expiration date")
    cvv = fields.Char(string="CVV")
    pin =fields.Char(string="PIN")