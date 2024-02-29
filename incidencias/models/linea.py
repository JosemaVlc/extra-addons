# -*- coding: utf-8 -*-

from odoo import models, fields, api


class incidencia(models.Model):
    _name = 'incidencias.linea'
    _description = 'Linea'

    # Relacion material [1:N] linea
    material_id = fields.Many2one('incidencias.material') # Devolverá el material asociado.
    # Relacion albaran [1:N] linea
    albaran_id = fields.Many2one('incidencias.albaran') # Devolverá el albarán asociado.