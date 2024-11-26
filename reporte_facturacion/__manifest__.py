{
    'name': 'Reporte de Compras y Ventas',
    'version': '1.0',
    'category': 'Accounting',
    'summary': 'Generación de reportes de compras y ventas en formato Excel',
    'description': 'Permite generar reportes de compras y ventas en formato Excel durante un periodo de tiempo establecido por el usuario.',
    'author': 'Tu Nombre',
    'depends': ['account', 'sale', 'purchase'],
    'data': [
        'security/ir.model.access.csv',
        'views/report_wizard_views.xml',
    ],
    'installable': True,
    'application': False,
}

