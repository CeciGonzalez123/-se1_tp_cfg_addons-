from odoo import models, fields

class AccountPayment(models.Model):
    _inherit = 'account.payment'

    cheque_id = fields.Many2one('gestion.cheque', string='Cheque')

    payment_method_id = fields.Many2one(
        'account.payment.method', string='Método de Pago',
        required=True, default=lambda self: self.env.ref('mi_personalizacion.account_payment_method_cheque').id)




