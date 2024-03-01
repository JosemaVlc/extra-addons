# -*- coding: utf-8 -*-

from odoo import models, fields, api


class incidencia(models.Model):
    _name = 'incidencias.linea'
    _description = 'Linea'

    # Relacion material [1:N] linea
    material_id = fields.Many2one('incidencias.material',string='Producto') # Devolverá el material asociado.

    quantity = fields.Integer(string='Cantidad')

    # Relacion albaran [1:N] linea
    albaran_id = fields.Many2one('incidencias.albaran', readonly=True) # Devolverá el albarán asociado.