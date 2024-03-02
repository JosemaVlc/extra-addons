# -*- coding: utf-8 -*-

from odoo import models, fields, api


class incidencia(models.Model):
    _name = 'incidencias.almacen'
    _description = 'Almacen'

    name= fields.Char(string="Nombre de almacén")
    location= fields.Char(string="Ubicación")

    # Relacion albaranes [N:1] almacen
    albaranes_ids = fields.One2many('incidencias.albaran', 'warehouse_id', string='Albaranes')

    # Relacion material [N:1] almacen
    materiales_ids = fields.One2many('incidencias.material', 'warehouse_id') # Devolverá todos los materiales.
    
    _sql_constraints = [
        ('name_uniq', 'unique(name)', 'El nombre de almacen debe ser único'),
    ]

    # Poner en data almacenes y materiales