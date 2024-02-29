# -*- coding: utf-8 -*-

from odoo import models, fields, api


class incidencia(models.Model):
    _name = 'incidencias.almacen'
    _description = 'Almacen'

    name= fields.Char(string="Nombre de almacén")
    location= fields.Char(string="Ubicación")

    # Relacion material [N:1] almacen
    materiales_ids = fields.One2many('incidencias.material', 'almacen_id') # Devolverá todos los materiales.