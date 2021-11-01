library(GA)

f <- function(solution){
    output = c(4,-2,3.5,5,-11,-4.7) %*% solution
    fitness = 1./abs(output-44)
    return(fitness)
}

# search space bounds
lowers = c(-20,-20,-20,-20,-20,-20)
uppers = c(20,20,20,20,20,20)

# maximum generations
maxiter = 200000

# set the population size
popSize = 100

# set the maximum number of generations to proceed if no improvment happens
run = 50

# mutation percentage 
pmutation = Sys.getenv('SLURM_ARRAY_TASK_ID')/100

GA <- ga(type = "real-valued", fitness = f, lower = lowers, upper = uppers, maxiter= maxiter, run=run, pmutation = pmutation, popSize = popSize)
summary(GA)

GA@solution %*% c(4,-2,3.5,5,-11,-4.7)

