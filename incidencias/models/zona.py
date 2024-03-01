from odoo import models, fields, api
from odoo.exceptions import ValidationError

class zona(models.Model):
    _name = 'incidencias.zona'
    _description = 'Zonas Técnicas'

    name = fields.Char("Nombre")
    code = fields.Integer(string = 'Codigo Postal')

    tecnico_id = fields.Many2one('hr.employee', string='Tecnico Responsable de Zona', domain=[('department_id.name', '=', 'Tecnico')])
    pais = fields.Many2one('res.country', string='Pais')
    contrato_ids = fields.One2many('incidencias.contrato', 'zona_id', invisible=True, readonly=True)

    _sql_constraints = [
        ('name_uniq', 'unique(name)', 'El nombre de la zona debe ser único'),
    ]

    @api.constrains('tecnico_id')
    def _check_department_tecnico(self):
        for zona in self:
            if zona.tecnico_id and zona.tecnico_id.department_id.name != 'Tecnico':
                raise ValidationError('El técnico seleccionado no pertenece al departamento "Tecnico". Vaya al modulo empleados para introducir el empleado en tal departamento. Si esta solución no funcionara, pongase en contacto con el proveedor del modulo')