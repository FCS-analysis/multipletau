#!/usr/bin/python
# -*- coding: utf-8 -*-
""" 
    A multiple-tau algorithm for python
    
    Multipe-tau correlation are computed on a logarithmic scale and are thus
    much faster than convnetional correlation on a linear scale such as 
    numpy.correlate.
"""
from _multipletau import *

__version__ = "0.1.3"
__author__ = "Paul Mueller"
__email__ = "paul.mueller@biotec.tu-dresden.de"
__license__ = "OpenBSD"
