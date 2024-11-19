#########################################################################
from odoo import models, fields, api

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    api_created = fields.Boolean(string="Creado vía API", default=False)    #Creamos un campo para controlar que sea creado por API
    state = fields.Selection(selection_add=[('bloqueado', 'Bloqueado')])    #Creamos un campo para controlar el estado de la compra
#########################################################################