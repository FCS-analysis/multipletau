#!/usr/bin/env python
# To create a distribution package for pip or easy-install:
# python setup.py sdist
from setuptools import setup, find_packages
from os.path import join, dirname, realpath
from warnings import warn

import multipletau

setup(
    name='multipletau',
    author='Paul Mueller',
    author_email='paul.mueller@biotec.tu-dresden.de',
    url='https://github.com/paulmueller/multipletau',
    version=multipletau.__version__,
    packages=['multipletau'],
    package_dir={'multipletau': 'multipletau'},
    license="OpenBSD",
    description='A multiple-tau algorithm using numpy arrays.',
    long_description=open(join(dirname(__file__), 'README.txt')).read(),
    install_requires=["NumPy >= 1.5.1"]
    )


