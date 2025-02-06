from odoo import fields,models, api
from datetime import date
from odoo.exceptions import ValidationError

class Product(models.Model):
    _name = "grupo4.product"
    _description = "Rovobank products"

    #Simple fields
    productId = fields.Integer(String="Product ID", required=True)
    owner = fields.Char(String="Owner")
    creationDate = fields.Date(String="Creation date", store=True)


    customer_product_ids = fields.Many2many(
        comodel_name="grupo4.customer",
        relation="customer_product_Ids",
        column1="customer_ids",
        column2="product_ids",
        string="Customer_products_relation"
    )

    @api.onchange('owner')
    def _check_creation_date(self):
        if self.creationDate and self.creationDate > date.today():
            return {
                "warning": {
                    "title": "Invalid Date",
                    "message": "The Creation Date cannot be in the future.",
                }
            }