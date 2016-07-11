#!/usr/bin/python
# -*- coding: utf-8 -*-
""" 
Comparison of correlation methods
---------------------------------
Comparison between the :py:mod:`multipletau` correlation methods
(:py:func:`multipletau.autocorrelate`, :py:func:`multipletau.correlate`) and :py:func:`numpy.correlate`.

.. image:: ../examples/compare_correlation_methods.png
   :align:   center

Download the 
:download:`full example <../examples/compare_correlation_methods.py>`.    
"""
from __future__ import print_function

import numpy as np
import os
from os.path import abspath, dirname, join
import sys
import time

sys.path.insert(0, dirname(dirname(abspath(__file__))))

from noise_generator import noise_exponential, noise_cross_exponential
from multipletau import autocorrelate, correlate, correlate_numpy


def compare_corr():
    ## Starting parameters
    N = np.int(np.pi*1e3)
    countrate = 250. * 1e-3 # in Hz
    taudiff = 55. # in us
    deltat = 2e-6 # time discretization [s]
    normalize = True

    # time factor
    taudiff *= deltat

    if N < 1e5:
        do_np_corr = True
    else:
        do_np_corr = False

    ## Autocorrelation
    print("Creating noise for autocorrelation")
    data = noise_exponential(N, taudiff, deltat=deltat)
    data -= np.average(data)
    if normalize:
        data += countrate
    # multipletau
    print("Performing autocorrelation (multipletau).")
    G = autocorrelate(data, deltat=deltat, normalize=normalize)
    # numpy.correlate for comparison
    if do_np_corr:
        print("Performing autocorrelation (numpy).")
        Gd = correlate_numpy(data, data, deltat=deltat,
                             normalize=normalize)
    else:
        Gd = G
    
    ## Cross-correlation
    print("Creating noise for cross-correlation")
    a, v = noise_cross_exponential(N, taudiff, deltat=deltat)
    a -= np.average(a)
    v -= np.average(v)
    if normalize:
        a += countrate
        v += countrate
    Gccforw = correlate(a, v, deltat=deltat, normalize=normalize) # forward
    Gccback = correlate(v, a, deltat=deltat, normalize=normalize) # backward
    if do_np_corr:
        print("Performing cross-correlation (numpy).")
        Gdccforw = correlate_numpy(a, v, deltat=deltat, normalize=normalize)
    
    ## Calculate the model curve for cross-correlation
    xcc = Gd[:,0]
    ampcc = np.correlate(a-np.average(a), v-np.average(v), mode="valid")
    if normalize:
        ampcc /= len(a) * countrate**2
    ycc = ampcc*np.exp(-xcc/taudiff)

    ## Calculate the model curve for autocorrelation
    x = Gd[:,0]
    amp = np.correlate(data-np.average(data), data-np.average(data),
                       mode="valid")
    if normalize:
        amp /= len(data) * countrate**2
    y = amp*np.exp(-x/taudiff)


    ## Plotting
    # AC
    fig = plt.figure()
    fig.canvas.set_window_title('testing multipletau')
    ax = fig.add_subplot(2,1,1)
    ax.set_xscale('log')
    if do_np_corr:
        plt.plot(Gd[:,0], Gd[:,1] , "-", color="gray", label="correlate (numpy)")
    plt.plot(x, y, "g-", label="input model")
    plt.plot(G[:,0], G[:,1], "-",  color="#B60000", label="autocorrelate")
    plt.xlabel("lag channel")
    plt.ylabel("autocorrelation")
    plt.legend(loc=0, fontsize='small')
    plt.ylim( -amp*.2, amp*1.2)
    plt.xlim( Gd[0,0], Gd[-1,0])

    # CC
    ax = fig.add_subplot(2,1,2)
    ax.set_xscale('log')
    if do_np_corr:
        plt.plot(Gdccforw[:,0], Gdccforw[:,1] , "-", color="gray", label="forward (numpy)")
    plt.plot(xcc, ycc, "g-", label="input model")
    plt.plot(Gccforw[:,0], Gccforw[:,1], "-", color="#B60000", label="forward")
    plt.plot(Gccback[:,0], Gccback[:,1], "-", color="#5D00B6", label="backward")
    plt.xlabel("lag channel")
    plt.ylabel("cross-correlation")
    plt.legend(loc=0, fontsize='small')
    plt.ylim( -ampcc*.2, ampcc*1.2)
    plt.xlim( Gd[0,0], Gd[-1,0])
    plt.tight_layout()

    savename = __file__[:-3]+".png"
    if os.path.exists(savename):
        savename = __file__[:-3]+time.strftime("_%Y-%m-%d_%H-%M-%S.png")

    plt.savefig(savename)
    print("Saved output to", savename)


if __name__ == '__main__':
    # move mpl import to main so travis automated doc build does not complain
    from matplotlib import pylab as plt
    compare_corr()
