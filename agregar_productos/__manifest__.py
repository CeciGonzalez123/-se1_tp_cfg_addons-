{
    'name': 'Agregar Productos',
    'version': '1.0',
    'summary': 'Módulo para agregar productos en el módulo de ventas.',
    'category': 'Sales',
    'author': 'Tu Nombre',
    'website': 'http://www.tusitio.com',
    'depends': ['sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/agregar_productos_views.xml',
    ],
    'installable': True,
    'application': False,
}
