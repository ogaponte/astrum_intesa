# -*- coding: utf-8 -*-
from odoo import models, fields, api

class AstrumIntesaPurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'
    
    analytic_distribution_key = fields.Char(
        string="Distribución Analítica",
        compute="_compute_analytic_distribution_key",
        store=True,
    )
    
    money_exit = fields.Float(
        string="Salida de Dinero",
        compute="_compute_money_exit",
        store=True,
    )
    
    @api.depends('analytic_distribution')
    def _compute_analytic_distribution_key(self):
        for record in self:
            if record.analytic_distribution:
                # Extract the first key or the specific key you want to group by
                keys = list(record.analytic_distribution.keys())
                if keys:
                    # Get the analytic account name instead of just the ID
                    try:
                        analytic_account = self.env['account.analytic.account'].browse(int(keys[0]))
                        record.analytic_distribution_key = analytic_account.name if analytic_account else keys[0]
                    except (ValueError, TypeError):
                        record.analytic_distribution_key = keys[0]
                else:
                    record.analytic_distribution_key = False
            else:
                record.analytic_distribution_key = False
    
    @api.depends('price_subtotal', 'state')
    def _compute_money_exit(self):
        for record in self:
            # Money exit is the negative of price_subtotal for confirmed purchase orders
            if record.state in ['purchase', 'done']:
                record.money_exit = -record.price_subtotal
            else:
                record.money_exit = 0.0