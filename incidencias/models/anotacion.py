# -*- coding: utf-8 -*-

from odoo import models, fields, api


class incidencia(models.Model):
    _name = 'incidencias.anotacion'
    _description = 'Anotaciones'

    name = fields.Text(string = 'Texto de la incidencia')
    date = fields.Date(string = 'Fecha')
    user = fields.Char(string = 'Usuario')

    # Relacion incidencia [1:N] anotaciones
    incidencia_id = fields.Many2one('incidencias.incidencia') # devolverá 1 incidencia.