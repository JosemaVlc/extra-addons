# -*- coding: utf-8 -*-
{
    'name': "incidencias",

    'summary': """
        Herramienta que le permite gestionar y dar seguimiento a las incidencias de los cliente
    """,

    #'description': """
    #    Long description of module's purpose
    #""",

    'author': "JosemaVlc",
    'website': "https://josemavlc.github.io/modulo_incidencias/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr'],

    'external_dependencies': {
        'python':['geopy']
    },
    # revisar requiredment para revisar e instalar dependencias

    # always loaded
    'data': [
        # seguridad
        'security/grupos.xml',
        'security/ir.model.access.csv',
        # vistas
        'views/views.xml',
        'views/templates.xml',
        # importacion de datos
        'data/autoincrementales.xml',
        'data/zona.xml',
        'data/almacen.xml',
        'data/material.xml',
        # reports
        'reports/incidencias_report_template.xml'

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
