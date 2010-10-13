====================
Older Array Packages
====================

Links to the older array packages for Python are provided here. New users
should start out with NumPy.

.. Much of the documentation for Numeric and Numarray is applicable to the NumPy
.. package.  However, there are :ref:`significant feature improvements
.. <new_features>`.  A complete guide to the new system has been written by the
.. primary developer, Travis Oliphant. It is now in the public domain.  Other
.. Documentation is available at `the scipy website <http://www.scipy.org/>`_ and
.. in the docstrings (which can be extracted using pydoc).
..
.. Free Documentation for
.. Numeric (most of which is still valid) is `here
.. <http://numpy.scipy.org/numpydoc/numdoc.htm>`_ or as a `pdf
.. <http://numpy.scipy.org/numpy.pdf>`_ file.   Obviously you should replace
.. references to Numeric in that document with numpy (i.e. instead of "import
.. Numeric", use "import numpy").

Upgrading from historical implementations
=========================================

NumPy derives from the old Numeric code base and can be used as a replacement
for Numeric.   It also adds the features introduced by Numarray and can also be
used to replace Numarray.

Numeric users should find the transition relatively easy (although not without
some effort).  There is a module (numpy.oldnumeric.alter_code1) that can
makemost of the necessary changes to your Python code that used Numeric to work
with NumPy's Numeric compatibility module.

Users of numarray can also transition their code using a similar module
(``numpy.numarray.alter_code1``) and the numpy.numarray compatibility layer.

C-code written to either package can be easily ported to NumPy using
"numpy/oldnumeric.h" and "numpy/libnumarray.h" for the Numeric C-API and the
Numarray C-API respectively.

For about 6 months at the end of 2005, Numpy was called SciPy Core (not to be
confused with the full SciPy package which remains a `separate
<http://www.scipy.org/>`_ package), and so you may occasionally see references
to SciPy Core floating around.  It was, however, decided in January 2006 to go
with the historical name of NumPy for the new package.

Numeric (version 24.2)
======================

Numeric was the first array object built for Python.  It has been quite
successful and is used in a wide variety of settings and applications.
Maintenance has ceased for Numeric, and users should transisition to NumPy as
quickly as possible.   There is a module called numpy.oldnumeric.alter_code1 in
NumPy that can make the transition to NumPy easier (it will automatically
perform the search-and-replace style changes that need to be made to python
code that uses Numeric to make it work with NumPy).

`Sourceforge Download Page for Numeric <http://sourceforge.net/project/showfiles.php?group_id=1369&package_id=1351>`__

Numarray
========

Numarray is another implementation of an array object for Python written after
Numeric and before NumPy. Sponsors of numarray have indicated they will be
moving to NumPy as soon as is feasible for them so that eventually numarray
will be phased out (probably sometime in 2007). This project shares some of the
resources with the Numeric sourceforge site but maintains its own web page at
http://www.stsci.edu/resources/software_hardware/numarray

`Sourceforge Download Page for Numarray <http://sourceforge.net/project/showfiles.php?group_id=1369&package_id=32367>`__
