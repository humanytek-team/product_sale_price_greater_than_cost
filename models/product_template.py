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

from openerp import api, fields, models
from openerp.exceptions import ValidationError
from openerp.tools.translate import _


class ProductTemplate(models.Model):
    _inherit = "product.template"

    @api.constrains('list_price')
    def _check_list_price_greater_than_standard_price(self):
        """ Checks value of field list_price greater than value of field
        standard_price. """

        for record in self:
            if record.product_variant_ids.mapped('standard_price'):
                min_standard_price = min(
                    record.product_variant_ids.mapped('standard_price'))
                if record.list_price < min_standard_price:
                    raise ValidationError(_(
                        'The selling price can not be lower than cost.'))

    @api.model
    def create(self, vals):

        if vals.get('list_price') < vals.get('standard_price'):
            raise ValidationError(_(
                'The selling price can not be lower than cost.'))

        return super(ProductTemplate, self).create(vals)
