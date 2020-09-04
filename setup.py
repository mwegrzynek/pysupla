# -*- coding: UTF-8 -*-
import pathlib
from setuptools import find_packages, setup


HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()
VERSION = '0.0.5'

setup(
    name='pysupla',
    description="Simple Supla's OpenAPI wrapper",
    long_description=README,
    long_description_content_type="text/markdown",
    author='Michal Wegrzynek',
    author_email='michal.wegrzynek@malloc.com.pl',
    url='https://github.com/mwegrzynek/pysupla',
    license='Apache License',
    version=VERSION,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: Apache Software License',
        'Topic :: Software Development :: Libraries',
        'Topic :: Home Automation'
    ],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'requests'
    ]
)