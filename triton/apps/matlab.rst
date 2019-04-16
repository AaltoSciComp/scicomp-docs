======
Matlab
======

This page will guide you through the serial computing with Matlab at
Triton cluster.  (Note (2017): We used to have the Matlab Distributed
Computing Server (MDCS), but because of low use we no longer have a
license.  You can still run in parallel on one node, up to 20-28 cores
depending on how new.)

Matlab configuration
--------------------

Matlab writes session data, compiled code and additional toolboxes to
``~/.matlab``. This can quicky fill up your ``$HOME`` quota. To fix this
we recommend that you replace the folder with a symlink that points to
a directory in your working directory.

::

   rsync -lrt ~/.matlab/ $WRKDIR/matlab-config/ && rm -r ~/.matlab
   ln -sT $WRKDIR/matlab-config ~/.matlab
   quotafix -gs --fix $WRKDIR/matlab-config

Interactive usage
-----------------

Interactive usage is currently available via the sinteractive tool. Do
not use the cluster front-end for doing heavy task. Only meant for
submitting jobs/compiling. Using MDCS for sending jobs is ok.

::

    ssh -X user@triton.aalto.fi
    sinteractive
    module load matlab
    matlab &

Simple serial script
--------------------

Running a single core Matlab job is easy through the slurm queue. A
sample slurm script is provided underneath::

    #!/bin/bash -l
    #SBATCH -p short
    #SBATCH -t 00:05:00
    #SBATCH -n 1
    #SBATCH --mem-per-cpu=100
    #SBATCH -o serial_Matlab.out
    module load matlab
    n=3
    m=2
    srun matlab -nojvm -nosplash -r "serial_Matlab($n,$m) ; exit(0)"

The above script can then be saved as a file (e.g. matlab_test.slrm) and the job can be submitted with ``sbatch matlab_test.slrm``. The actual calculation is done in ``serial_Matlab.m``\ -file::

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
interactive mode and do nothing while your cluster time wastes. 

NOTE: Starting from version r2019a the launch options  ``-r ...; exit(0)`` can be easily 
replaced with the ``-batch`` option which automatically exits matlab at the end of the command that is passed 
(`see here for details <https://se.mathworks.com/help/matlab/ref/matlablinux.html>`__). 
So the last command from the slurm script above for Matlab r2019a will look like::

    srun matlab -nojvm -nosplash -batch "serial_Matlab($n,$m);"


Multiple serial batchjobs
-------------------------

The most common way to utilize Matlab is to write a single .M-file that
can be used to run tasks as a non-interactive batch job. These jobs are
then submitted as independent tasks and when the heavy part is done, the
results are collected for analysis. For these kinds of jobs the Slurm
array jobs is the best choice; For more information on array jobs see
Array jobs in the Triton user guide.

Below you will find an example how-to prepare and run such type of jobs.

**run.m file doing the actual calculation task**

The file below calculates Sin-function in the interval 0-2\*PI and
stores the results into a file. The interval is divided into blocks that
are distributed over the nodes. ::

    function run(blockIndex,pointsPerBlock,totalBlocks)
    % blockindex runs from 0..totalblocks-1
    % range 0..2pi
    length=2*pi;
    % values to setup even spacing between given range 
    % and splitting the spacings to even number of points per block
    totalPoints=pointsPerBlock*totalBlocks;
    step=length/(totalPoints-1);
    start=blockIndex*pointsPerBlock*step;  
    % do some calculations, store the resulst so arrays A and B
    for index=0:pointsPerBlock-1
      i=index+1;
      x=start+index*step;
      y=sin(x);
      A(i)=x;
      B(i)=y;
    end
    % save the results based on the blockIndex to a file
    filename=strcat('output-',int2str(blockIndex));
    save( filename, 'A', 'B', 'blockIndex');
    % display message to output (log) that we have reached this far.
    disp(sprintf('SUCCESS blockIndex %d',blockIndex));
    % exit as this is a batch-job
    exit;

**Submission of 10 independent tasks**

Below the **run.m** is executed as an array job with 10 array tasks,
which will execute independently, potentially in parallel if there are
enough idle resources. Note that it is using play partition with 5min
time limit.

matslurm.sh::

    #!/bin/bash -l
    #SBATCH --time=0-00:05:00 --mem-per-cpu=500
    #SBATCH -p debug
    #SBATCH -o job-%a.out
    #SBATCH --array=0-9
    module load matlab
    matlab -nojvm -r "run($SLURM_ARRAY_TASK_ID,100,10); quit"

Submit the job with "sbatch matslurm.sh" (or whatever you called the
batch job script above).

**Collecting the results**

Finally a wrapper script to read in the .mat files and plots you tha
Sin-function calculated in parallel with 10 tasks.::

    function collectResults(numberOfBlocks) 
       X=[]; 
       Y=[];
       for index=0:numberOfBlocks-1
          % read the output from the jobs
          filename = strcat( 'output-', int2str( index ) );
          load( filename );
          % catenate results to a single arrays
          X=cat(2,X,A);
          Y=cat(2,Y,B); 
       end 
       plot(X,Y,'b+:')


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
    #SBATCH -p short
    #SBATCH -t 00:15:00
    #SBATCH --exclusive
    #SBATCH -o parallel_Matlab3.out
    
    export OMP_NUM_THREADS=$(nproc)
    
    module load matlab/r2017b
    srun -n 1 -c $OMP_NUM_THREADS matlab_multithread -nosplash -r "parallel_Matlab3($OMP_NUM_THREADS) ; exit(0)"

parallel\_Matlab3.m::

    function parallel_Matlab3(n)
            % Try-catch expression that quits the Matlab session if your code crashes
            try
                    % Initialize the parallel pool
                    c=parcluster();
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

Hints for Condor users
----------------------

The above example also works (even nicer way) for condor.

**A wrapper script to execute matlab on the department workstation.**

::

    #!/bin/bash -l
    # a wrapper to run Matlab with condor
    block=$1
    pointsPerBlock=10
    totalBlocks=10
    matlab -nojvm -r "run($block,$pointsPerBlock,$totalBlocks)"

**Condor submission script**

Condor actually contains ArrayJob functionality that makes the task
easier. ::

    ## Condor submit description (script) file for my_program.exe.
    ## 1. Specify the [path and] name for the executable file...
    Executable = run.sh
    ## 2. Specify Condor execution environment.
    Universe = vanilla
    notify   = Error
    ## 3. Specify remote execution machines running Linux (required)...
    Requirements = ((OpSys == "Linux") || (OpSysName == "Ubuntu"))
    ## 4. Define input files and arguments
    #Input = stdin.txt.$(Process)
    Arguments = $(Process)
    ## 5. Define output/error/log files
    Output = log/stdout.$(Process).txt
    Error  = log/stderr.$(Process).txt
    Log    = log/log.$(Process).txt
    ## 6. Tell Condor which files need to be transferred and when.
    Transfer_input_files = run.m
    Transfer_output_files = output-$(Process).mat
    Transfer_executable = true
    Should_transfer_files = YES
    When_to_transfer_output = ON_EXIT
    ## 7. Add 10 copies of the job to the queue
    Queue 10


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
