# This file is part of the carrier_shipment_note module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class CarrierShipmentNoteTestCase(ModuleTestCase):
    'Test Carrier Shipment Note module'
    module = 'carrier_shipment_note'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        CarrierShipmentNoteTestCase))
    return suite