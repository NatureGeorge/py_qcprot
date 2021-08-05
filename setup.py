from distutils.core import setup, Extension
from Cython.Build import cythonize
import numpy

ext_modules=[
    Extension("py_qcprot",
              sources=["py_qcprot.pyx", "qcprot.c"],
    )
]
setup(
  name = 'py_qcprot',
  ext_modules = cythonize(ext_modules),
  install_requires=['numpy'],
  include_dirs=[numpy.get_include()]
)
