Parallel R example
------------------

``Rparallel_4.slrm``::

    #!/bin/bash
    #SBATCH -p short
    #SBATCH -t 00:20:00
    #SBATCH --nodes=1
    #SBATCH --ntasks=1
    #SBATCH --cpus-per-task=4
    #SBATCH --mem=8G
    #SBATCH -o Rparallel_4.out
    module load R
    export OMP_NUM_THREADS=1
    srun Rscript --vanilla Rparallel.R $SLURM_CPUS_PER_TASK

``Rparallel.R``::

    library(pracma)
    library(parallel)
    args=commandArgs(trailingOnly=TRUE)
    invertRandom <- function(index) {
        #require(pracma)
        A<-matrix(runif(2000*2000),ncol=2000,nrow=2000);
        A<-A + t(A);
        B<-pinv(A);
        return(max(B %*% A));
    }
    ptm<-proc.time()
    mclapply(1:16,invertRandom, mc.cores=as.integer(args))
    proc.time()-ptm

When constrained to opt-architecture, run times for different core
numbers were

+-----------+-----------+-----------+-----------+----------+
| ncores    | 1         | 2         | 4         | 8        |
+===========+===========+===========+===========+==========+
| runtime   | 380.757   | 182.185   | 125.526   | 84.230   |
+-----------+-----------+-----------+-----------+----------+
