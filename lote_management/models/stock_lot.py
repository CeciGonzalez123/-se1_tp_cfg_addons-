from odoo import models, fields, api
from datetime import date, datetime

class StockLot(models.Model):
    _inherit = 'stock.lot'

    expiration_date = fields.Date(string='Expiration Date')
    is_expired = fields.Boolean(string='Is Expired', compute='_compute_is_expired', store=True)

    @api.depends('expiration_date')
    def _compute_is_expired(self):
        """Compute whether the lot is expired based on the expiration_date."""
        today = date.today()  # `today` es de tipo datetime.date
        for lot in self:
            # Convertir expiration_date a tipo date si no lo es
            expiration_date = lot.expiration_date
            if isinstance(expiration_date, datetime):
                expiration_date = expiration_date.date()

            lot.is_expired = bool(expiration_date and expiration_date < today)

    def action_open_expiration_wizard(self):
        """Opens a wizard to change the expiration date of the lot."""
        return {
            'type': 'ir.actions.act_window',
            'name': 'Change Expiration Date',
            'res_model': 'expiration.date.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {'default_lot_id': self.id},
        }






