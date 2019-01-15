# -*- coding: UTF-8 -*-

from setuptools import find_packages, setup

setup(
    name='pysupla',
    description="Simple Supla's OpenAPI wrapper",
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'aiohttp',
        'pytest'
    ],

)