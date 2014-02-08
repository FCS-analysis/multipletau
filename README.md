multipletau
===========

This repo provides the multiple-tau algorithm for Python using Cython (~.pyx).

- **multipletauc.pyx**: a module, providing auto- and cross-correlation of binned fluorescence siganl
- **multipletau.py**: seems to be as fast as multipletauc.pyx using pure python. It is an incomplete copy though.
- **setup.py**: compiles multipletauc.pyx using Cython

Testing the module:
- **TestMultiTau.py**: create exponentially correlated noise in a ~.dat file
- **TestMultiTauCC.py**: create exponentially cross-correlated noise in a ~.dat file

