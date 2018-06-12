library(pracma)
library(parallel)
args=commandArgs(trailingOnly=TRUE)
invertRandom <- function(index) {
    A<-matrix(runif(2000*2000),ncol=2000,nrow=2000);
    A<-A + t(A);
    B<-pinv(A);
    return(max(B %*% A));
}
ptm<-proc.time()
mclapply(1:16,invertRandom, mc.cores=as.integer(args))
proc.time()-ptm
