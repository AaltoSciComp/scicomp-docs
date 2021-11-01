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
    invMatrices = []
    # invert the matrices
    for i in range(6):
    	invMatrices.append(invertPart(i,randMat),)
    squaredRes = []
    # calc mean and invert again
    for i in range(6):
	squaredRes = means(i,invMatrices)   
    
    print(squaredRes)

main()    
