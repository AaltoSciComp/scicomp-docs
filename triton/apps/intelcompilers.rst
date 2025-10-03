===============
Intel Compilers
===============

Intel provides their own compiler suite which is popular in HPC settings.
This suite contains compilers for C (``icx``), C++ (``icpx``) and Fortran (``ifx``).

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
have a ``gcc``-module loaded with it:

.. code-block:: bash

  module load triton/2024.1-gcc gcc/12.3.0 intel-oneapi-compilers/2023.2.1

Intel compilers from `triton/2025.1-intel` environment and newer make the relevant 
gcc available automatically.

See :doc:`GCC page </triton/apps/gcc>` for more information on available GCC compilers.

.. include:: ../examples/c/hello-world/hello_icc.rst

Current installations
---------------------

There are various Intel compiler versions installed as modules. 
To make them available, you need to first load the appropriate software stack module.

.. csv-table::
   :delim: |
   :header-rows: 1

   Intel compiler version | Module                            | Software stack
   2023.2.1               | intel-oneapi-compilers/2023.2.1   | triton/2024.1-gcc
   2025.0.0               | intel-oneapi-compilers/2025.0.0   | triton/2025.1-intel

If you need a different version of these compilers, please send a request through the :ref:`issue tracker <issuetracker>`.