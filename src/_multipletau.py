# -*- coding: utf-8 -*-
""" 
    a multiple-tau algorithm for python
    
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


__all__ = ["autocorrelate"]


def autocorrelate(binned_array, m=16, deltat=1, normalize=False,
                  copy=True, dtype=np.float64):
    """ Apply the multiple tau algorithm to a float64 numpy array *trace*
        with time differences float *deltat*. Set copy to True to not
        manipulate the incoming *trace*. If set to False, this will
        help save memory. *m* is the number of bins to use for first
        *m* values of the correlation function.
        Returns an array of tuples. First element is the lagtime
        (same dimension as deltat) and second element is autocorrelation
        function.
        
        computes the correlation as numpy.correlate does in mode="full",
        except:
            - on a logarithmic plot
            - data is normalized to len(binned_array)
            - only the correlation in one direction is computed
        
        convention: correlation function decays to zero
        
        - trace     binned photon counts
        - m         defines the number of points on one level,
                    must be an even integer
        - deltat    distance between bins
        - normalize normalize the result to the square of the average
                    input signal (common for FCS measurements)
        - copy      copy input arrays, set to true to save memory
        - dtype     what dtype should be used for the output array
        
    """
    traceavg = binned_array.mean()
    if normalize and traceavg == 0:
        raise ZeroDivisionError("Normalization not possible. "+
                     "The average of the input *binned_array* is zero.")
    if copy:
        # Create a copy of the trace instead of binning the given one.
        trace = binned_array.copy()
    else:
        trace = binned_array
   
    # Check parameters
    if np.around(m/2) != m/2:
        mold = 1*m
        m = int((np.around(m/2)+1) * 2)
        warnings.warn("Invalid value of m={}. Using m={} instead"
                      .format(mold,m))
    else:
        m = int(m)
    N = len(trace)
    # Find out the length of the correlation function
    k = int(np.floor(np.log2(N/m)))
    # Initialize correlation array
    # additional data in the end if length of the input is not pow of 2
    number = np.int(np.floor(N/2**(k+1)) - m/2 )
    
    lenG = np.int(m+k*m/2) + number 
    G = np.zeros((lenG, 2), dtype=dtype)
    # We use the fluctuation of the signal around the mean
    trace -= traceavg
    if N < 2*m:
        # Otherwise the following for-loop will fail:
        raise ValueError("len(binned_array) must be larger than 2m.")
    ## Calculate autocorrelation function for first m bins
    # Discrete convolution of m elements
    for n in range(1,m+1):
        G[n-1,0] = deltat * n
        G[n-1,1] = np.sum(trace[:N-n]*trace[n:], dtype=dtype) / N
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
            #G[idx,1] = np.sum(trace[:N-(n+m/2)]*trace[(n+m/2):],
            #                  dtype=dtype) / N
            G[idx,1] = np.sum(trace[:N-(n+m/2)]*trace[(n+m/2):],
                              dtype=dtype) / N

        # Check if len(trace) is even:
        if N%2 == 1:
            N -= 1
        # Add up every second element
        trace = (trace[:N:2]+trace[1:N+1:2])/2
        N /= 2

    # Add elements that are still evaluable:
    step = k+1
    for n in range(1,number+1):
        idx = int(m + n - 1 + (step-1)*m/2)
        G[idx,0] = deltat * (n+m/2) * 2**step
        G[idx,1] = np.sum(trace[:N-(n+m/2)]*trace[(n+m/2):],
                          dtype=dtype) / N

    if normalize:
        G[:,1] /= traceavg**2
        
    # Discard the last element which is always zero because
    # we computed the sum of an empty array.
    return G[:-1]

