# This file is used to compile libraries from cython code.
# Run "python setup.py build_ext --inplace" to create those
# libraries.
# For more information visit cython.org.

from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules = [Extension("binningc", ["binningc.pyx"]),
               Extension("multipletauc", ["multipletauc.pyx"])
              ]

setup(
  name = 'Binning Stuff',
  cmdclass = {'build_ext': build_ext},
  ext_modules = ext_modules
)

