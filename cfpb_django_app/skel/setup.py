#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages

setup(
    name='{{app_name}}',
    url='{{app_url}}',
    author='CFPB',
    author_emaill='tech@cfpb.gov',
    license='CC0',

    # Read the version and description from the app itself.
    version=__import__('{{app_name}}').__version__,
    description=' '.join(__import__('{{app_name}}'
        ).__doc__.splitlines()).strip(),

    # Read the README for the long description
    long_description=open('README.md').read() \
            if os.path.exists('README.md') else '',

    # Be explicit in only using the app package, and include all data to
    # make sure we grab templates and other assets that aren't Python
    # files.
    packages=['{{app_name}}'],
    include_package_data=True,

    # NOTE: DO NOT ABUSE install_requires OR requirements.txt
    #
    # install_requires specifies what a project needs to run. This is
    # the specification PIP will use to install its dependencies within
    # ranges of version compatibility.
    #
    # requirements.txt specifies an exact Python environment with pinned
    # versions that creates a repeatable installation.
    # 
    # install_requires should be used for abstract requirements,
    # requirements.txt should be used to make those requirements
    # concrete. Think of it as the difference between a library (the
    # Django app) and an application (the Django project).
    # 
    # NEVER just "read" requirements.txt into install_requires.
    install_requires=[
        'Django>=1.8',
    ],

    # The test runner that allows us to run 'python setup.py test'
    test_suite = "{{app_name}}_proj.runtests.runtests",
)

