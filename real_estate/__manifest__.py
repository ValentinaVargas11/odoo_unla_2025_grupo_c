{
    'name': 'Inmobiliaria',
    'author': 'UNLa',
    'version': '1.0.0',
    'summary': 'Un módulo creado en forma de practica para aprender Odoo',
    'description': 'Aplicacion para gestionar venta de propiedades',
    'category': 'Tools',
    'depends': [
        'base'
    ],
    'data': [
        'security/real_estate_res_groups.xml',
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/estate_property_type_views.xml',
        'views/estate_property_tag_views.xml',
        'views/estate_property_offer_views.xml',
        'views/estate_menu_item.xml',
    ],
    'installable': True,
    'application': True,
}