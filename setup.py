#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import sys

from os import path as p

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

sys.dont_write_bytecode = True

setup(
    name='lambdaconf-tutorial',
    version='0.5.0',
    description='Materials for the LambdaConf tutorial',
    author='Reuben Cummings',
    author_email='reubano@gmail.com',
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    install_requires=['riko==0.51.0','meza==0.37.0'],
    zip_safe=False
)
