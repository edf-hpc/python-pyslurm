***********************************
PySlurm: Slurm Interface for Python
***********************************

:Authors: Mark Roberts <mark@gingergeeks.co.uk> and Giovanni Torres <giovanni.torres@gmail.com>

Overview
========

Currently `PySlurm` is under development to move from it's thin layer on top of the Slurm C API to an object orientated interface.

This release is based on Slurm 16.05.

Pre-requistes
*************

* [Slurm] http://www.schedmd.com
* [Python] http://www.python.org
* [Cython] http://www.cython.org

This PySlurm branch has been tested with:

    * Cython 0.15.1, 0.19.2, and 0.24
    * Python 2.6 and 2.7
    * Slurm 16.05.0 thru 16.05.4

Installation
************

You will need to instruct the setup.py script where either the Slurm install root 
directory or where the Slurm libraries and Slurm include files are :

#. Slurm default directory (/usr):

    * python setup.py build

    * python setup.py install

#. Indicate Blue Gene type (L/P/Q) on build line:

    * --bgl or --bgp or --bgq

#. Slurm root directory (Alternate installation directory):

    * python setup.py build --slurm=PATH_TO_SLURM_DIR

    * python setup.py install

#. Separate Slurm library and include directory paths:

    * python setup.py build --slurm-lib=PATH_TO_SLURM_LIB --slurm-inc=PATH_TO_SLURM_INC

    * python setup.py install

#. The build will automatically call a cleanup procedure to remove temporary build files but this can be called directly if needed as well with :

    * python setup.py clean

Documentation
*************

`Sphinx <http://www.sphinx-doc.org>`_ (needs to be installed) is currently used to generate the 
documentation from the reStructuredText based doc strings from the module once it is built 
and can be regenerated at any time :

    * cd doc
    * make clean
    * make html

Help
****

Ask questions on the `pyslurm group <https://groups.google.com/forum/#!forum/pyslurm>`_.
