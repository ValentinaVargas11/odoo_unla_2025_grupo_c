{
    'name': 'Gestion de canales de Venta',
    'version': '1.0',
    'summary': '',
    'category': 'Sale channel management',
    'depends': [ 'base','stock','account', 'sale_management'],
    'data': [
        'security/ir.model.access.csv',
        'views/sale_channel_views.xml',
        'views/sale_channel_menu_item.xml',
        'views/sale_order_views.xml',
        'views/stock_picking_views.xml',
        'views/stock_picking_search_views.xml'
    ], 
    'installable': True,
    'application': True,
}