from odoo import models, fields

class AccountPayment(models.Model):
    _inherit = 'account.payment'

    cheque_id = fields.Many2one('gestion.cheque', string='Cheque')


