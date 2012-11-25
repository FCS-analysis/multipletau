multipletau
===========

This repo provides the multiple-tau algorithm for calculation of correlation curves in Python.

- **multipletauc.pyx**: multiple-tau algorithm in Cython language (compile with setup.py)
- **binningc.pyx**: Convert 16 bit ~.dat file format to 32 bit ~.dat file format (See documentation of PyScanFCS at http://fcstools.dyndns.org/pyscanfcs)
- **dat2csv.py**: Using a photon stream from a ~.dat file, calculate the correlation curve and save as a ~.csv file for PyCorrFit http://fcstools.dyndns.org/pycorrfit
- **setup.py**: Compiles multipletauc.pyx and binningc.pyx using Cython

Testing the module:
- **TestMultiTau.py**: create exponentially correlated noise
- **TestMultiTauCC.py**: create exponentially cross-correlated noise
- **MakeTestDat_SFCS.py**: create a exponentially correlated noise in a ~.dat file that can be loaded with [PyScanFCS](https://github.com/paulmueller/PyScanFCS) (http://fcstools.dyndns.org/pyscanfcs)
- **ExampleFunc_Exp_correlated_noise.txt**: external model function for fitting of exponentially correlated noise using [PyCorrFit]https://github.com/paulmueller/PyCorrFit) (http://fcstools.dyndns.org/pycorrfit)
