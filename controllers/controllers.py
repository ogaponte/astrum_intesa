# -*- coding: utf-8 -*-
# from odoo import http


# class AstrumIntesa(http.Controller):
#     @http.route('/astrum_intesa/astrum_intesa', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/astrum_intesa/astrum_intesa/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('astrum_intesa.listing', {
#             'root': '/astrum_intesa/astrum_intesa',
#             'objects': http.request.env['astrum_intesa.astrum_intesa'].search([]),
#         })

#     @http.route('/astrum_intesa/astrum_intesa/objects/<model("astrum_intesa.astrum_intesa"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('astrum_intesa.object', {
#             'object': obj
#         })

