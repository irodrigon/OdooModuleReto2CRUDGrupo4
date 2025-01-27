from odoo import fields,models

class Customer(models.Model):
    _name = "grupo4.customer"
    _description="Rovobank's customers"
    _inherit = "grupo4.user"

    dni = fields.Char(string="DNI",required=True)
    phone = fields.Char(string="Telephone")



