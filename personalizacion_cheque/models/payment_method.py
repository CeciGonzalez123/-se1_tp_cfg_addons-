from odoo import models, fields

class PaymentMethod(models.Model):
    _inherit = 'account.payment.method'

    cheque = fields.Boolean(string='Cheque', default=False)


