=========
Libraries
=========

BLAS
====

**Basic Linear Algebra Subroutine** (**BLAS**) is a *de facto*
application programming interface standard for publishing libraries to
perform basic linear algebra operations such as vector and matrix
multiplication (from wikipedia).

On triton a number of different BLAS implementations are available. The
recommended ones are **MKL** and **OpenBLAS**. Other available BLAS
libraries are ATLAS, GotoBLAS2 ,ACML, and the Netlib reference BLAS. For
benchmark results see

::

    DGEMM benchmark on triton


Using MKL
---------

In order to use the MKL library you need to load the module. MKL is
provided both in the "mkl" modules and in the "intel" modules; the
"intel" module additonally give you the Intel compilers and debuggers.
Linking with MKL is a bit tricky and the exact link options varies from
version to version. Intel provides a webpage to build the correct
linking options at
http://software.intel.com/en-us/articles/intel-mkl-link-line-advisor .

Using OpenBLAS
--------------

OpenBLAS is installed on all the triton nodes on the default library
directory (/usr/lib64). 3 different variants of the library are
provided:

-  Serial version: Link using "-lopenblas"
-  OpenMP version: Link using "-lopenblaso"
-  pthreads version: Link using "-lopenblasp"

Other BLAS libraries
--------------------

In general MKL and OpenBLAS are recommended since they both provide good
performance on both the Xeon and Opteron nodes. Other BLAS libraries
have various issues such as crashing when running on the incorrect node
(e.g. running an Xeon optimized library on an Opteron node or vice
versa), or poor performance. In particular, the Netlib reference BLAS
has **VERY** poor performance and should be avoided at all cost. Use it
only for testing or if you need to debug numeric output. As can be seen
on the `DGEMM benchmark results <LINK/Benchmarks>`__ performance for
large matrices is an order of magnitude worse than the optimized
versions. For a real example see for instance
`tracker.triton.aalto.fi/issue194 <http://tracker.triton.aalto.fi/issue194>`__
where 50% performance loss was seen for a complete application.

LAPACK
======

**L**\ inear **A**\ lgebra **Pack**\ age (LAPACK) is a library of
numerical linear algebra algorithms, built on top of BLAS. The
recommended LAPACK implementation on triton is **MKL**. See instructions
above for how to use it.

Another option is architecture specific optimization and run on either
Opterons or Xeons only (see ``--constraint=opteron`` and
``--constraint=xeon`` options for sbatch/salloc). ``module avail`` shows
a number of alternatives:

::

    gotoblas2/opteron-1.13-gcc
    gotoblas2/xeon-1.13-gcc
    lapack/opteron-3.4.0-gcc
    lapack/xeon-3.4.0-gcc

These guys are compiled with the specific optimization for Xeons or
Opterons. Although GotoBlas2 is no longer developed it still provides
very efficient BLAS routines. Using that instead of generic BLAS is
recommended.

Usage for Opterons:

::

    $ module load gotoblas2/opteron-1.13-gcc
    $ module load lapack/opteron-3.4.0-gcc

Usage for Xeons:

::

    $ module load gotoblas2/xeon-1.13-gcc
    $ module load lapack/xeon-3.4.0-gcc

Check out with ``module list`` that you have no Opteron and Xeon libs
loaded at the same time and thus overlaping.

Scalapack
=========

MKL contains an implementation of ScaLAPACK as well, please try to use
that one first. Again, see the BLAS section for how to link with MKL.

Benchmark is done with full Scalapack LIN/EIG testsuite with 24
processors. Scalapack is compiled with -O3 using architecture optimized
gotoblas2. Given numbers are WallClockTimes in seconds.

+--------------------------+--------------------------+--------------------------+
| Library                  | Xeon processors          | Opteron processors       |
+==========================+==========================+==========================+
| Xeon-gcc optimized       | 342s                     | -na-                     |
| scalapack                |                          |                          |
+--------------------------+--------------------------+--------------------------+
| Opteron-gcc optimized    | 338s                     | 291s                     |
| scalapack                |                          |                          |
+--------------------------+--------------------------+--------------------------+
| Intel-compiler-mkl       | -na-                     | -na-                     |
+--------------------------+--------------------------+--------------------------+

Scalapck libs are available under /share/apps/scalapack/2.0.1/

FFT
===

The FFTW library is available on triton, in several different variants.
The recommended one is the one provided by MKL; see the BLAS section
above for how to link to it.

+--------------+--------------------------------+--------------------------------------------------------------------------------------------+
| Library      | module                         | Link line                                                                                  |
+==============+================================+============================================================================================+
| FFTW 3.2.1   | -                              | -lfftw3 / -lfftw3\_threads / -lfftw3f / -lfftw3f\_threads / -lfftw3l / -lfftw3l\_threads   |
+--------------+--------------------------------+--------------------------------------------------------------------------------------------+
| FFTW 3.3.2   | fftw/3.3.2                     | -lfftw3 / -lfftw3\_mpi                                                                     |
+--------------+--------------------------------+--------------------------------------------------------------------------------------------+
| MKL          | intel/VERSION or mkl/VERSION   | See http://software.intel.com/en-us/articles/intel-mkl-link-line-advisor                   |
+--------------+--------------------------------+--------------------------------------------------------------------------------------------+

Links
~~~~~

-  BLAS at `www.netlib.org/blas <http://www.netlib.org/blas>`__
-  LAPACK at `www.netlib.org/lapack <http://www.netlib.org/lapack>`__
-  GotoBLAS FAQ at
   [www.tacc.utexas.edu/tacc-projects/gotoblas2/faq\|http://www.tacc.utexas.edu/tacc-projects/gotoblas2/faq]
-  ACML User's Guide (pdf file) at
   `developer.amd.com/assets <http://developer.amd.com/assets/acml_userguide.pdf>`__
