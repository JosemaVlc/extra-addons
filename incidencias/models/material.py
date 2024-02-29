# -*- coding: utf-8 -*-

from odoo import models, fields, api


class incidencia(models.Model):
    _name = 'incidencias.material'
    _description = 'Material'

    name=fields.Char(string="Nombre")
    code=fields.Char(string="Código de producto")
    description=fields.Char(string="Descripción")
    unit=fields.Integer(string="Unidades")
    price=fields.Float(string="Precio")

    # Relacion almacen [1:N] material
    almacen_id = fields.Many2one('incidencias.almacen') # Devolverá el almacen.
    # Relacion linea [N:1] material
    lineas_ids = fields.One2many('incidencias.linea', 'material_id') # Devolverá todas las lineas con dicho material.  

    _sql_constraints = [
        ('name_uniq', 'unique(code)', 'El codigo de producto debe ser único'),
    ]