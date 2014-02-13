# -*- coding: utf-8 -*-
""" Multiple Tau Algorithms
    
    Author: Paul Müller
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
        
        computes the correlation as numpy.correlate does in mode="same",
        except:
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
    k = np.floor(np.log2(N/m))
    # Initialize correlation array
    G = np.zeros((np.int(m+k*m/2), 2), dtype=dtype)
    # We use the fluctuation of the signal around the mean
    trace -= traceavg
    if N < 2*m:
        # Otherwise the following for-loop will fail:
        raise ValueError("len(binned_array) must be larger than 2m.")
    ## Calculate autocorrelation function for first m bins
    # Discrete convolution of m elements
    for n in range(1,m+1):
        G[n-1,0] = deltat*(n)
        G[n-1,1] = np.sum(trace[:N-n]*trace[n:]) / (N-n)
    ## Now that we calculated the first m elements of G, let us
    ## go on with the next m/2 elements.
    step = 0
    # Check if len(trace) is even:
    if N%2 == 1:
        N -= 1
    # Add up every second element
    trace = (trace[:N:2]+trace[1:N+1:2])/2
    N /= 2
    while N > m:
        step += 1
        # Get the next m/2 values of the trace
        for n in range(1,int(m/2)+1):
            idx = int(m + n - 1 + (step-1)*m/2)
            G[idx,0] = deltat*(n+m/2)*2**step
            G[idx,1] = np.sum(trace[:N-(n+m/2)]*trace[(n+m/2):])/(N-n-m/2)
        # We put this in the end, because we want to break the while
        # loop when we will not be able to perform it anymore.
        ## Bin the countrate array.
        # Add up every second element
        # Check if len(trace) is even:
        if N%2 == 1:
            N -= 1
        trace = (trace[:N:2]+trace[1:N+1:2])/2.
        N /= 2
    G = np.array(G)
    if normalize:
        G[:,1] /= traceavg**2
    return G



def ac_bin_old(binned_array, deltat=1, m=16, normalize=False, copy=True):
    """ Apply the multiple tau algorithm to a float64 numpy array *trace*
        with time differences float *deltat*. Set copy to True to not
        manipulate the incoming *trace*. If set to False, this will
        help save memory. *m* is the number of bins to use for first
        *m* values of the correlation function.
        Returns an array of tuples. First element is the lagtime
        (same dimension as deltat) and second element is autocorrelation
        function.
        
        returns the same as numpy.correlate with mode="same", except:
            - data is normalized to len(binned_array)
            - only the correlation in one direction is computed
            
        
        convention: correlation function decays to zero
        
        - trace     binned photon counts
        - deltat    distance between bins
        - m         defines the number of points on one level,
                    must be an even integer
        - normalize normalize the result (common for FCS measurements)
        - copy      copy input arrays, set to true to save memory
        
    """
    ##
    ## TODO:
    ##   - Determine the total size of G beforehand and stop using lists
    #
    # Code was adapted from a C script from Fabian Heinemann.
    #
    # Autocorrelation function is a list of tuples
    #
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
    G = []
    N = len(trace)
    traceavg = trace.mean()
    trace -= traceavg
    if N < 2*m:
        # Otherwise the following for-loop will fail:
        raise ValueError("len(trace) must be larger than 2m")
    ## Calculate autocorrelation function for first m bins
    # Discrete convolution of m elements
    for n in range(1,m+1):
        Gtmp = 0
        Gtmp = np.sum(trace[:N-n]*trace[n:])
        Gtmp = 1.*Gtmp/((N-n))
        # Append to array
        G.append((deltat*(n), Gtmp))
    ## Now that we calculated the first m elements of G, let us
    ## go on with the next few elements.
    ## Calculate how many times we may perform binning migth increase 
    ## performance ? No, we bin less than 10000 times.
    step = 0
    ## Bin the countrate array.
    # Add up every second element
    # Check if len(trace) is even:
    if N%2 == 1:
        N -= 1
    trace = (trace[:N:2]+trace[1:N+1:2])/2
    N = N/2
    while N > m:
        step += 1
        # Get the next m/2 values of the trace
        for n in range(1,int(m/2)+1):
            Gtmp = 0
            # We only need elements from m/2 on.
            # This saves computing time.
            Gtmp = np.sum(trace[:N-(n+m/2)]*trace[(n+m/2):])
            Gtmp = 1.*Gtmp/((N-n-m/2))
            # Append to array
            G.append((deltat*(n+m/2)*2**step, Gtmp))
        # We put this in the end, because we want to break the while
        # loop when we will not be able to perform it anymore.
        ## Bin the countrate array.
        # Add up every second element
        # Check if len(trace) is even:
        if N%2 == 1:
            N = N-1
        trace = (trace[:N:2]+trace[1:N+1:2])/2
        N = N/2
        
    G = np.array(G)
    if normalize:
        G[:,1] /= traceavg**2
    return G
