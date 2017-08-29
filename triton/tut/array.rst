==========
Array jobs
==========

Introduction
============

By now, you should be able to do all the basic things to run programs on
Triton.  Now, you want to do it... a lot. The easiest way to parallize
things is to use array jobs.  With array jobs, you take a single code or
script, and Slurm (the batch system) runs it many times for you, with
all the parameters.  This is the simplest way of parallelizing things,
but only works for *embarrasingly parallel* problems: where your code
runs independently multiple times, and you use or combine the results
later.  Still, for most people, this is as far as you need to go.

 

Basic examples
==============

When you run an array job, Slurm runs your job script many times, with
one difference: the environment variable ``SLURM_ARRAY_TASK_ID``.  You
just need to have your job script or code read this variable and take
the right action, depending on what you need to do.

In the example below, the ``$SLURM_ARRAY_TASK_ID`` is used to change to
the right directory, make the application read the correct input file,
and to generate output in a unique directory.  This script is submitted
with ``sbatch scirpt.sh`` .

Same program, different data

::

    #!/bin/bash
    #SBATCH -n 1
    #SBATCH -t 04:00:00
    #SBATCH --mem-per-cpu=2500
    #SBATCH --array=0-29

    # Each array task runs the same program, but with a different input file.
    cd $SLURM_ARRAY_TASK_ID
    srun ./my_application -input input_data_$SLURM_ARRAY_TASK_ID
    cd ..

In the example below, we have the same program, but different command
line parameters.  In this case, everything is hard coded in the bash
script itself.  You could also do this directly inside your program, and
generate the parameters according to some algorithm.  This can be really
powerful: not only can you both hard code and generate with algorithm,
but if you never edit already-run parameters, you have a single place
where you can see everything that has been run before.  (Personally, I
always try to set up a system where parameters are defined in one place,
code in another, and I can always know what has been run for each output
by looking in just one place.  If you are going to be configuring stuff
by hand anyway, better to have it all together.).

Same program, different command line options

::

    #!/bin/bash
    #SBATCH -n 1
    #SBATCH -t 04:00:00
    #SBATCH --mem-per-cpu=2500
    #SBATCH --array=0-29

    case $SLURM_ARRAY_TASK_ID in
        0) ARGS="-res 5 -arg 3" ;;
        1) ARGS="-res 6 -arg 3" ;;
        2) ARGS="-res 5 -arg 4" ;;
        3) ARGS="-res 6 -arg 4" ;;
        4) ARGS="-res 5 -arg 5" ;;
    esac

    cd $SLURM_ARRAY_TASK_ID
    srun ./my_application $ARGS
    cd ..

Here  is an example that lets you sample from a 2D array, with
experiments and 10 replicas (but this might be approaching hackish, ask
first if it makes sense to have them together):

2D array: trials and replicas

::

    experiment=$(( $SLURM_ARRAY_TASK_ID / 10 ))
    replica=$(( $SLURM_ARRAY_TASK_ID % 10 ))

 

More control
============

You can specify the ``--array=`` option either in the script itself
using the ``#SBATCH`` syntax, or on the command line.  So, you can
control what runs different ways.  Let's say you have a fixed number of
parameters: put that directly in the script.  Or if you are just running
replicas, run them from the command line as you need more.  In any case,
us the command line when things fail and you need to run more.

You don't have to have the job script use the variable.  You could
directly pass it as a command line argument to your program, use it to
pattern input files, or even have your own code access the process
environment and get the variable.

Note that arrays are *only* a feature of ``sbatch``.  You can't use them
directly from the command line with ``srun``: you have to make a batch
script and submit with ``sbatch``.

 

Hints
=====

The array indices need not be sequential. E.g. if you discover that
after the above array job is finished, the job task id's 7 and 19
failed, you can relaunch just those jobs with "–array=7,19". While the
array job above is a set of serial jobs, parallel array jobs are
possible. For more information, see the `Slurm job array
documentation <http://slurm.schedmd.com/job_array.html>`__.

How do you map from ``$SLURM_ARRAY_TASK_ID`` to the parameters of the
job?  There are different strategies

-  Have a lookup table in your code or another config file (bash example
   in slurm script above)
-  Pre-create different input files
-  Programmatically generate the different configs in your code.
-  Don't have different config, just use them to run multiple replicas
   of the same parameters.  You increase the array ID until you have
   enough statistics to get your result.

You probably want to look at the slurm -o option to direct the script
output to somewhere useful.  See the ``sbatch`` manual page, ``-o``,
``-e``, and ``--open-mode`` options.  In the filenames, use %a for array
index, and %j (normal jobs) %A (array jobs) for jobid.

Array jobs have less overhead for accounting and scheduling, but you
still want them to not be too short.  30 minutes is a good target time,
so try to combine smaller tasks to fit that.

What's next?
============

For more information, you can see the CSC guide on array jobs:
`https://research.csc.fi/taito-array-jobs. <https://research.csc.fi/taito-array-jobs>`__

For more detailed information about running on Triton, see the main page
`Running programs on Triton <LINK/Running%20programs%20on%20Triton>`__.

Remember to check the `quick reference <LINK/Reference>`__ when needed.

 
