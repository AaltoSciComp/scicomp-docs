==========
Array jobs
==========

.. highlight:: bash

More often than not, problems involve running similar programs in parallel
where there is no dependency or communication among the processes.
Their results are thus combined as the final output, e.g. Monte Carlo simulations.

In Slurm context, *job arrays* are the way to run several instances of a
single-threaded program, known as the *embarrassingly parallel* paradigm.

Introduction
============

Array jobs allow you to parallelize your computations. They are used when you need
to run the same job many times with only slight changes among the jobs. For example,
you need to run 1000 jobs each with a different seed value for the random number generator.
Or perhaps you need to apply the same computation to a collection of data sets.
These can be done by submitting a single array job.

Slurm job array is a collection of jobs that are to be executed with identical
parameters. This means that there is one single batch script that is to be run
as many times as indicated by the ``--array`` directive, e.g.::

  #SBATCH --array=0-4

creates an array of 5 jobs (tasks) with index values 0, 1, 2, 3, 4.

The array tasks are copies of the "master" batch script that are automatically submitted
to Slurm. Slurm provides a unique environment variable ``SLURM_ARRAY_TASK_ID`` to each
task which could be used for handling input output files to each task.

.. note::

   You can alternatively pass the ``--array`` option as a command-line argument to
   ``sbatch``.

Your first array job
====================

Let's see a job array in action. Create a file with your favorite editor and name it
as you wish. Let's name it ``hello.sh`` and write it as follows.

.. code-block:: bash

   #SBATCH --job-name=slurm_env_var
   #SBATCH --output=/scratch/work/%u/task_number_%A_%a.out
   #SBATCH --array=0-15
   #SBATCH --time=00:15:00
   #SBATCH --mem=200
   # You may put the commands below:

   # Job step
   srun echo "I am array task number" $SLURM_ARRAY_TASK_ID

Submitting the job script to Slurm with ``sbatch hello.sh``, you will get the message::

  $ Submitted batch job 52608925

The job ID in the message is that of the "master" job - which is also used in the
batch script using ``%A`` for the output files (with the slurm ``-o`` option). To create unique output files for
each task in the job array, ``%a`` is used that is filled in with the array task ID.

Once the jobs are completed, the output files will be created in your work directory,
with the help ``%u`` to determine your user name::

   $ ls $WRKDIR
   task_number_52608925_12.out  task_number_52608925_3.out   task_number_52608925_8.out  task_number_52608925_9.out
   task_number_52608925_0.out   task_number_52608925_13.out  task_number_52608925_4.out
   task_number_52608925_1.out   task_number_52608925_14.out  task_number_52608925_5.out
   task_number_52608925_10.out  task_number_52608925_15.out  task_number_52608925_6.out
   task_number_52608925_11.out  task_number_52608925_2.out   task_number_52608925_7.out

You can ``cat`` one of the files to see the output of each task::

   $ cat task_number_52608925_5.out
   I am array task number 5

.. important::

   If your current directory is your home directory, please remember to direct
   your results to your work directory. You can keep your scripts/source codes
   in you home directory since it is backed up daily and should keep your calculations
   and analyses on your work directory.

More examples
=============

The following examples give you an idea on how to use job arrays for different
use cases and how to utilize the ``$SLURM_ARRAY_TASK_ID`` environment variable.


Reading input files
-------------------

In many cases, you would like to process several data files, that is, pass different
input files to your code to be processed. This can be achieved by using
``$SLURM_ARRAY_TASK_ID`` envinronment variable.

You could utilize to process several data files. In this case,
In the example below, the is used to change to
the right directory, make the application read the correct input file,
and to generate output in a unique directory. This script is submitted
with ``sbatch script.sh``::

    #!/bin/bash
    #SBATCH -n 1
    #SBATCH -t 04:00:00
    #SBATCH --mem-per-cpu=1G
    #SBATCH --array=0-29

    # Each array task runs the same program, but with a different input file.
    # e.g. srun ./my_application -input input_data_$SLURM_ARRAY_TASK_ID

Hardcoding arguments in the batch script
----------------------------------------

One way to pass arguments to your code is by hardcoding them in the batch script
you want to submit to Slurm.

Assume you would like to run the Pi estimation code for 5 different seed values, each
for 2.5 million iterations. You could assign a seed value to each task in you job array
and save each output to a file. Having calculated all estimations, you could take the
average of all the Pi values to arrive at a more accurate estimate. An example of such
a batch script is as follows.

.. code-block:: bash

   #!/bin/bash
   #SBATCH --job-name=pi_estimation
   #SBATCH --output=pi.out.log --open-mode=append
   #SBATCH --array=0-4
   #SBATCH --time=01:00:00
   #SBATCH --mem=500
   # Note that all jobs will write to the same file.  This makes less
   # files, but will be hard to tell the outputs apart.

   case $SLURM_ARRAY_TASK_ID in

       0)  SEED=123 ;;
       1)  SEED=38  ;;
       2)  SEED=22  ;;
       3)  SEED=60  ;;
       4)  SEED=432 ;;
   esac

   python ~/trit_examples/pi.py 2500000 --seed=$SEED > pi_$SEED.json

Save the script as e.g. ``run_pi.sh`` and submit to Slurm::

   $ sbatch run_pi.sh
   Submitted batch job 52655434

Once finished, 5 files will be created in your current directory each containing the
Pi estimation; total number of iterations (sum of iteration per task);
and total number of successes)::

   $ cat pi_22.json
   {"successes": 1963163, "pi_estimate": 3.1410608, "iterations": 2500000}

Reading parameters from one file
--------------------------------

Another way to pass arguments to your code via script is to save the arguments
to a file and have your script read the arguments from it.

Drawing on the previous example, let's assume you now want to run ``pi.py``
with different iterations. You can create a file, say ``iterations.txt``
and have all the values written to it, e.g.::

   $ cat iterations.txt
   100
   1000
   50000
   1000000

You can modify the previous script to have it read the ``iterations.txt``
one line at a time and pass it on to ``pi.py``. Here, ``sed`` is used
to get each line. Alternatively you can use any other command-line
utility in its stead, e.g. ``awk``. Do not worry if you don't know
how ``sed`` works - Google search and ``man sed`` always help.
Also note that the line numbers start at 1, not 0.

.. code-block:: bash

    #!/bin/bash
    #SBATCH -n 1
    #SBATCH --output=pi.2.out.log --open-mode=append
    #SBATCH --array=1-4
    #SBATCH --time=01:00:00
    #SBATCH --mem=500

    n=$SLURM_ARRAY_TASK_ID
    iteration=`sed -n "${n} p" iterations.txt`      # Get n-th line (1-indexed) of the file
    python ~/pi.py ${iteration} > pi_iter_${n}.json

You can additionally do this procedure in a more complex way, e.g. read in multiple
arguments from a csv file, etc.

(Advanced) Grouping runs together in bigger chunks
--------------------------------------------------
If your jobs are many and too short - a few minutes -,
using array jobs may induce too much overhead in scheduling.
Or you may simply have too many runs and creating too many array
jobs again is not recommended.

.. important::

   A good target time for the array jobs would be approximately 30 minutes,
   so please try to combine your tasks so that each job would at least take this long.

The workaround is exploiting shell's capabilities. For example,
assume you want to run the Pi script with 50 different seed values.
You could define a chunk size of 10 and 5 array jobs. Even with as
little as 5 array jobs, you can run 50 simulations.

This method demands for more knowledge of shell scripting which will
definitely be worth your while.

.. code-block:: bash

   #!/bin/bash
   #SBATCH -n 1
   #SBATCH --output=pi.3.out.log --open-mode=append
   #SBATCH --array=1-5
   #SBATCH --time=01:00:00
   #SBATCH --mem=500

   # Define and create a new directory (and an intermediate one) in your work directory
   DIRECTORY=/scratch/work/${USER}/pi_simulations_results/json_files
   mkdir -p ${DIRECTORY}

   CHUNKSIZE=100
   n=$SLURM_ARRAY_TASK_ID
   indexes=`seq $((n*CHUNKSIZE)) $(((n + 1)*CHUNKSIZE - 1))`

   for i in $indexes
   do
       python ~/pi.py 1500000 --seed=$i > ${DIRECTORY}/pi_$i.json
   done

.. important::

   The array indices need not be sequential, e.g. if you discover that
   after the array job is finished, the job task id's 2 and 5
   failed, you can relaunch just those jobs with ``--array=2,5``.
   In this case you can simply pass the ``--array`` option
   as a command-line argument to ``sbatch``.

Exercises
=========

1. Using the ``pi.py`` example from the :doc:`interactive tutorial
   <interactive>`, create a job array that calculates a combination
   of different iterations and seed values. Average them all to arrive
   at a more accurate Pi.

2. Using one of the techniques above, use ``memory-hog.py`` from the
   :doc:`interactive tutorial <interactive>`.  Make an array job that
   runs this with five different values of the memory (5M, 50M, 100M,
   200M, 500M).

3. Make job array which runs every other index, e.g. the array can be
   indexed as 1, 3, 5...(``sbatch`` manual page can be of help)


What's next?
============

.. seealso::

   For more information, you can see the
   `CSC guide on array jobs <https://docs.csc.fi/computing/running/array-jobs/>`_

   Please check the `quick reference <../ref/index>` when needed.

   if you need more detailed information about running on Triton, see the main page
   `Running programs on Triton <../usage/general>`.

The next tutorial is about :doc:`GPU computing <gpu>`.
