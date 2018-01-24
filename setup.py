#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


readme = """
For installation instructions see https://github.com/kbrownlees/bme280/blob/master/README.rst
"""

with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

requirements = [
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='bme280',
    version='0.4',
    description="Python Driver for the BME280 Temperature/Pressure/Humidity Sensor from Bosch.",
    long_description=readme + '\n\n' + history,
    author="Kieran Brownlees",
    author_email='kieran@mootium.co',
    url='https://github.com/kbrownlees/bme280',
    packages=[
        'bme280',
    ],
    package_dir={'bme280': 'bme280'},
    entry_points={
        'console_scripts': [
            'read_bme280 = bme280.bme280:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="BSD",
    zip_safe=False,
    keywords='bme280',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
