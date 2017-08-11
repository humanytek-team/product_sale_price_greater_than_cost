# Change Log
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## [Unreleased]
### Added
- Adds constraint to model of Products Templates (product.template) that checks that the selling price of the product not be lower than cost.
- Extends method create of model Products Templates (product.template) for validate that the selling price not be lower than cost on create operation.
- Extends method _set_product_lst_price() of model Variants (product.product) to prevent that the selling price of a variant be lower than the cost.
- Adds method of constraint over field price_extra in model Attibutes of Products (product.attribute.value) that checks that the new price of the attribute does not cause that the sale price of one or several variants is below the cost of the same.
