=====================
Storage: local drives
=====================

.. seealso::

   :doc:`the storage tutorial <../tut/storage>`.

Local disks on computing nodes are the preferred place for doing your
IO. The general idea is use network storage as a backend and local disk
for actual data processing.

-  In the beginning of the job cd to ``/tmp`` and make a unique directory
   for your run
-  copy needed input from WRKDIR to there
-  run your calculation normally forwarding all the output to ``/tmp``
-  in the end copy relevant output to WRKDIR for analysis and further
   usage

Pros

-  You get better and steadier IO performance. WRKDIR is shared over all
   users making per-user performance actually rather poor.
-  You save performance for WRKDIR to those who cannot use local disks.
-  You get much better performance when using many small files (Lustre
   works poorly here).
-  Saves your quota if your code generate lots of data but finally you
   need only part of it
-  In general, it is an excellent choice for single-node runs (that is
   all job's task run on the same node).

Cons

-  Not feasible for huge files (>100GB). Use WRKDIR instead.
-  Small learning curve (must copy files before and after the job).
-  Not feasible for cross-node IO (MPI jobs). Use WRKDIR instead.

How to use local drives on compute nodes
----------------------------------------

NOT for the long-term data. Cleaned every time your job is finished.

You have to use ``--gres=spindle`` to ensure that you get a hard
disk (note 2019-january: except GPU nodes).

``/tmp`` is a bind-mounted user specific directory. Directory is per-user
(not per-job that is), if you get two jobs running on the same node, you
get the same ``/tmp``.

Interactively
~~~~~~~~~~~~~

How to use /tmp when you login interactively

::

    $ sinteractive -t 1:00:00              # request a node for one hour
    (node)$ mkdir /tmp/$SLURM_JOB_ID       # create a unique directory, here we use
    (node)$ cd /tmp/$SLURM_JOB_ID
    ... do what you wanted ...
    (node)$ cp your_files $WRKDIR/my/valuable/data  # copy what you need
    (node)$ cd; rm -rf /tmp/$SLURM_JOB_ID  # clean up after yourself
    (node)$ exit

In batch script
~~~~~~~~~~~~~~~

Batch job example that prevents data lost in case program gets
terminated (either because of ``scancel`` or due to time limit).

::

    #!/bin/bash

    #SBATCH --time=0-12:00:00 --mem-per-cpu=2500                  # time and memory requirements

    mkdir /tmp/$SLURM_JOB_ID                                      # get a directory where you will send all output from your program
    cd /tmp/$SLURM_JOB_ID

    ## set the trap: when killed or exits abnormally you get the
    ## output copied to $WRKDIR/$SLURM_JOB_ID anyway
    trap "mkdir $WRKDIR/$SLURM_JOB_ID; mv -f /tmp/$SLURM_JOB_ID $WRKDIR/$SLURM_JOB_ID; exit" TERM EXIT

    ## run the program and redirect all IO to a local drive
    ## assuming that you have your program and input at $WRKDIR
    srun $WRKDIR/my_program $WRKDIR/input > output

    mv /tmp/$SLURM_JOB_ID/output $WRKDIR/SOMEDIR                   # move your output fully or partially

Batch script for thousands input/output files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If your job requires a large amount of files as input/output using tar
utility can greatly reduce the load on the ``$WRKDIR``-filesystem.

Using methods like this is recommended if you're working with thousands
of files.

Working with tar balls is done in a following fashion:

#. Determine if your input data can be collected into analysis-sized
   chunks that can be (if possible) re-used
#. Make a tar ball out of the input data (``tar cf <tar filename>.tar
   <input files>``)
#. At the beginning of job copy the tar ball into ``/tmp`` and untar it
   there (``tar xf <tar filename>.tar``)
#. Do the analysis here, in the local disk
#. If output is a large amount of files, tar them and copy them out.
   Otherwise write output to ``$WRKDIR``

A sample code is below:

::

    #!/bin/bash

    #SBATCH --time=0-12:00:00 --mem-per-cpu=2000      # time and memory requirements
    mkdir /tmp/$SLURM_JOB_ID                          # get a directory where you will put your data
    cp $WRKDIR/input.tar /tmp/$SLURM_JOB_ID           # copy tarred input files
    cd /tmp/$SLURM_JOB_ID

    trap "rm -rf /tmp/$SLURM_JOB_ID; exit" TERM EXIT  # set the trap: when killed or exits abnormally you clean up your stuff

    tar xf input.tar                                  # untar the files
    srun  input/*                            # do the analysis, or what ever else
    tar cf output.tar output/*                        # tar output
    mv output.tar $WRKDIR/SOMEDIR                     # copy results back

