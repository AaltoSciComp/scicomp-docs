Available compilers
-------------------

Please see full up to date listing of different toolchains and
compilers from  :doc:`Applications <../apps/index>`\ -page. This page
contains information on their usage.

GCC
~~~

Triton has the GCC set of compilers installed by default, but we
recommend that you use the provided module versions. The GNU Compiler
Collection (aka GCC) includes front ends for C, C+, Objective-C,
Fortran, Java, Ada, and Go, as well as libraries for these languages
(libstdc+, libgcj,...). In case of missing features,  :doc:`contact
admins <../help>`.

::

    $ gcc -v

    Using built-in specs.
    COLLECT_GCC=gcc
    COLLECT_LTO_WRAPPER=/share/apps/easybuild/software/GCCcore/5.4.0/libexec/gcc/x86_64-unknown-linux-gnu/5.4.0/lto-wrapper
    Target: x86_64-unknown-linux-gnu
    Configured with: ../configure --enable-languages=c,c++,fortran --enable-lto --enable-checking=release --disable-multilib --enable-shared=yes --enable-static=yes --enable-threads=posix --enable-gold=default --enable-plugins --enable-ld --with-plugin-ld=ld.gold --enable-bootstrap --prefix=/share/apps/easybuild/software/GCCcore/5.4.0 --with-local-prefix=/share/apps/easybuild/software/GCCcore/5.4.0
    Thread model: posix
    gcc-versio 5.4.0 (GCC) 

Example usage:

::

    $ gcc -lm -o my_code.c my_code  # compiling your C code and linking with Math lib
    $ gfortran -O2 -o my_code  my_code.f90 # compiling your Fortran code with -O2 optimization level (see also g77 for Fortran 77)
    $ g++ -O3 -funroll-loops -ffast-math -ftree-vectorize -mtune=native -o my_code  my_code.cpp # compiling your C++ code with aggressive optimizaton and architecture tuning

Thus GCC is the default compiler and is used to build most of the
software in the cluster.

See ``man gcc``, ``man gfortran`` and other mans for options. Online
`GCC Documentation <http://gcc.gnu.org/onlinedocs>`__.

GCC compiling examples
^^^^^^^^^^^^^^^^^^^^^^

::

    $ cat hello.c
    #include 
    int main(void) {
      printf("Hello World!");
      return 0;
    }
    $ gcc hello.c -o hello

Compiling your own code
^^^^^^^^^^^^^^^^^^^^^^^

-  Use gcc, g++, and gfortran compilers for compilation
-  Use mpicc, mpic++, and mpif90 for MPI (= MVAPICH, MPICH2 or OpenMPI +
   GCC)
-  Setup your environment with ``module load <toolchain>`` e.g. ``module
   load goolf/triton-2016b`` for BLAS/LAPACK, FFTW3, ScaLAPACK+BLACS,
   etc.. Modules will set ``CPATH`` and ``LD_LIBRARY_PATH`` variables for
   ``-I`` and
   ``-L, but you can use 'module show <module>' to see the exact library paths.``

MPI-code "mpihello.c":

::

    #include
    #include
    int main (int argc, char **argv) {
      int rank, size;
      MPI_Init (&argc, &argv);
      printf( "Hello world\n");
      MPI_Finalize();
      return 0;
    }

Compile MPI code:

::

    module load goolf
    mpicc mpihello.c -o mpihello

Optimization options for GCC
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

By default GCC/G++/GFortran do NOT perform any optimization; you must
add appropriate optimization flags yourself. Experiment and see what
works for your program!

-  Basic optimization level: ``-O2``
-  More aggressive optimization, arch specific: ``-O3 -march=native``
-  Might, or might not help:
   ``-O3 -march=native -funroll-loops -ftree-loop-linear -fprefetch-loop-arrays``

Might help a lot, but potentially dangerous: ``-ffast-math -mrecip``

OpenMP with GCC: ``-fopenmp``

Note that using ``-march=native`` will produce an arch specific code.
Thus when compiled on Haswell, that code must be run on Haswell,
otherwise expect segmentation fault errors on other architectures.

Intel Compilers
~~~~~~~~~~~~~~~

Intel Composer available through  ``module`` provides full set of
compilers C/C++/Fortran. In addition, it comes with MKL libraries, that
works well in case you need LAPACK/BLAS functionality, as well as
paralle version of them with ScaLAPACK and BLACS.

Example of linking for Intel Composer + MKL + OpenMPI

::

    $ module load ioolf
    $ mpif90 -o my.exe one.o two.o three.o libmpi_f90.a -lmkl_scalapack_lp64 -Wl,--start-group -lmkl_intel_lp64 -lmkl_sequential -lmkl_core  -lmkl_blacs_openmpi_lp64 -Wl,--end-group -lpthread -lm
