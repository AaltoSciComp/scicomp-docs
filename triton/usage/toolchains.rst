========================
Compilers and toolchains
========================

Individual compilers
~~~~~~~~~~~~~~~~~~~~

Some of our compilers are available as individual modules.
If you simply want a compiler, we recommend you use these modules.

.. include:: ../ref/compilers.rst

If you need libraries or tools (e.g. ``openmpi`` or ``cmake``) to compile
your software, use modules with lower-case names. These modules are
individual modules that do not have extra toolchain requirements.

Toolchains
~~~~~~~~~~

Some modules in Triton are organized in so-called toolchains. These are
collections of compilers and tools that are used for compiling
specialized software.

Typically a toolchain contains a compiler and a MPI implementation, but
it can also contain additional mathematical and computational libraries.

Naming convention is from
`EasyBuild <https://github.com/easybuilders/easybuild>`__ that is used to
administer the software collections. It goes like:

<compiler><mpi><blas><lapack><fftw><cuda>

eg.
**G**\ CC,\ **O**\ penMPI,\ **O**\ penBLAS,\ **L**\ APACK,\ **F**\ FTW,\ **C**\ UDA
would result in toolchain **goolfc**

Toolchains in detail
~~~~~~~~~~~~~~~~~~~~

.. include:: ../ref/toolchains.rst


Some of our software is compiled against these toolchains and we
update them to newer versions if needed. If you require older versions of
e.g. GCC we will install them as individual modules.

When asking for specialized software, these will be used as the starting
point. E.g. Armadillo/6.700.3-goolf-triton-2016a-Python-2.7.11 uses
goolf-triton-2016a as the base.
