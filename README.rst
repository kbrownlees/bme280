===============================
BME280 Python Driver
===============================

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

* TODO


Installation (Package)
----------------------

For I2C access you must have the 'smbus' package available - for debian based systems install python-smbus.


Installation (Compile)
----------------------

For full instructions see https://pypi.python.org/pypi/smbus-cffi/

Basic:

        sudo apt-get install build-essential libi2c-dev i2c-tools python-dev libffi-dev
        pip install cffi smbus-cffi
        pip install bme280
