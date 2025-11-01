from odoo import models, fields, api

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    channel_id = fields.Many2one(
        'sale.channel',
        string='Canal de venta',
        readonly=False
    )

    @api.model_create_multi
    def create(self, vals_list):
        pickings = super().create(vals_list)
        for picking in pickings:
            # Si viene de una orden de venta con canal, se propaga
            if picking.origin:
                sale = self.env['sale.order'].search([('name', '=', picking.origin)], limit=1)
                if sale and sale.sale_channel_id:
                    picking.sale_channel_id = sale.sale_channel_id.id
        return pickings
