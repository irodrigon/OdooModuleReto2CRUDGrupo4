from odoo import fields,models

class Customer(models.Model):
    _name = "grupo4.customer"
    _description="Rovobank's customers"
    _inherit ="grupo4.user"

    dni = fields.Char(string="DNI",required=True)
    phone = fields.Char(string="Telephone")

    channel_ids = fields.Many2many(
        comodel_name='mail.channel',
        relation='mail_channel_customer_grupo4_user_rel',
        column1='customer_grupo4_user_id',
        column2='channel_id',
        string="Channels"
    )

