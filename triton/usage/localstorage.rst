=====================
Storage: local drives
=====================

.. seealso::

   :doc:`the storage tutorial <../tut/storage>`.

Local disks on computing nodes are the preferred place for doing your
IO. The general idea is use network storage as a backend and local disk
for actual data processing.  **Some nodes have no disks** (local
storage comes out of the job memory, **some older nodes have HDDs**
(spinning disks), and some **SSDs**.

A general use pattern:

- In the beginning of the job, copy needed input from WRKDIR to ``/tmp``.
- Run your calculation normally reading input from or writing output
  to to ``/tmp``.
- In the end copy relevant output to WRKDIR for analysis and further
  usage.

Pros

-  You get better and steadier IO performance. WRKDIR is shared over all
   users making per-user performance actually rather poor.
-  You save performance for WRKDIR to those who cannot use local disks.
-  You get much better performance when using many small files (Lustre
   works poorly here) or random access.
-  Saves your quota if your code generate lots of data but finally you
   need only part of it
-  In general, it is an excellent choice for single-node runs (that is
   all job's task run on the same node).

Cons

-  NOT for the long-term data. Cleaned every time your job is finished.
-  Space is more limited (but still can be TBs on some nodes)
-  Need some awareness of what is on each node, since they are different
-  Small learning curve (must copy files before and after the job).
-  Not feasible for cross-node IO (MPI jobs where different tasks
   write to the same files). Use WRKDIR instead.



How to use local drives on compute nodes
----------------------------------------

``/tmp`` is the temporary directory.  It is per-user (not per-job), if
you get two jobs running on the same node, you get the same ``/tmp``.
It is automatically removed once the last job on a node finishes.


Nodes with local disks
~~~~~~~~~~~~~~~~~~~~~~

You can see the nodes with local disks on :doc:`../overview`.  (To
double check from within the cluster, you can verify node info with
``sinfo show node NODENAME`` and see the ``localdisk`` tag in
``slurm features``).  Disk sizes greatly vary from hundreds of GB to
tens of TB.

You have to use ``--constraint=localdisk`` to ensure that you get a
hard disk.  You can use ``--tmp=nnnG`` (for example ``--tmp=100G``) to
request a node with at least that much temporary space.  But,
``--tmp`` doesn't allocate this space just for you: it's shared among
all users, including those which didn't request storage space.  So,
you *might* not have as much as you think.  Beware and handle out of
memory gracefully.


Nodes without local disks
~~~~~~~~~~~~~~~~~~~~~~~~~

You can still use ``/tmp``, but it is an in-memory ramdisk.  This
means it is *very* fast, but is using the actual main memory that is
used by the programs.  It comes out of your job's memory allocation,
so use a ``--mem`` amount with enough space for your job and any
temporary storage.



Examples
--------

Interactively
~~~~~~~~~~~~~

How to use /tmp when you login interactively

.. code-block:: console

    $ sinteractive --time=1:00:00              # request a node for one hour
    (node)$ mkdir /tmp/$SLURM_JOB_ID       # create a unique directory, here we use
    (node)$ cd /tmp/$SLURM_JOB_ID
    ... do what you wanted ...
    (node)$ cp your_files $WRKDIR/my/valuable/data  # copy what you need
    (node)$ cd; rm -rf /tmp/$SLURM_JOB_ID  # clean up after yourself
    (node)$ exit

In batch script
~~~~~~~~~~~~~~~

This batch job example that prevents data loss in case program gets
terminated (either because of ``scancel`` or due to time limit).

.. code-block:: slurm

    #!/bin/bash

    #SBATCH --time=12:00:00
    #SBATCH --mem-per-cpu=2500M                                   # time and memory requirements

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

.. code-block:: slurm

    #!/bin/bash

    #SBATCH --time=12:00:00
    #SBATCH --mem-per-cpu=2000M                       # time and memory requirements
    mkdir /tmp/$SLURM_JOB_ID                          # get a directory where you will put your data
    cp $WRKDIR/input.tar /tmp/$SLURM_JOB_ID           # copy tarred input files
    cd /tmp/$SLURM_JOB_ID

    trap "rm -rf /tmp/$SLURM_JOB_ID; exit" TERM EXIT  # set the trap: when killed or exits abnormally you clean up your stuff

    tar xf input.tar                                  # untar the files
    srun  input/*                                     # do the analysis, or what ever else
    tar cf output.tar output/*                        # tar output
    mv output.tar $WRKDIR/SOMEDIR                     # copy results back

