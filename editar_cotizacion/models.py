from odoo import models, fields, api

class EditarCotizacion(models.Model):
    _inherit = 'sale.order'

    # Campo adicional como ejemplo
    descuento_especial = fields.Float(string='Descuento Especial (%)')

    @api.onchange('descuento_especial')
    def _onchange_descuento_especial(self):
        """Aplicar el descuento especial al total."""
        for record in self:
            if record.descuento_especial:
                descuento = record.amount_total * (record.descuento_especial / 100)
                record.amount_total -= descuento


