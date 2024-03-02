# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class incidencia(models.Model):
    _name = 'incidencias.linea'
    _description = 'Linea'

    # Relacion material [1:N] linea
    material_id = fields.Many2one('incidencias.material', string='Producto', domain="[('warehouse_id', '=', warehouse_associated_id)]" , required=True) # Devolverá el material asociado.    
    code = fields.Char(related="material_id.code", string="Codigo")
    unit_price = fields.Float(related="material_id.price", string="Precio Unitario")
    quantity = fields.Integer(string='Cantidad', required=True)
    price = fields.Float(compute="_compute_price", string="Precio")

    # Relacion albaran [1:N] linea
    albaran_id = fields.Many2one('incidencias.albaran', readonly=True) # Devolverá el albarán asociado.
    warehouse_associated_id = fields.Many2one(related='albaran_id.warehouse_id', string='Almacen')

    @api.depends('material_id', 'quantity', 'unit_price')
    def _compute_price(self):
        for record in self:
            if (record.material_id and record.unit_price and record.quantity):
                record.price = record.unit_price * record.quantity
            else:
                record.price = 0.0

    @api.onchange('material_id', 'quantity')
    def _onchange_avalible_units(self):
        for record in self:
            if record.quantity > record.material_id.unit:
                record.quantity = 0
                raise ValidationError("¡No es posible consumir más unidades de las existentes")
            
    @api.constrains('material_id')
    def _check_warehouse(self):
        for record in self:
            if record.material_id.warehouse_id != record.warehouse_associated_id:
                raise ValidationError("Uno de los materiales seleccionados no pertenece al almacén asociado al albarán.")
    
    # Restricción SQL única para asegurar que solo haya una línea por material en un albarán
    _sql_constraints = [
        ('unique_material_in_albaran', 'unique(albaran_id, material_id)', 'No es posible tener dos lineas con el mismo producto.'),
    ]

