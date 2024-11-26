from odoo import models, fields, api
from odoo.exceptions import UserError
import datetime

class Timbrado(models.Model):
    _name = 'gestion.timbrado'
    _description = 'Gestión de Timbrados'

    numero_timbrado = fields.Char(string='Número de Timbrado', required=True)
    fecha_inicio = fields.Date(string='Fecha de Inicio', required=True)
    fecha_fin = fields.Date(string='Fecha de Fin', required=True)
    nro_establecimiento = fields.Char(string='Nro de Establecimiento', required=True)
    nro_expedicion = fields.Char(string='Nro de Expedición', required=True)
    nro_factura = fields.Integer(string='Nro Factura', required=True, default=1)
    active = fields.Boolean(string='Activo', default=True)
    company_id = fields.Many2one('res.company', string='Compañía', required=True, default=lambda self: self.env.company)

    _sql_constraints = [
        ('unique_timbrado', 'unique(numero_timbrado, company_id)', 'El número de timbrado debe ser único por compañía.'),
        ('unique_factura', 'unique(nro_factura)', 'El número de factura debe ser único.')
    ]

    @api.constrains('active')
    def _check_unique_active(self):
        for record in self:
            if record.active:
                active_timbrados = self.search([
                    ('company_id', '=', record.company_id.id),
                    ('active', '=', True),
                    ('id', '!=', record.id)
                ])
                if active_timbrados:
                    raise UserError('Ya hay un timbrado activo para esta compañía. Solo puede haber un timbrado activo por compañía.')

    def generar_numero_factura(self):
        self.ensure_one()
        nro_factura_formateado = '{:07d}'.format(self.nro_factura)
        numero_factura = f'{self.nro_establecimiento}-{self.nro_expedicion}-{nro_factura_formateado}'
        self.nro_factura += 1
        return numero_factura

class AccountMove(models.Model):
    _inherit = 'account.move'

    timbrado_id = fields.Many2one('gestion.timbrado', string='Timbrado', required=True, domain=[('active', '=', True)])

    @api.constrains('timbrado_id', 'invoice_date')
    def _check_timbrado_date(self):
        for record in self:
            if record.timbrado_id:
                if not (record.timbrado_id.fecha_inicio <= record.invoice_date <= record.timbrado_id.fecha_fin):
                    raise UserError('La fecha de la factura debe estar dentro del periodo del timbrado.')

    @api.model
    def create(self, vals):
        if 'timbrado_id' in vals and vals.get('move_type') in ['out_invoice', 'out_refund']:
            timbrado = self.env['gestion.timbrado'].browse(vals['timbrado_id'])
            vals['name'] = timbrado.generar_numero_factura()
        return super(AccountMove, self).create(vals)

    def write(self, vals):
        if 'timbrado_id' in vals and vals.get('move_type') in ['out_invoice', 'out_refund']:
            timbrado = self.env['gestion.timbrado'].browse(vals['timbrado_id'])
            vals['name'] = timbrado.generar_numero_factura()
        return super(AccountMove, self).write(vals)
