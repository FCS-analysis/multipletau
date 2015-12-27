multipletau
===========

|PyPI Version| |Build Status| |Coverage Status|

Multipe-tau correlation is computed on a logarithmic scale (less
data points are computed) and is thus much faster than conventional
correlation on a linear scale such as `numpy.correlate`. 


- **multipletau** multiple-tau package, implemented using 
- **test** testing the algorithm
- **doc** the source of the 



Installation
------------
``multipletau`` supports Python 2.6+ and Python 3.3+ with a common codebase.
The only requirement for ``multipletau`` is `NumPy <http://www.numpy.org/>`__ (for fast
operations on arrays). Install ``multipletau`` from the Python package index:

::

    pip install multipletau


Documentation
-------------
A full code reference including examples is available `here <http://FCS-analysis.github.io/multipletau/>`__.


Usage
-----

.. code:: python

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
The multipletau package should be cited like this
(replace "x.x.x" with the actual version of multipletau that you used
and "DD Month YYYY" with a matching date).

Paul Müller (2012) _Python multiple-tau algorithm_ (Version x.x.x) [Computer program]. Available at https://pypi.python.org/pypi/multipletau/ (Accessed DD Month YYYY)

You can find out what version you are using by typing (in a Python console):

.. code:: python

    >>> import multipletau
    >>> multipletau.__version__
    '0.1.4'



.. |PyPI Version| image:: http://img.shields.io/pypi/v/multipletau.svg
   :target: https://pypi.python.org/pypi/multipletau
.. |Build Status| image:: http://img.shields.io/travis/FCS-analysis/multipletau.svg
   :target: https://travis-ci.org/FCS-analysis/multipletau
.. |Coverage Status| image:: https://img.shields.io/coveralls/FCS-analysis/multipletau.svg
   :target: https://coveralls.io/r/FCS-analysis/multipletau
