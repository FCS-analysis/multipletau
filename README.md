multipletau
===========

This repo provides the multiple-tau algorithm for Python using Cython (~.pyx).

- **binningc.pyx**: converts 16 bit ~.dat file format to 32 bit ~.dat file format (For further information, see the documentation of PyScanFCS at http://fcstools.dyndns.org/pyscanfcs)
- **multipletauc.pyx**: a module, providing auto- and cross-correlation of binned fluorescence siganl
- **multipletau.py**: seems to be as fast as multipletauc.pyx using pure python. It is an incomplete copy though.
- **dat2csv.py**: using a photon stream from a ~.dat file, it calculates the correlation curve and saves it as a ~.csv file for PyCorrFit http://fcstools.dyndns.org/pycorrfit
- **setup.py**: compiles multipletauc.pyx and binningc.pyx using Cython

Testing the module:
- **TestMultiTau.py**: create exponentially correlated noise in a ~.dat file
- **TestMultiTauCC.py**: create exponentially cross-correlated noise in a ~.dat file
- **MakeTestDat_SFCS.py**: create a exponentially correlated noise in a ~.dat file that can be loaded with [PyScanFCS](https://github.com/paulmueller/PyScanFCS) (http://fcstools.dyndns.org/pyscanfcs)
- **ExampleFunc_Exp_correlated_noise.txt**: external model function for fitting of exponentially correlated noise using [PyCorrFit]https://github.com/paulmueller/PyCorrFit) (http://fcstools.dyndns.org/pycorrfit)
