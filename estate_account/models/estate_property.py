from odoo import Command, fields, models
from odoo.exceptions import UserError

class EstateProperty(models.Model):
    _inherit = "estate.property"

    def action_sold(self):
        #raise UserError("Estro al metodo del modulo estate_ acount")
        for property in self:
            self.env["account.move"].create = ({
                "partner_id": property.buyer_id.id,  # a. partner_id = comprador
                "move_type": "out_invoice",  # b. move_type = "out_invoice"
                "property_id": property.id,
                "line_ids": [
                    # c. Primera línea: nombre propiedad, cantidad 1, precio venta
                    Command.create({
                        "name": property.name,
                        "quantity": 1,
                        "price_unit": property.selling_price,
                    }),
                    # c. Segunda línea: "Gastos administrativos", cantidad 1, precio 100
                    Command.create({
                        "name": "Gastos administrativos",
                        "quantity": 1,
                        "price_unit": 100.0,
                    }),
                ],
            }) 
        return super().action_sold()