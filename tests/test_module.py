
# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.

from trytond.modules.company.tests import CompanyTestMixin
from trytond.tests.test_tryton import ModuleTestCase


class SaleOpportunityCategoryTestCase(CompanyTestMixin, ModuleTestCase):
    'Test SaleOpportunityCategory module'
    module = 'sale_opportunity_category'


del ModuleTestCase
