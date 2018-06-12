library(pracma)
library(parallel)
invertRandom <- function(index) {
    A<-matrix(runif(2000*2000),ncol=2000,nrow=2000);
    A<-A + t(A);
    B<-pinv(A);
    return(max(B %*% A));
}
ptm<-proc.time()
mclapply(1:16,invertRandom, mc.cores=Sys.getenv('SLURM_ARRAY_TASK_ID'))
proc.time()-ptm
