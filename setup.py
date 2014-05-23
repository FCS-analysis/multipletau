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
    description='A multiple-tau algorithm for Python/NumPy.',
    long_description=open(join(dirname(__file__), 'README.txt')).read(),
    install_requires=["NumPy >= 1.5.1"],
    keywords=["multiple", "tau", "FCS", "correlation", "spectroscopy",
              "fluorescence"],
    extras_require={
                    'doc': ['sphinx']
                   },
    classifiers= [
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Topic :: Scientific/Engineering :: Visualization',
        'Intended Audience :: Science/Research'
                 ],
    platforms=['ALL']
    )


