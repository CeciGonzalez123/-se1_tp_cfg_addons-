{
    'name': 'Personalización de Pagos con Cheques',
    'version': '1.0',
    'category': 'Accounting',
    'summary': 'Personalización para agregar cheques en pagos',
    'description': 'Este módulo añade la funcionalidad de seleccionar cheques al registrar pagos en facturas.',
    'author': 'Tu Nombre',
    'depends': ['account', 'gestion_cheques'],
    'data': [
        'data/account_payment_method_data.xml',
        'views/account_payment_views.xml',
    ],
    'installable': True,
    'application': False,
}
