from odoo import fields,models

class Product(models.Model):
    _name = "grupo4.product"
    _description = "Rovobank products"

    #Simple fields
    productId = fields.Integer(String="Product ID", required=True)
    owner = fields.Char(String="Owner")
    creationDate = fields.Date(String="Creation date")