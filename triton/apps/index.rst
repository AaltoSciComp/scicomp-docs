Module environment
~~~~~~~~~~~~~~~~~~

.. raw:: html

   <div class="wiki-content">

In Triton the program development and software environments are managed
using the modules package. With the module environment management of
different application versions becomes easy. Modules makes it possible
to switch between different compiler suites and versions.

Modules will automatically set library and command paths
(``LD_LIBRARY_PATH`` and ``PATH`` variables correspondingly) upon
loading given module.

Basic module commands can be found below and these can be used in Slurm
batch submission scripts:

.. raw:: html

   <div>

.. raw:: html

   <div class="syntaxhighlighter nogutter java">

 

+--------------------------------------------------------------------------+
| .. raw:: html                                                            |
|                                                                          |
|    <div class="container" title="Hint: double-click to select code">     |
|                                                                          |
| .. raw:: html                                                            |
|                                                                          |
|    <div class="line number1 index0 alt2">                                |
|                                                                          |
| ``$ module list                  # list currently loaded modules``       |
|                                                                          |
| .. raw:: html                                                            |
|                                                                          |
|    </div>                                                                |
|                                                                          |
| .. raw:: html                                                            |
|                                                                          |
|    <div class="line number2 index1 alt1">                                |
|                                                                          |
| ``$ module avail                 # list all modules available``          |
|                                                                          |
| .. raw:: html                                                            |
|                                                                          |
|    </div>                                                                |
|                                                                          |
| .. raw:: html                                                            |
|                                                                          |
|    <div class="line number3 index2 alt2">                                |
|                                                                          |
| ``$ module load matlab/r2015b    # load module environment ``\ ``for``   |
| ``given module``                                                         |
|                                                                          |
| .. raw:: html                                                            |
|                                                                          |
|    </div>                                                                |
|                                                                          |
| .. raw:: html                                                            |
|                                                                          |
|    <div class="line number4 index3 alt1">                                |
|                                                                          |
| ``$ module help matlab/r2015b    # information about given module (what  |
| it does etc)``                                                           |
|                                                                          |
| .. raw:: html                                                            |
|                                                                          |
|    </div>                                                                |
|                                                                          |
| .. raw:: html                                                            |
|                                                                          |
|    <div class="line number4 index3 alt1">                                |
|                                                                          |
| $ module show matlab/r2015b    # show in detail the changes perpetuated  |
| by the module                                                            |
|                                                                          |
| .. raw:: html                                                            |
|                                                                          |
|    </div>                                                                |
|                                                                          |
| .. raw:: html                                                            |
|                                                                          |
|    <div class="line number5 index4 alt2">                                |
|                                                                          |
| ``$ module unload matlab/r2015b  # unload module (remove paths)``        |
|                                                                          |
| .. raw:: html                                                            |
|                                                                          |
|    </div>                                                                |
|                                                                          |
| .. raw:: html                                                            |
|                                                                          |
|    <div class="line number5 index4 alt2">                                |
|                                                                          |
| $ module save <name>           # save current modules as a collection    |
|                                                                          |
| .. raw:: html                                                            |
|                                                                          |
|    <div class="line number5 index4 alt2">                                |
|                                                                          |
| $ module restore <name>        # restore modules from a collection       |
|                                                                          |
| .. raw:: html                                                            |
|                                                                          |
|    </div>                                                                |
|                                                                          |
| .. raw:: html                                                            |
|                                                                          |
|    </div>                                                                |
|                                                                          |
| .. raw:: html                                                            |
|                                                                          |
|    </div>                                                                |
+--------------------------------------------------------------------------+

It is highly recommended that you use the save/restore commands to save
your used module environment. The save/restore commands are much faster
when loading large number of modules as the module environment does not
need to check against possible conflicts between modules.

.. raw:: html

   </div>

.. raw:: html

   </div>

Some of the module files are in /cvmfs/fgi.csc.fi/fgci/centos7/modules
directory, which is the common for all FGI clusters.

For additional info see '``man modules``'.

.. rubric:: Toolchains
   :name: toolchains

.. raw:: html

   </div>

The modules in Triton are organized in so-called toolchains. These are
collections of compilers and tools that are used for compiling
specialized software.

Typically a toolchain contains a compiler and a MPI implementation, but
it can also contain additional mathematical and computational libraries.

Naming convention is from
`EasyBuild <https://github.com/hpcugent/easybuild>`__ that is used to
administer the software collections. It goes like:

<compiler><mpi><blas><lapack><fftw><cuda>

eg.
**G**\ CC,\ **O**\ penMPI,\ **O**\ penBLAS,\ **L**\ APACK,\ **F**\ FTW,\ **C**\ UDA
would result in toolchain **goolfc**

Toolchains in detail
~~~~~~~~~~~~~~~~~~~~

true\ `Available Toolchains <LINK/Available%20Toolchains>`__

Other software is compiled against these toolchains and we update them to newer versions if needed. If you require older versions of e.g. GCC we will install them separately.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When asking for specialized software, these will be used as the starting
point. E.g. Armadillo/6.700.3-goolf-triton-2016a-Python-2.7.11 uses
goolf-triton-2016a as the base.

New software will in time be installed against all toolchains, if you
have preference on some toolchain, we'll start with that.

Matlab
~~~~~~

Described on `VASP <LINK/VASP>`__ page.

Old makefiles
             

Here is a number of Makefiles copy-pasted from old Rocks installation.
Can be useful in general, though may require adaptation to new
installation. Please, send us a fully working copy if you have one.

`Triton FAQ#Ineedtoconnecttosomeserveronanode. <LINK/Triton%20FAQ>`__

See issue #13:
https://version.aalto.fi/gitlab/AaltoScienceIT/triton/issues/13 for some
user experiences.  (Note: the author of this entry is not a paraview
expert, suggestions welcome.)

Other applications
~~~~~~~~~~~~~~~~~~

If you know some application which is missing from this list but is
widely in use (anyone else than you is using it) it would make sense
install to ``/share/apps/`` directory and create a module file. Drop
your request on tracker to wishlist.
