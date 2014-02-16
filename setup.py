# setup.py

from distutils.core import setup
from distutils.extension import Extension
import numpy

try:
    from Cython.Distutils import build_ext
except ImportError:
    from distutils.command import build_ext

setup( name = 'pnpoly',
       version = '0.1',
       author = 'Greg von Winckel',
       description = 'Identify points in polygon',
       ext_modules=[Extension("pnpoly",sources=["pnpoly.pyx"],
                        include_dirs=[numpy.get_include()]),
       ],
       cmdclass = {'build_ext': build_ext},
)          
