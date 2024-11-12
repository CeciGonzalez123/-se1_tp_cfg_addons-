from odoo import models, fields, api, exceptions

class PurchaseRestriction(models.Model):
    _name = 'purchase.restriction'
    _description = 'Restricciones de Compra'

    name = fields.Char(string='Nombre de la Restricción', required=True)
    product_id = fields.Many2one('product.product', string='Producto', required=True)
    max_qty = fields.Float(string='Cantidad Máxima', required=True, help='Cantidad máxima que se puede comprar')

    @api.constrains('max_qty')
    def _check_max_qty(self):
        for record in self:
            if record.max_qty <= 0:
                raise exceptions.ValidationError('La cantidad máxima debe ser mayor que cero.')


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    @api.model
    def create(self, vals):
        product_id = vals.get('product_id')
        product_qty = vals.get('product_qty')
        restriction = self.env['purchase.restriction'].search([('product_id', '=', product_id)], limit=1)

        if restriction and product_qty > restriction.max_qty:
            raise exceptions.ValidationError(
                f'La cantidad máxima para {restriction.product_id.name} es {restriction.max_qty}.'
            )

        return super(PurchaseOrderLine, self).create(vals)

    def write(self, vals):
        for record in self:
            product_id = vals.get('product_id', record.product_id.id)
            product_qty = vals.get('product_qty', record.product_qty)
            restriction = self.env['purchase.restriction'].search([('product_id', '=', product_id)], limit=1)

            if restriction and product_qty > restriction.max_qty:
                raise exceptions.ValidationError(
                    f'La cantidad máxima para {restriction.product_id.name} es {restriction.max_qty}.'
                )

        return super(PurchaseOrderLine, self).write(vals)
