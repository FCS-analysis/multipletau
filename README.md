multipletau
===========
[![PyPI](http://img.shields.io/pypi/v/multipletau.svg)](https://pypi.python.org/pypi/multipletau)
[![Travis](http://img.shields.io/travis/paulmueller/multipletau.svg)](https://travis-ci.org/paulmueller/multipletau)
[![Coveralls](https://img.shields.io/coveralls/paulmueller/multipletau.svg)](https://coveralls.io/r/paulmueller/multipletau)



This repo contains a multiple-tau algorithm for Python

- **multipletau** multiple-tau package, implemented using [numpy](http://www.numpy.org/)
- **test** testing the algorithm
- **doc** the source of the [documentation](http://paulmueller.github.io/multipletau/)




Installation
------------
The package can be installed from the Python package index.


    pip install multipletau


Usage
-----

    >>> import numpy as np
    >>> import multipletau
    >>> a = np.linspace(2,5,42)
    >>> v = np.linspace(1,6,42)
    >>> multipletau.correlate(a, v, m=2)
    array([[   1.        ,  549.87804878],
           [   2.        ,  530.37477692],
           [   4.        ,  491.85812017],
           [   8.        ,  386.39500297]])


Citing
------
The multipletau package should be cited like this (replace "x.x.x" with the actual version of multipletau that you used and "DD Month YYYY" with a matching date).

Paul Müller (2012) _Python multiple-tau algorithm_ (Version x.x.x) [Computer program]. Available at https://pypi.python.org/pypi/multipletau/ (Accessed DD Month YYYY)

You can find out what version you are using by typing (in a Python console):


    >>> import multipletau
    >>> multipletau.__version__
    '0.1.4'
