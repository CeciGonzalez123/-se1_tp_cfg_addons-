from odoo import models, fields, api

class StockQuantReportWizard(models.Model):
    _name = 'stock.quant.report.wizard'
    _description = 'Wizard para Reporte de Inventario'
    _inherit = 'stock.quant'
    report_date = fields.Datetime(
        string='Inventario a la fecha',
        required=True,
        default=fields.Datetime.now,
    )

    def action_generate_inventory_pdf(self):
        """Genera un reporte en formato PDF con los datos del inventario."""
        products = self.env['stock.quant'].search([])
        report_data = []
        for quant in products:
            report_data.append({
                'product_name': quant.product_id.name,
                'location': quant.location_id.display_name,
                'quantity': quant.quantity,
                'lot_name': quant.lot_id.name if quant.lot_id else 'Sin lote',
                'expiration_date': quant.lot_id.expiration_date if quant.lot_id and quant.lot_id.expiration_date else 'N/A',
            })

        # Renderizando el reporte
        return self.env.ref('inventory_reports_1.report_inventory_pdf_template').report_action(self)






