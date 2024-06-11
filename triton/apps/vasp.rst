====
VASP
====

.. admonition:: Warning: page not updated for current Triton
  :class: warning, triton-v2-apps

  This page hasn't been updated since Triton was completely upgraded
  in May 2024.  The software might not be installed and the old
  information below might not work anymore (or  might need adapting).
  If you need this software, :ref:`open an issue <issuetracker>` and
  tell us so we can reinstall/update it.

`VASP <http://www.vasp.at/>`__  (Vienna Ab initio Simulation Package) is
a computer program for atomic scale materials modelling, e.g. electronic
structure calculations and quantum-mechanical molecular dynamics, from
first principles.

VASP is licensed software, requiring the licensee to keep the vasp team
updated with a list of user names. Thus, in order to use VASP arrange
with the "vaspmaster" for your group to be put on the vasp licensed user
list. Afterwards, contact your local triton admin who will take care of
the IT gymnastics, and CC the vaspmaster so that he is aware of who gets
added to the list.

For the PHYS department, the vaspmaster is Ivan Tervanto.

For each VASP version, there are 3 binaries compiled. All versions are
MPI and OpenMP versions.

-  vasp\_std: The "standard" vasp, compiled with NGZhalf
-  vasp\_gam: Gamma point only. Faster if you use only a single k-point.
-  vasp\_ncl: For non-collinear spin calculations

VASP 6.4.1
==========

The binaries are compiled with the GNU compilers, MKL (incl ScaLAPACK) and OpenMPI
libraries, the used modules ``gcc/11.2.0 intel-oneapi-mkl/2021.4.0 openmpi/4.0.5``.
Example batch script

::

    #!/bin/bash -l
    #SBATCH --nodes=1
    #SBATCH --ntasks=8
    #SBATCH --time=06:00:00
    #SBATCH --mem-per-cpu=1500M
    module load vasp/6.4.1
    srun vasp_std


Potentials
==========

Potentials are stored at ``/share/apps/vasp/pot``.



Old VASP versions (obsolete, for reference only!)
=================================================

These old versions are unlikely to work as they use old MPI and IB
libraries that have stopped working due to upgrades over the years.

VASP 5.4.4
~~~~~~~~~~

The binaries are compiled with the Intel compiler suite and the MKL
library, the used toolchain module is ``intel-parallel-studio/cluster.2020.0-intelmpi``.
Example batch script

::

    #!/bin/bash -l
    #SBATCH --nodes=1
    #SBATCH --ntasks=8
    #SBATCH --time=06:00:00
    #SBATCH --mem-per-cpu=1500M
    module load vasp/5.4.4
    export I_MPI_PMI_LIBRARY=/usr/lib64/libpmi.so
    srun vasp_std



VASP 5.4.1
~~~~~~~~~~

Currently the binaries are compiled with GFortran instead of Intel
Fortran (the Intel Fortran binaries crashed, don't know why yet).
Example batch script

::

    #!/bin/bash -l
    #SBATCH --nodes=1
    #SBATCH --ntasks=8
    #SBATCH --time=06:00:00
    #SBATCH --mem-per-cpu=1500M
    module load vasp/5.4.1-gmvolf-triton-2016a
    srun vasp_std



For each VASP version, there are two binaries compiled with slightly
different options:

::

    vasp.mpi.NGZhalf
    vasp.mpi

Both are MPI versions. The first one is what you should normally use; it
is compiled with the NGZhalf option which reduces charge density in the
Z direction, leading to less memory usage and faster computation. The
second version is needed for non-collinear spin calculations. The
binaries can be found in the directory /share/apps/vasp/$VERSION/ . For
those of you who need to compile your own version of VASP, the makefiles
used for these builds can be used as a starting point, and are found in
the directory /share/apps/vasp/makefiles .

VASP 5.3.5
~~~~~~~~~~

The binaries are optimized for the Xeon Ivy Bridge nodes, although they
will also work fine on the older Xeon Westmere and Opteron nodes. Note
that for the moment only the NGZhalf version has been built. If you need
the non-NGZhalf version for non-collinear spin calculations please
contact triton support. Example job script below:

::

    #!/bin/bash -l
    #SBATCH --nodes=1
    #SBATCH --ntasks=12
    #SBATCH --time=06:00:00
    #SBATCH --mem-per-cpu=2500M

    module load vasp/5.3.5

    srun vasp.mpi.NGZhalf

The relative time to run the vasptest v2 testsuite on 12 cores (so a
full node for Xeon Westmere and Opteron nodes, and 12/20 cores on a Xeon
Ivy Bridge node) is for Xeon IB/Xeon Westmere/Opteron 1.0/2.0/2.8. So
one sees that the Xeon Ivy Bridge nodes are quite a lot faster per core
than the older nodes (with the caveat that the timings may vary
depending on other jobs that may have been running on the Xeon IB node
during the benchmark).

VASP 5.3.3
~~~~~~~~~~

The binaries are optimized for the Xeon nodes, although they also work
on the Opteron nodes. Some simple benchmarks suggest that the Opteron
nodes are a factor of 1.5 slower than the Xeon nodes, although it is
recommended to write the batch script such that Opteron nodes can also
be used, as the Opteron queue is often shorter. An example script below:

::

    #!/bin/bash -l
    #SBATCH --nodes=1
    #SBATCH --ntasks=12
    #SBATCH --time=06:00:00
    #SBATCH --mem-per-cpu=2500M

    module load vasp/5.3.3

    srun vasp.mpi.NGZhalf

VASP 5.3.2 and older
~~~~~~~~~~~~~~~~~~~~

The binaries are optimized for the Intel Xeon architecture nodes, and
are not expected to work on the Opteron nodes. An example job script is
below (Note that it is different from the script for version 5.3.3 and
newer above!):

::

    #!/bin/bash -l
    #SBATCH --nodes=1
    #SBATCH --ntasks=12
    #SBATCH --time=1-00:00:00
    #SBATCH --mem-per-cpu=3500M

    module load vasp/5.3.2

    srun vasp.mpi.NGZhalf

Potentials
~~~~~~~~~~

PAW potentials for VASP can be found in the directory
/share/apps/vasp/pot. The recommended potentials are the ones in the
Apr2012.52 subdirectory. For reference, an older set of potentials
dating back to 2003 can be found in the "2003" subdirectory.

Validation
~~~~~~~~~~

The vasp.mpi.NGZhalf builds have been verified to pass all the tests in
the `vasptest <http://www.nsc.liu.se/~pla/vasptest/>`__ suite.



Other
~~~~~

Old makefiles

Here is a number of Makefiles copy-pasted from old Rocks installation.
Can be useful in general, though may require adaptation to new
installation. Please, send us a fully working copy if you have one.

See old wiki: https://wiki.aalto.fi/display/Triton/Applications

Rename vasp.x.y.makefile => vasp.x.y/makefile
