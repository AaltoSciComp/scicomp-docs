===============================
Running serial jobs in parallel
===============================

Very often you need to run a given script with multiple different sets of parameters. This is 
what is commonly called an **embarrassingly parallel** problem, because a) there are commonly 
many more problems than available processors, and b) it is very easy to parallelize.
Here, we will show you how to adapt your code in this kind of situation, based on a non-parallel
version of a problem. We will assume an individual script with fixed parameter values and modify 
it to adapt it's input based on the serial job number id from slurm.



The unparallelized version
==========================

Lets assume you have a genetic algorithm optimization pipeline with a few fixed parameters.

.. tabs::

  .. group-tab:: python
  
    .. literalinclude:: python/serial_base.py
       :language: python
       
  .. group-tab:: R
  
    .. literalinclude:: r/serial_base.R
       :language: R  
    
  .. group-tab:: MATLAB

    .. literalinclude:: matlab/serial_base.m
       :language: MATLAB
  

The parameters set in this example are: the maximum number of generations, the population size 
the maximum stalled generations (i.e. how many generations the algorithm should continue if it does not 
improve) and the mutation rate. 
Lets assume, we want to test how different mutation rates change the outcome of the algorithm and its runtime. 
We could run this within each language, for-looping over percentages from 0-100%, which can take quite some time. 
Alternatively, we can run 100 jobs, each determining one percentage.


Running a Slurm array job
=========================


Array jobs are defined in Slurm by the Parameter ``--array=XXX-YYY``, where XXX is the lowest index and YYY the highest index.
Each job will have access to an individual ``SLURM_ARRAY_TASK_ID`` environment variable. There are two ways how this can be 
incorporated into a job. Either directly in the submission script, or by retrieving it in your code. The former allows 
the selection of input_file names based on the array ID number e.g.:

.. code-block:: slurm

  #!/bin/bash
  #SBATCH --time=01:00:00
  #SBATCH --mem=500M
  #SBATCH --array=1-4

  srun ./my_application -input input_data_${SLURM_ARRAY_TASK_ID}
  
In our case however, we would like to directly use it within the script we run. So we will set up the following slurm script:

.. tabs::
       
  .. group-tab:: python
  
    .. literalinclude:: python/serial.sh
       :language: slurm
       
  .. group-tab:: R
  
    .. literalinclude:: r/serial.sh
       :language: slurm

  .. group-tab:: MATLAB
  
      .. literalinclude:: matlab/serial.sh
         :language: slurm


Then we modify the script as follows:

.. tabs::

  .. group-tab:: python
  
    .. literalinclude:: python/serial.py
       :language: python
       :emphasize-lines: 18
       
  .. group-tab:: R
  
    .. literalinclude:: r/serial.R
       :language: R
       :emphasize-lines: 23
       
  .. group-tab:: MATLAB
  
    .. literalinclude:: matlab/serial.m
       :language: MATLAB
       :emphasize-lines: 4

Now, our mutation rate is set based on the ``SLURM_ARRAY_TASK_ID`` environment variable. 

.. admonition:: Best Practices
    
    In general you should try not to create too many jobs at once as this can cause unnecessary stress on the scheduler.
    This is particularily important if your individual array jobs only take a very short time (<30 minutes). If you have 
    a large amount of very short array jobs, it is a good idea to group them into batches. In our example this would 
    work as follows.
    
Grouping array jobs
===================

To group jobs without extensive modification of your script, you can simply create a batch loop that repeatedly calls your
script and only changes either the provided input parameters, or export the variable defined in the batch for loop and
access it within the script. For the genetic algorithm example the code would need to be modified as follows.
First, we need to introduce a for loop in he slurm script that runs the job a number of times based on our requests.


.. tabs::
       
  .. group-tab:: python
  
    .. literalinclude:: python/serial_grouped.sh
       :language: slurm
       :emphasize-lines: 10-22
              
  .. group-tab:: R
  
    .. literalinclude:: r/serial_grouped.sh
       :language: slurm
       :emphasize-lines: 10-22       

  .. group-tab:: MATLAB
  
    .. literalinclude:: matlab/serial_grouped.sh
       :language: slurm
       :emphasize-lines: 10-22         

and then we need to change the environment variable used in the script. 


.. tabs::

  .. group-tab:: python
  
    .. literalinclude:: python/serial_array.py
       :language: python
       :emphasize-lines: 18
       
  .. group-tab:: R
  
    .. literalinclude:: r/serial_array.R
       :language: R
       :emphasize-lines: 23
       
  .. group-tab:: MATLAB
  
    .. literalinclude:: matlab/serial_array.m
       :language: MATLAB
       :emphasize-lines: 4

