#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Test correlation-autocorrelation identity"""
from __future__ import division, print_function

import sys

import numpy as np

import multipletau

from test_autocorrelate import get_sample_arrays


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
                                      dtype=np.float_)
        res.append(r)
    res = np.concatenate(res)

    rescc = []
    for m in ms:
        r = multipletau.correlate(a=a, v=a,
                                  m=m,
                                  deltat=1,
                                  normalize=False,
                                  copy=True,
                                  dtype=np.float_)
        rescc.append(r)
        # test minimal length of array
        multipletau.correlate(a=a[:2*m], v=a[:2*m],
                              m=m,
                              deltat=1,
                              normalize=False,
                              copy=True,
                              dtype=np.float_)

    rescc = np.concatenate(rescc)
    assert np.all(res == rescc)


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
                                      dtype=np.float_)
        res.append(r)

    res = np.concatenate(res)

    rescc = []
    for a in arrs:
        r = multipletau.correlate(a=a, v=a,
                                  m=16,
                                  deltat=1,
                                  normalize=True,
                                  copy=True,
                                  dtype=np.float_)
        rescc.append(r)

    rescc = np.concatenate(rescc)

    assert np.all(res == rescc)


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
                                  dtype=np.float_)
        rescc.append(r)

    rescc = np.concatenate(rescc)

    resac = []
    for a in arrs:
        r = multipletau.autocorrelate(a=a,
                                      m=16,
                                      deltat=1,
                                      normalize=False,
                                      copy=True,
                                      dtype=np.float_)
        resac.append(r)

    resac = np.concatenate(resac)

    assert np.all(resac == rescc)


if __name__ == "__main__":
    # Run all tests
    loc = locals()
    for key in list(loc.keys()):
        if key.startswith("test_") and hasattr(loc[key], "__call__"):
            loc[key]()
