from odoo import models, fields, api

class DescuentoAutomatico(models.Model):
    _name = 'descuento.automatico'
    _description = 'Configuración de Descuentos Automáticos'

    name = fields.Char(string='Nombre')
    cantidad_productos = fields.Integer(string='Cantidad de Productos')
    monto_total = fields.Float(string='Monto Total')
    descuento_porcentaje = fields.Float(string='Porcentaje de Descuento')

    @api.model
    def aplicar_descuento(self, order):
        for regla in self.search([]):
            cantidad_productos = sum(line.product_uom_qty for line in order.order_line)
            monto_total = order.amount_total

            if ((regla.cantidad_productos and cantidad_productos >= regla.cantidad_productos) or
                (regla.monto_total and monto_total >= regla.monto_total)):
                
                # Aplicar descuento solo si no se ha aplicado previamente
                if not order.aplico_descuento:
                    for line in order.order_line:
                        descuento = (line.price_unit * regla.descuento_porcentaje) / 100
                        line.write({'price_unit': line.price_unit - descuento})
                    order.write({'aplico_descuento': True})


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    aplico_descuento = fields.Boolean(string="Aplicó Descuento", default=False)

    @api.model
    def create(self, vals):
        order = super(SaleOrder, self).create(vals)
        self.env['descuento.automatico'].aplicar_descuento(order)
        return order

    def write(self, vals):
        res = super(SaleOrder, self).write(vals)
        self.env['descuento.automatico'].aplicar_descuento(self)
        return res
