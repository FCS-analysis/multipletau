multipletau
===========

This repo contains a multiple-tau algorithm for Python

- **multipletau** multiple-tau package, implemented using [numpy](http://www.numpy.org/)
- **test** testing the algorithm
- **doc** the source of the [documentation](http://paulmueller.github.io/multipletau/)


Installation
============
The package can be installed from the Python package index.

    pip install multipletau


Usage
=====

    >>> import numpy as np
    >>> import multipletau
    >>> a = np.linspace(2,5,42)
    >>> v = np.linspace(1,6,42)
    >>> multipletau.correlate(a, v, m=2)
    array([[   1.        ,  549.87804878],
           [   2.        ,  530.37477692],
           [   4.        ,  491.85812017],
           [   8.        ,  386.39500297]])
