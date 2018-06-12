Serial R example
----------------

serial\_R.slrm:

::

    #!/bin/bash
    #SBATCH -p short
    #SBATCH -t 00:05:00
    #SBATCH -n 1
    #SBATCH --mem=100
    #SBATCH -o serial_R.out
    module load R
    n=3
    m=2
    srun Rscript --vanilla serial_R.R $n $m

serial\_R.R:

::

    args = commandArgs(trailingOnly=TRUE)
    n<-as.numeric(args[1])
    m<-as.numeric(args[2])
    print(n)
    print(m)
    A<-t(matrix(0:5,ncol=n,nrow=m))
    print(A)
    B<-t(matrix(2:7,ncol=n,nrow=m))
    print(B)
    C<-matrix(0.5,ncol=n,nrow=n)
    print(C)
    C<-A %*% t(B) + 2*C
    print(C)
