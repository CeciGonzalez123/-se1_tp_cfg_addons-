{
    'name': 'ProcessOrder',
    'version': '1.0',
    'summary': 'Módulo para procesar pedidos',
    'description': 'Módulo personalizado para gestionar y procesar pedidos en Odoo.',
    'author': 'Tu Nombre',
    'depends': ['base', 'sale', 'stock'],
    'data': [
        'security/ir.model.access.csv',
        'views/process_order_views.xml',
    ],
    'installable': True,
    'application': True,
}

