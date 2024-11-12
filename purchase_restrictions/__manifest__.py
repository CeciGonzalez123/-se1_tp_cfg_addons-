# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

# Copyright (c) 2011 CCI Connect asbl (http://www.cciconnect.be) All Rights Reserved.
#                       Philmer <philmer@cciconnect.be>

{
    'name': 'Restricciones de Compra',
    'version': '1.0',
    'summary': 'Aplica restricciones en el módulo de compras.',
    'description': """
    Este módulo añade restricciones al proceso de compras en Odoo.
    """,
    'category': 'Purchases',
    'author': 'Federico',
    'website': 'http://www.tusitio.com',
    'depends': ['purchase'],
    'data': [
        'security/ir.model.access.csv',
        'views/purchase_restriction_views.xml',
    ],
    'installable': True,
    'application': False,
}
