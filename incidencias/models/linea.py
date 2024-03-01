# -*- coding: utf-8 -*-

from odoo import models, fields, api


class incidencia(models.Model):
    _name = 'incidencias.linea'
    _description = 'Linea'

    # Relacion material [1:N] linea
    material_id = fields.Many2one('incidencias.material', string='Producto') # Devolverá el material asociado.
    code = fields.Char(related="material_id.code", string="Codigo")
    unit_price = fields.Float(related="material_id.price", string="Precio Unitario")
    quantity = fields.Integer(string='Cantidad')
    price = fields.Float(compute="_compute_price", string="Precio")

    # Relacion albaran [1:N] linea
    albaran_id = fields.Many2one('incidencias.albaran', readonly=True) # Devolverá el albarán asociado.

    @api.depends('material_id', 'quantity', 'quantity')
    def _compute_price(self):
        for record in self:
            if (record.material_id and record.unit_price and record.quantity):
                self.price = self.unit_price * self.quantity
            else:
                self.price = 0.0