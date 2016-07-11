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

    idx = np.array(restau[:,0].real, dtype=int)[:m+1]

    assert np.allclose(reslin[idx, 1], restau[:m+1,1])


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

    idx = np.array(restau[:,0].real, dtype=int)[:m+1]

    assert np.allclose(reslin[idx, 1], restau[:m+1,1])


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

    idx = np.array(restau[:,0].real, dtype=int)[:m+1]

    assert np.allclose(reslin[idx, 1], restau[:m+1,1])
    

def test_corresponds_ac_first_loop():
    """
    numpy correlation:
    G_m = sum_i(a_i*a_{i+m})
    
    multipletau correlation 2nd order:
    b_j = (a_{2i} + a_{2i+1} / 2)
    G_m = sum_j(b_j*b_{j+1})
        = 1/4*sum_i(a_{2i}   * a_{2i+m}   +
                    a_{2i}   * a_{2i+m+1} +
                    a_{2i+1} * a_{2i+m}   +   
                    a_{2i+1} * a_{2i+m+1}
                    )
    
    The values after the first m+1 lag times in the multipletau
    correlation differ from the normal correlation, because the
    traces are averaged over two consecutive items, effectively
    halving the size of the trace. The multiple-tau correlation
    can be compared to the regular correlation by using an even
    sized sequence (here 222) in which the elements 2i and 2i+1
    are equal, as is done in this test.
    """
    myframe = sys._getframe()
    myname = myframe.f_code.co_name
    print("running ", myname)
    
    a = [ arr / np.average(arr) for arr in get_sample_arrays_cplx() ]
    a = np.concatenate(a)[:222]
    # two consecutive elements are the same, so the multiple-tau method
    # corresponds to the numpy correlation for the first loop.
    a[::2] = a[1::2]
    
    for m in [2,4,6,8,10,12,14,16]:
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
        
        idtau = np.where(restau[:,0]==m+2)[0][0]
        tau3 = restau[idtau, 1] #m+1 initial bins
    
        idref = np.where(reslin[:,0]==m+2)[0][0]
        tau3ref = reslin[idref, 1]
        
        assert np.allclose(tau3, tau3ref)


if __name__ == "__main__":
    # Run all tests
    loc = locals()
    for key in list(loc.keys()):
        if key.startswith("test_") and hasattr(loc[key], "__call__"):
            loc[key]()
