from odoo import models, Command
from odoo.exceptions import UserError


class EstateProperty(models.Model):
    _inherit = "estate.property"

    def action_sold(self):
        for property in self:
            self.env["account.move"].create = ({
                'partner_id': property.buyer_id.id,  # a. partner_id = comprador
                'move_type': 'out_invoice',  # b. move_type = "out_invoice"
                'invoice_line_ids': [
                    # c. Primera línea: nombre propiedad, cantidad 1, precio venta
                    Command.create({
                        'name': property.name,
                        'quantity': 1,
                        'price_unit': property.selling_price,
                    }),
                    # c. Segunda línea: "Gastos administrativos", cantidad 1, precio 100
                    Command.create({
                        'name': "Gastos administrativos",
                        'quantity': 1,
                        'price_unit': 100.0,
                    }),
                ],
            }) 
        return super().action_sold()