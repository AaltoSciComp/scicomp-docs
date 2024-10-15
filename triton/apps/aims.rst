========
FHI-aims
========

`FHI-aims <https://fhi-aims.org/>`__  (Fritz Haber
Institute ab initio molecular simulations package) is an electronic
structure theory code package for computational molecular and
materials science. FHI-aims density functional theory and many-body
perturbation calculations at all-electron, full-potential level.

FHI-aims is licensed software with voluntary payment for an `academic
license
<https://fhi-aims.org/get-the-code-menu/get-the-code>`__. While
the license grants access to the FHI-aims source code each holder of a
license can use pre-built binaries available on Triton. To this end,
contact Ville Havu at the PHYS department after obtaining the license.

On Triton the most recent version of FHI-aims is available via the
module ``aims/240507`` that is compiled using OpenMPI.
The binaries are available in 
``/appl/manual_installations/software/aims/<version>`` as
``aims.<version>.scalapack.mpi.x`` where <version> indicates the version
stamp. The module will also add the executable to your PATH.

Notes:

- ``module spider aims`` will show various versions available.
- Search the Triton issue tracker for some more debugging about this.


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

   ulimit -s unlimited
   export OMP_NUM_THREADS=1
   module purge
   module load aims/240507
   srun aims.240507.scalapack.mpi.x
