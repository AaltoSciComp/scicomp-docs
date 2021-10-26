# Adapted from caret-parallel-train.R in Caret examples
# to Triton by Simo Tuomisto, 2017
# further adapted by Thomas Pfau, 2021

# Load relevant libraries
library(caret); 
library(doParallel)

# load data
data(BloodBrain); 

# get the number of available cores
cores <- as.integer(Sys.getenv("SLURM_CPUS_PER_TASK"))

# start the parallel cluster
cl <- makeCluster(cores)
registerDoParallel(cl) 

# train the data
fit1 <- train(bbbDescr, logBBB, "knn")

# clean up
stopCluster(cl)
registerDoSEQ()
