# -*- coding: utf-8 -*-
from odoo import models, fields, api

class AstrumIntesaPurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'
    
    analytic_distribution_key = fields.Char(
        string="Analytic Distribution Key",
        compute="_compute_analytic_distribution_key",
        store=True,
    )
    
    @api.depends('analytic_distribution')
    def _compute_analytic_distribution_key(self):
        for record in self:
            if record.analytic_distribution:
                # Extract the first key or the specific key you want to group by
                keys = list(record.analytic_distribution.keys())
                record.analytic_distribution_key = keys[0] if keys else False
            else:
                record.analytic_distribution_key = False