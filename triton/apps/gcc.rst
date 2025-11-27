===
GCC
===

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
Other versions of GCC are installed as modules and are all part of one 
of our software stacks. To make them available, you need to first load 
the appropriate software stack module. Versions labeled "default" are 
the ones that have been used to build the rest of that software stack.

.. csv-table::
   :delim: |
   :header-rows: 1

   GCC version       | Module name                 | Software stack
   11.5.0            | none (on login node only)   | none (available by default)
   6.5.0             | gcc/6.5.0                   | triton/2024.1-gcc
   10.5.0            | gcc/10.5.0                  | triton/2024.1-gcc
   11.4.0            | gcc/11.4.0                  | triton/2024.1-gcc
   12.3.0 (default)  | gcc/12.3.0                  | triton/2024.1-gcc
   13.2.0            | gcc/13.2.0                  | triton/2024.1-gcc
   13.3.0 (default)  | gcc/13.3.0                  | triton/2025.1-gcc


If you need a different version of GCC, please send a request through the :ref:`issue tracker <issuetracker>`.
