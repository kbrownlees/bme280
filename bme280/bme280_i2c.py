# -*- coding: utf-8 -*-

import smbus

bus_number = 1

default_i2c_address = 0x77
default_bus = smbus.SMBus(bus_number)


def read_byte_data(cmd, bus=None, i2c_address=None):
    if bus is None:
        bus = default_bus
    if i2c_address is None:
        i2c_address = default_i2c_address
    return bus.read_byte_data(i2c_address, cmd)


def write_byte_data(cmd, value, bus=None, i2c_address=None):
    if bus is None:
        bus = default_bus
    if i2c_address is None:
        i2c_address = default_i2c_address
    return bus.write_byte_data(i2c_address, cmd, value)
