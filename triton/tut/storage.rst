============
Data storage
============

Triton has various different filesystems.  Each has a purpose, and when
you are dealing with the large data sets or intensive IO, efficiency
becomes important.

Roughly, we have

-  Home directories: for user init files, some small config files, etc.
   No calculation data. Daily backup.
-  Lustre (/scratch): a high-performance filesystem shared among all
   nodes. The primary place for calculations, data analyzes etc.  Not
   backed up.
-  Local disks are on each node separately.  For the fastest IOs with
   single-node jobs. It is cleaned up after job is finished.
-  RAM filesystems.  As fast as memory. Data lost when node is rebooted.

Compare this to what is available at Aalto:

-  Aalto Linux has a separate home directory, not shared with Triton.
-  Departments can have their own shares, called variously project,
   work, teamwork, archive.  These are not on triton, because they are
   not high performance enough (it just takes one person to start
   50-node job that brings it down for everyone).

Triton storage locations
========================

.. include:: ../ref/storage.rst

Think about I/O before you start! - General notes
=================================================

When people think of computer speed, they usually think of CPU speed.
But this is missing an important factor: how fast can data get to the
CPU?  In very many cases, I/O (input/output) is the true bottleneck.
This must be considered just as much as code efficiency.

The answer is that users have a variety of needs, and a variety of
filesystems.  The following checklist aims to help you to choose the
best approach for you calculations.

| Do you need IO in the first place?

-  E.g. checkpointing code state to disk may be unwise if the code runs
   less that couple of days.
-  Some programs use local disk as swap-space. Only turn on if you know
   it is reasonable.

Avoid many small files! Use a few big ones instead.  See the :doc:`Compute
node local drives <../usage/localstorage>` page for further details and script
examples.

**ramfs** - highly temporary storage - $XDG\_RUNTIME\_DIR
=========================================================

On Triton, $XDG\_RUNTIME\_DIR is a ramfs, which means that it looks like
files but is stored only in memory.  Because of this, it is extremely
fast, but has no persistence whatsoever.  Use it if you have to make
small temporary files that don't need to last long.  Note that this is
no different than just holding the data in memory, if you can hold in
memory that's better.


Quotas
======

All directories under /scratch (as well as /home) have quotas. Two
quotas are set per-filesystem: disk space and files number.

Disk quota and current usage are printed with the command "quota". 
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

 

Transferring files
==================

Transferring files to/from triton is exactly the same as any other
remote Linux server.

Using scp
^^^^^^^^^

You can use ``scp`` to copy your files to/from triton, and for accessing
the Triton home directory this is the only way. Note however the quite
limited disk quota in your home directory.

::

    # copying to HOME
    user@pc123 $ scp testCluster.m user12@triton:
    testCluster.m                                 100%  391     0.4KB/s   00:00    
    # copying to WRKDIR
    user@pc123 $ scp testCluster.m user12@triton:/scratch/work/USERNAME/
    ... 

Rsync
^^^^^

Rsync is similar to scp, but is smarter at restarting files.  Use rsync
for large file transfers.

Using sshfs
^^^^^^^^^^^

sshfs is a neat program that lets you mount remote filesystems via ssh
only.  It is at least well-supported in Linux, for other operating
systems check.  The below command makes ``triton_work`` on your local
computer access all files in ``/scratch/work/USERNAME``.  Can be done
with other folders.

::

    sshfs triton.aalto.fi:/scratch/work/USERNAME triton_work

Accessing files from Department workstations
============================================

This varies per department, with some strategies that work from
everywhere.

These mounts that are already on workstations require a valid Kerberos
ticket (usually generated when you log in). On long sessions these might
expire, and you have to renew them with ``kinit`` to keep going.

**Generic**

The staff shell server ``taltta.aalto.fi`` has scratch and work mounted
at ``/m/triton``, and department directories are also in the standard
paths ``/m/{cs,nbe}/{scratch,work}/``.

NBE
^^^

Work directories are available at ``/m/nbe/work`` and group scratch
directories at ``/m/nbe/scratch``/$project/.

PHYS
^^^^

Directories available on demand through SSHFS. See the `Data
transferring <https://wiki.aalto.fi/display/TFYintra/Data+transferring>`__ page
at PHYS Intranet (accessible by PHYS users only).

CS
^^

Work directories are available at ``/m/cs/work/``, and group scratch
directories at `` /m/cs/scratch/$project/.``
