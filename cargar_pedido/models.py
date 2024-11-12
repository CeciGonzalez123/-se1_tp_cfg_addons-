from odoo import models, fields, api

class CargarPedido(models.Model):
    _name = 'cargar.pedido'
    _description = 'Cargar Pedido'

    name = fields.Char(string='Nombre del Pedido', required=True)
    product_id = fields.Many2one('product.product', string='Producto', required=True)
    order_qty = fields.Float(string='Cantidad', required=True)

    sale_order_id = fields.Many2one('sale.order', string='Pedido de Venta')
