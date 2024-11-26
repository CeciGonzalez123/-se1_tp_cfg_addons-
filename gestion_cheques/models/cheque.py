from odoo import models, fields

class Cheque(models.Model):
    _name = 'gestion.cheque'
    _description = 'Gestión de Cheques'

    numero_cheque = fields.Char(string='Número de Cheque', required=True)
    banco = fields.Char(string='Banco', required=True)
    monto = fields.Float(string='Monto', required=True)
    moneda = fields.Selection([
        ('usd', 'USD'),
        ('eur', 'EUR'),
        ('pyg', 'PYG'),
    ], string='Moneda', required=True)
    fecha_emision = fields.Date(string='Fecha de Emisión', required=True)
    fecha_vencimiento = fields.Date(string='Fecha de Vencimiento', required=True)
    tipo_cheque = fields.Selection([
        ('a_la_vista', 'A la Vista'),
        ('diferido', 'Diferido')
    ], string='Tipo de Cheque', required=True)



