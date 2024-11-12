{
    'name': 'Proveedores',
    'version': '1.0',
    'summary': 'Gestión de proveedores',
    'description': 'Permite añadir, editar y eliminar proveedores mediante el módulo de compras.',
    'category': 'Purchases',
    'author': 'Federico',
    'depends': ['purchase'],
    'data': [
        'security/ir.model.access.csv',
        'views/proveedor_views.xml',
    ],
    'installable': True,
    'application': True,
}
