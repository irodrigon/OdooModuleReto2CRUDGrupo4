from odoo import fields,models

class User(models.Model):
    _name = "grupo4.user"
    _description = "Rovobank's users"
    _inherit ={'res.partner':'name',
               'res.partner':'street',
               'res.partner':'city',
               'res.partner':'active',
               'res.partner':'zip'}

    def init(self):
        # Check if the column already exists
        self.env.cr.execute("""
               SELECT column_name 
               FROM information_schema.columns 
               WHERE table_name='res_partner' and column_name='signup_token'
           """)
        # If the column does not exist, add it
        if not self.env.cr.fetchone():
            self.env.cr.execute("ALTER TABLE res_partner ADD COLUMN signup_token varchar")

    username = fields.Char(String="Username",required=True)

    channel_ids = fields.Many2many(
        comodel_name='mail.channel',
        relation='mail_channel_res_partner_grupo4_user_rel',
        column1='res_partner_grupo4_user_id',
        column2='channel_id',
        string="Channels"
    )


