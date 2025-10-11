from odoo import models, fields, api
from odoo.exceptions import UserError
from odoo import Command

class EstateProperty(models.Model):
    _inherit = "estate.property"
    
    def action_sold(self):
        # Llama al método original primero para validaciones
        result = super().action_sold()
        
        # Crea la factura para cada propiedad vendida
        for property in self:
            if not property.buyer_id:
                raise UserError("Debe seleccionar un comprador antes de generar la factura.")
            
            # Crea la factura
            invoice_vals = {
                'partner_id': property.buyer_id.id,
                'move_type': 'out_invoice',
                'invoice_line_ids': [
                    Command.create({
                        'name': f"Venta de propiedad: {property.name}",
                        'quantity': 1,
                        'price_unit': property.selling_price,
                    }),
                    Command.create({
                        'name': "Gastos administrativos",
                        'quantity': 1,
                        'price_unit': 100.0,
                    }),
                ]
            }
            
            # Crea el registro de factura
            invoice = self.env['account.move'].create(invoice_vals)
            property.message_post(body=f"Factura generada: {invoice.name}")
            
        return result