=====================
Storage: local drives
=====================

.. admonition:: Abstract

   - Path is ``/tmp/``
   - Local drives are useful for large temporary data or unpacking
     many small files before analysis.  They are most important for
     GPU training data but are useful other times, too.
   - Local storage can be either SSD drives (big and reasonably fast),
     spinning hard disks (HDDs; older nodes), or ramdisk (using your
     job's memory; extremely fast).
   - Request a spinning disk or SSD with ``--constraint=localdisk``
     and ``--tmp=NNg`` (but the space isn't reserved just for you).
   - For ramdisk, the space comes out of your ``--mem=`` allocation.

.. seealso::

   :doc:`The storage tutorial <../tut/storage>`.

Local disks on computing nodes are the preferred place for doing
extensive input/output (IO; reading/writing files).  The general idea
is use network storage as a backend and local disk for actual data
processing when it requires many reads or writes.  **Different nodes
have different types of disks, Triton is very heterogeneous**:

.. list-table::
   :header-rows: 1

   - - Type
     - Description
     - Requesting
     - Path
   - - Solid-state drives (SSDs)
     - Much faster than HDDs but much slower than ramdisk.  Generally
       GPU nodes have SSDs these days.
     - ``--constraint=localdisk`` and ``--tmp=NNg``.  The space is not
       guaranteed just for you.
     - ``/tmp/``
   - - Spinning hard disks (HDDs)
     - Generally only older CPU nodes have HDDs.
     - ``--constraint=localdisk`` and ``--tmp=NNg`` to specify size
       you need.  The space is not guaranteed just for you.
     - ``/tmp/``
   - - Ramdisk
     - Uses your jobs memory allocation.  Limited space but lightning
       fast.
     - ``--mem=NNg`` to request enough memory for your job and your
       storage.
     - ``/tmp/`` on diskless nodes and ``/dev/shm/`` on every node.

See :doc:`../overview` for details on each node's local storage.

The reason that local storage matters is that :doc:`lustre` (scratch)
is not good for many :doc:`smallfiles`.  Read those articles for
background.


Background
----------

A general use pattern:

- In the beginning of the job, copy needed input from Scratch to ``/tmp``.
- Run your calculation normally reading input from or writing output
  to to ``/tmp``.
- In the end copy relevant output to Scratch for analysis and further
  usage.

Pros:

-  You get better and steadier IO performance. Scratch is shared over all
   users making per-user performance can be poor at times, especially
   for many small files.
-  You save performance for Scratch to those who cannot use local disks.
-  You get much better performance when using many small files (Lustre
   works poorly here) or random access.
-  Saves your quota if your code generate lots of data but you only
   need to save part of it.
-  In general, it is an excellent choice for single-node runs (that is
   all job's task run on the same node).

Cons:

-  NOT for the long-term data. Cleaned every time your job is finished.
-  Space is more limited (but still can be TBs on some nodes)
-  Need some awareness of what is on each node, since they are different
-  Small learning curve (must copy files before and after the job).
-  Not feasible for cross-node IO (MPI jobs where different tasks
   write to the same files). Use Scratch instead.



Usage
-----

``/tmp`` is the temporary directory.  It is ramdisk on diskless nodes.

It is per-user (not per-job), if you get two jobs running on the same
node, you get the same ``/tmp``.  Thus, it is wise to ``mkdir
/tmp/$SLURM_JOB_ID/`` and use that directory, and delete it once the
job is done.

Everything is automatically removed once the last job on a node
finishes.


Nodes with local disks
~~~~~~~~~~~~~~~~~~~~~~

You can see the nodes with local disks on :doc:`../overview`.  Disk
sizes greatly vary from hundreds of GB (older nodes, when everything
had spinning disks) to tens of TB (new GPU nodes designed for ML
training).

.. admonition:: Verifying node details directly through Slurm

   You don't usually need to do this.  You can verify node info with
   ``sinfo show node NODENAME`` and look for ``TmpDisk=`` or
   ``AvailableFeatures=localdisk``.  ``slurm features`` will list all
   nodes (look for ``localdisk`` in features).

You have to use ``--constraint=localdisk`` to ensure that you get a
disk of some type.  You can use ``--tmp=nnnG`` (for example
``--tmp=100G``) to request a node with at least that much temporary
space.  But, ``--tmp`` doesn't allocate this space just for you: it's
shared among all users, including those which didn't request storage
space.  So, you *might* not have as much as you think.  Beware and
handle "out of space" errors gracefully.


Nodes without local disks
~~~~~~~~~~~~~~~~~~~~~~~~~

You can still use ``/tmp``, but it is an in-memory ramdisk.  This
means it is *very* fast, but is using the actual main memory that is
used by the programs.  It comes out of your job's memory allocation,
so use a ``--mem=nnG`` amount with enough space for your job and any
temporary storage.



Examples
--------

Interactively
~~~~~~~~~~~~~

How to use /tmp when you login interactively, for example space to
decompress a big file.

.. code-block:: console

    $ sinteractive --time=1:00:00 --tmp=500G         # request a node for one hour
    (node)$ mkdir /tmp/$SLURM_JOB_ID                 # create a unique directory, here we use
    (node)$ cd /tmp/$SLURM_JOB_ID
    ... do what you wanted ...
    (node)$ cp YOUR_FILES $WRKDIR/my/valuable/data   # copy what you need
    (node)$ cd; rm -rf /tmp/$SLURM_JOB_ID            # clean up after yourself
    (node)$ exit



In batch script - save data if job ends prematurely
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This batch job example that has a trigger (``trap``) that prevents
data loss in case the program gets terminated early (either because of
``scancel``, the time limit, or some other error).  It copies the data
to a different location (``$WRKDIR/$SLURM_JOB_ID``) in case of errors
compared to other normal exits.

.. code-block:: slurm
   :emphasize-lines: 14-16,25-26

   #!/bin/bash
   #SBATCH --time=12:00:00
   #SBATCH --mem-per-cpu=2500M            # time and memory requirements
   #SBATCH --output=test-local.out

   # The below, if uncommented, will cause the script to abort (and trap
   # to run) if there are any unhandled errors.
   #set -euo pipefail

   # get a directory where you will send all output from your program
   mkdir /tmp/$SLURM_JOB_ID
   cd /tmp/$SLURM_JOB_ID

   ## set the trap: when killed or exits abnormally you get the
   ## output copied to $WRKDIR/$SLURM_JOB_ID anyway
   trap "rsync -a /tmp/$SLURM_JOB_ID/ $WRKDIR/$SLURM_JOB_ID/ ; exit" TERM EXIT

   ## run the program and redirect all IO to a local drive
   ## assuming that you have your program and input at $WRKDIR
   srun $WRKDIR/my_program $WRKDIR/input > output

   # move your output fully or partially
   mv /tmp/$SLURM_JOB_ID/output $WRKDIR/SOMEDIR

   # Un-set the trap since we ended successfully
   trap - TERM EXIT



Batch script for thousands input/output files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If your job requires a large amount of files as input/output, you can
store the files in a single archive format (``.tar``, ``.zip``, etc.)
and unpack them to local storage when needed.  This can greatly reduce
the load on the scratch filesystem.

Using methods like this is recommended if you're working with thousands
of files.

Working with tar balls is done in a following fashion:

#. Determine if your input data can be collected into analysis-sized
   chunks that can be (if possible) re-used
#. Make a tar ball out of the input data (``tar cf ARCHIVE_FILENAME.tar
   INPUT_FILES ...``)
#. At the beginning of job copy the tar ball into ``/tmp`` and untar it
   there (``tar xf ARCHIVE_FILENAME.tar``)
#. Do the analysis here, in the local disk
#. If output is a large amount of files, tar them and copy them out.
   Otherwise write output to ``$WRKDIR``

A sample code is below:

.. code-block:: slurm
   :emphasize-lines: 9-10,18-23

    #!/bin/bash
    #SBATCH --time=12:00:00
    #SBATCH --mem-per-cpu=2000M                       # time and memory requirements

    # get a directory where you will put your data and change to it
    mkdir /tmp/$SLURM_JOB_ID
    cd /tmp/$SLURM_JOB_ID

    # set the trap: when killed or exits abnormally you clean up your stuff
    trap "rm -rf /tmp/$SLURM_JOB_ID; exit" TERM EXIT

    # untar the files.  If we only unpack once, there is no point in
    # making an initial copy to local disks.
    tar xf $WRKDIR/input.tar

    srun MY_PROGRAM input/*                           # do the analysis, or what ever else, on the input files

    # If you generate many output files, tar them before copying them
    # back.
    # If it's just a few files of output, you can copy back directly
    # (or even output them straight to scratch)
    tar cf output.tar output/                         # tar output (if needed)
    mv output.tar $WRKDIR/SOMEDIR                     # copy results back

   # Un-set the trap since we ended successfully
    trap - TERM EXIT
