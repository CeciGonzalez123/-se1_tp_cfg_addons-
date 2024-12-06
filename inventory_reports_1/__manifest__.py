{
    'name': 'Inventory report 1',
    'version': '1.0',
    'summary': 'Agrega un botón de reporte de inventario.',
    'category': 'Inventory',
    'description': """
        Este módulo agrega un botón para crear un reporte en PDF del inventario.
    """,
    'author': 'Gustavo Perez',
    'depends': ['stock'],
    'data': [
        'security/ir.model.access.csv',
        'views/stock_quant_report_wizard_views.xml',
        'views/report_template.xml',
    ],
    'installable': True,
    'application': True,
}

