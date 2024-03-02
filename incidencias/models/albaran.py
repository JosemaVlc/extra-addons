# -*- coding: utf-8 -*-

from odoo import models, fields, api


class incidencia(models.Model):
    _name = 'incidencias.albaran'
    _description = 'Albaran'
    
    date = fields.Date(string = 'Fecha', default=lambda self: fields.Datetime.now(), readonly=1)
    name= fields.Char(string="Nº Albaran", readonly=1)
    incidencia_id = fields.Many2one('incidencias.incidencia', string='Incidencia Asociada', required=True)
    warehouse_id = fields.Many2one('incidencias.almacen', string='Almacen', default=1)
    
    # Relacion lineas [N:1] albaran
    lineas_ids = fields.One2many('incidencias.linea', 'albaran_id', required=True) #Devolverá todas las lineas.

    total_price = fields.Float(compute='_compute_total', readonly=True, string="Total")

    _sql_constraints = [
        ('name_uniq', 'unique(name)', 'El numero de albaran debe ser único'),
    ]

    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('albaranes_secuencia')
        return super(incidencia, self).create(vals)
    
    @api.onchange('warehouse_id')
    def _onchange_warehouse(self):
        for record in self:
            record.lineas_ids.unlink()
    
    @api.depends('lineas_ids.price')
    def _compute_total(self):
        for record in self:
            total = sum(linea.price for linea in record.lineas_ids)
            record.total_price = total

