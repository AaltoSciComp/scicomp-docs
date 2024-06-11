===
GCC
===

.. admonition:: Warning: page not updated for current Triton
  :class: warning, triton-v2-apps

  This page hasn't been updated since Triton was completely upgraded
  in May 2024.  The software might not be installed and the old
  information below might not work anymore (or  might need adapting).
  If you need this software, :ref:`open an issue <issuetracker>` and
  tell us so we can reinstall/update it.

GNU Compiler Collection (GCC) is one of the most popular compilers for compiling
C, C++ and Fortran programs.

In Triton we have various GCC versions installed, but only some of them are
actively supported.

Basic usage
-----------

.. include:: ../examples/c/hello-world/hello_gcc.rst


Available installations
-----------------------

System compiler is installed only on the login node.
Other versions of GCC are installed as modules.

.. csv-table::
   :delim: |
   :header-rows: 1

   GCC version | Module name
   4.8.5       | none (on login node only)
   8.4.0       | gcc/8.4.0
   9.3.0       | gcc/9.3.0
   11.2.0      | gcc/11.2.0

If you need a different version of GCC, please send a request through the :ref:`issue tracker <issuetracker>`.


Old installations
-----------------

These installations will work, but they are not actively updated.

.. csv-table::
   :delim: |
   :header-rows: 1

   GCC version                  | Module name
   6.5.0                        | gcc/6.5.0
   9.2.0                        | gcc/9.2.0
   9.2.0 with (CUDA offloading) | gcc/9.2.0-cuda-nvptx

Other old installations are not recommended.
