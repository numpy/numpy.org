.. _obtaining:

===============
Obtaining NumPy
===============

.. _download-official:

Official Source and Binary Releases
-----------------------------------

For each official `release of NumPy`_, we provide source code (tarball)
as well as binary wheels for several major platforms (Windows, OSX, Linux) on
PyPI_. In addition, Intel releases a `patched NumPy`_ that used their proprietary
compiler and MKL libraries, please check the license before use. 

.. _release of NumPy: https://github.com/numpy/numpy/releases
.. _PyPI: https://pypi.org/project/numpy
.. _patched Numpy: https://pypi.org/project/intel-numpy/

Source Code Repository Access
-----------------------------

The most recent development version of NumPy is available through
the official repository hosted on `Github`_.

.. _Github: https://github.com/numpy/numpy

To check out the latest **NumPy** sources::

  git clone https://github.com/numpy/numpy.git numpy

To check out the latest **SciPy** sources::

  git clone https://github.com/scipy/scipy.git scipy

Build instructions
------------------

Build instructions for Numpy can be found in the documentation_.

.. _documentation: devdocs/dev/development_environment

.. _download-thirdpartypackages:

Third-Party/Vendor Package Managers
-----------------------------------

While you can install NumPy into your system-wide python, we strongly recommend
using a `virtual environment`_ and a local python install. On most linux
systems, your package manager will provide a ``python-numpy`` or
``python3-numpy`` package.

**IMPORTANT:** If you experience problems with these packages (*especially* 
those related to installation/build errors), **please report the problem to 
the package maintainer first, rather than to the NumPy/SciPy mailing lists**. 

.. _virtual environment: https://docs.python.org/3.6/library/venv.html
