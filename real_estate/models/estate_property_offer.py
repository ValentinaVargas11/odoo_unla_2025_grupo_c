from odoo import models, fields

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
    
    # Ejercicio 16 - Botón Aceptar oferta
    def action_accept_offer(self):
        """Aceptar una oferta:
        - marca comprador y precio en la propiedad
        - cambia estado de la propiedad a 'offer_accepted'
        - marca esta oferta como aceptada y las demás como rechazadas
        """
        for offer in self:
            # 1. carga el comprador y precio en la propiedad
            offer.property_id.buyer_id = offer.partner_id
            offer.property_id.selling_price = offer.price

            # 2. cambia el estado de la propiedad
            offer.property_id.state = 'offer_accepted'

            # 3. actualiza los estados
            offer.status = 'accepted'
            # rechaza las demás ofertas
            other_offers = offer.property_id.offer_ids - offer
            other_offers.write({'status': 'refused'})