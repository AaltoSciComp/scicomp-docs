======
Matlab
======

.. admonition:: Warning: page not updated for current Triton
  :class: warning, triton-v2-apps

  This page hasn't been updated since Triton was completely upgraded
  in May 2024.  The software might not be installed and the old
  information below might not work anymore (or  might need adapting).
  If you need this software, :ref:`open an issue <issuetracker>` and
  tell us so we can reinstall/update it.

.. admonition:: Video

   `See an example in the Winter Kickstart 2021 course <https://www.youtube.com/watch?v=24NxYtDkw8s&list=PLZLVmS9rf3nN_tMPgqoUQac9bTjZw8JYc&index=22>`__


This page will explain how to run Matlab jobs on triton, and introduce 
important details about Matlab on triton.
(Note: We used to have the Matlab Distributed Computing Server (MDCS),
but because of low use we no longer have a license.  You can still
run in parallel on one node, with up to 40 cores.)

.. include:: importantnotes/matlab.rst

Memory requirements
-------------------

The matlab runtime is quite memory hungry.  If you are running a job keep in mind
that even for small examples you will likely need a minimum of 2 GB just for the 
runtime. If you plan to run anything in a parpool, you will likely need at least
2 GB per worker + 2 GB for the runtime.

Interactive usage
-----------------

Interactive usage is currently available via our `ondemand service <https://ondemand.triton.aalto.fi>`__
On there, request a Triton Desktop instance and you can run Matlab interactively.
On the desktop, start a terminal (click on Application (Top right corner -> Favorites -> Terminal).
Run ``module load matlab`` and then ``matlab`` and you will get a matlab gui. 

Simple serial script
--------------------

Running a simple Matlab job is easy through the slurm queue. A
sample slurm script is provided below::

    #!/bin/bash -l
    #SBATCH --time=00:05:00
    #SBATCH --mem-per-cpu=3G
    #SBATCH -o serial_Matlab.out
    module load matlab
    n=3
    m=2
    srun matlab -nojvm -nosplash -r "serial_Matlab($n,$m) ; exit(0)"

The above script can then be saved as a file (e.g. matlab_test.sh) and the job can be submitted with ``sbatch matlab_test.sh``. The actual calculation is done in ``serial_Matlab.m``\ -file:

.. code:: matlab

    function C = serial_Matlab(n,m)
            try
                    A=0:(n*m-1);
                    A=reshape(A,[2,3]).'

                    B=2:(n*m+1);
                    B=reshape(B,[2,3]).'

                    C=0.5*ones(n,n)
                    C=A*(B.') + 2.0*C
            catch error
                    disp(getReport(error))
                    exit(1)
            end
    end

Remember to *always* set exit into your slurm script so that the program quits
once the function ``serial_Matlab`` has finished. Using a
try-catch-statement will allow your job to finish in case of any error
within the program.  If you don't do this, Matlab will drop into
interactive mode and do nothing while your job wastes time. 

NOTE: Starting from version r2019a the launch options  ``-r ...; exit(0)`` can be easily 
replaced with the ``-batch`` option which automatically exits matlab at the end of the command that is passed 
(`see here for details <https://se.mathworks.com/help/matlab/ref/matlablinux.html>`__). 
So the last command from the slurm script above for Matlab r2019a will look like::

    srun matlab -nojvm -nosplash -batch "serial_Matlab($n,$m);"


Running Matlab Array jobs
-------------------------

The most common way to utilize Matlab is to write a single .M-file that
can be used to run tasks as a non-interactive batch job. These jobs are
then submitted as independent tasks and when the heavy part is done, the
results are collected for analysis. For these kinds of jobs the Slurm
array jobs is the best choice; :doc:`For more information on array jobs see
Array jobs in the Triton user guide</triton/tut/serial>`.

Here is an example of testing multiple mutation rates for a genetic algorithm.
First, the matlab code.

.. literalinclude:: /triton/examples/multilang/matlab/serial.m
   :language: MATLAB

We run this code with the following slurm script using ``sbatch``

.. literalinclude:: /triton/examples/multilang/matlab/serial.sh
   :language: slurm

**Collecting the results**

Finally a wrapper script to read in the .mat files and plots the resulting values

.. literalinclude:: /triton/examples/multilang/matlab/collectResults.m
   :language: MATLAB


Seeding the random number generator
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Note that by default MATLAB always initializes the random number
generator with a constant value. Thus if you launch several matlab
instances e.g. to calculate distinct ensembles, then you need to seed
the random number generator such that it's distinct for each
instance. In order to do this, you can call the ``rng()`` function,
passing the value of ``$SLURM_ARRAY_TASK_ID`` to it.


.. include:: ../examples/matlab/int_parallel.rst

.. include:: ../examples/matlab/parpool_parallel.rst

Parallel matlab in exclusive mode
---------------------------------
::

    #!/bin/bash -l
    #SBATCH --time=00:15:00
    #SBATCH --exclusive
    #SBATCH --mem=4G
    #SBATCH -o parallel_Matlab3.out

    export OMP_NUM_THREADS=$(nproc)

    module load matlab
    matlab -nosplash -r "parallel_Matlab3($OMP_NUM_THREADS) ; exit(0)"

parallel\_Matlab3.m::

    function parallel_Matlab3(n)
            % Try-catch expression that quits the Matlab session if your code crashes
            try
                    % Initialize the parallel pool
                    c=parcluster();
                    % Ensure that workers don't overlap with other jobs on the cluster
                    t=tempname()
                    mkdir(t)
                    c.JobStorageLocation=t;
                    parpool(c,n);
                    % The actual program calls from matlab's example.
                    % The path for r2017b
                    addpath(strcat(matlabroot, '/examples/distcomp/main'));
                    % The path for r2016b
                    % addpath(strcat(matlabroot, '/examples/distcomp'));
                    pctdemo_aux_parforbench(10000,100,n);
            catch error
                    getReport(error)
                    disp('Error occured');
                    exit(0)
            end
    end


FAQ / troubleshooting
---------------------

If things randomly don't work, you can try removing or moving either the
``~/.matlab`` directory or ``~/.matlab/Rxxxxy`` directory to see if it's
caused by configuration.

Random error messages about things not loading and/or something
(Matlab Live Editor maybe) doesn't work: ``ls *.m``, do you have any
unexpected files like ``pathdef.m`` in there?  Remove them.

Also, check your home quota.  Often ``.matlab`` gets large and fills up
your home directory.  Check the answer at the very top of the page,
under "Matlab Configuration".

