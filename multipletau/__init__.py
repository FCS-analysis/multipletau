#!/usr/bin/env python
# -*- coding: utf-8 -*-
u""" 
    Provides a multiple-τ algorithm for Python 2.7 and Python 3.x and
    requires the package :py:mod:`numpy`.

    Multipe-τ correlation is computed on a logarithmic scale (less
    data points are computed) and is thus much faster than conventional
    correlation on a linear scale such as  :py:func:`numpy.correlate`.

    Recommended literature: 
    
    - Klaus Schaetzel and Rainer Peters; *Noise on multiple-tau photon
      correlation data*. Proc. SPIE 1430, Photon Correlation
      Spectroscopy: Multicomponent Systems, 109 (June 1, 1991);    
      http://doi.org/10.1117/12.44160
      
    - Thorsten Wohland, Rudolf Rigler, and Horst Vogel; *The Standard 
      Deviation in Fluorescence Correlation Spectroscopy*. Biophysical
      Journal, 80 (June 1, 2001);  
      http://dx.doi.org/10.1016/S0006-3495(01)76264-9
      
    The source code of multipletau is available at
    https://github.com/paulmueller/multipletau.
"""
from ._multipletau import *
from ._version import version as __version__

__author__ = u"Paul Müller"
__license__ = "OpenBSD"
