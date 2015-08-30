====================
BME280 Python Driver
====================

.. image:: https://img.shields.io/travis/kbrownlees/bme280.svg
        :target: https://travis-ci.org/kbrownlees/bme280

.. image:: https://img.shields.io/pypi/v/bme280.svg
        :target: https://pypi.python.org/pypi/bme280


Python Driver for the BME280 Temperature/Pressure/Humidity Sensor from Bosch.

* Free software: BSD license
* Documentation: https://bme280.readthedocs.org.

Full credit to https://github.com/IDCFChannel/bme280-meshblu-py for most of the logic, I simply packaged
/ tidied it.


Features
--------

* i2c reading of the bme280 Temperature/Pressure/Humidity sensor
* munin plugins for graphing the results


Installation (Package)
----------------------

For I2C access you must have the 'smbus' package available - for debian based systems install python-smbus.
If you wish to compile it, the packages required is smbus-cffi (https://pypi.python.org/pypi/smbus-cffi/)

Then:
        pip install bme280


Usage
-----

Adafruit have a good run through of setting up their break out version of the bme280 at
https://learn.adafruit.com/adafruit-bme280-humidity-barometric-pressure-temperature-sensor-breakout/wiring-and-test

You will need to know the i2c address being used by the bme280, it is usually 0x76 or 0x77. You can use

        i2cdetect -y 1

To verify which devices are connected.

Then:

        $ read_bme280 --help

        usage: read_bme280 [-h] [--pressure] [--humidity] [--temperature]
                           [--i2c-address I2C_ADDRESS] [--i2c-bus I2C_BUS]

        optional arguments:
          -h, --help            show this help message and exit
          --pressure
          --humidity
          --temperature
          --i2c-address I2C_ADDRESS
          --i2c-bus I2C_BUS

Example:

        $ read_bme280 --i2c-address 0x77

        1017.58 hPa
        50.55   ％
        19.03   ℃

Munin
-----

Three plugins are available in the /munin folder. To use them link them into /etc/munin/plugins:

        ln -s /path/to/bme280/munin* /etc/munin/plugins

You can configure the plugins by editing /etc/munin/plugin-conf.d/munin-node and adding:

        [bme280_*]
        group i2c
        env.I2C_ADDRESS 0x77


You can test it with:

        sudo munin-run bme280_humidity
