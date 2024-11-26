from odoo import models, fields, api

class SalesReport(models.Model):
    _name = 'reporte.ventas'
    _description = 'Reporte de Ventas'

    name = fields.Char(string='Nombre')
    start_date = fields.Date(string='Fecha de Inicio')
    end_date = fields.Date(string='Fecha de Fin')
    sales_team_id = fields.Many2one('crm.team', string='Equipo de Ventas')
    user_id = fields.Many2one('res.users', string='Vendedor')
    sale_order_ids = fields.One2many('sale.order', 'report_id', string='Órdenes de Venta')
    total_sales = fields.Float(string='Total de Ventas', compute='_compute_total_sales')

    @api.depends('sale_order_ids')
    def _compute_total_sales(self):
        for record in self:
            record.total_sales = sum(order.amount_total for order in record.sale_order_ids)

    @api.model
    def generar_reporte(self):
        for record in self:
            record.sale_order_ids = self.env['sale.order'].search([
                ('team_id', '=', record.sales_team_id.id),
                ('user_id', '=', record.user_id.id),
                ('date_order', '>=', record.start_date),
                ('date_order', '<=', record.end_date)
            ])



class SaleOrder(models.Model):
    _inherit = 'sale.order'

    partner_id = fields.Many2one('res.partner', string='Customer', required=True, default=lambda self: self.env['res.partner'].search([], limit=1).id)
    company_id = fields.Many2one('res.company', string='Company', required=True, default=lambda self: self.env.company)
    report_id = fields.Many2one('reporte.ventas', string='Reporte de Ventas')
