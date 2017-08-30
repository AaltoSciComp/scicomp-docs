============
Applications
============

Module environment
~~~~~~~~~~~~~~~~~~


In Triton the program development and software environments are managed
using the modules package. With the module environment management of
different application versions becomes easy. Modules makes it possible
to switch between different compiler suites and versions.

Modules will automatically set library and command paths
(``LD_LIBRARY_PATH`` and ``PATH`` variables correspondingly) upon
loading given module.

Basic module commands can be found below and these can be used in Slurm
batch submission scripts:

.. include:: ../ref/modules.rst


It is highly recommended that you use the save/restore commands to save
your used module environment. The save/restore commands are much faster
when loading large number of modules as the module environment does not
need to check against possible conflicts between modules.

Some of the module files are in the ``/cvmfs/fgi.csc.fi/fgci/centos7/modules``
directory, which is the common for all FGI clusters.

For additional info see ``man modules``.


Toolchains
~~~~~~~~~~

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

.. include:: ../ref/toolchains.rst


Other software is compiled against these toolchains and we update them to newer versions if needed. If you require older versions of e.g. GCC we will install them separately.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When asking for specialized software, these will be used as the starting
point. E.g. Armadillo/6.700.3-goolf-triton-2016a-Python-2.7.11 uses
goolf-triton-2016a as the base.

New software will in time be installed against all toolchains, if you
have preference on some toolchain, we'll start with that.

Matlab
~~~~~~

Described on a `separate
page <matlab>`.

GPAW
~~~~

There is GPAW version installed in
GPAW/1.0.0-goolf-triton-2016a-Python-2.7.11. It has been compiled with
GCC, OpenBLAS and OpenMPI and it uses Python/2.7.11-goolf-triton-2016a
as its base Python. You can load it with::

    $ module load GPAW/1.0.0-goolf-triton-2016a-Python-2.7.11

You can create a virtual environment against the Python environment with::

    $ export VENV=/path/to/env
    $ virtualenv --system-site-packages $VENV
    $ cd $VENV
    $ source bin/activate
    # test installation
    $ python -c 'import gpaw; print gpaw'

GPAW site: https://wiki.fysik.dtu.dk/gpaw/

Gromacs
~~~~~~~

[FIXME: could be installed in case of need, none yet requested it.]

VASP
~~~~

See the `VASP <vasp>` page.

Old makefiles


Here is a number of Makefiles copy-pasted from old Rocks installation.
Can be useful in general, though may require adaptation to new
installation. Please, send us a fully working copy if you have one.

-  
-  
-  
-  

Rename vasp.x.y.makefile => vasp.x.y/makefile

Siesta & Transiesta
~~~~~~~~~~~~~~~~~~~

Copy-pasted Makefiles from Rocks. Should be used as a starting point. If
you have a fully working version for SL6.2, send us a copy please.

-  
-  

Rename siesta-3.0.arch.make.xxx => siesta-3.0-b/Obj/arch.make

COMSOL Multiphysics
~~~~~~~~~~~~~~~~~~~

-  Version 4.3 installed. Use module command to enable.

   -  Runing on the fat-nodes straight out of the box.
   -  Would be interesting to submit cluster jobs from the fat node.
   -  Pure MPI-parallel Tests have worked straight-forward. Something
      like the following was within the batch-job submit file::

          module  load mvapich2-x86_64
          BIN=/share/apps/comsol/comsol43/COMSOL43/bin/comsol
          INPUT_FILE=perX_inf.mph
          OUTPUT_FILE=perX_inf_$SLURM_JOB_ID.mph
          $BIN   batch \
              -clustersimple \
              -mpibootstrap slurm\
              -inputfile $INPUT_FILE \
              -outputfile $OUTPUT_FILE \
              -launcher slurm

-  Comsol uses a lot of temp file storage, which by default goes to
   $HOME. Fix a bit like the following::

       $ rm -rf ~/.comsol/v43a/recoveries 
       $ mkdir /triton/tfy/work/$USER/comsol_revoveries/ 
       $ ln -s /triton/tfy/work/$USER/comsol_revoveries/ ~/.comsol/ 

Freesurfer
~~~~~~~~~~

::

    module load freesurfer

Follow the instruction to source the init script specific to your shell.

MNE
~~~

::

    module load mne

Follow the instruction to source the init script specific to your shell.
In the directory

::

    $MNE_ROOT/..

you can find the relase notes, the manual, and some sample data.

FSL
~~~

::

    module load fsl

Follow the instruction to source the init script specific to your shell.

Paraview
~~~~~~~~

A serial version is available on login2. You will need to use the
"forward connection" strategy by using ssh port forwarding. For example,
run ``ssh -L BBBB:nnnNNN:AAAA username@triton``\ , where BBBB is the
server you connect to locally and nnnNNN is the node name and AAAA is
the port on that node. See `this FAQ question <faq-connecttoserveronnode>`.

See issue #13:
https://version.aalto.fi/gitlab/AaltoScienceIT/triton/issues/13 for some
user experiences. (Note: the author of this entry is not a paraview
expert, suggestions welcome.)

Other applications
~~~~~~~~~~~~~~~~~~

If you know some application which is missing from this list but is
widely in use (anyone else than you is using it) it would make sense
install to ``/share/apps/`` directory and create a module file. Drop
your request on tracker to wishlist.
