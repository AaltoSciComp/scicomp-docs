Julia language on triton
========================

The `Julia programming language <https://julialang.org/>`__ is a
high-level, high-performance dynamic programming language for technical
computing, in the same space as e.g. MATLAB, Scientific Python, or R.
For more details, see the web page https://julialang.org/ .

Interactive usage
-----------------

Julia is available in the module system. By default the latest stable
release is loaded::

  module load julia
  julia

Batch usage
-----------

Running Julia scripts as batch jobs is also possible. An example batch
job is

Batch script for Julia job::

    #!/bin/sh
    #SBATCH -p play
    #SBATCH -n 1
    #SBATCH --time=00:01:00
    #SBATCH --mem-per-cpu=1G
    module load julia
    srun julia juliascript.jl

Number of threads to use
------------------------

By default Julia uses up to 16 threads for linear algebra (BLAS)
computations. However, the julia module on triton sets the environment
variable OMP\_NUM\_THREADS to 1, so only a single thread is used. If you
wish to use more threads than that (e.g. you have launched a batch job
with multiple threads per task with the "#SBATCH -c N" option), you can
set the OMP\_NUM\_THREADS environment variable to some other value, or
alternatively inside julia you can use the blas\_set\_num\_threads()
function.

