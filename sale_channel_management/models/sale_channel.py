from odoo import fields, models

class SaleChannel(models.Model):
    _name = 'sale.channel'
    _description = 'Canal de Venta'
    
    name = fields.Char(string='Nombre', required=True)
    code = fields.Char(string='Codigo', required=True, copy=False)
    warehouse_id = fields.Many2one(
        'stock.warehouse',
        string='Deposito'
    )
    journal_id = fields.Many2one(
        'account.journal',
        string='Diario de factura'
    )
    _sql_constraints = [
        ('code_unique', 'UNIQUE(code)','El codigo del canal de venta debe ser unico!')
    ]