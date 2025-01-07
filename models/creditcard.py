from odoo import fields,models

class CreditCard(models.Model):
    _name = "grupo4.creditcard"
    _inherit="grupo4.product"
    _description = "saves credit cards"

    #simple fields
    creditCardNumber = fields.Char(string="Credit card number")
    expirationDate = fields.Date(string="Expiration date")
    cvv = fields.Char(string="CVV")
    pin =fields.Char(string="PIN")

    #relational fields
    accountNumber = fields.Many2one(comodel_name="grupo4.account", string="Account", required=True, ondelete="cascade")
    creditCardMovement = fields.One2many(comodel_name="grupo4.movements", inverse_name="creditCard", string="Movements", required=True)

    customer_product_ids = fields.Many2many(
        'grupo4.product',
        'product_creditcard_rel', 'creditcard_id', 'product_id',
        string='Customer Products'
    )