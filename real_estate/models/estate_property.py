from dateutil.relativedelta import relativedelta
from odoo import models, fields, api
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
    
    # Ejercicio 13 - Onchange garden
    @api.onchange('garden')
    def _onchange_garden(self):
        """Si se tilda 'garden', asigna 10 a garden_area.
        Si se destilda, pone 0."""
        if self.garden:
            self.garden_area = 10
        else:
            self.garden_area = 0
            
            
    # Ejercicio 14 - Onchange expected_price

    @api.onchange('expected_price')
    def _onchange_expected_price(self):
        """Muestra advertencia no bloqueante si expected_price < 10000"""
        if self.expected_price and self.expected_price < 10000:
            return {
                'warning': {
                    'title': "Precio esperado bajo",
                    'message': "El precio ingresado es menor a 10.000. "
                               "Verifique si no fue un error de tipeo.",
                }
            }
            
    # Ejercicio 15 - Botones Cancelar / Vender
    @api.onchange('expected_price')
    def action_cancel(self):
        """Botón 'Cancelar': no puede cancelar si ya está vendida"""
        for rec in self:
            if rec.state == 'sold':
                raise UserError("No se puede cancelar una propiedad vendida.")
            rec.state = 'canceled'

    def action_sold(self):
        """Botón 'Marcar como vendida': no puede vender si está cancelada"""
        for rec in self:
            if rec.state == 'canceled':
                raise UserError("No se puede vender una propiedad cancelada.")
            rec.state = 'sold'
