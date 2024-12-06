{
    'name': 'Restricción de Stock en Transferencias',
    'version': '1.0',
    'category': 'Inventory',
    'author': 'Gustavo Perez',
    'summary': 'Restringe la validación de transferencias sin stock suficiente.',
    'description': """
        Este módulo implementa una validación adicional en el botón "Validar" de las transferencias
        de inventario. Si no hay stock suficiente para completar la operación, se muestra una ventana 
        de notificación.
    """,
    'depends': ['stock'],  # Dependencia del módulo de inventario
    'data': [
        'security/ir.model.access.csv',
        'views/stock_picking_views.xml',
        'views/insufficient_stock_wizard_views.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
