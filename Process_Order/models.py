from odoo import models, fields, api
from odoo.exceptions import UserError

class ProcessOrder(models.Model):
    _name = 'process.order'
    _description = 'Process Order'

    name = fields.Char(string='Order Name', required=True)
    order_date = fields.Date(string='Order Date', default=fields.Date.today)
    customer_id = fields.Many2one('res.partner', string='Customer', required=True)
    product_id = fields.Many2one('product.product', string='Product', required=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled')
    ], string='Status', default='draft')

    def action_confirm(self):
        self.state = 'confirmed'

    def action_check_stock(self):
        if self.product_id.qty_available > 0:
            self.state = 'done'
        else:
            raise UserError('El producto está agotado.')

    def action_cancel(self):
        self.state = 'cancelled'

