#!/usr/bin/python
# -*- coding: utf-8 -*-
"""test strategies for propagating values to the next level"""
import numpy as np

from multipletau import autocorrelate, correlate


def test_ac_compress_average():
    ist = autocorrelate(range(42), m=2, dtype=np.float_, compress="average")
    soll = np.array([[0.00000000e+00,   2.38210000e+04],
                     [1.00000000e+00,   2.29600000e+04],
                     [2.00000000e+00,   2.21000000e+04],
                     [4.00000000e+00,   2.03775000e+04],
                     [8.00000000e+00,   1.50612000e+04]])
    assert np.allclose(soll, ist)


def test_cc_compress_average():
    ist = correlate(range(42), range(1, 43), m=2, dtype=np.float_,
                    compress="average")
    soll = np.array([[0.00000000e+00,   2.46820000e+04],
                     [1.00000000e+00,   2.38210000e+04],
                     [2.00000000e+00,   2.29600000e+04],
                     [4.00000000e+00,   2.12325000e+04],
                     [8.00000000e+00,   1.58508000e+04]])
    assert np.allclose(soll, ist)


def test_ac_compress_first():
    ist = autocorrelate(range(42), m=2, dtype=np.float_,
                        compress="first")
    soll = np.array([[0.00000e+00, 2.38210e+04],
                     [1.00000e+00, 2.29600e+04],
                     [2.00000e+00, 2.21000e+04],
                     [4.00000e+00, 1.96080e+04],
                     [8.00000e+00, 1.31712e+04]])

    assert np.allclose(soll, ist)


def test_cc_compress_first():
    ist = correlate(range(42), range(1, 43), m=2, dtype=np.float_,
                    compress="first")
    soll = np.array([[0.00000e+00, 2.46820e+04],
                     [1.00000e+00, 2.38210e+04],
                     [2.00000e+00, 2.29600e+04],
                     [4.00000e+00, 2.04440e+04],
                     [8.00000e+00, 1.39104e+04]])

    assert np.allclose(soll, ist)


def test_ac_compress_second():
    ist = autocorrelate(range(42), m=2, dtype=np.float_,
                        compress="second")
    soll = np.array([[0.00000e+00, 2.38210e+04],
                     [1.00000e+00, 2.29600e+04],
                     [2.00000e+00, 2.21000e+04],
                     [4.00000e+00, 2.11660e+04],
                     [8.00000e+00, 1.71024e+04]])

    assert np.allclose(soll, ist)


def test_cc_compress_second():
    ist = correlate(range(42), range(1, 43), m=2, dtype=np.float_,
                    compress="second")
    soll = np.array([[0.00000e+00, 2.46820e+04],
                     [1.00000e+00, 2.38210e+04],
                     [2.00000e+00, 2.29600e+04],
                     [4.00000e+00, 2.20400e+04],
                     [8.00000e+00, 1.79424e+04]])

    assert np.allclose(soll, ist)


if __name__ == "__main__":
    # Run all tests
    loc = locals()
    for key in list(loc.keys()):
        if key.startswith("test_") and hasattr(loc[key], "__call__"):
            loc[key]()
