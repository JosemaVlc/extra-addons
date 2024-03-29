# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError



class incidencia(models.Model):
    _name = 'incidencias.incidencia'
    _description = 'Incidencias'

    name = fields.Char(string = 'NºIncidencia', readonly=1)
    fecha_entrada = fields.Datetime(string='Entrada', default=lambda self: fields.Datetime.now(), readonly=True)
    fecha_planificada = fields.Datetime(string = 'Planificación')
    fecha_solucion = fields.Datetime(string = 'Solución', readonly=True)
    fase = fields.Selection([('ENT', 'Entrada'), ('PRO', 'En Progreso'), ('SOL', 'Solucionada')], required=True, default='ENT')
    incidence_text = fields.Text(string = 'Texto de la incidencia', required=True)
    solution_text = fields.Text(string = 'Texto de la solución')
    service_tlf = fields.Boolean(string = 'Tlf', related="contrato_id.service_tlf")
    service_tv = fields.Boolean(string = 'Tv', related="contrato_id.service_tv")
    service_net = fields.Boolean(string = 'Net', related="contrato_id.service_net")
    cliente_nif = fields.Char(string='NIF', related="contrato_id.partner_id.vat", store=True)
    cliente_nombre = fields.Char(string='Nombre', related='contrato_id.partner_id.name')
    cliente_calle = fields.Char(string='Direccion', related='contrato_id.partner_id.street', store=True)
    cliente_ciudad = fields.Char(string='Municipio', related='contrato_id.partner_id.city', store=True)
    cliente_telefono = fields.Char(string='Telefono', related='contrato_id.partner_id.phone')
    cliente_movil = fields.Char(string='Movil', related='contrato_id.partner_id.mobile')
    cliente_email = fields.Char(string='Email', related='contrato_id.partner_id.email')
    cliente_zona_tecnica = fields.Char(string='Zona Tecnica', related='contrato_id.zona_id.name')
    cliente_tecnico_asociado = fields.Char(string="Tecnico Asociado", related='contrato_id.zona_id.tecnico_id.name')

    cliente_provincia = fields.Char(string='Provincia', compute='_compute_client_info', store=True)

    
    # Relacion contrato [1:N] incidencia
    contrato_id = fields.Many2one('incidencias.contrato', readonly=True, store=True) # devolverá 1 contrato.
    # Relacion anotacion [N:1] incidencia
    annotations_ids = fields.One2many('incidencias.anotacion', 'incidencia_id') # devolverá todas las anotaciones.
    # Relación albaran [1:1] incidencia
    albaran_id = fields.One2many('incidencias.albaran', 'incidencia_id', string='Albaran de consumo')

    _sql_constraints = [
        ('name_uniq', 'unique(name)', 'El numero de contrato debe ser único'),
    ]    
    
    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('incidencias_secuencia')
        return super(incidencia, self).create(vals)
    
    @api.depends('contrato_id')
    def _compute_client_info(self):
        for incidencia in self:
            if incidencia.contrato_id:
                state_id = incidencia.contrato_id.partner_id.state_id.id
                state_record = incidencia.env['res.country.state'].browse(state_id)
                self.cliente_provincia = state_record.name
            else:
                self.cliente_provincia = ""

    def funcion_confirmar(self):
        if self.fase == 'ENT':
            if self.fecha_planificada != False and self.fecha_entrada <= self.fecha_planificada:
                self.write({'fase':'PRO'})
            else:
                raise ValidationError("¡No es posible confirmar con fecha de planificación anterior a la de entrada o sin fecha de planificación")

        elif self.fase == 'PRO':
            if not self.solution_text:
                raise ValidationError("¡Sin texto de solucion no es posible solucionar la incidencia!")
            if self.solution_text != '':
                self.write({'fase':'SOL'})
                self.fecha_solucion = fields.Datetime.now()

    def funcion_cambiar_tecnico(self):
        pass