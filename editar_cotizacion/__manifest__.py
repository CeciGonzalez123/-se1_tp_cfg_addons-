{
    'name': 'Editar Cotización',
    'version': '1.0',
    'summary': 'Módulo para editar cotizaciones en el módulo de ventas.',
    'category': 'Sales',
    'author': 'Tu Nombre',
    'website': 'http://www.tusitio.com',
    'depends': ['sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/editar_cotizacion_views.xml',
    ],
    'installable': True,
    'application': False,
}
