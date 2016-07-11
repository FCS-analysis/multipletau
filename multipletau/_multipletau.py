#!/usr/bin/python
# -*- coding: utf-8 -*-
""" 
A multiple-τ algorithm for Python 2.7 and 3.x.

Copyright (c) 2014 Paul Müller

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are
met:

  1. Redistributions of source code must retain the above copyright
     notice, this list of conditions and the following disclaimer.
   
  2. Redistributions in binary form must reproduce the above copyright
     notice, this list of conditions and the following disclaimer in
     the documentation and/or other materials provided with the
     distribution.

  3. Neither the name of multipletau nor the names of its contributors
     may be used to endorse or promote products derived from this
     software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL INFRAE OR
CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""
from __future__ import division

import numpy as np
import warnings

__all__ = ["autocorrelate", "correlate", "correlate_numpy"]


def autocorrelate(a, m=16, deltat=1, normalize=False,
                  copy=True, dtype=None):
    """ 
    Autocorrelation of a 1-dimensional sequence on a log2-scale.

    This computes the correlation similar to 
    :py:func:`numpy.correlate` for positive :math:`k` on a base 2
    logarithmic scale.

        :func:`numpy.correlate(a, a, mode="full")[len(a)-1:]`
    
        :math:`z_k = \Sigma_n a_n a_{n+k}`


    Parameters
    ----------
    a : array-like
        input sequence
    m : even integer
        defines the number of points on one level, must be an
        even integer
    deltat : float
        distance between bins
    normalize : bool
        normalize the result to the square of the average input
        signal and the factor :math:`M-k`.
    copy : bool
        copy input array, set to ``False`` to save memory
    dtype : object to be converted to a data type object
        The data type of the returned array and of the accumulator
        for the multiple-tau computation.


    Returns
    -------
    autocorrelation : ndarray of shape (N,2)
        the lag time (1st column) and the autocorrelation (2nd column).

    Notes
    -----
    .. versionchanged :: 0.1.6
       Compute the correlation for zero lag time.

    The algorithm computes the correlation with the convention of the
    curve decaying to zero.

    For experiments like e.g. fluorescence correlation spectroscopy,
    the signal can be normalized to :math:`M-k` by invoking ``normalize = True``.           

    For normalizing according to the behavior of :py:func:`numpy.correlate`,
    use ``normalize = False``.

    For complex arrays, this method falls back to the method
    :func:`correlate`.


    Examples
    --------
    >>> from multipletau import autocorrelate
    >>> autocorrelate(range(42), m=2, dtype=np.float)
    array([[  0.00000000e+00,   2.38210000e+04],
           [  1.00000000e+00,   2.29600000e+04],
           [  2.00000000e+00,   2.21000000e+04],
           [  4.00000000e+00,   2.03775000e+04],
           [  8.00000000e+00,   1.50612000e+04]])
    """
    assert isinstance(copy, bool)
    assert isinstance(normalize, bool)

    if dtype is None:
        dtype = np.dtype(a[0].__class__)
    else:
        dtype = np.dtype(dtype)

    # Complex data
    if dtype.kind == "c":
        # run cross-correlation
        return correlate(a=a,
                         v=a,
                         m=m,
                         deltat=deltat,
                         normalize=normalize,
                         copy=copy,
                         dtype=dtype)
    elif dtype.kind != "f":
        warnings.warn("Input dtype is not float; casting to np.float!")
        dtype = np.dtype(np.float)

    # If copy is false and dtype is the same as the input array,
    # then this line does not have an effect:
    trace = np.array(a, dtype=dtype, copy=copy)

    # Check parameters
    if m//2 != m/2:
        mold = m
        m = np.int((m//2 + 1) * 2)
        warnings.warn("Invalid value of m={}. Using m={} instead"
                      .format(mold, m))
    else:
        m = np.int(m)

    N = N0 = trace.shape[0]

    # Find out the length of the correlation function.
    # The integer k defines how many times we can average over
    # two neighboring array elements in order to obtain an array of
    # length just larger than m.
    k = np.int(np.floor(np.log2(N/m)))

    # In the base2 multiple-tau scheme, the length of the correlation
    # array is (only taking into account values that are computed from
    # traces that are just larger than m):
    lenG = m + k*(m//2) + 1

    G = np.zeros((lenG, 2), dtype=dtype)

    normstat = np.zeros(lenG, dtype=dtype)
    normnump = np.zeros(lenG, dtype=dtype)

    traceavg = np.average(trace)

    # We use the fluctuation of the signal around the mean
    if normalize:
        trace -= traceavg
        assert traceavg != 0, "Cannot normalize: Average of `a` is zero!"
    
    # Otherwise the following for-loop will fail:
    assert N >= 2*m, "len(a) must be larger than 2m!"

    # Calculate autocorrelation function for first m+1 bins
    # Discrete convolution of m elements
    for n in range(0, m+1):
        G[n, 0] = deltat * n
        # This is the computationally intensive step
        G[n, 1] = np.sum(trace[:N - n] * trace[n:])
        normstat[n] = N - n
        normnump[n] = N
    # Now that we calculated the first m elements of G, let us
    # go on with the next m/2 elements.
    # Check if len(trace) is even:
    if N%2 == 1:
        N -= 1
    # Add up every second element
    trace = (trace[:N:2] + trace[1:N:2]) / 2
    N //= 2
    # Start iteration for each m/2 values
    for step in range(1, k + 1):
        # Get the next m/2 values via correlation of the trace
        for n in range(1, m//2 + 1):
            npmd2 = n + m//2
            idx = m + n + (step - 1) * m//2
            if len(trace[:N - npmd2]) == 0:
                # This is a shortcut that stops the iteration once the
                # length of the trace is too small to compute a corre-
                # lation. The actual length of the correlation function
                # does not only depend on k - We also must be able to
                # perform the sum with respect to k for all elements.
                # For small N, the sum over zero elements would be
                # computed here.
                #
                # One could make this for-loop go up to maxval, where
                #   maxval1 = int(m/2)
                #   maxval2 = int(N-m/2-1)
                #   maxval = min(maxval1, maxval2)
                # However, we then would also need to find out which
                # element in G is the last element...
                G = G[:idx - 1]
                normstat = normstat[:idx - 1]
                normnump = normnump[:idx - 1]
                # Note that this break only breaks out of the current
                # for loop. However, we are already in the last loop
                # of the step-for-loop. That is because we calculated
                # k in advance.
                break
            else:
                G[idx, 0] = deltat * npmd2 * 2**step
                # This is the computationally intensive step
                G[idx, 1] = np.sum(trace[:N - npmd2] *
                                   trace[npmd2:])
                normstat[idx] = N - npmd2
                normnump[idx] = N
        # Check if len(trace) is even:
        if N%2 == 1:
            N -= 1
        # Add up every second element
        trace = (trace[:N:2] + trace[1:N:2]) / 2
        N //= 2

    if normalize:
        G[:, 1] /= traceavg**2 * normstat
    else:
        G[:, 1] *= N0 / normnump

    return G


def correlate(a, v, m=16, deltat=1, normalize=False,
              copy=True, dtype=None):
    """ 
    Cross-correlation of two 1-dimensional sequences
    on a log2-scale.

    This computes the cross-correlation similar to
    :py:func:`numpy.correlate` for positive :math:`k`  on a base 2
    logarithmic scale.

        :func:`numpy.correlate(a, v, mode="full")[len(a)-1:]`

        :math:`z_k = \Sigma_n a_n v_{n+k}`

    Note that only the correlation in the positive direction is computed.
    To obtain the correlation for negative lag times swap the input variables
    ``a`` and ``v``.

    Parameters
    ----------
    a, v : array-like
        input sequences with equal length
    m : even integer
        defines the number of points on one level, must be an
        even integer
    deltat : float
        distance between bins
    normalize : bool
        normalize the result to the square of the average input
        signal and the factor :math:`M-k`.
    copy : bool
        copy input array, set to ``False`` to save memory
    dtype : object to be converted to a data type object
        The data type of the returned array and of the accumulator
        for the multiple-tau computation.


    Returns
    -------
    cross_correlation : ndarray of shape (N,2)
        the lag time (1st column) and the cross-correlation (2nd column).


    Notes
    -----
    .. versionchanged :: 0.1.6
       Compute the correlation for zero lag time and correctly normalize
       the correlation for a complex input sequence `v`.

    The algorithm computes the correlation with the convention of the
    curve decaying to zero.

    For experiments like e.g. fluorescence correlation spectroscopy,
    the signal can be normalized to :math:`M-k` by invoking ``normalize = True``.           

    For normalizing according to the behavior of :py:func:`numpy.correlate`,
    use ``normalize = False``.


    Examples
    --------
    >>> from multipletau import correlate
    >>> correlate(range(42), range(1,43), m=2, dtype=np.float)
    array([[  0.00000000e+00,   2.46820000e+04],
           [  1.00000000e+00,   2.38210000e+04],
           [  2.00000000e+00,   2.29600000e+04],
           [  4.00000000e+00,   2.12325000e+04],
           [  8.00000000e+00,   1.58508000e+04]])

    """
    assert isinstance(copy, bool)
    assert isinstance(normalize, bool)
    # See `autocorrelation` for better documented code.
    traceavg1 = np.average(v)
    traceavg2 = np.average(a)
    if normalize:
        assert traceavg1 != 0, "Cannot normalize: Average of `v` is zero!"
        assert traceavg2 != 0, "Cannot normalize: Average of `a` is zero!"

    if dtype is None:
        dtype = np.dtype(v[0].__class__)
        dtype2 = np.dtype(a[0].__class__)
        if dtype != dtype2:
            if dtype.kind == "c" or dtype2.kind == "c":
                # The user might try to combine complex64 and float128.
                warnings.warn("Input dtypes not equal; casting to np.complex!")
                dtype = np.dtype(np.complex)
            else:
                warnings.warn("Input dtypes not equal; casting to np.float!")
                dtype = np.dtype(np.float)
    else:
        dtype = np.dtype(dtype)

    if not dtype.kind in ["c", "f"]:
        warnings.warn("Input dtype is not float; casting to np.float!")
        dtype = np.dtype(np.float)

    trace1 = np.array(v, dtype=dtype, copy=copy)

    # Prevent traces from overwriting each other
    if a is v:
        # Force copying trace 2
        copy = True

    trace2 = np.array(a, dtype=dtype, copy=copy)

    assert trace1.shape[0] == trace2.shape[0], "`a`,`v` must have same length!"

    # Complex data
    if dtype.kind == "c":
        np.conjugate(trace1, out=trace1)

    # Check parameters
    if m//2 != m/2:
        mold = m
        m = np.int(m//2 + 1) * 2
        warnings.warn("Invalid value of m={}. Using m={} instead"
                      .format(mold, m))
    else:
        m = np.int(m)


    N = N0 = trace1.shape[0]
    # Find out the length of the correlation function.
    # The integer k defines how many times we can average over
    # two neighboring array elements in order to obtain an array of
    # length just larger than m.
    k = np.int(np.floor(np.log2(N/m)))

    # In the base2 multiple-tau scheme, the length of the correlation
    # array is (only taking into account values that are computed from
    # traces that are just larger than m):
    lenG = m + k * m//2 + 1

    G = np.zeros((lenG, 2), dtype=dtype)
    normstat = np.zeros(lenG, dtype=dtype)
    normnump = np.zeros(lenG, dtype=dtype)

    # We use the fluctuation of the signal around the mean
    if normalize:
        trace1 -= np.conj(traceavg1)
        trace2 -= traceavg2

    # Otherwise the following for-loop will fail:
    assert N >= 2*m, "len(a) must be larger than 2m!"

    # Calculate autocorrelation function for first m+1 bins
    for n in range(0, m + 1):
        G[n, 0] = deltat * n
        G[n, 1] = np.sum(trace1[:N - n] * trace2[n:])
        normstat[n] = N - n
        normnump[n] = N
    # Check if len(trace) is even:
    if N%2 == 1:
        N -= 1
    # Add up every second element
    trace1 = (trace1[:N:2] + trace1[1:N:2]) / 2
    trace2 = (trace2[:N:2] + trace2[1:N:2]) / 2
    N //= 2

    for step in range(1, k + 1):
        # Get the next m/2 values of the trace
        for n in range(1, m//2 + 1):
            npmd2 = (n + m//2)
            idx = m + n + (step - 1) * m//2
            if len(trace1[:N - npmd2]) == 0:
                # Abort
                G = G[:idx - 1]
                normstat = normstat[:idx - 1]
                normnump = normnump[:idx - 1]
                break
            else:
                G[idx, 0] = deltat * npmd2 * 2**step
                G[idx, 1] = np.sum(
                    trace1[:N - npmd2] * trace2[npmd2:])
                normstat[idx] = N - npmd2
                normnump[idx] = N

        # Check if len(trace) is even:
        if N%2 == 1:
            N -= 1
        # Add up every second element
        trace1 = (trace1[:N:2] + trace1[1:N:2]) / 2
        trace2 = (trace2[:N:2] + trace2[1:N:2]) / 2
        N //= 2

    if normalize:
        G[:, 1] /= traceavg1 * traceavg2 * normstat
    else:
        G[:, 1] *= N0 / normnump

    return G


def correlate_numpy(a, v, deltat=1, normalize=False,
                    dtype=None, copy=True):
    """
    Convenience function that wraps around :py:func:`numpy.correlate` and
    returns the correlation in the same format as :func:`correlate` does.


    Parameters
    ----------
    a, v : array-like
        input sequences
    deltat : float
        distance between bins
    normalize : bool
        normalize the result to the square of the average input signal
        and the factor :math:`M-k`. The resulting curve follows
        the convention of decaying to zero for large lag times.
    copy : bool
        copy input array, set to ``False`` to save memory
    dtype : object to be converted to a data type object
        The data type of the returned array.


    Returns
    -------
    cross_correlation : ndarray of shape (N,2)
        the lag time (1st column) and the cross-correlation (2nd column).


    Notes
    -----
    .. versionchanged :: 0.1.6
       Removed false normalization when `normalize==False`.
    """
    ab = np.array(a, dtype=dtype, copy=copy)
    vb = np.array(v, dtype=dtype, copy=copy)

    assert ab.shape[0] == vb.shape[0], "`a`,`v` must have same length!"

    avg = np.average(ab)
    vvg = np.average(vb)

    if normalize:
        ab -= avg
        vb -= vvg
        assert avg != 0, "Cannot normalize: Average of `a` is zero!"
        assert vvg != 0, "Cannot normalize: Average of `v` is zero!"

    Gd = np.correlate(ab, vb, mode="full")[len(ab) - 1:]

    if normalize:
        N = len(Gd)
        m = N - np.arange(N)
        Gd /= m * avg * vvg
    
    G = np.zeros((len(Gd), 2), dtype=dtype)
    G[:, 1] = Gd
    G[:, 0] = np.arange(len(Gd)) * deltat
    return G
