#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages

setup(
    name='cfpb-django-app',
    url='http://cfpb.github.io',
    author='CFPB',
    author_emaill='tech@cfpb.gov',
    license='CC0',
    version='0.1.0',
    description='A utility to create a CFPB-style Django app',

    # Read the README for the long description
    long_description=open('README.md').read() \
            if os.path.exists('README.md') else '',

    packages=['cfpb_django_app',],
    include_package_data=True,
    install_requires=[],

    entry_points={
        'console_scripts':['cfpb-django-app = cfpb_django_app:main',]
    }
)


