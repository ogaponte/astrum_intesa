# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class astrum_intesa(models.Model):
#     _name = 'astrum_intesa.astrum_intesa'
#     _description = 'astrum_intesa.astrum_intesa'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

