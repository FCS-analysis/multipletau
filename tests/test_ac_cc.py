#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Tests correlation-autocorrelation identity
"""
from __future__ import division, print_function

import numpy as np
import os
from os.path import abspath, basename, dirname, join, split, exists
import platform
import sys
import warnings
import zipfile

# Add parent directory to beginning of path variable
DIR = dirname(abspath(__file__))
sys.path = [split(DIR)[0]] + sys.path

import multipletau

from test_autocorrelate import get_sample_arrays


def test_ac_cc_simple():
    myframe = sys._getframe()
    myname = myframe.f_code.co_name
    print("running ", myname)
    
    arrs = get_sample_arrays()
    
    rescc = []
    for a in arrs:
        r = multipletau.correlate(a=a, v=a,
                                  m=16,
                                  deltat=1,
                                  normalize=False,
                                  copy=True,
                                  dtype=np.float)
        rescc.append(r)
    
    rescc = np.concatenate(rescc)

    resac = []
    for a in arrs:
        r = multipletau.autocorrelate(a=a,
                                      m=16,
                                      deltat=1,
                                      normalize=False,
                                      copy=True,
                                      dtype=np.float)
        resac.append(r)
    
    resac = np.concatenate(resac)
    
    assert np.all(resac==rescc)


def test_ac_cc_normalize():
    myframe = sys._getframe()
    myname = myframe.f_code.co_name
    print("running ", myname)
    
    arrs = get_sample_arrays()
    
    res = []
    for a in arrs:
        r = multipletau.autocorrelate(a=a,
                                      m=16,
                                      deltat=1,
                                      normalize=True,
                                      copy=True,
                                      dtype=np.float)
        res.append(r)
    
    res = np.concatenate(res)

    rescc = []
    for a in arrs:
        r = multipletau.correlate(a=a, v=a,
                                  m=16,
                                  deltat=1,
                                  normalize=True,
                                  copy=True,
                                  dtype=np.float)
        rescc.append(r)
    
    rescc = np.concatenate(rescc)

    assert np.all(res==rescc)


def test_ac_cc_m():
    myframe = sys._getframe()
    myname = myframe.f_code.co_name
    print("running ", myname)
    
    arrs = get_sample_arrays()

    ms = [8, 16, 32, 64, 128]
    a = np.concatenate(arrs)

    res = []    
    for m in ms:
        r = multipletau.autocorrelate(a=a,
                                      m=m,
                                      deltat=1,
                                      normalize=False,
                                      copy=True,
                                      dtype=np.float)
        res.append(r)
    res = np.concatenate(res)

    rescc = []    
    for m in ms:
        r = multipletau.correlate(a=a, v=a,
                                  m=m,
                                  deltat=1,
                                  normalize=False,
                                  copy=True,
                                  dtype=np.float)
        rescc.append(r)
        # test minimal length of array
        _r2 = multipletau.correlate(a=a[:2*m], v=a[:2*m],
                                    m=m,
                                    deltat=1,
                                    normalize=False,
                                    copy=True,
                                    dtype=np.float)
    
    rescc = np.concatenate(rescc)
    assert np.all(res==rescc)


if __name__ == "__main__":
    # Run all tests
    loc = locals()
    for key in list(loc.keys()):
        if key.startswith("test_") and hasattr(loc[key], "__call__"):
            loc[key]()
