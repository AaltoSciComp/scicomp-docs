===============
Intel Compilers
===============

Intel provides their own compiler suite which is popular in HPC settings.
This suite contains compilers for C (``icc``), C++ (``icpc``) and Fortran (``ifc``).

Previously this suite was licensed, but nowadays Intel provides it for free as a part of
their
`oneAPI-program <https://www.intel.com/content/www/us/en/developer/tools/oneapi/overview.html>`_.
This change has had an effect on many module names.

In Triton we have various versions of Intel compiler suite installed, but only
some of them are actively supported.

Basic usage
-----------

Choosing a GCC for Intel compilers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Intel uses many tools from the GNU suite and thus requires a GCC for compilation.
Thus it is recommended to load a GCC with

.. code-block:: bash

  module load gcc/8.4.0 intel-oneapi-compilers/2021.3.0

See :ref:`GCC page <triton/apps/gcc>` for more information on available GCC compilers.

.. include:: ../examples/c/hello-world/hello_icc.rst

Current installations
---------------------

Besides system compiler on login node, there are various GCC versions installed as modules.

.. csv-table::
   :delim: |
   :header-rows: 1

   GCC version | Module
   4.8.5       | none (on login node only)
   8.4.0       | gcc/8.4.0
   9.3.0       | gcc/9.3.0
   11.2.0      | gcc/11.2.0

Old installations
-----------------

These installations will work, but they are not actively updated.

.. csv-table::
   :delim: |
   :header-rows: 1

   GCC version                  | Module
   6.5.0                        | gcc/6.5.0
   9.2.0                        | gcc/9.2.0
   9.2.0 with (CUDA offloading) | gcc/9.2.0-cuda-nvptx

Other old installations are not recommended.
