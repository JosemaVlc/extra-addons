# -*- coding: utf-8 -*-

from odoo import models, fields, api


class incidencia(models.Model):
    _name = 'incidencias.albaran'
    _description = 'Albaran'
    
    code= fields.Integer(string="Nº Albaran")

    # Relacion lineas [N:1] albaran
    lineas_ids = fields.One2many('incidencias.linea', 'albaran_id') #Devolverá todas las lineas.