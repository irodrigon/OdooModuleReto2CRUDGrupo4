from odoo import fields, models
from odoo.release import description


class Loan (models.Model) :
    _name = "grupo4.loan"
    _inherit = "grupo4.product"
    _description = "guarda los prestamos de cada usuario"


    # campos simples
    interestRate = fields.Integer(string="El porcentage de interes del prestamo")
    endDate = fields.Date(string="La fecha limite en la que el prestamo ha de ser pagado")
    remainingBalance = fields.Float(string= "El monto que falta por pagar")
    period = fields.Integer(string="La periodicidad con la que se paga el prestamo en dias")
    description = fields.Char(string="Descripción personal del motivo del prestamo")
