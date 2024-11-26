{
    'name': 'Reporte de Ventas',
    'version': '1.0',
    'category': 'Sales',
    'summary': 'Generar reportes de ventas por usuario y equipo en PDF',
    'description': 'Módulo para generar reportes de ventas detallados en PDF',
    'author': 'Tu Nombre',
    'depends': ['sale', 'crm'],
    'data': [
        'security/ir.model.access.csv',
        'views/sales_report_views.xml',
        'views/sales_report_menu.xml',
        'report/sales_report_template.xml',
        'report/sales_report_action.xml',
    ],
}




