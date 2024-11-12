from odoo import models, fields, api

class AgregarProducto(models.Model):
    _name = 'agregar.producto'
    _description = 'Agregar Producto'

    name = fields.Char(string='Nombre del Producto', required=True)
    product_id = fields.Many2one('product.product', string='Producto', required=True)
    cantidad = fields.Float(string='Cantidad', required=True)
    sale_order_id = fields.Many2one('sale.order', string='Pedido de Venta')

