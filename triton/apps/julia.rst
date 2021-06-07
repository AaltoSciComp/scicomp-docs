Julia
=====

The `Julia programming language <https://julialang.org/>`__ is a
high-level, high-performance dynamic programming language for technical
computing, in the same space as e.g. MATLAB, Scientific Python, or R.
For more details, see their `web page <https://julialang.org/>`__.

Interactive usage
-----------------

Julia is available in the module system. By default the latest stable
release is loaded::

  module load julia
  julia

Batch usage
-----------

Running Julia scripts as batch jobs is also possible. An example batch script
is provided below::

    #!/bin/bash
    #SBATCH --time=00:01:00
    #SBATCH --mem=1G

    export OMP_NUM_THREADS=${SLURM_CPUS_PER_TASK:-1}
    module load julia
    srun julia juliascript.jl

Number of threads to use
------------------------

By default Julia uses up to 16 threads for linear algebra (BLAS)
computations. In most cases, this number will be larger than the amount
of CPUs reserved for the job. Thus when running Julia jobs it is a good idea
to set the number of parallelization threads to be equal to the number of
threads reserved for the job with ``--cpus-per-task``. Otherwise, the
performance of your program might be poor. This can be done by adding the
following line to your slurm-script::

  export OMP_NUM_THREADS=${SLURM_CPUS_PER_TASK:-1}

Alternatively, you can use the ``blas_set_num_threads()``-function in Julia.

