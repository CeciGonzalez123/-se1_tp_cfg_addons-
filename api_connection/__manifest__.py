# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

# Copyright (c) 2011 CCI Connect asbl (http://www.cciconnect.be) All Rights Reserved.
#                       Philmer <philmer@cciconnect.be>
#########################################################################
{
    'name': 'Conexión API',
    'version': '1.0',
    'summary': 'Genera presupuestos de compra a partir de conexiones externas vía API',
    'author': 'Federico',
    'category': 'Purchases',
    'license': 'AGPL-3',
    'depends': ['base', 'purchase'],
    'data': [
        'security/ir.model.access.csv',
        'views/api_views.xml',
    ],
    'installable': True,
    'application': False,
}
#########################################################################