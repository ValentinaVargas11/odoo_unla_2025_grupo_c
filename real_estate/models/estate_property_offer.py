from odoo import models, fields
from datetime import timedelta
from odoo import api
from odoo.exceptions import UserError

class EstatePropertyOffer(models.Model):
    _name = 'estate.property.offer'
    _description = 'Oferta sobre propiedad'

    #Ejercicio 18 uni 2
    _sql_constraints = [
        ("unique_offer_id", "UNIQUE(partner_id, property_id)", "Una misma persona no puede hacer mas de una oferta en la misma propiedad")
    ]


    price = fields.Float(string="Precio", required=True)
    status = fields.Selection(
        [
            ('accepted', 'Aceptada'),
            ('refused', 'Rechazada'),
        ]
    )
    partner_id = fields.Many2one(
        comodel_name = "res.partner",
        string = "Ofertante", required = True,
    )
    property_id = fields.Many2one(
        comodel_name = "estate.property",
        string = "Propiedad", required = True,
        ondelete='cascade'
    )
    
    # Unidad 2 - Ejercicio 16 
    def action_accept_offer(self):
        for offer in self:
            if offer.status == 'accepted':
                raise UserError("Esta oferta ya fue aceptada.")
            offer.status = 'accepted'

            property = offer.property_id
            property.buyer_id = offer.partner_id
            property.selling_price = offer.price
            property.state = 'offer_accepted'

            other_offers = property.offer_ids - offer
            other_offers.write({'status': 'refused'})

    def action_refuse_offer(self):
        for offer in self:
            if offer.status == 'accepted':
                raise UserError("No se puede rechazar una oferta ya aceptada.")
            offer.status = 'refused'


    #Punto 11
    #property_type_name = fields.Char(
    #string="Tipo propiedad",
    #related='property_id.property_type_name',
    #store=True,
    #)
    property_type_id = fields.Many2one(
    comodel_name='estate.property.type',
    string="Tipo de propiedad",
    related='property_id.property_type_id',
    store=True,
)

    

    #Punto 9
    validity = fields.Integer(
        string="Validez (días)",
        default=7
    )
    date_deadline = fields.Date(
    string="Fecha límite",
    #Parte del punto 10
    compute="_compute_date_deadline",
    inverse="_inverse_date_deadline",
    store=True,
    )
    
    #Punto 10
    @api.depends('create_date', 'validity')
    def _compute_date_deadline(self):
        for record in self:
            create = record.create_date or fields.Datetime.now()
            record.date_deadline = create.date() + timedelta(days=record.validity)

    def _inverse_date_deadline(self):
        for record in self:
            create = record.create_date or fields.Datetime.now()
            if record.date_deadline:
                record.validity = (record.date_deadline - create.date()).days

    @api.model
    def create(self, data_list):
        if not isinstance(data_list, list):
            data_list = [data_list]
        for data in data_list:
            property_id= self.env["estate.property"].browse(data["property_id"])
            offer_ids = property_id.offer_ids
            if property_id.state not in ('new','offer_received'):
                raise UserError(f"No se pueden crear ofertas para una propiedad que está en estado '{property_id.state}'.")
            elif offer_ids and data["price"]<= max(offer_ids.mapped("price")) if offer_ids else 0 :
                raise UserError("La oferta no debe ser menor a la oferta mejor registrada")
            
        new_offers = super(EstatePropertyOffer, self).create(data_list)
        properties_to_update = new_offers.mapped('property_id')
        if properties_to_update:
            properties_to_update.write({'state':'offer_received'})
        return new_offers
