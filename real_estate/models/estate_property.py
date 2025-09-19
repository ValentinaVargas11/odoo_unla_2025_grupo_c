from dateutil.relativedelta import relativedelta
from odoo import models, fields
class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = 'Propiedades'

    name = fields.Char(string="Título", required =True)
    description = fields.Text(string = "Descripción")
    postcode = fields.Char(string = "Código Postal")
    date_availability = fields.Date(string="Fecha disponibilidad", 
                                    copy=False, 
                                    default=lambda self: fields.Date.today() + relativedelta(months=3))
    expected_price = fields.Float(string="Precio esperado")
    selling_price = fields.Float(string="Precio de venta", copy=False)
    bedrooms = fields.Integer(string="Habitaciones", default=2)
    living_area = fields.Integer(string="Superficie cubierta")
    facades = fields.Integer(string="Fachadas")
    garage = fields.Boolean(string="Garage")
    garden = fields.Boolean(string="Jardín")
    garden_orientation= fields.Selection(selection=[
                                            ('north', 'Norte'),
                                            ('south', 'Sur'),
                                            ('east', 'Este'),
                                            ('west', 'Oeste'),
                                            ],
                                            default="north",
                                            string="Orientación del jardín")
    garden_area = fields.Integer(string="Superficie jardín")
    state = fields.Selection(
        [
            ('new', 'Nuevo'),
            ('offer_received', 'Oferta recibida'),
            ('offer_accepted', 'Oferta aceptada'),
            ('sold', 'Vendido'),
            ('canceled', 'Cancelado')
        ],
        string="Estado",
        required=True,
        copy=False,
        default="new"
    )
    #Many2one al modelo estate.property.type
    property_type_id = fields.Many2one(
        comodel_name='estate.property.type',
        string='Tipo Propiedad'
    )

    #Many2one al modelo res.partner
    buyer_id = fields.Many2one(
        comodel_name='res.partner',
        string='Comprador'
    )

    #Many2one al modelo res.users
    salesman_id = fields.Many2one(
        comodel_name='res.users',
        string='Vendedor',
        copy=False,
        index=True,
        tracking=True,
        default=lambda self: self.env.user
    )

    # Ejercicio 35 - Relación Many2many 
    tag_ids = fields.Many2many(
        "estate.property.tag",
        string="Etiquetas"
    )

    # Ejercicio 36 - Relación One2Many 

    offer_ids = fields.One2many(
        comodel_name = "estate.property.offer",
        inverse_name = "property_id",
        string = "Ofertas"
    ) 