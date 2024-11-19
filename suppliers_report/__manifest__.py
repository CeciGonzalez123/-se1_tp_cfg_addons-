# -*- coding: utf-8 -*-
{
    'name': 'Reportes de Proveedor',
    'version': '1.0',
    'summary': 'Módulo para generar reportes de proveedores en el módulo de compras',
    'description': 'Este módulo agrega una sección de reportes de proveedores en el módulo de compras, con opción de descarga en PDF.',
    'category': 'Purchases',
    'author': 'Federico',
    'license': 'AGPL-3',
    'depends': ['purchase'],
    'data': [
        'views/proveedor_reportes_view.xml',
        'security/ir.model.access.csv',
        'reports/report_proveedor_reportes.xml', 
        'reports/report.xml',
    ],
    'installable': True,
    'application': False,
}
