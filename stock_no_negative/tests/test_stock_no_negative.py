# -*- coding: utf-8 -*-
# © 2015-2016 Akretion (http://www.akretion.com)
# @author Alexis de Lattre <alexis.delattre@akretion.com>
# © 2016 Eficent Business and IT Consulting Services S.L.
#   (http://www.eficent.com)
# © 2016 Serpent Consulting Services Pvt. Ltd. (<http://www.serpentcs.com>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


from odoo.tests import common
from odoo.exceptions import ValidationError


@common.at_install(False)
@common.post_install(True)
class TestStockNoNegative(common.TransactionCase):

    def setUp(self):
        super(TestStockNoNegative, self).setUp()
        self.product_model = self.env['product.product']
        self.product_ctg_model = self.env['product.category']
        self.picking_type = self.env.ref('stock.picking_type_out')
        self.location = self.env.ref('stock.stock_location_stock')
        self.location_dest = self.env.ref('stock.stock_location_customers')
        # Create product category
        self.product_ctg = self._create_product_category()
        # Create a Product
        self.product = self._create_product('test_product1')
        self._create_picking()

    def _create_product_category(self):
        product_ctg = self.product_ctg_model.create({
            'name': 'test_product_ctg',
        })
        return product_ctg

    def _create_product(self, name):
        product = self.product_model.create({
            'name': name,
            'categ_id': self.product_ctg.id,
            'type': 'product',
        })
        return product

    def _create_picking(self):
        self.stock_picking = self.env['stock.picking'].create({
            'picking_type_id': self.picking_type.id,
            'move_type': 'direct',
            'location_id': self.location.id,
            'location_dest_id': self.location_dest.id
        })

        self.stock_move = self.env['stock.move'].create({
            'name': 'Test Move',
            'product_id': self.product.id,
            'product_uom_qty': 100.0,
            'product_uom': self.product.uom_id.id,
            'picking_id': self.stock_picking.id,
            'state': 'draft',
            'location_id': self.location.id,
            'location_dest_id': self.location_dest.id
        })

    def test_check_constrains(self):
        """Assert that constraint is raised when user
        tries to validate the stock operation which would
        make the stock level of the product negative """
        self.product.product_tmpl_id.write({'allow_negative_stock': False})
        self.location.write({'allow_negative_stock': False})
        self.stock_picking.action_confirm()
        self.stock_picking.action_assign()
        self.stock_picking.force_assign()
        self.stock_picking.do_new_transfer()
        self.stock_immediate_transfer = self.env['stock.immediate.transfer'].\
            create({'pick_id': self.stock_picking.id})
        with self.assertRaises(ValidationError):
            self.stock_immediate_transfer.with_context(
                test_stock_no_negative=True).process()

    def test_true_allow_negative_stock_product(self):
        """Assert that negative stock levels are allowed when
        the allow_negative_stock is set active in the product"""
        self.product.product_tmpl_id.write({'allow_negative_stock': True})
        self.location.write({'allow_negative_stock': False})
        self.stock_picking.action_confirm()
        self.stock_picking.action_assign()
        self.stock_picking.force_assign()
        self.stock_picking.do_new_transfer()
        self.stock_immediate_transfer = self.env['stock.immediate.transfer'].\
            create({'pick_id': self.stock_picking.id})
        self.stock_immediate_transfer.with_context(
            test_stock_no_negative=True).process()
        quant = self.env['stock.quant'].search([
            ('product_id', '=', self.product.id),
            ('location_id', '=', self.location.id)])
        self.assertEqual(quant.qty, -self.stock_move.product_uom_qty)

    def test_true_allow_negative_stock_location(self):
        """Assert that negative stock levels are allowed when
        the allow_negative_stock is set active in the location"""
        self.product.product_tmpl_id.write({'allow_negative_stock': False})
        self.location.write({'allow_negative_stock': True})
        self.stock_picking.action_confirm()
        self.stock_picking.action_assign()
        self.stock_picking.force_assign()
        self.stock_picking.do_new_transfer()
        self.stock_immediate_transfer = self.env['stock.immediate.transfer'].\
            create({'pick_id': self.stock_picking.id})
        self.stock_immediate_transfer.with_context(
            test_stock_no_negative=True).process()
        quant = self.env['stock.quant'].search([
            ('product_id', '=', self.product.id),
            ('location_id', '=', self.location.id)])
        self.assertEqual(quant.qty, -self.stock_move.product_uom_qty)
