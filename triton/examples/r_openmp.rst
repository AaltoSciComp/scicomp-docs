R OpenMP Example
----------------

ROpenMP\_4.slrm

::

    #!/bin/bash
    #SBATCH -p batch-hsw
    #SBATCH -t 01:00:00
    #SBATCH --nodes=1
    #SBATCH --ntasks=1
    #SBATCH --cpus-per-task=4
    #SBATCH --mem=8G
    #SBATCH -o ROpenMP_4.out
    module load R
    export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
    time srun Rscript --default-packages=methods,utils,stats --vanilla R-benchmark-25-triton.R

Benchmark script (modified version of script from `this
page <https://www.r-bloggers.com/r-benchmark-for-high-performance-analytics-and-computing-i/>`__):

+-----+-----+-----+-----+-----+
|     |     |     |     |     |
+=====+=====+=====+=====+=====+
|     |     |     |     |     |
+-----+-----+-----+-----+-----+
