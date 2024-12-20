from odoo import fields, models

class InventoryReportPivot(models.Model):
    _name = 'inventory.report.pivot'
    _description = 'Reporte de Inventario para Vista Pivot'
    _auto = False

    product_id = fields.Many2one('product.product', string='Producto')
    lot_id = fields.Many2one('stock.production.lot', string='Lote')
    stock_quantity = fields.Float(string='Cantidad en Stock')
    expiration_date = fields.Date(string='Fecha de Vencimiento')
    location_id = fields.Many2one('stock.location', string='Ubicación')

def init(self):
    
    self.env.cr.execute("""
        CREATE OR REPLACE VIEW inventory_report_pivot AS (
            SELECT
                row_number() OVER () AS id,
                quants.product_id AS product_id,
                quants.quantity AS stock_quantity,
                quants.location_id AS location_id
            FROM
                stock_quant AS quants
            WHERE
                quants.quantity > 0
        )
    """)

