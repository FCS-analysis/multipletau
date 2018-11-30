#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Test correlation-autocorrelation identity"""
from __future__ import division, print_function

import numpy as np

import multipletau

from test_autocorrelate import get_sample_arrays


def test_ac():
    arrs = get_sample_arrays()

    try:
        multipletau.autocorrelate(a=arrs[0],
                                  copy=2)
    except ValueError as e:
        assert "`copy` must be boolean!" in e.args
    else:
        assert False

    try:
        multipletau.autocorrelate(a=arrs[0],
                                  ret_sum=2)
    except ValueError as e:
        assert "`ret_sum` must be boolean!" in e.args
    else:
        assert False

    try:
        multipletau.autocorrelate(a=arrs[0],
                                  normalize=2)
    except ValueError as e:
        assert "`normalize` must be boolean!" in e.args
    else:
        assert False

    try:
        multipletau.autocorrelate(a=arrs[0],
                                  compress="peter")
    except ValueError as e:
        assert "Invalid value for `compress`!" in e.args[0]
    else:
        assert False

    try:
        multipletau.autocorrelate(a=arrs[0],
                                  normalize=True,
                                  ret_sum=True)
    except ValueError as e:
        assert "'normalize' and 'ret_sum' must not both be True!" in e.args
    else:
        assert False


def test_ac_trace0():
    arrs = get_sample_arrays()
    try:
        multipletau.autocorrelate(a=arrs[0] - np.mean(arrs[0]),
                                  normalize=True)
    except ValueError as e:
        assert "Cannot normalize: Average of `a` is zero!" in e.args
    else:
        assert False


def test_ac_tracesize():
    arrs = get_sample_arrays()
    try:
        multipletau.autocorrelate(a=arrs[0][:31],
                                  m=16)
    except ValueError as e:
        assert '`len(a)` must be >= `2m`!' in e.args
    else:
        assert False


def test_cc():
    arrs = get_sample_arrays()

    try:
        multipletau.correlate(a=arrs[0], v=arrs[0],
                              copy=2)
    except ValueError as e:
        assert "`copy` must be boolean!" in e.args
    else:
        assert False

    try:
        multipletau.correlate(a=arrs[0], v=arrs[0],
                              ret_sum=2)
    except ValueError as e:
        assert "`ret_sum` must be boolean!" in e.args
    else:
        assert False

    try:
        multipletau.correlate(a=arrs[0], v=arrs[0],
                              normalize=2)
    except ValueError as e:
        assert "`normalize` must be boolean!" in e.args
    else:
        assert False

    try:
        multipletau.correlate(a=arrs[0], v=arrs[0],
                              compress="peter")
    except ValueError as e:
        assert "Invalid value for `compress`!" in e.args[0]
    else:
        assert False

    try:
        multipletau.correlate(a=arrs[0], v=arrs[0],
                              normalize=True,
                              ret_sum=True)
    except ValueError as e:
        assert "'normalize' and 'ret_sum' must not both be True!" in e.args
    else:
        assert False


def test_cc_trace0():
    arrs = get_sample_arrays()
    try:
        multipletau.correlate(a=arrs[0] - np.mean(arrs[0]),
                              v=arrs[0],
                              normalize=True)
    except ValueError as e:
        assert "Cannot normalize: Average of `a` is zero!" in e.args
    else:
        assert False

    try:
        multipletau.correlate(a=arrs[0],
                              v=arrs[0] - np.mean(arrs[0]),
                              normalize=True)
    except ValueError as e:
        assert "Cannot normalize: Average of `v` is zero!" in e.args
    else:
        assert False


def test_cc_tracesize():
    arrs = get_sample_arrays()
    try:
        multipletau.correlate(a=arrs[0][:31],
                              v=arrs[0][:31],
                              m=16)
    except ValueError as e:
        assert '`len(a)` must be >= `2m`!' in e.args
    else:
        assert False


def test_cc_samesize():
    arrs = get_sample_arrays()
    try:
        multipletau.correlate(a=arrs[0],
                              v=arrs[1],
                              normalize=True)
    except ValueError as e:
        assert "`a` and `v` must have same length!" in e.args
    else:
        assert False


def test_numpy_cc_trace0():
    arrs = get_sample_arrays()
    try:
        multipletau.correlate_numpy(a=arrs[0] - np.mean(arrs[0]),
                                    v=arrs[0],
                                    normalize=True)
    except ValueError as e:
        assert "Cannot normalize: Average of `a` is zero!" in e.args
    else:
        assert False

    try:
        multipletau.correlate_numpy(a=arrs[0],
                                    v=arrs[0] - np.mean(arrs[0]),
                                    normalize=True)
    except ValueError as e:
        assert "Cannot normalize: Average of `v` is zero!" in e.args
    else:
        assert False


def test_numpy_cc_samesize():
    arrs = get_sample_arrays()
    try:
        multipletau.correlate_numpy(a=arrs[0],
                                    v=arrs[1],
                                    normalize=True)
    except ValueError as e:
        assert "`a` and `v` must have same length!" in e.args
    else:
        assert False


if __name__ == "__main__":
    # Run all tests
    loc = locals()
    for key in list(loc.keys()):
        if key.startswith("test_") and hasattr(loc[key], "__call__"):
            loc[key]()
