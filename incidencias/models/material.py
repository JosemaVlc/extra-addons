# -*- coding: utf-8 -*-

from odoo import models, fields, api


class incidencia(models.Model):
    _name = 'incidencias.material'
    _description = 'Material'

    name=fields.Char(string="Nombre", required=True)
    code=fields.Char(string="Código de producto", required=True)
    description=fields.Char(string="Descripción", required=True)
    unit=fields.Integer(string="Unidades", required=True)
    price=fields.Float(string="Precio", required=True)

    # Relacion almacen [1:N] material
    warehouse_id = fields.Many2one('incidencias.almacen', required=True) # Devolverá el almacen.
    # Relacion linea [N:1] material
    lineas_ids = fields.One2many('incidencias.linea', 'material_id') # Devolverá todas las lineas con dicho material.  

    _sql_constraints = [
        ('name_uniq', 'unique(code)', 'El codigo de producto debe ser único'),
    ]