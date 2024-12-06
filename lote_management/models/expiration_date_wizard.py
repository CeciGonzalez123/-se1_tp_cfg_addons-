from odoo import models, fields

class ExpirationDateWizard(models.TransientModel):
    _name = 'expiration.date.wizard'
    _description = 'Wizard to change expiration date'

    expiration_date = fields.Date(string="New Expiration Date", required=True)

    def apply_new_expiration_date(self):
        """Actualiza la fecha de expiración del lote."""
        active_id = self.env.context.get('active_id')
        if active_id:
            lot = self.env['stock.lot'].browse(active_id)
            lot.expiration_date = self.expiration_date
