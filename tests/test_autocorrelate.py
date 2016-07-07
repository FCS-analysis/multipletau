#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Tests autocorrelation algorithm
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


def get_reference_data(funcname, pyfile):
    adir = os.path.dirname(pyfile)+"/data/"
    aname = os.path.basename(pyfile)+"_"+funcname+".npy"
    return np.load(adir + aname)


def get_sample_arrays():
    a = [-4.3,   1,    9, -99.2, 13]
    b = [9921, 281, 23.5,   5.3, 77]
    l = [  33,  92,   47,    54, 99]
    r = [   0,   1,   12,     4,  0] 
    p = [   1,   4,   .5,     2,  3]
    arrs = []
    
    for ai, bi, li, ri, pi in zip(a,b,l,r,p): 
        x = np.linspace(ai,bi,li)
        a = (x*np.roll(x,ri))**pi
        arrs.append(a)
    
    return arrs


def test_ac_simple():
    myframe = sys._getframe()
    myname = myframe.f_code.co_name
    print("running ", myname)
    
    arrs = get_sample_arrays()
    
    res = []
    for a in arrs:
        r = multipletau.autocorrelate(a=a,
                                      m=16,
                                      deltat=1,
                                      normalize=False,
                                      copy=True,
                                      dtype=np.float)
        res.append(r)
    
    res = np.concatenate(res)
    #np.save(os.path.dirname(__file__)+"/data/"+os.path.basename(__file__)+"_"+myname+".npy", res)
    ref = get_reference_data(myname, __file__)

    assert np.all(res==ref)


def test_ac_normalize():
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
    #np.save(os.path.dirname(__file__)+"/data/"+os.path.basename(__file__)+"_"+myname+".npy", res)
    ref = get_reference_data(myname, __file__)

    assert np.all(res==ref)


def test_ac_m():
    myframe = sys._getframe()
    myname = myframe.f_code.co_name
    print("running ", myname)
    
    arrs = get_sample_arrays()
    
    res = []
    ms = [8, 16, 32, 64, 128]
    a = np.concatenate(arrs)
    
    for m in ms:
        r = multipletau.autocorrelate(a=a,
                                      m=m,
                                      deltat=1,
                                      normalize=False,
                                      copy=True,
                                      dtype=np.float)
        res.append(r)
    
    res = np.concatenate(res)
    #np.save(os.path.dirname(__file__)+"/data/"+os.path.basename(__file__)+"_"+myname+".npy", res)
    ref = get_reference_data(myname, __file__)

    assert np.all(res==ref)


def test_ac_copy():
    myframe = sys._getframe()
    myname = myframe.f_code.co_name
    print("running ", myname)
    
    arrs = get_sample_arrays()

    res1 = []
    for a in arrs:
        r = multipletau.autocorrelate(a=a,
                                      m=16,
                                      deltat=1,
                                      normalize=True,
                                      copy=True,
                                      dtype=np.float)
        res1.append(r)

    res2 = []
    for a in arrs:
        r = multipletau.autocorrelate(a=a,
                                      m=16,
                                      deltat=1,
                                      normalize=True,
                                      copy=False,
                                      dtype=np.float)
        res2.append(r)
    
    # simple test if result is the same
    assert np.all(np.concatenate(res1) == np.concatenate(res2))

    arrs = np.concatenate(arrs)
    refarrs = np.concatenate(get_sample_arrays())

    # make sure the copy function really changes something
    assert not np.all(arrs == refarrs)
    
    
    


if __name__ == "__main__":
    # Run all tests
    loc = locals()
    for key in list(loc.keys()):
        if key.startswith("test_") and hasattr(loc[key], "__call__"):
            loc[key]()
    
