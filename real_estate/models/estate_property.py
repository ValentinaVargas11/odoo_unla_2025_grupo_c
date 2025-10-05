from dateutil.relativedelta import relativedelta
from odoo import api,models, fields
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

    # Ejercicio 1 - 5 - Uni 2 Campo computado
    total_area = fields.Integer(string="Superficie Total", compute="_compute_total_area", store=True)

    @api.depends("living_area", "garden_area")
    def _compute_total_area(self):
        for property in self:
            property.total_area = property.living_area + property.garden_area

    # Ejercicio 7  Uni 2 Campo computado
    best_offer = fields.Float(string="Mejor oferta", compute="_compute_best_offer")

    @api.depends("offer_ids.price")
    def _compute_best_offer(self):
        for property in self:
            property.best_offer = max(property.mapped('offer_ids.price'))

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