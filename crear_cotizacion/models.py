from odoo import models, fields, api

class CrearCotizacion(models.Model):
    _name = 'crear.cotizacion'
    _description = 'Crear Cotización'

    name = fields.Char(string='Nombre de la Cotización', required=True)
    cliente_id = fields.Many2one('res.partner', string='Cliente', required=True)
    product_id = fields.Many2one('product.product', string='Producto', required=True)
    cantidad = fields.Float(string='Cantidad', required=True)
    precio_unitario = fields.Float(string='Precio Unitario', required=True)
    total = fields.Float(string='Total', compute='_compute_total', store=True)

    @api.depends('cantidad', 'precio_unitario')
    def _compute_total(self):
        for record in self:
            record.total = record.cantidad * record.precio_unitario

