from odoo import fields, models


class User(models.Model):
    _name = "grupo4.user"
    _description = "Rovobank's users"

    username = fields.Char(string="username")
    name = fields.Char(string="name")
    surname = fields.Char(string="surname", store=True)
    street = fields.Char(string="street")
    city = fields.Char(string="city")
    zip = fields.Char(string="zip")

    accountNumber = fields.Many2one(comodel_name="grupo4.account", string="Account Number")



