{
    'name': 'Gestión de Timbrados',
    'version': '1.0',
    'category': 'Accounting',
    'summary': 'Gestión y administración de timbrados para facturación',
    'description': 'Módulo para la gestión y administración de timbrados en facturación.',
    'author': 'Tu Nombre',
    'depends': ['account'],
    'data': [
        'security/ir.model.access.csv',
        'views/timbrado_views.xml',
        'views/factura_views.xml',
    ],
    'installable': True,
    'application': False,
}
