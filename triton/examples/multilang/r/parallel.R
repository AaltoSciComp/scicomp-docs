library(pracma)
library(parallel)

ar <- array(runif(1000*1000*6), c(1000, 1000, 6));  

invertRandom <- function(index,cmat) {
  A<-cmat[,,index];
  B<-inv(t(A));
  return(B);
}

invertMeanLOO <- function(index,cmat) {
  A<-cmat[,,-index];
  A<-apply(A,c(1,2),mean)
  B<-inv(t(A));
  return(B);
}

res = mclapply(1:6,invertRandom, cmat=ar,mc.cores=Sys.getenv('SLURM_CPUS_PER_TASK'))
res = array(unlist(res),c(1000,1000,6))
res = mclapply(1:6,invertMeanLOO, cmat=res,mc.cores=Sys.getenv('SLURM_CPUS_PER_TASK'))

