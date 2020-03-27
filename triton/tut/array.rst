==========
Array jobs
==========

.. highlight:: bash

Introduction
============

By now, you should be able to do all the basic things to run programs on
Triton. Now, you want to do it... a lot. The easiest way to parallize
things is to use array jobs. With array jobs, you take a single code or
script, and Slurm (the batch system) runs it many times for you, with
all the parameters. This is the simplest way of parallelizing things,
but only works for *embarrasingly parallel* problems: where your code
runs independently multiple times, and you use or combine the results
later. Still, for most people, this is as far as you need to go.

Basic examples
==============

When you run an array job (with ``--array=1-5``), Slurm runs your job
script many (5) times, with
one difference: the environment variable ``SLURM_ARRAY_TASK_ID``
(1,2,3,4,5). You have your job script or code read this variable and take
the right action, depending on what you need to do.

Below are four examples.  The first and third are probably most
recommended for starting out.

Different inputs
~~~~~~~~~~~~~~~~

In the example below, the ``$SLURM_ARRAY_TASK_ID`` is used to change to
the right directory, make the application read the correct input file,
and to generate output in a unique directory. This script is submitted
with ``sbatch script.sh``::

    #!/bin/bash
    #SBATCH -n 1
    #SBATCH -t 04:00:00
    #SBATCH --mem-per-cpu=2500
    #SBATCH --array=0-29

    # Each array task runs the same program, but with a different input file.
    cd $SLURM_ARRAY_TASK_ID
    srun echo I am number $SLURM_ARRAY_TASK_ID
    # e.g. srun ./my_application -input input_data_$SLURM_ARRAY_TASK_ID
    cd ..

Different parameters in script
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In the example below, we have the same program, but different command
line parameters. In this case, everything is hard coded in the bash
script itself. You could also do this directly inside your program, and
generate the parameters according to some algorithm. This can be really
powerful: not only can you both hard code and generate with algorithm,
but if you never edit already-run parameters, you have a single place
where you can see everything that has been run before. (Personally, I
always try to set up a system where parameters are defined in one place,
code in another, and I can always know what has been run for each output
by looking in just one place. If you are going to be configuring stuff
by hand anyway, better to have it all together.)::

    #!/bin/bash
    #SBATCH -n 1
    #SBATCH -t 04:00:00
    #SBATCH --mem-per-cpu=2500
    #SBATCH --array=0-4

    case $SLURM_ARRAY_TASK_ID in
        0) ARGS="-res 5 -arg 3" ;;
        1) ARGS="-res 6 -arg 3" ;;
        2) ARGS="-res 5 -arg 4" ;;
        3) ARGS="-res 6 -arg 4" ;;
        4) ARGS="-res 5 -arg 5" ;;
    esac

    cd $SLURM_ARRAY_TASK_ID
    srun I am doing $ARGS !
    # e.g. python input.py $ARGS
    cd ..

Read parameters from file
~~~~~~~~~~~~~~~~~~~~~~~~~

Now we do basically the same thing as above, but we have all of the
parameters stored in another file ``arrayparams.txt``::

  input_561 --opt1
  input_418 --opt2
  input_569 --opt1

In our script, we use the ``sed`` program to read just one line from
the file.  This is stored in the variable ``line``, and then we can
use this however: in this case by using it as the parameters to the
program.  Don't worry about how the ``sed`` command works - no one
really knows, we just find it via a web search.  Note that the line
numbers start at one, not zero!

::

    #!/bin/bash
    #SBATCH -n 1
    #SBATCH -t 04:00:00
    #SBATCH --mem-per-cpu=2500
    #SBATCH --array=1-3

    n=$SLURM_ARRAY_TASK_ID                  # define n
    line=`sed "${n}q;d" arrayparams.txt`    # get n:th line (1-indexed) of the file

    # Do whatever with arrayparams.txt
    srun echo I am doing $line
    # e.g. srun ./my_program $line


(advanced) Grouping runs together in bigger chunks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Let's say your tasks are very short - only a few minutes.  This is
still a bit short to use array jobs, because you will still have too
much overhead in scheduling.  We want to try for 30 minutes and if
possible more.  So, below is an example script that uses shell

In the below script, we take a chunk size of 100.  Array #0 will run
0-99, array #1 will run 100-199, etc.  The for loop handles the
running.  Before each one runs, it uses ``test -s output_$i`` to see if
the output filename ``output_$i`` exists: only run the task if it does
not exist already (see ``man test`` to see other types of tests you
can do).  This example starts using more advanced shell scripting,
which might be worth learning.

::

   [... all the initial stuff from above]

   CHUNKSIZE=100
   arrayID=$SLURM_ARRAY_TASK_ID
   indexes=`seq $((arrayID * CHUNKSIZE)) $(((arrayID+1)*CHUNKSIZE - 1))`

   for i in $indexes ; do
       if ! test -s output_$i ; then
           run $i
       fi
   done



2D sampling
~~~~~~~~~~~

Here is an example that lets you sample from a 2D array, with
experiments and 10 replicas (but this might be approaching hackish, ask
first if it makes sense to have them together)::

    experiment=$(( $SLURM_ARRAY_TASK_ID / 10 ))
    replica=$(( $SLURM_ARRAY_TASK_ID % 10 ))

More control
============

You can specify the ``--array=`` option either in the script itself
using the ``#SBATCH`` syntax, or on the command line to ``sbatch``. So, you can
control what runs different ways. Let's say you have a fixed number of
parameters: put that directly in the script. Or if you are just running
replicas, run them from the command line as you need more. In any case,
us the command line when things fail and you need to repeat only
certain runs.

You don't have to have the job script use the variable. You could
directly pass it as a command line argument to your program, use it to
pattern input files, or even have your own code access the process
environment and get the variable.

You can use ``%N``, like ``--array=1-100%10``, to limit number of jobs
running at once.

Note that arrays are *only* a feature of ``sbatch``. You can't use them
directly from the command line with ``srun``: you have to make a batch
script and submit with ``sbatch``.

Hints
=====

The array indices need not be sequential. E.g. if you discover that
after the above array job is finished, the job task id's 7 and 19
failed, you can relaunch just those jobs with ``--array=7,19``. While the
array job above is a set of serial jobs, parallel array jobs are
possible. For more information, see the `Slurm job array
documentation <https://slurm.schedmd.com/job_array.html>`__.

How do you map from ``$SLURM_ARRAY_TASK_ID`` to the parameters of the
job? There are different strategies

-  Have a lookup table in your code or another config file (bash example
   in slurm script above)
-  Pre-create different input files
-  Programmatically generate the different configs in your code.
-  Don't have different config, just use them to run multiple replicas
   of the same parameters. You increase the array ID until you have
   enough statistics to get your result.

You probably want to look at the slurm ``-o`` option to direct the script
output to somewhere useful. See the ``sbatch`` manual page, ``-o``,
``-e``, and ``--open-mode`` options. In the filenames, use ``%a`` for array
index and ``%A`` (array jobs) for array jobid.  For normal jobs, use
``%j`` for the jobid.  (If you use ``%j`` for array jobs, you get a
different number even when things were started as part of the same
array.  Maybe it's what you want).

Array jobs have less overhead for accounting and scheduling, but you
still want them to not be too short. 30 minutes is a good target time,
so try to combine smaller tasks to fit that.


Exercises
=========

1. Look at ``man sbatch`` and investigate the ``--array`` parameter.

2. Using the ``pi.py`` example from the :doc:`interactive tutorial
   <interactive>`, make an array job that calculates pi 10 times.

   a) The ``pi.py`` program takes an extra option: ``--seed=SEED``.
      Use the array task ID as the seed.

   b) Verify that the runs worked.  Average all values together to get
      your more accurate pi.

3. Using one of the techniques above, use ``memory-hog.py`` from the
   :doc:`interactive tutorial <interactive>`.  Make an array job that
   runs this with five different values of the memory (5M, 50M, 100M,
   200M, 500M).  You have to use one of the techniques above.

3. Make job array which runs every other index (like 1, 3, 5,
   etc).  You'll have to look at the ``sbatch`` manual page.


What's next?
============

The next tutorial is about :doc:`GPU computing <gpu>`.

For more information, you can see the CSC guide on array jobs:
`https://research.csc.fi/taito-array-jobs. <https://docs.csc.fi/computing/running/array-jobs/>`_

For more detailed information about running on Triton, see the main page
`Running programs on Triton <../usage/general>`.

Remember to check the `quick reference <../ref/index>` when needed.


