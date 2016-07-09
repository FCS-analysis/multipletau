#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Compare to numpy data.
"""
import numpy as np
from os.path import abspath, dirname, join
import sys

sys.path.insert(0, dirname(dirname(abspath(__file__))))

import multipletau

from test_correlate import get_sample_arrays_cplx



def test_corresponds_ac():
    myframe = sys._getframe()
    myname = myframe.f_code.co_name
    print("running ", myname)
    
    a = np.concatenate(get_sample_arrays_cplx()).real
    m=16

    restau = multipletau.autocorrelate(a=1*a,
                                       m=m,
                                       copy=True,
                                       normalize=True,
                                       dtype=np.float128)

    reslin = multipletau.correlate_numpy(a=1*a,
                                         v=1*a,
                                         copy=True,
                                         normalize=True,
                                         dtype=np.float128)

    idx = np.array(restau[:,0].real, dtype=int)[:m]

    assert np.allclose(reslin[idx, 1], restau[:m,1])


def test_corresponds_ac_nonormalize():
    myframe = sys._getframe()
    myname = myframe.f_code.co_name
    print("running ", myname)
    
    a = np.concatenate(get_sample_arrays_cplx()).real
    m=16

    restau = multipletau.autocorrelate(a=1*a,
                                       m=m,
                                       copy=True,
                                       normalize=False,
                                       dtype=np.float128)

    reslin = multipletau.correlate_numpy(a=1*a,
                                         v=1*a,
                                         copy=True,
                                         normalize=False,
                                         dtype=np.float128)

    idx = np.array(restau[:,0].real, dtype=int)[:m]

    assert np.allclose(reslin[idx, 1], restau[:m,1])


def test_corresponds_cc():
    myframe = sys._getframe()
    myname = myframe.f_code.co_name
    print("running ", myname)
    
    a = np.concatenate(get_sample_arrays_cplx())
    m=16

    restau = multipletau.correlate(a=a,
                                   v=a.imag+1j*a.real,
                                   m=m,
                                   copy=True,
                                   normalize=True,
                                   dtype=np.complex256)

    reslin = multipletau.correlate_numpy(a=a,
                                         v=a.imag+1j*a.real,
                                         copy=True,
                                         normalize=True,
                                         dtype=np.complex256)

    idx = np.array(restau[:,0].real, dtype=int)[:m]

    assert np.allclose(reslin[idx, 1], restau[:m,1])


def test_corresponds_cc_nonormalize():
    myframe = sys._getframe()
    myname = myframe.f_code.co_name
    print("running ", myname)
    
    a = np.concatenate(get_sample_arrays_cplx())
    m=16

    restau = multipletau.correlate(a=a,
                                   v=a.imag+1j*a.real,
                                   m=m,
                                   copy=True,
                                   normalize=False,
                                   dtype=np.complex256)

    reslin = multipletau.correlate_numpy(a=a,
                                         v=a.imag+1j*a.real,
                                         copy=True,
                                         normalize=False,
                                         dtype=np.complex256)

    idx = np.array(restau[:,0].real, dtype=int)[:m]

    assert np.allclose(reslin[idx, 1], restau[:m,1])
    


if __name__ == "__main__":
    # Run all tests
    loc = locals()
    for key in list(loc.keys()):
        if key.startswith("test_") and hasattr(loc[key], "__call__"):
            loc[key]()
