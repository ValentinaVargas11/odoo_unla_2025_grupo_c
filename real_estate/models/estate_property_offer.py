from odoo import models, fields
from odoo.exceptions import UserError

class EstatePropertyOffer(models.Model):
    _name = 'estate.property.offer'
    _description = 'Oferta sobre propiedad'

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
        string = "Propiedad", required = True
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
