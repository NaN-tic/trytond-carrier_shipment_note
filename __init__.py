# This file is part of the carrier_shipment_note module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import Pool
from . import shipment

def register():
    Pool.register(
        shipment.ShipmentOut,
        shipment.ShipmentOutReturn,
        module='carrier_shipment_note', type_='model')
