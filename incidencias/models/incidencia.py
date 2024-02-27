# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError



class incidencia(models.Model):
    _name = 'incidencias.incidencia'
    _description = 'Incidencias'

    name = fields.Char(string = 'NºIncidencia')
    fecha_entrada = fields.Datetime(string='Entrada', default=lambda self: fields.Datetime.now(), readonly=True)
    fecha_planificada = fields.Datetime(string = 'Planificación')
    fecha_solucion = fields.Datetime(string = 'Solución', readonly=True)
    fase = fields.Selection([('0', 'Entrada'), ('1', 'En Progreso'), ('2', 'Solucionada')], required=True, default='0')
    incidence_text = fields.Text(string = 'Texto de la incidencia', required=True)
    solution_text = fields.Text(string = 'Texto de la solución')
    service_tlf = fields.Boolean(string = 'Tlf', compute='_compute_client_info')
    service_tv = fields.Boolean(string = 'Tv', compute='_compute_client_info')
    service_net = fields.Boolean(string = 'Net', compute='_compute_client_info')
    cliente_nif = fields.Char(string='NIF', compute='_compute_client_info')
    cliente_nombre = fields.Char(string='Nombre', compute='_compute_client_info')
    cliente_calle = fields.Char(string='Direccion', compute='_compute_client_info', store=True)
    cliente_ciudad = fields.Char(string='Municipio', compute='_compute_client_info', store=True)
    cliente_provincia = fields.Char(string='Provincia', compute='_compute_client_info', store=True)
    cliente_telefono = fields.Char(string='Telefono', compute='_compute_client_info')
    cliente_movil = fields.Char(string='Movil', compute='_compute_client_info')
    cliente_email = fields.Char(string='Email', compute='_compute_client_info')
    cliente_zona_tecnica = fields.Char(string='Zona Tecnica', compute='_compute_client_info')

    
    # Relacion contrato [1:N] incidencia
    contrato_id = fields.Many2one('incidencias.contrato') # devolverá 1 contrato.
    # Relacion anotacion [N:1] incidencia
    annotations_ids = fields.One2many('incidencias.anotacion', 'name') # devolverá todas las anotaciones.
    

    _sql_constraints = [
        ('name_uniq', 'unique(name)', 'El numero de contrato debe ser único'),
    ]
    
    @api.depends('contrato_id')
    def _compute_client_info(self):
        for incidencia in self:
            if incidencia.contrato_id:
                self.service_net = incidencia.contrato_id.service_net
                self.service_tlf = incidencia.contrato_id.service_tlf
                self.service_tv = incidencia.contrato_id.service_tv
                self.cliente_nif = incidencia.contrato_id.partner_id.vat
                self.cliente_nombre = incidencia.contrato_id.partner_id.name
                self.cliente_calle = incidencia.contrato_id.partner_id.street
                self.cliente_ciudad = incidencia.contrato_id.partner_id.city
                state_id = incidencia.contrato_id.partner_id.state_id.id
                state_record = incidencia.env['res.country.state'].browse(state_id)
                self.cliente_telefono = incidencia.contrato_id.partner_id.phone
                self.cliente_movil = incidencia.contrato_id.partner_id.mobile
                self.cliente_email = incidencia.contrato_id.partner_id.email
                self.cliente_provincia = state_record.name
                self.cliente_zona_tecnica = incidencia.contrato_id.zona_id.name
            else:
                self.cliente_nif = ""
                self.cliente_nombre = ""
                self.cliente_calle = ""
                self.cliente_ciudad = ""
                self.cliente_provincia = ""
                self.cliente_telefono = ""
                self.cliente_movil = ""
                self.cliente_email = ""
                self.service_net = ""
                self.service_tlf = ""
                self.service_tv = ""
                self.cliente_nif = ""
                self.cliente_zona_tecnica = ""

    def funcion_confirmar(self):
        if self.fase == '0':
            if self.fecha_planificada != False and self.fecha_entrada <= self.fecha_planificada:
                futuro_estado = int(self.fase)+1
                self.write({'fase':str(futuro_estado)})
            else:
                raise ValidationError("¡No es posible confirmar con fecha de planificación anterior a la de entrada o sin fecha de planificación")

        elif self.fase == '1':
            if not self.solution_text:
                raise ValidationError("¡Sin texto de solucion no es posible solucionar la incidencia!")
            if self.solution_text != '':
                futuro_estado = int(self.fase)+1
                self.write({'fase':str(futuro_estado)})
                self.fecha_solucion = fields.Datetime.now()

    def funcion_cambiar_tecnico(self):
        pass
