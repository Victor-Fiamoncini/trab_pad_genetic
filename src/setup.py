from distutils.core import setup
from Cython.Build import cythonize

setup(name="parallel_test", ext_modules=cythonize('parallel_test.pyx'),)
