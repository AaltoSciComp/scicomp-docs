
import multiprocessing
import numpy as np
import os
from functools import partial

def invertPart(index,matrix):  
    return np.linalg.inv(matrix[:,:,index])

def means(index, matrix):
    return np.linalg.inv(np.mean(np.delete(matrix,index,0),0))
  

def main():
    # Create random set of matrices
    randMat = np.random.rand(1000,1000,6)
    # get the number of available CPUs from the SLURM environment, need to cast from string to int
    maxprocesses = int(os.getenv('SLURM_CPUS_PER_TASK'))
    # start the respective Pool
    p = multiprocessing.Pool(processes=maxprocesses)    
    # this reshapes the dimensions of the matrix, as it generates an array of the results, i.e. the 3rd dimension gets is now the first.
    invMatrices = p.map(partial(invertPart,matrix=randMat),range(6))
    
    squaredRes = p.map(partial(means, matrix=invMatrices), range(6))    
    
    print(squaredRes)
    
main()
