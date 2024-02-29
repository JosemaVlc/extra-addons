# -*- coding: utf-8 -*-

from odoo import models, fields, api


class incidencia(models.Model):
    _name = 'incidencias.albaran'
    _description = 'Albaran'
    
    name= fields.Char(string="Nº Albaran", readonly=1)

    # Relacion lineas [N:1] albaran
    lineas_ids = fields.One2many('incidencias.linea', 'albaran_id') #Devolverá todas las lineas.
    incidencia_id = fields.Many2one('incidencias.incidencia', compute='compute_albaran', inverse='stage_inverse')
    incidencias_ids = fields.One2many('incidencias.incidencia', 'albaran_id')

    @api.depends('incidencias_ids')
    def compute_albaran(self):
        if len(self.incidencias_ids) > 0:
            self.incidencia_id = self.incidencias_ids[0]

    def stage_inverse(self):
        if len(self.incidencias_ids) > 0:
            # delete previous reference
            incidencia = self.env['incidencias.incidencia'].browse(self.incidencias_ids[0].id)
            incidencia.albaran_id = False
        # set new reference
        self.incidencia_id.albaran_id = self

    _sql_constraints = [
        ('name_uniq', 'unique(name)', 'El numero de albaran debe ser único'),
    ]

    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('albaranes_secuencia')
        return super(incidencia, self).create(vals)