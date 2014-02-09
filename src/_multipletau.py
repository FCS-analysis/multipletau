# -*- coding: utf-8 -*-
""" Multiple Tau Algorithms
    
    Author: Paul Müller
"""

import numpy as np
import platform

__all__ = ["ac_bin"]

def ac_bin(trace, deltat, m=16, copy=False):
    """ Apply the multiple tau algorithm to a float64 numpy array *trace*
        with time differences float *deltat*. Set copy to True to not
        manipulate the incoming *trace*. If set to False, this will
        help save memory. *m* is the number of bins to use for first
        *m* values of the correlation function.
        Returns an array of tuples. First element is the lagtime
        (same dimension as deltat) and second element is autocorrelation
        function.
    """
    # Code was adapted from a C script from Fabian Heinemann.
    #
    # Autocorrelation function is a list of tuples
    G = []
    N = len(trace)
    traceavg = trace.mean()
    if N < 2*m:
        # Otherwise the following for-loop will fail:
        raise ValueError("len(trace) must be larger than 2m")
    ## Calculate autocorrelation function for first m bins
    # Discrete convolution of m elements
    for n in np.arange(m):
        Gtmp = 0
        Gtmp = np.sum(trace[:N-(n+1)]*trace[(n+1):])
        #for j in np.arange(N-(n+1)):
        #    Gtmp += trace[j]*trace[j+n+1]
        # Normalize G(n)
        # Sutract 1, because we calculated G from signal,
        # not from signal deviations.
        Gtmp = 1.*Gtmp/((N-n-1)*traceavg**2)
        # Append to array
        G.append((deltat*(n+1), Gtmp))
    ## Now that we calculated the first m elements of G, let us
    ## go on with the next few elements.
    if copy != False:
        # Create a copy of the trace instead of binning the given one.
        trace = 1.*trace
    ## Calculate how many times we may perform binning migth increase 
    ## performance ? No, we bin less than 10000 times.
    step = 0
    ## Bin the countrate array.
    # Add up every second element
    # Check if len(trace) is even:
    if N%2 == 1:
        N = N-1
    trace = (trace[:N:2]+trace[1:N+1:2])/2.
    N = N/2
    while N >= m:
        step += 1
        # Get the next m/2 values of the trace
        for n in np.arange(m/2):
            Gtmp = 0
            # We only need elements from m/2 on.
            # This saves computing time.
            ## Might be faster with arrays?
            Gtmp = np.sum(trace[:N-(n+1+m/2)]*trace[(n+1+m/2):])
            #for j in np.arange(N-(n+1+m/2)):
            #    Gtmp += trace[j]*trace[j+n+1+m/2]
            # Normalize G(n)
            # Sutract 1, because we calculated G from signal,
            # not from signal deviations.
            Gtmp = 1.*Gtmp/((N-n-1-m/2)*traceavg**2)
            # Append to array
            G.append((deltat*(n+1+m/2)*2**step, Gtmp))
        # We put this in the end, because we want to break the while
        # loop when we will not be able to perform it anymore.
        ## Bin the countrate array.
        # Add up every second element
        # Check if len(trace) is even:
        if N%2 == 1:
            N = N-1
        trace = (trace[:N:2]+trace[1:N+1:2])/2.
        N = N/2
    return np.array(G)











