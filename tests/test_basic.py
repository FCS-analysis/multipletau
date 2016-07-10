#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
basic tests also available in the function docs 
"""
import numpy as np
from os.path import abspath, dirname, join
import sys

sys.path.insert(0, dirname(dirname(abspath(__file__))))

from multipletau import autocorrelate, correlate


def test_ac():
    ist = autocorrelate(range(42), m=2, dtype=np.dtype(float))
    soll = np.array([[  0.00000000e+00,   2.38210000e+04],
                     [  1.00000000e+00,   2.29600000e+04],
                     [  2.00000000e+00,   2.21000000e+04],
                     [  4.00000000e+00,   2.03775000e+04],
                     [  8.00000000e+00,   1.50612000e+04]])
    assert np.allclose(soll, ist)


def test_cc():
    ist = correlate(range(42), range(1,43), m=2, dtype=np.dtype(float))
    soll = np.array([[  0.00000000e+00,   2.46820000e+04],
                     [  1.00000000e+00,   2.38210000e+04],
                     [  2.00000000e+00,   2.29600000e+04],
                     [  4.00000000e+00,   2.12325000e+04],
                     [  8.00000000e+00,   1.58508000e+04]])
    assert np.allclose(soll, ist)

    
if __name__ == "__main__":
    # Run all tests
    loc = locals()
    for key in list(loc.keys()):
        if key.startswith("test_") and hasattr(loc[key], "__call__"):
            loc[key]()
    