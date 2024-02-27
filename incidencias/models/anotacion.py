# -*- coding: utf-8 -*-

from odoo import models, fields, api


class incidencia(models.Model):
    _name = 'incidencias.anotacion'
    _description = 'Anotaciones'

    # Relacion incidencia [1:N] anotaciones
    incidencia_id = fields.Many2one('incidencias.incidencia', readonly=1) # devolverá 1 incidencia.

    name = fields.Text(string = 'Texto de la anotación')
    date = fields.Date(string = 'Fecha', default=lambda self: fields.Datetime.now(), readonly=1)
    user = fields.Char(string = 'Usuario', default = lambda self: self.env.user.name, readonly=1)
