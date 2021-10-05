============
Data storage
============

.. admonition:: Video

   `Watch this in the Winter Kickstart 2021 course <https://www.youtube.com/watch?v=guZYMgwdP4Q&list=PLZLVmS9rf3nN_tMPgqoUQac9bTjZw8JYc&index=10>`__

In this tutorial, we go over places to store data on Triton and how to
access it remotely.

Optimizing data storage isn't very glamorous, but is an important
part of high-performance computing.

This page roughly has three parts:

- What storage locations are available?
- Where are they available (mounted) on Aalto computers?
- How can you access them remotely?



Basics
------

Triton has various ways to store data.  Each has a purpose, and when
you are dealing with large data sets or intensive I/O, efficiency
becomes important.

Roughly, we have small **home** directories (only for configuration
files), large Lustre (**scratch** and **work**, large, primary calculation
data), and special places for scratch during computations (**local
disks**).  At Aalto, there is **aalto home**, **project**, and
**archive** directories which, unlike Triton, are backed up but don't
scale to the size of Triton.

A file consists of its contents and metadata.  The metadata is information
like user, group, timestamps, permissions.  To view metadata, use ``ls
-l`` or ``stat``.

Filesystem performance can be measured by both IOPS (input-output
operations per second) and stream I/O speed.  ``/usr/bin/time -v`` can
give you some hints here.  You can see the :doc:`profiling
<../usage/profiling>` page for more information.



Think about I/O before you start! - General notes
-------------------------------------------------

When people think of computer speed, they usually think of CPU speed.
But this is missing an important factor: How fast can data get to the
CPU?  In many cases, input/output (IO) is the true bottleneck and
must be considered just as much as processor speed.  **In fact,
modern computers and especially GPUs are so fast that it becomes very easy
for a few GPUs with bad data access patterns to bring the cluster down for
everyone.**

The solution is similar to how you have to consider memory: There are
different types of filesystems with different tradeoffs between speed,
size, and performance, and you have to use the right one for the right
job.  Often times.  So you have to use several in tandem: For example,
store original data on **archive**, put your working copy on
**scratch**, and maybe even make a per-calculation copy on **local
disks**.  Check out `wikipedia:Memory Hierarchy`__ and `wikipedia:List of
interface bit rates`__.

__ https://en.wikipedia.org/wiki/Memory_hierarchy
__ https://en.wikipedia.org/wiki/List_of_interface_bit_rates

The following factors are useful to consider:

-  How much I/O are you doing in the first place?  Do you continually re-read the
   same data?
-  What's the pattern of your I/O and which filesystem is best for it?  If
   you read all at once, scratch is fine. But if there are many small
   files or random access, local disks may help.
-  Do you write log files/checkpoints more often than is needed?
-  Some programs use local disk as swap-space. Only turn on if you know
   it is reasonable.

There's a checklist in the :doc:`storage details page
<../usage/storage>`.

Avoid many small files! Use a few big ones instead. (we have a
:doc:`dedicated page <../usage/smallfiles>` on the matter)



Available data storage options
------------------------------

Each storage location has different sizes, speed, types of backups,
and availability.  You need to balance between these.

.. include:: ../ref/storage.rst

Home directories
~~~~~~~~~~~~~~~~
The place you start when you log in.  Home directory should be used for init files,
small config files, etc.  It is however not suitable for storing calculation data.
Home directories are backed up daily.  You usually want to use scratch instead.

scratch and work: Lustre
~~~~~~~~~~~~~~~~~~~~~~~~
Scratch is the big, high-performance, 2PB Triton storage.  It is the primary
place for calculations, data analyzes etc. It is not backed up but is
reliable against hardware failures (RAID6, redundant servers), but
*not* safe against human error..  It is
shared on all nodes, and has very fast access.  It is divided into two
parts, **scratch (by groups)** and **work (per-user)**.  In general, always
change to ``$WRKDIR`` or a group ``scratch`` directory when you first
log in and start doing work. (note: home and work may be deleted six
months after your account expires: use a group-based space instead).

Lustre separates metadata and contents onto separate object and
metadata servers.  This allows fast access to large files, but induces
a larger overhead than normal filesystems.  See our :doc:`small
files <../usage/smallfiles>` page for more information.

See :doc:`../usage/lustre`

Local disks
~~~~~~~~~~~
Local disks are on each node separately.  It is used for the fastest I/Os
with single-node jobs and is cleaned up after job is finished.  Since 2019,
things have gotten a bit more complicated given that our newest (skl) nodes
don't have local disks.  If you want to ensure you have local storage,
submit your job with ``--gres=spindle``.

See the :doc:`Compute
node local drives <../usage/localstorage>` page for further details and script
examples.

ramfs - fast and highly temporary storage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**On login nodes only**,
``$XDG_RUNTIME_DIR`` is a ramfs, which means that it looks like files
but is stored only in memory.  Because of this, it is extremely fast,
but has no persistence whatsoever.  Use it if you have to make small
temporary files that don't need to last long.  Note that this is no
different than just holding the data in memory, if you can hold in
memory that's better.

Other Aalto data storage locations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Aalto has other non-Triton data storage locations available.  See
:doc:`/aalto/aaltostorage` and :doc:`/aalto/aaltodata` for more info.



Quotas
------

All directories under ``/scratch`` (as well as ``/home``) have quotas. Two
quotas are set per-filesystem: disk space and file number.

Disk quota and current usage are printed with the command ``quota``.
'space' is for the disk space and 'files' for the total number of files
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

If you get a quota error, see the :doc:`quotas <../usage/quotas>`
page for a solution.



Data availability throughout Aalto
----------------------------------

Data is the basis of almost everything we do, and accessing it
seamlessly throughout Aalto is a great benefit.  Various other Aalto
systems have the data available.  However, this varies per department:
each department can manage its data as it likes.  So, we can't make
general promises about what is available where.


Linux shell server mounts require a valid Kerberos ticket (usually
generated when you log in). On long sessions these might expire, and
you have to renew them with ``kinit`` to keep going.  If you get a
permission denied, try ``kinit``.


vdi.aalto.fi
~~~~~~~~~~~~

`vdi.aalto.fi <https://vdi.aalto.fi>`__ has scratch mounted at ``/m/triton/scratch/``.
Your work folder can be access at ``/m/triton/scratch/work/USERNAME``. For SCI departments the
standard paths you have on your workstations are also working ``/m/{cs,nbe}/{scratch,work}/``.  

Shell servers
~~~~~~~~~~~~~

Departments have various shell servers, see below.  There isn't a
generally available shell server anymore.

NBE
~~~

On workstations, work directories are available at ``/m/nbe/work`` and group scratch
directories at ``/m/nbe/scratch/$project/``, including the shell
server ``amor.org.aalto.fi``.

PHYS
~~~~

Directories available on demand through SSHFS. See the `Data
transferring <https://wiki.aalto.fi/display/TFYintra/Data+transferring>`__ page
at PHYS wiki.

CS
~~

On workstations, work directories are available at ``/m/cs/work/``, and group scratch
directories at ``/m/cs/scratch/$project/``.  The department shell
server is ``magi.cs.aalto.fi`` and has these available.


.. _remote_access_to_data:
Remote access
-------------

There are many ways to access Triton data remotely.  These days, we
recommending figuring out how to **mount** the data remotely, so that
it appears as local data but is accessed over the network.  This saves
copying data back and forth and is better for data security, but is
slower and less reliable than local data.

Remote mounting using SMB
~~~~~~~~~~~~~~~~~~~~~~~~~

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
* Windows 10: In the "File Explorer", go to "This PC" → "Computer"
  menu at the top → "Map Network Drive".  Use the URLs above but
  replace ``smb://`` with ``\\`` and ``/`` with ``\``.  For example,
  ``\\data.triton.aalto.fi\scratch\``.
* Mac: Finder → Go → Connect to Server.  Use the ``smb://`` URLs above.
* From Aalto managed computers, you can use ``lgw01.triton.aalto.fi``
  instead of ``data.triton.aalto.fi`` and it might auto-login.

Depending on your OS, you may need to use either your username
directly or ``AALTO\username``.

.. warning::

   In the future, you will only be able to do this from Aalto managed
   computers.  This remote mounting will really help your work, so we
   recommend you to request an Aalto managed computer (citing this
   section) to make your work as smooth as possible (or use
   vdi.aalto.fi, see below.


Remote mounting using SFTP (Linux and Mac)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can use sftp and one of the shell servers to mount triton directly to your machine.
Easiest is to set up your ssh config (``.ssh/config``) on your machine as follows (replace ``USERNAME`` by your username):

::

    Host kosh
        User USERNAME
        Hostname kosh.aalto.fi
    	
    Host triton_via_kosh	
        User USERNAME
        Hostname triton.aalto.fi
        ProxyJump kosh    


Instead of ``kosh``, you can also use ``taltta`` or any other shell server (see :doc:`Remote Access <../../aalto/remoteaccess>`) as a proxy to jump the firewall.
You can now open a graphic file manager that supports the sftp protocol (e.g. Files on Aalto Linux), and open:

``sftp://triton_via_kosh``


which will direct you to the root folder of triton. To access scratch use:


``sftp://triton_via_kosh/scratch``


And to access your home folder use:

``sftp://triton_via_kosh/home/USERNAME``




Via `vdi.aalto.fi <https://vdi.aalto.fi>`__
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is more like remote working, not remote access, but is useful
here anyway.  It doesn't provide easy ways to upload/download files.

vdi.aalto.fi (described under :doc:`connecting`) has Triton
directories mounted (see below).

Note: work directories can be accessed via
``/m/triton/scratch/work/``.


Remote mounting using sshfs
~~~~~~~~~~~~~~~~~~~~~~~~~~~

``sshfs`` is a neat program that lets you mount remote filesystems via
ssh only.  It is well-supported in Linux, and somewhat on other
operating systems.  Its true advantage is that you can mount any
remote ssh server - it doesn't have to be set up specially for SMB or
any other type of mounting.  On Ubuntu, you can mount by "File → Connect to
server" and using ``sftp://triton.aalto.fi/scratch/work/USERNAME``.
This also works from any shell server with data (see previous section).

The below uses command line programs to do the same, and makes the
``triton_work`` on your local computer access all files in
``/scratch/work/USERNAME``.  Can be done with other folders.::

    mkdir triton_work
    sshfs USERNAME@triton.aalto.fi:/scratch/work/USERNAME triton_work

Note that ``ssh`` binds together many ways of accessing Triton, with a
similar syntax and options.  ``ssh`` is a very important program and
binds together all types of remote access, and learning to use it well
will help you for a long time.  Learn more about ssh on :doc:`the ssh
page </scicomp/ssh>`.

For Aalto Linux workstation users: it is recommended that you mount ``/scratch/``
under the local disk ``/l/``. You should be able to create the subfolder folder under ``/l/`` 
and point sshfs to that subfolder as in the example here above.


Using sftp
~~~~~~~~~~

The *SFTP* protocol uses ssh to transfer files.  On Linux and Mac, the
``sftp`` command line program are the must fundamental way to do this,
and are available everywhere.

A more user-friendly way of doing this (with a nice GUI) is the
`Filezilla program <https://filezilla-project.org/>`__. Make sure you are using
`Aalto VPN <https://www.aalto.fi/en/services/establishing-a-remote-connection-vpn-to-an-aalto-network>`__, then
you can put triton.aalto.fi as SFTP server with port 22.

Below is an example of the "raw" SFTP usage::

    # Copying from HOME to local PC
    user@pc123 $ sftp user12@triton.aalto.fi:filename
    Connected to triton.aalto.fi.
    Fetching /home/user12/filename to filename
    # copying to HOME
    user@pc123 $ sftp -b - user12@triton <<< 'put testCluster.m'
    sftp> put foo
    # copying to WRKDIR
    user@pc123 $ sftp -b - user12@triton:/scratch/work/USERNAME/ <<< 'put testCluster.m'
    ...

With all modern OS it is also possible to just open your OS file manager (e.g. Nautilus on Linux) and just put as address in the bar::

    sftp://triton.aalto.fi

If you are connecting from remote and cannot use the VPN, you can connect instead to department machines like kosh.aalto.fi, amor.org.aalto.fi (for NBE). The port is 22. *Note:* If you do not see your shared folder, you need to manually specify the full path (i.e. the folder is there, just not yet visible).

.. _rsync_data_transfer:

Using rsync
~~~~~~~~~~~

Rsync is similar to sftp, but is smarter at restarting files.  Use rsync
for large file transfers.  ``rsync`` actually uses the ssh protocol so
you can ``rsync`` from anywhere you can ``ssh`` from. ``rsync`` is installed
by default on Linux and Mac terminals. On Windows machines we recommend using `GIT-bash <https://gitforwindows.org/>`__.

While there are better places on the internet to read about rsync, it is good
to try it out to sychronise a local folder on your triton's scratch. Sometimes
the issue with copying files is related to group permissions. This command takes
care of permissions and makes sure that all your local files are identical (= same
MD5 fingerprint) to your remote files::

    rsync -avzc -e "ssh" --chmod=g+s,g+rw --group=GROUPNAME PATHTOLOCALFOLDER USERNAME@triton.aalto.fi:/scratch/DEPT/PROJECTNAME/REMOTEFOLDER/

Replace the bits in CAPS with your own case. Briefly, ``-a`` tries to preserve all attributes of the file, ``-v`` increases verbosity to see what rsync is doing, ``-z`` uses compression, ``-c`` skips files that have identical MD5 checksum, ``-e`` specifies to use ssh (not necessary but needed for the commands coming after), ``--chmod`` sets the group permissions to shared (as common practice on scratch project folders), and ``--group`` sets the groupname to the group you belong to (note that GROUPNAME == PROJECTNAME on our scratch filesystem).

If you want to just check that your local files are different from the remote ones, you can run rsync in "dry run" so that you only see what the command would do, without actually doing anything.::

    rsync --dry-run -avzc ...

Sometimes you want to copy only certain files. E.g. go through all folders, consider only files ending with ``py``::

    rsync -avzc --include '*/' --include '*.py' --exclude '*' ...

Sometimes you want to copy only files under a certain size (e.g. 100MB)::

   rsync -avzc --max-size=100m ...

Rsync does NOT delete files by default, i.e. if you delete a file from the local folder, the remote file will not be deleted automatically, unless you specify the ``--delete`` option.

Please note that when working with files containing code or simple text, git is a better option to synchronise your local folder with your remote one, because not only it will keep the two folders in sycn, but you will also gain version controlling so that you can revert to previous version of your code, or txt/csv files.




Exercises
---------

**Data storage locations:**

1. (Optional) Look at the list of data storage locations above.  Also look at the
   :doc:`/aalto/aaltostorage`.  Which do you
   think are suitable for your work?  Do you need to share with
   others?  Ask your group what they use and if you can use that, too.

.. note::

   Many of the following exercises don't work out of the box on other
   sites (depends on local files).

**Remote access:**

2. Mount your work directory by SMB - and alternatively sftp or sshfs - and transfer a file to Triton.
   Note that you must be connected to the Aalto VPN (from outside campus), or on ``eduroam``, the ``aalto`` *with Aalto
   laptop* (from campus).

3. (Advanced) If you have a Linux on Mac computer, study the ``rsync``
   manual page and try to transfer a file.


**About filesystem performance:**

``strace`` is a command which tracks **system calls**, basically the
number of times the operating system has to do something.  It can be
used as a rudimentary way to see how much I/O load there is.

4. Use ``strace -c`` to compare the number of system calls in ``ls``,
   ``ls -l``, ``ls --no-color``, and ``ls --color``.  You can use the directory
   ``/scratch/scip/lustre_2017/many-files/`` as a place with many
   files in it.  How many system calls per file were there for each
   option?

5. Using ``strace -c``, compare the times of ``find`` and ``lfs find``
   on the directory mentioned above.  Why is it different?

6. (Advanced, requires slurm knowledge from future tutorials)  You
   will find some sample files in ``/scratch/scip/hpc-examples/io``.
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

**Misc:**

7. What do all of the following have in common?

   a) A job is submitted but fails with no output or messages.

   b) I can't start a Jupyter server on jupyter.triton.

   c) Some files are randomly empty.  Or the file had content, I tried
      to save it again, and now it's empty!

   d) I can't log in.

   e) I can log in with ssh, but ``ssh -X`` doesn't work for graphical programs.

   f) I get an error message about corruption, such as
      ``InvalidArchiveError("Error with archive ... You probably need
      to delete and re-download or re-create this file.``

   g) I can't install my own Python/R/etc libraries.




What's next?
------------

.. seealso::

   * :doc:`../usage/lustre`
   * :doc:`../usage/localstorage`
   * :doc:`../usage/quotas`
   * :doc:`../usage/smallfiles`
   * If you are doing heavy I/O: :doc:`../usage/storage`

The next tutorial is about :doc:`interactive jobs <interactive>`.
