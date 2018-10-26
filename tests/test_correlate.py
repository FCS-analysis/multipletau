#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests correlation algorithm"""
from __future__ import division, print_function

import sys

import numpy as np
import pytest

import multipletau

from test_autocorrelate import get_reference_data


def get_sample_arrays_cplx():
    a = [-4.3,   1,    9, -99.2, 13]
    b = [9921, 281, 23.5,   5.3, 77]
    c = [12,   0,  2.1,   1.3, 33]
    d = [32,  .1,   -2,   6.3, 88]
    ll = [33,  92,   47,    54, 99]
    r = [0,   1,   12,     4,  0]
    p = [1,   4,   .5,     2,  3]
    arrs = []

    for ai, bi, ci, di, li, ri, pi in zip(a, b, c, d, ll, r, p):
        x = np.linspace(ai, bi, li)
        y = np.linspace(ci, di, li)
        arr = (x*np.roll(x, ri))**pi + 1j*y
        arrs.append(arr)

    return arrs


def test_cc_copy():
    myframe = sys._getframe()
    myname = myframe.f_code.co_name
    print("running ", myname)

    arrs = get_sample_arrays_cplx()

    res1 = []
    for a in arrs:
        r = multipletau.correlate(a=a,
                                  v=a,
                                  m=16,
                                  deltat=1,
                                  normalize=True,
                                  copy=True)
        res1.append(r)

    res2 = []
    for a in arrs:
        r = multipletau.correlate(a=a,
                                  v=a,
                                  m=16,
                                  deltat=1,
                                  normalize=True,
                                  copy=False)
        res2.append(r)

    # simple test if result is the same
    assert np.all(np.concatenate(res1) == np.concatenate(res2))

    arrs = np.concatenate(arrs)
    refarrs = np.concatenate(get_sample_arrays_cplx())

    # make sure the copy function really changes something
    assert not np.all(arrs == refarrs)


@pytest.mark.filterwarnings("ignore::multipletau.core.InvalidMWarning")
def test_cc_dtype():
    myframe = sys._getframe()
    myname = myframe.f_code.co_name
    print("running ", myname)

    a = np.round(get_sample_arrays_cplx()[0].real)

    # integer
    rf = multipletau.correlate(a=a,
                               v=a,
                               m=16,
                               deltat=1,
                               normalize=True,
                               copy=True,
                               dtype=np.float_)

    ri = multipletau.correlate(a=a,
                               v=a,
                               m=16,
                               deltat=1,
                               normalize=True,
                               copy=True,
                               dtype=np.int_)

    ri2 = multipletau.correlate(a=np.array(a, dtype=np.int_),
                                v=np.array(a, dtype=np.int_),
                                m=16,
                                deltat=1,
                                normalize=True,
                                copy=True,
                                dtype=None)

    assert ri.dtype == np.dtype(
        np.float_), "if wrong dtype, dtype should default to np.float_"
    assert ri2.dtype == np.dtype(
        np.float_), "if wrong dtype, dtype should default to np.float_"
    assert np.all(
        rf == ri), "result should be the same, because input us the same"
    assert np.all(
        rf == ri2), "result should be the same, because input us the same"


@pytest.mark.filterwarnings("ignore::multipletau.core.InvalidMWarning")
def test_cc_dtype2():
    myframe = sys._getframe()
    myname = myframe.f_code.co_name
    print("running ", myname)

    a = np.round(get_sample_arrays_cplx()[0])

    rf = multipletau.correlate(a=a.real,
                               v=a,
                               m=16,
                               deltat=1,
                               normalize=True,
                               copy=True)
    assert np.dtype(rf.dtype) == np.dtype(np.complex_)

    rf2 = multipletau.correlate(a=a.real,
                                v=np.array(a.imag, dtype=np.int_),
                                m=16,
                                deltat=1,
                                normalize=True,
                                copy=True)
    assert np.dtype(rf2.dtype) == np.dtype(np.float_)


def test_cc_m():
    myframe = sys._getframe()
    myname = myframe.f_code.co_name
    print("running ", myname)

    arrs = get_sample_arrays_cplx()

    ms = [4, 8, 10, 16, 20, 64, 128]
    a = np.concatenate(arrs)

    res = []
    for m in ms:
        r = multipletau.correlate(a=a,
                                  v=a,
                                  m=m,
                                  deltat=1,
                                  normalize=False,
                                  copy=True,
                                  dtype=np.complex_)
        res.append(r)

        # test minimal length of array
        multipletau.correlate(a=a[:2*m],
                              v=a[:2*m],
                              m=m,
                              deltat=1,
                              normalize=False,
                              copy=True,
                              dtype=np.complex_)

    res = np.concatenate(res)
    # np.save(os.path.dirname(__file__)
    #         + "/data/"+os.path.basename(__file__)+"_"+myname+".npy", res)
    ref = get_reference_data(myname, __file__)

    assert np.allclose(res, ref, atol=0, rtol=1e-15)


@pytest.mark.filterwarnings("ignore::multipletau.core.InvalidMWarning")
def test_cc_m_wrong():
    myframe = sys._getframe()
    myname = myframe.f_code.co_name
    print("running ", myname)

    a = get_sample_arrays_cplx()[0]

    # integer
    r1 = multipletau.correlate(a=a,
                               v=a,
                               m=16,
                               deltat=1,
                               normalize=True,
                               copy=True)

    r2 = multipletau.correlate(a=a,
                               v=a,
                               m=15,
                               deltat=1,
                               normalize=True,
                               copy=True)

    r3 = multipletau.correlate(a=a,
                               v=a,
                               m=15.5,
                               deltat=1,
                               normalize=True,
                               copy=True)

    r4 = multipletau.correlate(a=a,
                               v=a,
                               m=14.5,
                               deltat=1,
                               normalize=True,
                               copy=True)

    r5 = multipletau.correlate(a=a,
                               v=a,
                               m=16.,
                               deltat=1,
                               normalize=True,
                               copy=True)

    assert np.all(r1 == r2)
    assert np.all(r1 == r3)
    assert np.all(r1 == r4)
    assert np.all(r1 == r5)


def test_cc_normalize():
    myframe = sys._getframe()
    myname = myframe.f_code.co_name
    print("running ", myname)

    arrs = get_sample_arrays_cplx()

    res = []
    for a in arrs:
        r = multipletau.correlate(a=a.real,
                                  v=a.imag,
                                  m=16,
                                  deltat=1,
                                  normalize=True,
                                  copy=True,
                                  dtype=np.float_)
        res.append(r)
    res = np.concatenate(res)
    # np.save(os.path.dirname(__file__)
    #         + "/data/"+os.path.basename(__file__)+"_"+myname+".npy", res)
    ref = get_reference_data(myname, __file__)

    assert np.allclose(res, ref, atol=0, rtol=1e-14)


def test_cc_simple():
    myframe = sys._getframe()
    myname = myframe.f_code.co_name
    print("running ", myname)

    arrs = get_sample_arrays_cplx()

    res = []
    for a in arrs:
        r = multipletau.correlate(a=a,
                                  v=a,
                                  m=16,
                                  deltat=1,
                                  normalize=False,
                                  copy=True,
                                  dtype=np.complex_)
        res.append(r)
    res = np.concatenate(res)

    # np.save(os.path.dirname(__file__)
    #         + "/data/"+os.path.basename(__file__)+"_"+myname+".npy", res)
    ref = get_reference_data(myname, __file__)

    assert np.allclose(res, ref, atol=0, rtol=1e-15)

    # also check result of autocorrelate
    res2 = []
    for a in arrs:
        r = multipletau.autocorrelate(a=a,
                                      m=16,
                                      deltat=1,
                                      normalize=False,
                                      copy=True,
                                      dtype=np.complex_)
        res2.append(r)
    res2 = np.concatenate(res2)

    assert np.allclose(res, res2, atol=0, rtol=1e-15)


if __name__ == "__main__":
    # Run all tests
    loc = locals()
    for key in list(loc.keys()):
        if key.startswith("test_") and hasattr(loc[key], "__call__"):
            loc[key]()
