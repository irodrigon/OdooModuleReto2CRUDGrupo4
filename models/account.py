from odoo import fields, models

class Account(models.Model):
    _name = "grupo4.account"
    _inherit="grupo4.product"
    _description = "guarda las cuentas de los usuarios"

    # campos simples
    balance = fields.Float(string="The ammount of money in the account")

    #campos relacionales
    accountNumber = fields.One2many(comodel_name="grupo4.creditcard", inverse_name="accountNumber", string="Credit Card")
    account_ids= fields.Many2many(comodel_name="grupo4.account", string="Transfer", relation="account_account_rel",column1="account_id",column2="related_account_id")

    customer_product_ids = fields.Many2many(
        'grupo4.product',
        'product_account_rel', 'account_id', 'product_id',
        string='Customer Products'
    )