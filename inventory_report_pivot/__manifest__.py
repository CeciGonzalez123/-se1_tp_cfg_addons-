{
    'name': 'Reporte de Inventario con Pivot',
    'version': '1.0',
    'category': 'Inventory',
    'summary': 'Reporte dinámico de inventario con lotes, fechas de vencimiento y ubicación.',
    'description': 'Módulo para generar un reporte de inventario en vista Pivot con datos como lotes, fechas de vencimiento y ubicación.',
    'author': 'Gustavo Perez',
    'website': 'https://tusitio.com',
    'depends': ['stock'],
    'data': [
        'views/inventory_report_pivot_view.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
