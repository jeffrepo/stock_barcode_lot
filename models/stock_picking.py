# -*- coding: utf-8 -*-

from odoo import fields, models, api, _
import logging

# class StockPickingOperation(models.Model):
#     _inherit = 'stock.move'
#
#     barcode = fields.Char('Barcode')
#
#     @api.onchange('barcode')
#     def _onchange_barcode(self):
#         if self.barcode and len(self.barcode) > 11:
#             product_id = self.env['product.product'].search([('barcode', '=', self.barcode[0:11])])
#             logging.warning('producto')
#             logging.warning(self.barcode[0:11])
#             if product_id:
#                 logging.warning(self.barcode[12:17])
#                 lot_id = self.env['stock.production.lot'].search([('name','=', self.barcode[11:17]),('product_id','=',product_id.id)])
#                 logging.warning(lot_id)
#                 self.product_id = product_id.id
#                 self.move_line_ids = []
#                 if lot_id:
#                     move_line_dic = {
#                         'location_id': self.picking_id.location_id.id,
#                         'location_dest_id': self.picking_id.location_dest_id.id,
#                         'product_id': product_id.id,
#                         'lot_id': lot_id.id,
#                         'move_id': self.id,
#                         'product_uom_id': product_id.uom_id.id,
#                         'qty_done': 1,
#                         'picking_id': self.picking_id._origin.id,
#                     }
#                     move_line_id = self.env['stock.move.line'].create(move_line_dic)
#                     logging.warning('LINE')
#                     logging.warning(move_line_id)
#                     logging.warning(self.picking_id._origin.id)
#                     logging.warning(self.id)

class StockMoveLine(models.Model):
    _inherit = 'stock.move.line'

    barcode = fields.Char('Barcode')

    @api.onchange('barcode')
    def _onchange_barcode(self):
        if self.barcode and len(self.barcode) > 11:
            product_id = self.env['product.product'].search([('barcode', '=', self.barcode[0:11])])
            logging.warning('producto')
            logging.warning(self.barcode[0:11])
            if product_id:
                logging.warning(self.barcode[12:17])
                lot_id = self.env['stock.production.lot'].search([('name','=', self.barcode[11:18]),('product_id','=',product_id.id)])
                logging.warning(lot_id)
                self.product_id = product_id.id
                if lot_id:
                    self.lot_id = lot_id.id
                    self.qty_done = 1
