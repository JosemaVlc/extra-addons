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
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'data/zona.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
