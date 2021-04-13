========
FHI-aims
========

`FHI-aims <https://aimsclub.fhi-berlin.mpg.de/>`__  (Fritz Haber
Institute ab initio molecular simulations package) is an electronic
structure theory code package for computational molecular and
materials science. FHI-aims density functional theory and many-body
perturbation calculations at all-electron, full-potential level.

FHI-aims is licensed software with voluntary payment for an `academic
license
<https://aimsclub.fhi-berlin.mpg.de/aims_obtaining_simple.php>`__. While
the license grants access to the FHI-aims source code each holder of a
license can use pre-built binaries available on Triton. To this end,
contact Ville Havu at the PHYS department after obtaining the license.

On Triton the most recent version of FHI-aims is available via the
modules ``FHI-aims/latest-intel-2020.0`` that is compiled using the
Intel Parallel Studio and
``FHI-aims/latest-OpenMPI-intel-2020.0-scalapack`` that is compiled
without any Intel parallel libraries since in rare cases they can
result in spurious segfaults. The binaries are available in
``/share/apps/easybuild/software/FHI-aims/<module name>/bin`` as
``aims.YYMMDD.scalapack.mpi.x`` where ``YYMMDD`` indicates the version
stamp.

Running FHI-aims on Triton
==========================

To run FHI-aims on Triton a following example batch script can be used:

::

   #!/bin/bash -l
   #SBATCH --time=01:00:00
   #SBATCH --constraint=avx     # FHI-aims build requires at least AVX instrution set
   #SBATCH  --mem-per-cpu=2000M
   #SBATCH --nodes=1
   #SBATCH --ntasks=24

   export OMP_NUM_THREADS=1
   module load FHI-aims/latest-intel-2020.0
   srun aims.YYMMDD.scalapack.mpi.x
