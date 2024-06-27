multipletau documentation
=========================

General
:::::::
.. automodule:: multipletau
   :members:

Methods
:::::::

Summary:

.. autosummary:: 
    autocorrelate
    correlate
    correlate_numpy


.. _sec_ac:

Autocorrelation
---------------
.. autofunction:: autocorrelate


.. _sec_cc:

Cross-correlation
-----------------
.. autofunction:: correlate


.. _sec_cc_numpy:

Cross-correlation (NumPy)
-------------------------
.. autofunction:: correlate_numpy


.. _sec_constants:

Constants
---------
.. autodata:: multipletau.core.ZERO_CUTOFF


.. _sec_examples:

Examples
========
.. fancy_include:: compare_correlation_methods.py



.. _sec_changelog:

Changelog
=========
List of changes in-between nanite releases.

.. include_changelog:: ../CHANGELOG
