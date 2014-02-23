#!/usr/bin/python
# -*- coding: utf-8 -*-
""" 
    A multiple-tau algorithm for python
    
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
                  copy=True, dtype=None, mode='full'):
    """ 
    Autocorrelation of a 1-dimensional sequence on a log2-scale.
    
    This computes the correlation according to 
    :py:func:`numpy.correlate` for positive :math:`k`  on a base 2
    logarithmic scale.
    
        numpy.correlate(a, a, mode="full")[len(a)-1:]  
        
        :math:`z_k = \Sigma_n a_n a_{n+k}`

    
    Note that only the correlation in the positive direction is
    computed.
    
    Parameters
    ----------
    a : ndarray
       1-dimensional array of length N
    m : even integer
        defines the number of points on one level, must be an
        even integer
    deltat : float
        distance between bins
    normalize : bool
        normalize the result to the square of the average input
        signal and the factor (M-k). The resulting curve follows
        the convention of decaying to zero for large lag times.
    copy : bool
        copy input array, set to False to save memory
    dtype : dtype, optional
        The type of the returned array and of the accumulator in 
        which the elements are summed.  By default, the dtype of 
        `a` is used.
    mode : {'full', 'base2'}
        'full': 
          By default, mode is 'full'.  This also returns the convolution
          for the last step. Boundary effects may be seen.
        'base2':
          This only returns the correlation for all levels of sample
          size m.

    Returns
    -------
    autocorrelation : ndarray
        Nx2 array containing lag time and autocorrelation


    Notes
    -----
    For FCS, with the convention of the curve decaying to zero use:
        
           normalize = True
    
    For emulating the numpy.correlate behavior on a logarithmic
    scale (default behavior) use:

           normalize = False
    
    """
    traceavg = np.average(a)
    if normalize and traceavg == 0:
        raise ZeroDivisionError("Normalization not possible. "+
                     "The average of the input *binned_array* is zero.")
    if copy:
        # Create a copy of the trace instead of binning the given one.
        trace = a.copy()
    else:
        trace = a
   
    if dtype is None:
        dtype = a.dtype
   
    # Check parameters
    if np.around(m/2) != m/2:
        mold = 1*m
        m = int((np.around(m/2)+1) * 2)
        warnings.warn("Invalid value of m={}. Using m={} instead"
                      .format(mold,m))
    else:
        m = int(m)
        
    if mode not in ["full", "base2"]:
        raise NotImplementedError("Unknonw mode {}!".format(mode))
    
    N = N0 = len(trace)
    # Find out the length of the correlation function
    k = int(np.floor(np.log2(N/m)))
    # Initialize correlation array
    
  
    lenG = np.int(np.floor(m+k*m/2))
    
    # Too many statistical errors and we would have to discard last
    # element of the correlation function:
    # additional data in the end if length of the input is not pow of 2
    if mode == "full":
        number = np.int(np.floor(N/2**(k+1)) - m/2) - 1
        if number == -1:
            number = 0
        lenG += number
        
    G = np.zeros((lenG, 2), dtype=dtype)
    normstat = np.zeros(lenG, dtype=dtype)
    normnump = np.zeros(lenG, dtype=dtype)
    
    # We use the fluctuation of the signal around the mean
    if normalize:
        trace -= traceavg
    if N < 2*m:
        # Otherwise the following for-loop will fail:
        raise ValueError("len(binned_array) must be larger than 2m.")
    ## Calculate autocorrelation function for first m bins
    # Discrete convolution of m elements
    for n in range(1,m+1):
        G[n-1,0] = deltat * n
        G[n-1,1] = np.sum(trace[:N-n]*trace[n:], dtype=dtype)
        normstat[n-1] = N-n
        normnump[n-1] = N
    ## Now that we calculated the first m elements of G, let us
    ## go on with the next m/2 elements.
    # Check if len(trace) is even:
    if N%2 == 1:
        N -= 1
    # Add up every second element
    trace = (trace[:N:2]+trace[1:N+1:2])/2
    N /= 2

    for step in range(1,k+1):
        # Get the next m/2 values of the trace
        for n in range(1,int(m/2)+1):
            idx = int(m + n - 1 + (step-1)*m/2)
            G[idx,0] = deltat * (n+m/2) * 2**step
            G[idx,1] = np.sum(trace[:N-(n+m/2)]*trace[(n+m/2):],
                              dtype=dtype)
            normstat[idx] = N-(n+m/2)
            normnump[idx] = N

        # Check if len(trace) is even:
        if N%2 == 1:
            N -= 1
        # Add up every second element
        trace = (trace[:N:2]+trace[1:N+1:2])/2
        N /= 2

    ## Add elements that are still evaluable:
    if mode == "full":
        step = k+1
        for n in range(1,number+1):
            idx = int(m + n - 1 + (step-1)*m/2)
            G[idx,0] = deltat * (n+m/2) * 2**step
            G[idx,1] = np.sum(trace[:N-(n+m/2)]*trace[(n+m/2):],
                              dtype=dtype) / N 
            normstat[idx] = N-(n+m/2)
            normnump[idx] = N

    
    if normalize:
        G[:,1] /= traceavg**2 * normstat
    else:
        G[:,1] *= N0/normnump 
    
    print normstat
    import IPython
    IPython.embed()
    return G



def correlate(a, v, m=16, deltat=1, normalize=False,
              copy=True, dtype=None):
    """ 
    Cross-correlation of two 1-dimensional sequences
    on a log2-scale.
    
    This computes the cross-correlation according to
    :py:func:`numpy.correlate` for positive :math:`k`  on a base 2
    logarithmic scale.
    
        numpy.correlate(a, v, mode="full")[len(a)-1:]
        
        :math:`z_k = \Sigma_n a_n v_{n+k}`
    
    Note that only the correlation
    in the positive direction is computed.
    
    
    Parameters
    ----------
    a, v : ndarrays
        Input sequences
    m : even integer
        defines the number of points on one level, must be an
        even integer
    deltat : float
        distance between bins
    normalize : bool
        normalize the result to the square of the average input
        signal and the factor (M-k). The resulting curve follows
        the convention of decaying to zero for large lag times.
    copy : bool
        copy input array, set to False to save memory
    dtype : dtype, optional
        The type of the returned array and of the accumulator in 
        which the elements are summed.  By default, the dtype of 
        `a` is used.

    Returns
    -------
    crosscorrelation : ndarray
        Nx2 array containing lag time and cross-correlation
        
    
    Notes
    -----
    For FCS, with the convention of the curve decaying to zero use:
        
           normalize = True
    
    For emulating the numpy.correlate behavior on a logarithmic
    scale (default behavior) use:

           normalize = False
    """
    traceavg1 = np.average(a)
    traceavg2 = np.average(v)
    if normalize and traceavg1*traceavg2 == 0:
        raise ZeroDivisionError("Normalization not possible. "+
                     "The average of the input *binned_array* is zero.")
    if copy:
        # Create a copy of the trace instead of binning the given one.
        trace1 = a.copy()
        trace2 = v.copy()
    else:
        trace = a
        trace = v
    
    if dtype is None:
        dtype = a.dtype
   
   
    # Check parameters
    if np.around(m/2) != m/2:
        mold = 1*m
        m = int((np.around(m/2)+1) * 2)
        warnings.warn("Invalid value of m={}. Using m={} instead"
                      .format(mold,m))
    else:
        m = int(m)
        
    if len(a) != len(v):
        raise ValueError("Arrays must be of same length.")
        
    N = N0 = len(trace1)
    # Find out the length of the correlation function
    k = int(np.floor(np.log2(N/m)))
    # Initialize correlation array
    
    # Too many statistical errors and we would have to discard last
    # element of the correlation function:
    # additional data in the end if length of the input is not pow of 2
    #number = np.int(np.floor(N/2**(k+1)) - m/2 )
    # lenG = np.int(m+k*m/2) + number
    
    
    lenG = np.int(m+k*m/2)
    G = np.zeros((lenG, 2), dtype=dtype)
    normstat = np.zeros(lenG, dtype=dtype)
    normnump = np.zeros(lenG, dtype=dtype)
    
    # We use the fluctuation of the signal around the mean
    if normalize:
        trace1 -= traceavg1
        trace2 -= traceavg2
    if N < 2*m:
        # Otherwise the following for-loop will fail:
        raise ValueError("len(binned_array) must be larger than 2m.")
    ## Calculate autocorrelation function for first m bins
    # Discrete convolution of m elements
    for n in range(1,m+1):
        G[n-1,0] = deltat * n
        G[n-1,1] = np.sum(trace1[:N-n]*trace2[n:], dtype=dtype)
        normstat[n-1] = N-n
        normnump[n-1] = N
    ## Now that we calculated the first m elements of G, let us
    ## go on with the next m/2 elements.
    # Check if len(trace) is even:
    if N%2 == 1:
        N -= 1
    # Add up every second element
    trace1 = (trace1[:N:2]+trace1[1:N+1:2])/2
    trace2 = (trace2[:N:2]+trace2[1:N+1:2])/2
    N /= 2

    for step in range(1,k+1):
        # Get the next m/2 values of the trace
        for n in range(1,int(m/2)+1):
            idx = int(m + n - 1 + (step-1)*m/2)
            G[idx,0] = deltat * (n+m/2) * 2**step
            G[idx,1] = np.sum(trace1[:N-(n+m/2)]*trace2[(n+m/2):],
                              dtype=dtype)
            normstat[idx] = N-(n+m/2)
            normnump[idx] = N

        # Check if len(trace) is even:
        if N%2 == 1:
            N -= 1
        # Add up every second element
        trace1 = (trace1[:N:2]+trace1[1:N+1:2])/2
        trace2 = (trace2[:N:2]+trace2[1:N+1:2])/2
        N /= 2

    ## Add elements that are still evaluable:
    #step = k+1
    #for n in range(1,number+1):
    #    idx = int(m + n - 1 + (step-1)*m/2)
    #    G[idx,0] = deltat * (n+m/2) * 2**step
    #    G[idx,1] = np.sum(trace[:N-(n+m/2)]*trace[(n+m/2):],
    #                      dtype=dtype) / N 
    #    print trace[:N-(n+m/2)]*trace[(n+m/2):]
    #    normstat[idx] = N-(n+m/2)
    #    normnump[idx] = N

        
    if normalize:
        G[:,1] /= traceavg1*traceavg2 * normstat
    else:
        G[:,1] *= N0/normnump 
    
    return G



def correlate_numpy(a, v, deltat=1, normalize=False,
                     dtype=None, copy=True):
    """
    Convenience function that wraps around numpy.correlate and
    returns the data as multipletau.correlate does.
        
    Parameters
    ----------
    a, v : array_like
        Input sequences
    deltat : float
        distance between bins
    normalize : bool
        normalize the result to the square of the average input
        signal and the factor (M-k). The resulting curve follows
        the convention of decaying to zero for large lag times.
    copy : bool
        copy input array, set to False to save memory
    dtype : dtype, optional
        The type of the returned array and of the accumulator in 
        which the elements are summed.  By default, the dtype of 
        `a` is used.

    Returns
    -------
    crosscorrelation : ndarray
        Nx2 array containing lag time and cross-correlation
    """
    
    avg = np.average(a)
    vvg = np.average(v)
    
    if dtype is None:
        dtype = a.dtype
    
    if len(a) != len(v):
        raise ValueError("Arrays must be of same length.")

    ab = np.array(a, dtype=dtype, copy=copy)
    vb = np.array(v, dtype=dtype, copy=copy)


    Gd = np.correlate(ab-avg, vb-vvg, mode="full")[len(ab)-1:]

    if normalize:
        N = len(Gd)
        m = N - np.arange(N)
        Gd /= m * avg * vvg
    G = np.zeros((len(Gd),2))
    G[:,1] = Gd        
    G[:,0] = np.arange(len(Gd))*deltat
    return G
        
