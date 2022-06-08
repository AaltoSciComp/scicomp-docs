===============
Intel Compilers
===============

Intel provides their own compiler suite which is popular in HPC settings.
This suite contains compilers for C (``icc``), C++ (``icpc``) and Fortran (``ifc``).

Previously this suite was licensed, but nowadays Intel provides it for free as a part of
their
`oneAPI-program <https://www.intel.com/content/www/us/en/developer/tools/oneapi/overview.html>`_.
This change has had an effect on many module names.

In Triton we have various versions of the Intel compiler suite installed, but only
some of them are actively supported.

Basic usage
-----------

Choosing a GCC for Intel compilers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Intel uses many tools from the GCC suite and thus it is recommended to
load a ``gcc``-module with it:

.. code-block:: bash

  module load gcc/8.4.0 intel-oneapi-compilers/2021.4.0

See :doc:`GCC page </triton/apps/gcc>` for more information on available GCC compilers.

.. include:: ../examples/c/hello-world/hello_icc.rst

Current installations
---------------------

There are various Intel compiler versions installed as modules.

.. csv-table::
   :delim: |
   :header-rows: 1

   Intel compiler version | Module
   2021.2.0               | intel-oneapi-compilers/2021.2.0
   2021.3.0               | intel-oneapi-compilers/2021.3.0
   2021.4.0               | intel-oneapi-compilers/2021.4.0

If you need a different version of these compilers, please send a request through the :ref:`issue tracker <issuetracker>`.

Old installations
-----------------

These installations will work, but they are not actively updated.

.. csv-table::
   :delim: |
   :header-rows: 1

   Intel compiler version                        | Module
   2019.3 with Intel MPI                         | intel-parallel-studio/cluster.2019.3-intelmpi
   2019.3                                        | intel-parallel-studio/cluster.2019.3
   2020.0 with Intel MPI                         | intel-parallel-studio/cluster.2020.0-intelmpi
   2020.0                                        | intel-parallel-studio/cluster.2020.0

Other old installations are not recommended.
