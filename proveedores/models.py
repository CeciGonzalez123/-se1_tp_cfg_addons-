from odoo import models, fields

class Proveedor(models.Model):
    _name = 'proveedor'
    _description = 'Proveedores'

    name = fields.Char(string='Nombre', required=True)
    email = fields.Char(string='Correo Electrónico')
    phone = fields.Char(string='Teléfono')
    address = fields.Text(string='Dirección')
    product_ids = fields.Many2many('product.product', string='Productos')
