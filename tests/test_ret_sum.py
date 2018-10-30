#!/usr/bin/python
# -*- coding: utf-8 -*-
"""test returning exact sum plus normalization factor"""
import numpy as np

from multipletau import autocorrelate, correlate


def test_ac_return_sum():
    ist, ist_count = autocorrelate(range(42), m=2, dtype=np.float_,
                                   ret_sum=True)
    soll = np.array([[0.000000e+00, 2.382100e+04],
                     [1.000000e+00, 2.296000e+04],
                     [2.000000e+00, 2.210000e+04],
                     [4.000000e+00, 1.018875e+04],
                     [8.000000e+00, 3.586000e+03]])
    soll_count = [42., 41., 40., 19.,  8.]
    assert np.allclose(soll, ist)
    assert np.allclose(soll_count, ist_count)


def test_cc_compress_average():
    ist, ist_count = correlate(range(42), range(1, 43), m=2, dtype=np.float_,
                               ret_sum=True)
    soll = np.array([[0.000000e+00, 2.468200e+04],
                     [1.000000e+00, 2.382100e+04],
                     [2.000000e+00, 2.296000e+04],
                     [4.000000e+00, 1.061625e+04],
                     [8.000000e+00, 3.774000e+03]])
    soll_count = [42., 41., 40., 19.,  8.]
    assert np.allclose(soll, ist)
    assert np.allclose(soll_count, ist_count)


if __name__ == "__main__":
    # Run all tests
    loc = locals()
    for key in list(loc.keys()):
        if key.startswith("test_") and hasattr(loc[key], "__call__"):
            loc[key]()
