from odoo import models, _, fields

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    def button_validate(self):
        """
        Valida si hay suficiente stock antes de permitir la validación de la transferencia.
        Si no hay stock suficiente, muestra un wizard con el detalle.
        """
        for move in self.move_ids:  # Validamos sobre stock.move, no sobre stock.move.line
            if move.product_uom_qty > move.product_id.qty_available:
                # Crear el wizard para mostrar el mensaje de stock insuficiente
                return self.env['insufficient.stock.wizard'].create({
                    'product_id': move.product_id.id,
                    'message': _(
                        f"No hay suficiente stock para el producto: {move.product_id.display_name}. "
                        f"Disponible: {move.product_id.qty_available}, Requerido: {move.product_uom_qty}."
                    ),
                }).action_show()
        # Si todo está correcto, continúa con la validación normal
        return super(StockPicking, self).button_validate()

