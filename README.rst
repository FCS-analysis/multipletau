multipletau
===========

|PyPI Version| |Tests Status| |Coverage Status| |Docs Status|

Multiple-tau correlation is computed on a logarithmic scale (less
data points are computed) and is thus much faster than conventional
correlation on a linear scale such as `numpy.correlate <http://docs.scipy.org/doc/numpy/reference/generated/numpy.correlate.html>`__. 


Installation
------------
Multipletau supports Python 2.7 and Python 3.3+ with a common codebase.
The only requirement for ``multipletau`` is `NumPy <http://www.numpy.org/>`__ (for fast
operations on arrays). Install multipletau from the Python package index:

::

    pip install multipletau


Documentation
-------------

The documentation, including the reference and examples, is available on `readthedocs.io <https://multipletau.readthedocs.io/en/stable/>`__.


Usage
-----

.. code:: python

    import numpy as np
    import multipletau
    a = np.linspace(2,5,42)
    v = np.linspace(1,6,42)
    multipletau.correlate(a, v, m=2)
    array([[   0.        ,  569.56097561],
    	   [   1.        ,  549.87804878],
           [   2.        ,  530.37477692],
           [   4.        ,  491.85812017],
           [   8.        ,  386.39500297]])


Citing
------
The multipletau package should be cited like this
(replace "x.x.x" with the actual version of multipletau that you used
and "DD Month YYYY" with a matching date).

Paul Müller (2012) *Python multiple-tau algorithm* (Version x.x.x) [Computer program]. Available at `<https://pypi.python.org/pypi/multipletau/>`__ (Accessed DD Month YYYY)

You can find out what version you are using by typing (in a Python console):

.. code:: python

    >>> import multipletau
    >>> multipletau.__version__
    '0.3.0'



.. |PyPI Version| image:: https://img.shields.io/pypi/v/multipletau.svg
   :target: https://pypi.python.org/pypi/multipletau
.. |Tests Status| image:: https://img.shields.io/github/actions/workflow/status/FCS-analysis/multipletau/check.yml
   :target: https://github.com/FCS-analysis/multipletau/actions?query=workflow%3AChecks
.. |Coverage Status| image:: https://img.shields.io/codecov/c/github/FCS-analysis/multipletau/master.svg
   :target: https://codecov.io/gh/FCS-analysis/multipletau
.. |Docs Status| image:: https://readthedocs.org/projects/multipletau/badge/?version=latest
   :target: https://readthedocs.org/projects/multipletau/builds/
