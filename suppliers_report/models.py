########################################################################################
from odoo import models, fields, api
############## Clase para el Reporte de Proveedor ##########################################################################
class ProveedorReportes(models.Model):
    _name = 'proveedor.reportes'
    _description = 'Reportes de Proveedor'
    _auto = False

    proveedor_id = fields.Many2one('res.partner', string='Proveedor')   #Campo para el id del proveedor
    total_compras = fields.Float(string='Total de Compras')             #Campo para el totalizador
    compras_ids = fields.One2many('proveedor.compras', 'proveedor_id', string='Compras', compute='_compute_compras_ids') #Campo para el id de las compras y sus relaciones
############# Definicion de la tabla de Reportes de Proveedor ###########################################################################
    @api.model
    def init(self):
        self.env.cr.execute("""
            DROP VIEW IF EXISTS proveedor_reportes;
            CREATE VIEW proveedor_reportes AS (
                SELECT
                    row_number() OVER () AS id,
                    rp.id AS proveedor_id,
                    SUM(po.amount_total) AS total_compras
                FROM
                    purchase_order po
                JOIN
                    res_partner rp ON po.partner_id = rp.id
                WHERE
                    po.state NOT IN ('cancelado', 'bloqueado') AND rp.is_company = True
                GROUP BY
                    rp.id
            )
        """)

    @api.depends('proveedor_id')
    def _compute_compras_ids(self):
        for record in self:
            compras = self.env['proveedor.compras'].search([
                ('proveedor_id', '=', record.proveedor_id.id)
            ])
            record.compras_ids = compras
############## Clase para las Compras del Proveedor ##########################################################################
class ProveedorCompras(models.Model):
    _name = 'proveedor.compras'
    _description = 'Compras por Proveedor'
    _auto = False

    proveedor_id = fields.Many2one('res.partner', string='Proveedor')   #Campo del id del proveedor
    compra_referencia = fields.Char(string='Referencia de Compra')      #Campo de la referencia de la compra
    fecha_compra = fields.Date(string='Fecha de Compra')                #Campo de la fecha de la compra
    monto = fields.Float(string='Monto')                                #Campo del monto de la compra
############### Definicion de la tabla de Compras del Proveedor #########################################################################
    @api.model
    def init(self):
        self.env.cr.execute("""
            DROP VIEW IF EXISTS proveedor_compras;
            CREATE VIEW proveedor_compras AS (
                SELECT
                    row_number() OVER () AS id,
                    po.partner_id AS proveedor_id,
                    po.name AS compra_referencia,
                    po.date_order AS fecha_compra,
                    po.amount_total AS monto
                FROM
                    purchase_order po
                JOIN
                    res_partner rp ON po.partner_id = rp.id
                WHERE
                    po.state NOT IN ('cancelado', 'bloqueado')
            )
        """)
########################################################################################