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

.. tabs::

  .. group-tab:: python
  
     .. include:: /triton/apps/importantnotes/python.rst
    
  .. group-tab:: R
     
     .. include:: ../../apps/importantnotes/r.rst
        
  .. group-tab:: MATLAB
  
     .. include:: /triton/apps/importantnotes/matlab.rst
    

Using existing parallelisation
==============================

To allow code to access multiple cores, we need the ``-c`` or ``--cpus_per_task`` parameter 
in slurm. 
A typical slurm script for code that is parallelized looks as follows:

.. tabs::

  .. group-tab:: python
  
     .. literalinclude:: python/parallel_fun.sh
       :language: slurm
           
  .. group-tab:: R
  
     .. literalinclude:: r/parallel_fun.sh
       :language: slurm
               
  .. group-tab:: MATLAB
  
     .. literalinclude:: matlab/parallel_fun.sh
       :language: slurm
         

To make use of this code, you need to provide the respective functions with the relevant information.

.. tabs::

  .. group-tab:: python
  
    .. literalinclude:: python/parallel_fun.py
       :language: python
       
  .. group-tab:: R
  
    .. literalinclude:: r/parallel_fun.R
       :language: R  
    
  .. group-tab:: MATLAB

    .. literalinclude:: matlab/parallel_fun.m
       :language: MATLAB

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

.. tabs::
       
  .. group-tab:: python
  
    .. literalinclude:: python/nonparallel.py
       :language: python
       
  .. group-tab:: R
  
    .. literalinclude:: r/nonparallel.R
       :language: R

  .. group-tab:: MATLAB
  
      .. literalinclude:: matlab/nonparallel.m
         :language: MATLAB


We can easily parallelize the following comparatively expensive steps:
1. The first matrix inversions
2. The second matrix inversions (along with the mean calculation)

Lets start with the required slurm script. Here, we will request 4 cpus, along with 500Mb of memory:

.. tabs::

  .. group-tab:: python
  
    .. literalinclude:: python/parallel.sh
       :language: slurm
       
  .. group-tab:: R
  
    .. literalinclude:: r/parallel.sh
       :language: slurm
              
  .. group-tab:: MATLAB
  
    .. literalinclude:: matlab/parallel.sh
       :language: slurm
       


Then, we need to modify this code to run in parallel.

.. tabs::

  .. group-tab:: python
  
    .. literalinclude:: python/parallel.py
       :language: python
       
  .. group-tab:: R
  
    .. literalinclude:: r/parallel.R
       :language: R
       
  .. group-tab:: MATLAB
  
    .. literalinclude:: matlab/parallel.m
       :language: MATLAB
