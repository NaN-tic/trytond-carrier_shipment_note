# This file is part of carrier_shipment_note module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta

__all__ = ['ShipmentOut', 'ShipmentOutReturn']
__metaclass__ = PoolMeta


class ShipmentOut:
    __name__ = 'stock.shipment.out'
    carrier_note = fields.Text('Carrier Note')


class ShipmentOutReturn:
    __name__ = 'stock.shipment.out.return'
    carrier_note = fields.Text('Carrier Note')
