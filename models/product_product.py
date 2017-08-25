# -*- coding: utf-8 -*-
###############################################################################
#
#    Odoo, Open Source Management Solution
#    Copyright (C) 2017 Humanytek (<www.humanytek.com>).
#    Manuel Márquez <manuel@humanytek.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

import openerp.addons.decimal_precision as dp
from openerp.exceptions import ValidationError
from openerp.osv import osv, fields
from openerp.tools.translate import _


class product_product(osv.osv):
    _inherit = 'product.product'

    def _product_lst_price(self, cr, uid, ids, name, arg, context=None):
        return super(product_product, self)._product_lst_price(
            cr, uid, ids, name, arg, context=context)

    def _set_product_lst_price(
        self, cr, uid, id, name, value, args, context=None):

        product = self.browse(cr, uid, id, context=context)
        if value <= product.standard_price:
            raise ValidationError(_(
                'The selling price can not be lower than cost.'))

        return super(product_product, self)._set_product_lst_price(
            cr, uid, id, name, value, args, context=context)

    _columns = {
        'lst_price': fields.function(
            _product_lst_price,
            fnct_inv=_set_product_lst_price,
            type='float',
            string='Sale Price',
            digits_compute=dp.get_precision('Product Price')),
    }
