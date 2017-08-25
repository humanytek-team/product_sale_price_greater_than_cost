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

from openerp import api, models
from openerp.exceptions import ValidationError
from openerp.tools.translate import _


class ProductAttributeValue(models.Model):
    _inherit = "product.attribute.value"

    @api.constrains('price_extra')
    def _check_price_extra(self):
        """ Checks that price extra of attribute does not causes that the sale
        price of the variants of the template that contain it be lower than
        cost. """

        for record in self:

            product_tmpl_id = self.env.context.get('default_product_tmpl_id')
            if product_tmpl_id:
                ProductProduct = self.env['product.product']
                attribute_id = self.attribute_id.id
                attribute_value = self.name
                product_template_variants = ProductProduct.search([
                    ('product_tmpl_id', '=', product_tmpl_id),
                    ('attribute_value_ids.attribute_id.id', '=', attribute_id),
                    ('attribute_value_ids.name', '=', attribute_value),
                ])

                for variant in product_template_variants:

                    if variant.lst_price <= variant.standard_price:
                        raise ValidationError(_(
                                'The new price of the attribute causes that the sale price of one or several variants is below the cost of the same.'
                                ))
