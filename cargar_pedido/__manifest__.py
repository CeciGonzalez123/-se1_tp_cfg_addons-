{
    'name': 'Cargar Pedido',
    'version': '1.0',
    'summary': 'Módulo para cargar pedidos en el módulo de ventas.',
    'category': 'Sales',
    'author': 'Tu Nombre',
    'website': 'http://www.tusitio.com',
    'depends': ['sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/cargar_pedido_views.xml',
    ],
    'installable': True,
    'application': False,
}
