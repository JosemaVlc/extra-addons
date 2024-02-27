from odoo import models, fields, api

class zona(models.Model):
    _name = 'incidencias.zona'
    _description = 'Zonas Técnicas'

    name = fields.Char("Nombre")
    code = fields.Integer(string = 'Codigo Postal')

    tecnicos_ids = fields.Many2one('hr.employee', string='Tecnico Responsable de Zona', domain=[('department_id.name', '=', 'Tecnico')])
    pais = fields.Many2one('res.country', string='Pais')

    _sql_constraints = [
        ('name_uniq', 'unique(name)', 'El nombre de la zona debe ser único'),
    ]