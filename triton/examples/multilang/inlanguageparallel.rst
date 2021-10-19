===========================
In language parallelization
===========================

In language parallelization assumes, that either your code (or a function you call) already
knows how to parallelize its work, or that you want to use tools from within the language to
run parts of your code in parallel. 

We will handle both instances in this example. First, we will use functions from the language
that already do parallelisation to improve runtime efficiency of an existing code. This is
dependent on the actual code you use and you have to check the documentation to see, whether
the libraries, packages or toolboxes you use offer this option.  
After this, we will show you simple ways to use general in language parallelization options
and point you to the relevant documentation for your language.

Using existing parallelisation
==============================

To allow code to access multiple cores, we need the ``-c`` or ``--cpus_per_task`` parameter 
in slurm. 
A typical slurm script for code that is parallelized looks as follows:

input_in_language_parallel_slurmscript

To make use of this code, you need to provide the respective functions with the relevant information.

input_important_language_info

input_in_language_parallel_code


Now your code can run on the specified number of cores, speeding up the individual computation.


Parallelizing your code
=======================


Parallel processing lets you run independent similar processes simultaneously. 
This allows you to make use of multiple processors, potentially reducing run-times by a factor 
up to the number of processors used, for the parallelized parts. However, keep in mind, that 
parallelization also creates an overhead. So if you have very fast methods, and don't need to 
repeat them often trying to parallelize them might actually make our code slower.

Lets assume we have a function, that inverts a set of matrices, calculates means of the 
resulting marices, always leaving one inverted matrix out and then inverts the resulting mean 
matrix again.

The code looks as follows:

input_parallelize_code_original

We can easily parallelize the following comparatively expensive steps:
1. The first matrix inversions
2. The second matrix inversions (along with the mean calculation)

Lets start with the required slurm script. Here, we will request 4 cpus, along with 500Mb of memory:

input_parallelize_code_slurm

Then, we need to modify this code to run in parallel.

input_important_language_info_own_code

input_parallelize_code_parallel


