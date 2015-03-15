#!/usr/bin/env python
# -*- coding: utf-8 -*-
# To create a distribution package for pip or easy-install:
# python setup.py sdist
from os.path import join, dirname, realpath
from setuptools import setup, find_packages
import sys
from warnings import warn


author = u"Paul Müller"
authors = [author]
description = 'A multiple-tau algorithm for Python/NumPy.'
name = 'multipletau'
year = "2013"


sys.path.insert(0, realpath(dirname(__file__))+"/"+name)
try:
    from _version import version
except:
    version = "unknown"



if __name__ == "__main__":
    setup(
        name=name,
        author=author,
        author_email='paul.mueller@biotec.tu-dresden.de',
        url='https://github.com/paulmueller/multipletau',
        version=version,
        packages=[name],
        package_dir={name: name},
        license="BSD (3 clause)",
        description=description,
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


