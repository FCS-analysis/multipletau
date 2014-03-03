#!/usr/bin/python
# -*- coding: utf-8 -*-
""" This module is used for testing the multiple-tau algorithm.
    Executing this module by invoking
    
        python __init__.py
    
    creates plots that illustrate the difference between the multiple-tau
    correlation and numpy.correlate.
"""

from __future__ import division
from __future__ import print_function

import numpy as np

__all__=["noise_exponential"]

def noise_exponential(N, tau=20., variance=1., deltat=1.):
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
       exp_noise : ndarray
          Exponentially correlated noise
    """
    # length of mean0 trace
    N_steps = N
    dt = int(deltat)
    # time trace
    t = np.arange(N_steps)
    # AR-1 processes - what does that mean?
    # time constant (inverse of correlationtime tau)
    g = 1./tau
    # variance
    s0 = variance
    
    # normalization factor (memory of the trace)
    exp_g = np.exp(-g*dt)
    one_exp_g = 1-exp_g
    z_norm_factor = np.sqrt(1-np.exp(-2*g*dt))/one_exp_g
    
    # create random number array
    # generates random numbers in interval [0,1)
    randarray = np.random.random(N_steps)
    # make numbers random in interval [-1,1)
    randarray = 2*(randarray-0.5)
    
    # simulate exponential random behavior
    z = np.zeros(N_steps)
    z[0] = one_exp_g*randarray[0]
    for i in np.arange(N_steps-1)+1:
        z[i] = exp_g*z[i-1] + one_exp_g*randarray[i]
        
    z = z * z_norm_factor*s0
    return z, t

if __name__ == "__main__":
    import os
    import sys
    from matplotlib import pylab as plt
    sys.path.append(os.path.realpath("../"))
    from multipletau import *
    
    
    # Edit parameters
    N = np.int(np.pi*1e4)
    #N= 2*16+8

    countrate = 250. # in kHz
    taudiff = 55. # in us
    deltat = 2e-6 # time discretization [s]

    print("Generating exponentially correlated noise.")
    # Do not edit
    #taudiff *= 1e-6/deltat
    data, times = noise_exponential(N, taudiff, deltat=1)
    countrate *= deltat*5000 # since we want kHz instead of Hz
    # We set one bin to 1e-6 s.


    data += - np.average(data)
    normalize = False

    if normalize:
        data += countrate


    print("Performing autocorrelation.")
    G = autocorrelate(data, deltat=deltat, normalize=normalize)

    print("Performing numpy correlation.")

    # Use numpy.correlate for comparison
    if len(data) < 1e5:
        Gd = correlate_numpy(data, data, deltat=deltat, normalize=normalize)

    # Calculate the expected curve
    x = G[:,0]
    amp = np.correlate(data-np.average(data), data-np.average(data), mode="valid")
    if normalize:
        amp /= len(data) * countrate**2
    y = amp*np.exp(-x/taudiff/deltat)


    print("Plotting.")
    fig = plt.figure()
    ax = fig.add_subplot(2,1,1)
    ax.set_xscale('log')
    if len(data) < 1e5:
        plt.plot(Gd[:,0], Gd[:,1] , "b--")
    plt.plot(G[:,0], G[:,1], "r-")

    plt.plot(x, y, "g-")
    plt.show()

    import IPython
    IPython.embed()
