{
    'name': 'Lote Management',
    'version': '1.0',
    'category': 'Inventory',
    'summary': 'Agrega un boton para cambiar la fecha de vencimiento a los lotes',
    'description': """
        Este módulo agrega un boton para cambiar la fecha de vencimiento a los lotes.
    """,
    'author': 'Gustavo Perez',
    'depends': ['stock'],  # Dependencia del módulo de inventario
    'data': [
        'security/ir.model.access.csv',
        'views/stock_lot_views.xml',
        'views/expiration_date_wizard_views.xml',
    ],
    'installable': True,
    'application': True,
}
