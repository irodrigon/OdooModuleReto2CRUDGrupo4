from odoo import fields,models

class Grupo4Accounts(models.Model):
    _inherit = "grupo4.account"

    # campos que se van insertar en la vista heredada
    usernames = fields.One2many(comodel_name="grupo4.user", inverse_name="accountNumber",string="Users email")

    login = fields.Char(string="Email", related="usernames.username")
