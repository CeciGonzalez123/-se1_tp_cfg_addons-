from odoo import models, fields, api, exceptions

class PurchaseRestriction(models.Model):
    _name = 'purchase.restriction'
    _description = 'Restricciones de Compra'

    name = fields.Char(string='Nombre de la Restricción', required=True)
    product_id = fields.Many2one('product.product', string='Producto')
    min_qty = fields.Float(string='Cantidad Mínima', required=True, default=1)
    max_qty = fields.Float(string='Cantidad Máxima')
    min_total = fields.Float(string='Monto Mínimo Total', default=1)
    max_total = fields.Float(string='Monto Máximo Total')

    @api.constrains('min_qty', 'max_qty', 'min_total', 'max_total')
    def _check_amounts(self):
        for record in self:
            if record.min_qty <= 0:
                raise exceptions.ValidationError('La cantidad mínima debe ser mayor que cero.')
            if record.min_total < 0:
                raise exceptions.ValidationError('El monto mínimo no puede ser negativo.')
            if record.max_qty and record.min_qty > record.max_qty:
                raise exceptions.ValidationError('La cantidad mínima no puede ser mayor que la cantidad máxima.')
            if record.max_total and record.min_total > record.max_total:
                raise exceptions.ValidationError('El monto mínimo no puede ser mayor que el monto máximo.')

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    state = fields.Selection(selection_add=[('bloqueado', 'Bloqueado')])

    def button_confirm(self):
        for order in self:
            total = sum(line.price_subtotal for line in order.order_line)
            
            # Buscar restricciones generales (sin producto específico)
            general_restrictions = self.env['purchase.restriction'].search([('product_id', '=', False)])
            for restriction in general_restrictions:
                if total < restriction.min_total or (restriction.max_total and total > restriction.max_total):
                    order.message_post(body=f"Compra bloqueada: el monto total de la compra no cumple con las restricciones generales. Monto mínimo: {restriction.min_total}, Monto máximo: {restriction.max_total}.")
                    order.write({'state': 'bloqueado'})
                    return False

            for line in order.order_line:
                # Buscar restricciones específicas por producto
                product_restrictions = self.env['purchase.restriction'].search([('product_id', '=', line.product_id.id)])
                if product_restrictions:
                    for restriction in product_restrictions:
                        if line.product_qty < restriction.min_qty or (restriction.max_qty and line.product_qty > restriction.max_qty):
                            order.message_post(body=f"Compra bloqueada: la cantidad del producto {line.product_id.name} no cumple con las restricciones. Cantidad mínima: {restriction.min_qty}, Cantidad máxima: {restriction.max_qty}.")
                            order.write({'state': 'bloqueado'})
                            return False
                        if total < restriction.min_total or (restriction.max_total and total > restriction.max_total):
                            order.message_post(body=f"Compra bloqueada: el monto total de la compra no cumple con las restricciones del producto {line.product_id.name}. Monto mínimo: {restriction.min_total}, Monto máximo: {restriction.max_total}.")
                            order.write({'state': 'bloqueado'})
                            return False
                else:
                    for restriction in general_restrictions:
                        if line.product_qty < restriction.min_qty or (restriction.max_qty and line.product_qty > restriction.max_qty):
                            order.message_post(body=f"Compra bloqueada: la cantidad del producto {line.product_id.name} no cumple con las restricciones generales. Cantidad mínima: {restriction.min_qty}, Cantidad máxima: {restriction.max_qty}.")
                            order.write({'state': 'bloqueado'})
                            return False
        return super(PurchaseOrder, self).button_confirm()



    def button_unlock(self):
        for order in self:
            if self.env.user.has_group('base.group_system'):
                order.message_post(body='Desbloqueo ejecutado por un administrador.')
                order.write({'state': 'purchase'})
            else:
                raise exceptions.UserError('Solo los administradores pueden desbloquear esta orden.')
