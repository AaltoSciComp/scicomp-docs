Parallel Example

Parallel processing lets you run independent similar processes simultaneously. 
It's most useful, if either multiple steps have to be performed where dependencies come in after 
parallelizable steps.
Let us assume we have a job that needs to calculate a complex function for each row of a large matrix,
then further compute the results each time leaving out one each time to feed a final algorithm.
in Pseudo-code:

::
 
	in = matrix
	for i in rows(matrix)
		res_step1[i] = function(matrix[i,:])
	
	for j in res_step1:
		res_step2[j] = function2(res_step1[not j])
	
	res_final = final_function(res_step2)


In this instance both for loops can be parallelized. 

To make use of parallelisation you will need to request multiple cpus in your batch script.
Here, we will request 4 cpus, along with 500Mb of memory:


