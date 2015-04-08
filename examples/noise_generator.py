#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
This module contains methods for correlated noise generation.

"""

from __future__ import division
from __future__ import print_function

import numpy as np

__all__ = ["noise_exponential", "noise_cross_exponential"]

def noise_exponential(N, tau=20, variance=1, deltat=1):
    """
       Generate exponentially correlated noise.
       
       Parameters
       ----------
       N : integer
          Total number of samples
       tau : float
          Correlation time of the exponential in `deltat`
       variance : float
          Variance of the noise
       deltat : float
          Bin size of output array, defines the time scale of `tau`
       
       Returns
       -------
       a : ndarray
          Exponentially correlated noise.
    """
    # time constant (inverse of correlationtime tau)
    g = deltat/tau
    # variance
    s0 = variance
    
    # normalization factor (memory of the trace)
    exp_g = np.exp(-g)
    one_exp_g = 1-exp_g
    z_norm_factor = np.sqrt(1-np.exp(-2*g))/one_exp_g
    
    # create random number array
    # generates random numbers in interval [0,1)
    randarray = np.random.random(N)
    # make numbers random in interval [-1,1)
    randarray = 2*(randarray-0.5)
    
    # simulate exponential random behavior
    a = np.zeros(N)
    a[0] = one_exp_g*randarray[0]
    b = 1* a
    for i in np.arange(N-1)+1:
        a[i] = exp_g*a[i-1] + one_exp_g*randarray[i]
    
        # Solving the equation iteratively leads to this equation:
        #j = np.arange(i)
        #a[i] = a[0]*exp_g**(i) + \
        #       one_exp_g)*np.sum(exp_g**(i-1-j)*randarray[1:i+1])
        
    a = a * z_norm_factor*s0
    return a


def noise_cross_exponential(N, tau=20, variance=1, deltat=1):
    """
       Generate exponentially cross-correlated noise.
       
       Parameters
       ----------
       N : integer
          Total number of samples
       tau : float
          Correlation time of the exponential in `deltat`
       variance : float
          Variance of the noise
       deltat : float
          Bin size of output array, defines the time scale of `tau`
       
       Returns
       -------
       a, randarray : ndarrays
          Array `a` has positive exponential correlation to the 'truly'
          random array `randarray`.
    """
    # length of mean0 trace
    N_steps = N
    # time constant (inverse of correlationtime tau)
    g = deltat/tau
    # variance
    s0 = variance
    # normalization factor (memory of the trace)
    exp_g = np.exp(-g)
    one_exp_g = 1-exp_g
    z_norm_factor = np.sqrt(1-np.exp(-2*g))/one_exp_g
    
    # create random number array
    # generates random numbers in interval [0,1)
    randarray = np.random.random(N)
    # make numbers random in interval [-1,1)
    randarray = 2*(randarray-0.5)
    
    # simulate exponential random behavior
    a = np.zeros(N)
    a[0] = one_exp_g*randarray[0]
    
    b = np.zeros(N)
    b[0] = one_exp_g*randarray[0]
    # slow
    #for i in np.arange(N-1)+1:
    #    for j in np.arange(i-1):
    #        a[i] += exp_g**j*randarray[i-j]
    #    a[i] += one_exp_g*randarray[i]
    # faster
    j = np.arange(N+5)
    for i in np.arange(N-1)+1:
        a[i] += np.sum(exp_g**j[2:i+1] * randarray[2:i+1][::-1])
        a[i] += one_exp_g*randarray[i]
   
    a *= z_norm_factor*s0
    randarray = randarray * z_norm_factor*s0
    
    return a, randarray

