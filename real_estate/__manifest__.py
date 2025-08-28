{
    'name': 'Inmobiliaria',
    'author': 'UNLa',
    'version': '1.0.0',
    'description': 'Aplicacion para gestionar venta de propiedades',
    'depends': [
        'base'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/estate_menu_item.xml',
    ],
    'application': True,
}