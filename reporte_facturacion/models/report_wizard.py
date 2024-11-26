import base64
import io
import xlsxwriter
from odoo import models, fields
from odoo.exceptions import UserError
from odoo.http import content_disposition, request

class ReportWizard(models.TransientModel):
    _name = 'report.wizard'
    _description = 'Reporte de Compras y Ventas'

    start_date = fields.Date(string='Fecha de Inicio', required=True)
    end_date = fields.Date(string='Fecha de Fin', required=True)
    company_id = fields.Many2one('res.company', string='Compañía', required=True, default=lambda self: self.env.company)

    def generate_purchase_report(self):
        purchases = self.env['purchase.order'].search([
            ('date_order', '>=', self.start_date),
            ('date_order', '<=', self.end_date),
            ('company_id', '=', self.company_id.id),
            ('state', 'in', ['purchase', 'done'])
        ])
        if not purchases:
            raise UserError('No hay compras en el periodo seleccionado.')

        return self.generate_excel_report(purchases, 'Compras')

    def generate_sales_report(self):
        sales = self.env['sale.order'].search([
            ('date_order', '>=', self.start_date),
            ('date_order', '<=', self.end_date),
            ('company_id', '=', self.company_id.id),
            ('state', 'in', ['sale', 'done'])
        ])
        if not sales:
            raise UserError('No hay ventas en el periodo seleccionado.')

        return self.generate_excel_report(sales, 'Ventas')

    def generate_excel_report(self, records, report_type):
        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output)
        worksheet = workbook.add_worksheet()

        headers = ['Nombre de la Compañía', 'Periodo', 'Nro Factura', 'Fecha Factura', 'Cliente', 'Total Registrado']
        worksheet.write_row(0, 0, headers)

        row = 1
        total = 0
        for record in records:
            worksheet.write(row, 0, self.company_id.name)
            worksheet.write(row, 1, f'{self.start_date} - {self.end_date}')
            worksheet.write(row, 2, record.name)
            worksheet.write(row, 3, str(record.date_order))
            worksheet.write(row, 4, record.partner_id.name)
            worksheet.write(row, 5, record.amount_total)
            total += record.amount_total
            row += 1

        worksheet.write(row, 4, 'Total')
        worksheet.write(row, 5, total)
        
        workbook.close()
        output.seek(0)

        # Codificar el archivo en base64
        file_data = base64.b64encode(output.getvalue()).decode('utf-8')

        # Preparar la respuesta
        attachment_id = self.env['ir.attachment'].create({
            'name': f'Reporte_{report_type}.xlsx',
            'type': 'binary',
            'datas': file_data,
            'store_fname': f'Reporte_{report_type}.xlsx',
            'mimetype': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        })

        return {
            'type': 'ir.actions.act_url',
            'url': f'/web/content/{attachment_id.id}?download=true',
            'target': 'self',
        }




