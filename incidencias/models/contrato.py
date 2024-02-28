# -*- coding: utf-8 -*-

from odoo import models, fields, api
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

class contrato(models.Model):
    _name = 'incidencias.contrato'
    _description = 'Contratos'

    name = fields.Char(string = 'NºContrato', readonly=1)
    #number = fields.Integer(string = 'Zona Tecnica', compute='_compute_zona_tecnica', store=True)
    service_tlf = fields.Boolean(string = 'Tlf')
    service_tv = fields.Boolean(string = 'Tv')
    service_net = fields.Boolean(string = 'Net')

    zona_tecnica = fields.Char(string = 'CP Zona Tecnica', compute = '_compute_cp')
    # Relacion zona [1:N] contrato
    zona_id = fields.Many2one('incidencias.zona', 'Zona Tecnica', compute = '_compute_zona_tecnica', store = True) # Devolverá su cliente las incidencias.
    
    # Relacion incidencia [N:1] contrato
    incidencia_ids = fields.One2many('incidencias.incidencia', 'contrato_id') # Devolverá todas las incidencias.

    # Relacion cliente [1:N] contrato
    partner_id = fields.Many2one('res.partner', 'Cliente', domain=[('active','=',True)]) # Devolverá su cliente las incidencias.

    _sql_constraints = [
        ('name_uniq', 'unique(name)', 'El numero de contrato debe ser único')
    ]

    def codigo_postal_mas_cercano(self, codigos_postales, paises, codigo_postal_referencia, pais_referencia):

        # Crear un geolocalizador
        geolocalizador = Nominatim(user_agent="modulo_incidencias")

        # Obtener las coordenadas del código postal de referencia
        referencia = geolocalizador.geocode(codigo_postal_referencia + ", " + pais_referencia)
        coordenadas_referencia = (referencia.latitude, referencia.longitude)

        # Inicializar variables para el código postal más cercano y su distancia
        codigo_postal_mas_cercano = None
        distancia_minima = float('inf')

        # Iterar sobre la lista de códigos postales
        it = 0        
        for cp in codigos_postales:
            pais = paises[it]
            # Obtener las coordenadas del código postal actual
            ubicacion_cp = geolocalizador.geocode(cp + ", " + pais)
            coordenadas_cp = (ubicacion_cp.latitude, ubicacion_cp.longitude)

            # Calcular la distancia entre el código postal actual y el de referencia
            distancia = geodesic(coordenadas_referencia, coordenadas_cp).kilometers

            # Actualizar el código postal más cercano si se encuentra uno más cercano
            if distancia < distancia_minima:
                codigo_postal_mas_cercano = cp
                distancia_minima = distancia
            it += 1

        return codigo_postal_mas_cercano
    
    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('contratos_secuencia')
        return super(contrato, self).create(vals)
    
    @api.depends('partner_id')
    def _compute_cp(self):
        codigos_postales = []
        paises = []
        zonas = self.env['incidencias.zona'].search([])
        for zona in zonas:
            codigos_postales.append(str(zona.code))
            paises.append(str(zona.pais.name))


        for record in self:
            if (self.partner_id.zip != False):
                codigo_postal_referencia = str(self.partner_id.zip)          
                pais_referencia = self.partner_id.country_id.name
                record.zona_tecnica = record.codigo_postal_mas_cercano(codigos_postales, paises, codigo_postal_referencia, pais_referencia)
            else:
                record.zona_tecnica = False

    @api.depends('zona_tecnica')
    def _compute_zona_tecnica(self):
        for record in self:
            if record.zona_tecnica:
                zona = self.env['incidencias.zona'].search([('code', '=', record.zona_tecnica)], limit=1)
                if zona:
                    record.zona_id = zona.id
            else:
                record.zona_id = False
        

    
