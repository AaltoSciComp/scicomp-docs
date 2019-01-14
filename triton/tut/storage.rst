============
Data storage
============

In this tutorial, we go over places to store data on Triton and how to
access it remotely.

Basics
======

Triton has various ways to store data.  Each has a purpose, and when
you are dealing with the large data sets or intensive IO, efficiency
becomes important.

Roughly, we have small home directories (only for configuration
files), large Lustre (scratch and work, large, primary calculation
data), and special places for scratch during computations (local
disks, ramfs, fast but temporary)

Compare this to what is available at Aalto:

-  Aalto Linux has a separate home directory, not shared with Triton.
-  Departments can have their own shares, called variously project,
   work, teamwork, archive.  These are not on Triton except the login
   node, because they are
   not high performance enough (it just takes one person to start
   50-node job that brings it down for everyone).

A file consists of its contents and metadata.  The metadata is things
like user, group, timestamps, permissions.  To view metadata, use ``ls
-l`` or ``stat``.

Think about I/O before you start! - General notes
=================================================

When people think of computer speed, they usually think of CPU speed.
But this is missing an important factor: how fast can data get to the
CPU?  In very many cases, I/O (input/output) is the true bottleneck.
This must be considered just as much as code efficiency.  **In fact,
modern computers and especially GPUs are so fast, that they can use
data so quickly that they can slow down the cluster down for
everyone.**

The answer is that users have a variety of needs, and a variety of
filesystems.  The following checklist aims to help you to choose the
best approach for you calculations.

-  How much IO in the first place?
-  What's the pattern of it, and which filesystem is best for it?
-  E.g. checkpointing code state to disk may be unwise if the code runs
   less that couple of days.
-  Some programs use local disk as swap-space. Only turn on if you know
   it is reasonable.

Filesystem performance can be measures by both IOPS (input-output
operations per second) and stream I/O speed.  ``/usr/bin/time -v`` can
give you some hints here.  You can see the :doc:`profiling
<../usage/profiling>` page for more info.

Avoid many small files! Use a few big ones instead. (we have a
:doc:`dedicated page <../usage/smallfiles>` on the matter)

Summary table
=============

.. include:: ../ref/storage.rst

Home directories
^^^^^^^^^^^^^^^^
The place you start when you log in.  For user init files, some small
config files, etc.  No calculation data. Daily backup.  Usually you
want to use scratch instead.

Lustre (/scratch)
^^^^^^^^^^^^^^^^^
This is the big, high-performance, 2PB Triton storage.  The primary
place for calculations, data analyzes etc.  Not backed up.  It is
shared on all nodes, and has very fast access.  It is divided into two
parts, scratch (by groups) or work (per-user).  In general, always
change to ``$WRKDIR`` or a group ``scratch`` directory when you first
log in and start doing work.

Lustre separates metadata and contents onto separate object and
metadata servers.  This allows fast access to large files, but a
larger overhead than normal filesystems.

See :doc:`../usage/lustre`

Local disks
^^^^^^^^^^^
Local disks are on each node separately.  For the fastest IOs with
single-node jobs. It is cleaned up after job is finished.  Since 2019,
things have gotten a bit more complicated since our newest (skl) nodes
don't have local disks.

See the :doc:`Compute
node local drives <../usage/localstorage>` page for further details and script
examples.

**ramfs** - fast and highly temporary storage
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

On Triton, ``$XDG_RUNTIME_DIR`` is a ramfs, which means that it looks like
files but is stored only in memory.  Because of this, it is extremely
fast, but has no persistence whatsoever.  Use it if you have to make
small temporary files that don't need to last long.  Note that this is
no different than just holding the data in memory, if you can hold in
memory that's better.


Quotas
======

All directories under ``/scratch`` (as well as ``/home``) have quotas. Two
quotas are set per-filesystem: disk space and files number.

Disk quota and current usage are printed with the command ``quota``.
'space' is for the disk space and 'files' for the total files number
limit. There is a separate quota for groups on which the user is a
member.

::

    $ quota
    User quotas for darstr1
         Filesystem   space   quota   limit   grace   files   quota   limit   grace
    /home              484M    977M   1075M           10264       0       0
    /scratch          3237G    200G    210G       -    158M      1M      1M       -

    Group quotas
    Filesystem   group                  space   quota   limit   grace   files   quota   limit   grace
    /scratch     domain users            132G     10M     10M       -    310M    5000    5000       -
    /scratch     some-group              534G    524G    524G       -    7534   1000M   1000M       -
    /scratch     other-group              16T     20T     20T       -   1088M      5M      5M       -

If you get a quota error, see :doc:`the quotas page <../usage/quotas>`
for the solution.


Accessing and transferring files remotely
=========================================

Transferring files to/from triton is exactly the same as any other
remote Linux server.

Remote mounting using SMB
^^^^^^^^^^^^^^^^^^^^^^^^^

By far, remote mounting of files is the easiest method to transfer files.  If you are
not on the Aalto networks (wired, ``eduroam``, or ``aalto`` with
Aalto-managed laptop), connect to the :doc:`Aalto VPN
</aalto/remoteaccess>` first.  Note that
this is automatically done on some department workstations (see
below) - if not, request it!

The scratch filesystem can be remote mounted using SMB inside secure
Aalto networks at the URLs

* scratch: ``smb://data.triton.aalto.fi/scratch/``.
* work: ``smb://data.triton.aalto.fi/work/$username/``.

On different operating systems:

* Linux (Ubuntu for example): File manager (Nautilus) → File →
  Connect to server.  Use the ``smb://`` URLs above.
* Windows: In the file manager, go to Computer (in menu bar on top, at
  least in Windows 10) → Map Network Drive) and "Map Network Drive".
  In Windows 10 → "This PC" → right click → "Add Network Location".
  (Note that this is different from right-click "Add network location"
  which just makes a folder link and has had some problems in the past.)
  Use the URLs above but replace ``smb://`` with ``\\`` and ``/`` with
  ``\``.  For example, ``\\data.triton.aalto.fi\scratch\``.
* Mac: Finder → Go → Connect to Server.  Use the ``smb://`` URLs above.

Depending on your OS, you may need to use either your username
directly or ``AALTO\username``.


Using scp or sftp
^^^^^^^^^^^^^^^^^

The *scp* and *sftp* protocols use ssh to transfer files.  On Linux
and Mac, the the ``scp`` and ``sftp`` command line programs are the
must fundamental way to do this, and are available everywhere.

A more user-friendly way of doing this (with a nice GUI) is the
`Filezilla program <https://filezilla-project.org/>`__.

Below is an example of the "raw" scp usage::

    # copying to HOME
    user@pc123 $ scp testCluster.m user12@triton:
    testCluster.m                                 100%  391     0.4KB/s   00:00
    # copying to WRKDIR
    user@pc123 $ scp testCluster.m user12@triton:/scratch/work/USERNAME/
    ...

Rsync
^^^^^

Rsync is similar to scp, but is smarter at restarting files.  Use rsync
for large file transfers.  ``rsync`` actually uses ``ssh``, so
you can ``rsync`` from anywhere you can ``ssh`` from.


Remote mounting using sshfs
^^^^^^^^^^^^^^^^^^^^^^^^^^^

``sshfs`` is a neat program that lets you mount remote filesystems via
ssh only.  It is well-supported in Linux, and somewhat on other
operating systems.  It's true advantage is that you can mount any
remote ssh server - it doesn't have to be set up specially for SMB or
any other type of mounting.  On Ubuntu, you can mount by "File → Connect to
server" and using ``sftp://triton.aalto.fi/scratch/work/USERNAME``.

The below uses command line programs to do the same, and makes the
``triton_work`` on your local computer access all files in
``/scratch/work/USERNAME``.  Can be done with other folders.::

    mkdir triton_work
    sshfs USERNAME@triton.aalto.fi:/scratch/work/USERNAME triton_work

Note that ``ssh`` binds together many ways of accessing Triton, with a
similar syntax and options.  ``ssh`` is a very important program and
binds together all types of remote access, and learning to use it well
will help you for a long time.


Exercises
^^^^^^^^^
1. Mount your work directory by SMB and transfer a file to Triton.
   Note that you must be on ``eduroam``, the ``aalto`` *with Aalto
   laptop*, or connected to the Aalto VPN.

2. Or, use rsync, scp/sftp, or sshfs to transfer a file.

3. (Advanced) If you have a Linux on Mac computer, study the ``rsync``
   manual page and try to transfer a file.


Accessing files from Department workstations
============================================

This varies per department, with some strategies that work from
everywhere.

These mounts that are already on workstations require a valid Kerberos
ticket (usually generated when you log in). On long sessions these might
expire, and you have to renew them with ``kinit`` to keep going.

Generic
^^^^^^^

The staff shell server ``taltta.aalto.fi`` has scratch and work mounted
at ``/m/triton``, and department directories are also in the standard
paths ``/m/{cs,nbe}/{scratch,work}/``.

NBE
^^^

Work directories are available at ``/m/nbe/work`` and group scratch
directories at ``/m/nbe/scratch/$project/``.

PHYS
^^^^

Directories available on demand through SSHFS. See the `Data
transferring <https://wiki.aalto.fi/display/TFYintra/Data+transferring>`__ page
at PHYS Intranet (accessible by PHYS users only).

CS
^^

Work directories are available at ``/m/cs/work/``, and group scratch
directories at ``/m/cs/scratch/$project/``.


Exercises
=========

``strace`` is a command which tracks **system calls**, basically the
number of times the operating system has to do something.  It can be
used as a rudimentary way to see how much I/O load there is.

1. Use ``strace -c`` to compare the number of system calls in ``ls``,
   ``ls -l``, ``ls --no-color``, and ``ls --color``.  You can use the directory
   ``/scratch/scip/lustre_2017/many-files/`` as a place with many
   files in it.  How many system calls per file were there for each
   option?

2. Using ``strace -c``, compare the times of ``find`` and ``lfs find``
   on the directory mentioned above.  Why is it different?

3. (Advanced, requires slurm knowledge from future tutorials)  You
   will find some sample files in ``/scratch/scip/examples/io``.
   Create a temporary directory and...

   a) Run ``create_iodata.sh`` to make some data files in ``data/``

   b) Compare the IO operations of ``find`` and ``lfs find`` on this
      directory.

   c) use the ``iotest.sh`` script to do some basic analysis.  How
      long does it take?  Submit it as a slurm batch job.

   d) Modify the iotest.sh script to copy the ``data/`` directory to
      local storage, do the operations, then remove the data.  Compare
      to previous strategy.

   e) Use ``tar`` to compress the data while it is on lustre.  Unpack
      this tar archive to local storage, do the operations, then
      remove.  Compare to previous strategies.



Next steps
==========

The next tutorial is about :doc:`interactive jobs <interactive>`.

Optimizing data storage isn't very glamorous, but it's an important
part of high-performance computing.  You can find some hints on the
:doc:`profiling <../usage/profiling>` page.

We have these related pages:

* :doc:`../usage/lustre`
* :doc:`../usage/localstorage`
* :doc:`../usage/quotas`
* :doc:`../usage/smallfiles`
