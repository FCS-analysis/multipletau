#!/usr/bin/env python
# -*- coding: utf-8 -*-
u"""
Multipletau provides a multiple-τ algorithm for Python 2.7 and
Python 3.x with :py:mod:`numpy` as its sole dependency.

Multiple-τ correlation is computed on a logarithmic scale (less
data points are computed) and is thus much faster than conventional
correlation on a linear scale such as  :py:func:`numpy.correlate`.

Recommended literature
----------------------

- Klaus Schaetzel and Rainer Peters; *Noise on multiple-tau photon
  correlation data*. Proc. SPIE 1430, Photon Correlation
  Spectroscopy: Multicomponent Systems, 109 (June 1, 1991);
  http://doi.org/10.1117/12.44160

- Thorsten Wohland, Rudolf Rigler, and Horst Vogel; *The Standard
  Deviation in Fluorescence Correlation Spectroscopy*. Biophysical
  Journal, 80 (June 1, 2001);
  http://dx.doi.org/10.1016/S0006-3495(01)76264-9

Obtaining multipletau
---------------------
If you have Python and :py:mod:`numpy` installed, simply run

   pip install multipletau

The source code of multipletau is available at
https://github.com/FCS-analysis/multipletau.


Citing multipletau
------------------
The multipletau package should be cited like this (replace "x.x.x"
with the actual version of multipletau used and "DD Month YYYY"
with a matching date).

.. topic:: cite

    Paul Müller (2012) *Python multiple-tau algorithm* (Version x.x.x)
    [Computer program].
    Available at https://pypi.python.org/pypi/multipletau/
    (Accessed DD Month YYYY)


You can find out what version you are using by typing
(in a Python console):


    >>> import multipletau
    >>> multipletau.__version__
    '0.3.0'


Usage
-----
The package is straightforward to use. Here is a quick example:


    >>> import numpy as np
    >>> import multipletau
    >>> a = np.linspace(2,5,42)
    >>> v = np.linspace(1,6,42)
    >>> multipletau.correlate(a, v, m=2)
    array([[   0.        ,  569.56097561],
           [   1.        ,  549.87804878],
           [   2.        ,  530.37477692],
           [   4.        ,  491.85812017],
           [   8.        ,  386.39500297]])

"""
from .core import autocorrelate, correlate, correlate_numpy  # noqa: F401
from ._version import version as __version__  # noqa: F401

__author__ = u"Paul Müller"
__license__ = "BSD (3 clause)"
