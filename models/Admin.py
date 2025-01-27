from odoo import fields,models

class Admin(models.Model):
    _name = "grupo4.admin"
    _description="Rovobank's admins"
    _inherit = "grupo4.user"

    password = fields.Char(string="Password", required = True)
    active = fields.Boolean(string="active")