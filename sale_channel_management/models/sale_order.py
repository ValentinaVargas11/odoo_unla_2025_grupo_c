from odoo import fields, models, api

class SaleOrder(models.Model):
    # Heredamos del modelo 'sale.order' (que es de Odoo)
    _inherit = 'sale.order'

    # Punto 2.a: Añadimos el campo 'channel_id' a la orden de venta
    channel_id= fields.Many2one(
        'sale.channel',
        string='Canal de venta',
        required=True,
        tracking=True
    )

    # Punto 2.b: Añadimos la lógica 'onchange'
    @api.onchange('channel_id')
    def _onchange_channel_id(self):
        if self.channel_id and self.channel_id.warehouse_id:
            self.warehouse_id = self.channel_id.warehouse_id
        else:
            self.warehouse_id = False