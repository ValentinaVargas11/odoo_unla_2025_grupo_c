from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    canal_id = fields.Many2one('sale.channel', string='Canal de venta')

    @api.model
    def _create_invoices(self, grouped=False, final=False):
        # Llamamos al método original para crear las facturas
        invoices = super()._create_invoices(grouped=grouped, final=final)

        # Por cada orden, si tiene canal y diario definido, lo aplicamos
        for order in self:
            if order.canal_id and order.canal_id.journal_id:
                invoices.filtered(lambda inv: inv.invoice_origin == order.name).write({
                    'journal_id': order.canal_id.journal_id.id
                })

        return invoices
