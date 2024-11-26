{
    'name': 'Gestión de Cheques',
    'version': '1.0',
    'category': 'Accounting',
    'summary': 'Gestión de Cheques',
    'description': 'Módulo para la gestión de cheques, incluyendo registro y listado de cheques.',
    'author': 'Tu Nombre',
    'depends': ['account'],
    'data': [
        'security/ir.model.access.csv',
        'views/cheque_views.xml',
        'views/cheque_menu.xml',
        'views/account_payment_views.xml',
    ],
}





