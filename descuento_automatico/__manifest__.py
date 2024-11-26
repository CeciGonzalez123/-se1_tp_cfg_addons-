{
    'name': 'Descuento Automático',
    'version': '1.0',
    'summary': 'Módulo para aplicar descuentos automáticos enlazado al módulo de ventas',
    'description': """
        Este módulo aplica descuentos automáticos a las órdenes de venta.
    """,
    'category': 'Sales',
    'author': 'Tu Nombre',
    'depends': ['sale'],
    'data': [
        'views/descuento_automatico_views.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': False,
}
