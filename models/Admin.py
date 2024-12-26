from odoo import fields,models

class Admin(models.Model):
    _name = "grupo4.admin"
    _description="Rovobank's admins"
    _inherit ="grupo4.user"

    password = fields.Char(string="Password", required = True)

    channel_ids = fields.Many2many(
        comodel_name='mail.channel',
        relation='mail_channel_admin_grupo4_user_rel',
        column1='admin_grupo4_user_id',
        column2='channel_id',
        string="Channels"
    )