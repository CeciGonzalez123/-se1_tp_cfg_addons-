from odoo import models, fields

class InsufficientStockWizard(models.TransientModel):
    _name = 'insufficient.stock.wizard'
    _description = 'Wizard para notificar stock insuficiente'

    product_id = fields.Many2one('product.product', string="Producto", readonly=True)
    message = fields.Text(string="Mensaje", readonly=True)

    def action_show(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Stock Insuficiente',
            'res_model': 'insufficient.stock.wizard',
            'view_mode': 'form',
            'target': 'new',
            'res_id': self.id,
        }

