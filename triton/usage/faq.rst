==========================
Frequently asked questions
==========================

Frequently Asked Questions. The latest are at the beginning.

libcuda.so.1: cannot open shared object file: No such file or directory
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
You are trying to run a GPU program (using CUDA) on a node without a
GPU (and thus, no ``libcuda.so.1``.  Remember to :doc:`specify that
you need GPUs <../tut/gpu>`


Why are my jobs waiting in the queue with reason AssocGrpMemRunMinutes/AssocGrpCPURunMinutes or such
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Accounts are limited in how much the can run at a time, in order to
prevent a single or a few users from hogging the entire cluster with
long-running jobs if it happens to be idle (e.g. after a service break).
The limit is such that it limits the maximum remaining runtime of all
the jobs of a user. So the way to run more jobs concurrently is to run
shorter and/or smaller (less CPU's, less memory) jobs. For an in-depth
explanation see
http://tech.ryancox.net/2014/04/scheduler-limit-remaining-cputime-per.html
and for a graphical simulator you can play around with:
https://rc.byu.edu/simulation/grpcpurunmins.php . You can see the
exact limits of your account with

::

    sacctmgr -s show user $USER format=user,account,grptresrunmins%70

Why are my jobs in state "launch failed requeued held"
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Slurm is configured such that if a job fails due to some outside reason
(e.g. the node where it's running fails rather than the job itself
crashing due to a bug in the job) the job is requeued in a held state.
If you're sure that everything is ok again you can release the job for
scheduling with "scontrol release JOBID". If you don't want this
behavior (i.e. you'd prefer that such failed jobs would just disappear)
then you can prevent the requeuing with

::

    #SBATCH --no-requeue

Invalid account ... error message
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

While submitting a job you receive an error message like

::

    sbatch: error: Batch job submission failed: Invalid account or account/partition combination specified

Most probably your account is missing from SLURM database, to check it
out run

::

    $ sacctmgr show user $USER
          User   Def Acct     Admin 
    ---------- ---------- --------- 
      YOUR_LOGIN     YOUR_DEPART      None

That should return your login and associated department/school. If
empty, please contact your `local support team <../help>`
member and ask to add your account to SLURM db.

How can I find out the remaining runtime of my job/allocation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can find out the remaining time of any job that is running with

::

    squeue -h -j  -o %L

Inside a job script or *sinteractive* session you can use the
environment variable SLURM\_JOB\_ID to refer to the current job ID.

``Disk quota exceeded`` error but I have plenty of space
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Main article: `Triton Quotas <quotas>`

Everyone should have a group quota, but no user quota. All files need to
be in a proper group (either a shared group with quota, or your "user
private group"). First of all, use the 'quota' command to make sure that
neither disk space nor number of files are exceeded. Also, make sure
that you use $WRKDIR for data and not $HOME. If you actually need more
quota, ask us.

*Solution:* add to your main directory and all your subdirectories to
the right group, and make sure all directories have the group s-bit set,
(SETGID bit, see ``man chmod``). This means "any files created within
this directory get the directory's group". Since your default group is
"domain users" which has no quota, if the s-bit is not set, you get an
immediate quota exceeded by default.

::

    # Fix everything
    #  (only for $WRKDIR or group directories, still in testing):
    /share/apps/bin/quotafix -sg --fix /path/to/dir/

    # Manual fixing:
    # Fix sticky bit:
    lfs find $WRKDIR -type d --print0 | xargs -0 chmod g+s
    # Fix group:
    lfs find /path/to/dir  ! --group $GROUP -print0 | xargs -0 chgrp $GROUP

*Why this happens:* $WRKDIR directory is owned by the user and user's
group that has the same name and GID as UID. Quota is set per group, not
per user. That is how it was implemented since 2011 when we got Lustre
in use. Since spring 2015 Triton is using Aalto AD for the
authentication which sets everyone a default group ID to 'domain users'.
If you copy anything to $WRKDIR/subdirectory that has no +s bit you copy
as a 'domain users' member and file system refuses to do so due to no
quota available. If g+s bit is set, all your directories/files
copied/created will get the directory's group ownership instead of that
default group 'domain users'. There can be very confusing interactions
between this and user/shared directories.

My $WRKDIR is not visible on my department computer
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Most likely your Kerberos ticket has expired. If you log in with a
password or use 'kinit', you can get an another ticket. See page on
`data storage <../tut/storage>` for more information.

While copying to $WRKDIR with rsync or cp I'm getting 'Disk quota exceeded' error, though my quota is fine.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

It is related to the above mentioned issue, something like rsync -a ...
or cp -p ... are trying to save original group ownership attribute,
which will not work. Try this instead:

::

    ## mainly one should avoid -g (as well as -a) that preserves group attributes
    $ rsync -urlptDxv --chmod=Dg+s somefile triton.aalto.fi:/path/to/work/directory

    ## avoid '-p' with cp, or if you want to keep timestapms, mode etc, then use '--preserve='
    $ cp -r --preserve=mode,timestamps  somefile /path/to/mounted/triton/work/directory

Can I change zsh to bash?
^^^^^^^^^^^^^^^^^^^^^^^^^

Yes. Change shell to your Aalto account and re-login to Triton to get
your newly changed shell to work. For Aalto account changes one can
login to kosh.aalto.fi, run ``kinit`` first and then run ``chsh``, then
type /bin/bash. To find out what is your current shell, run
``echo $SHELL``

For the record: your default shell is not set by Triton environment but
by your Aalto account.

Job fails due to missed module environment variables.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You have included 'module load module/name' but job still fails due to
missing shared libraries or that it can not find some binary etc. That
is a known ZSH related issue. In your sbatch script please use ``-l``
option (aka ``--login``) which forces bash to read all the
initialization files at /etc/profile.

::

    #!/bin/bash -l
    ...

Alternatively, one can change shell from ZSH to BASH to avoid this
hacks, see the post above.

There seems to be running a lot of jobs in the short queue that has gone for longer than 4 hours. Should that be possible?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

SLURM kills jobs based on the partition's TimeLimit + OverTimeLimit
parameter. The later in our case is 60 minutes. If for instance queue
time limit is 4 hours, SLURM will allow to run on it 4 hours, plus 1
hour, thus no longer than 5 hours. Though OverTimeLimit may vary, don't
rely on it. Partition's (aka queue's) TimeLimit is the one that end user
should take into account when submit his/her job. Time limits per
partiton one can check with ``slurm p`` command.

For setting up exact time frame after which you want your job to be
killed anyway, set ``--time`` parameter when submitting the job. When
the time limit is reached, each task in each job step is sent SIGTERM
followed by SIGKILL. If you run a parallel job, set ``--time`` with
``srun`` as well. See '``man srun'`` and '``man sbatch``' for details.

::

    #SBATCH --time=1:00:00
    ...
     
    srun --time=1:00:00 ...

How can I print my text file to a local department printer?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We don't have local department printers configured anywhere on Triton.
But one can use SSH magic to send a file or command output to a remote
printer. Run from your local workstation, insert the target printer
name:

::

    ... printing text file
    $ ssh user@triton.aalto.fi "cat file.txt" | enscript -P printer_name
    ... printing a PostScript file
    $ ssh user@triton.aalto.fi "cat file.ps" | lp -d printer_name -
    ... printing a man page
    $ ssh user@triton.aalto.fi "man -t sbatch" | lp -d printer_name -

How can I access my Triton files from outside?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Remote mounting
...............

The scratch filesystem can be mounted from inside the Aalto networks
by using ``smb://data.triton.aalto.fi/scratch/``.  For example, from
Nautilus (the file manager) on Ubuntu, use "File" -> "Connect to
server".  Outside Aalto networks, use the Aalto VPN.  If it is not an
Aalto computer, you may need to us ``AALTO\username`` as the username,
and your Aalto password.

Or you can use ``sshfs`` – filesystem client based on SSH. Most Linux workstations
have it installed by default, if not, install it or ask your local IT
support to do it for you. For setting up your SSHFS mount from your
local workstation: create a local directory and mount remote directory
with sshfs

::

    $ mkdir /LOCALDIR/triton
    $ sshfs user1@triton.aalto.fi:/triton/PATH/TO/DIR /LOCALDIR/triton

Replace ``user1`` with your real username and ``/LOCALDIR`` with
a real directory on your local drive. After successful mount, use you
/LOCALDIR ``/triton``  directory as it would be local. To unmount it,
run ``fusermount -u /LOCALDIR/triton``.

PHYS users example, assuming that Triton and PHYS accounts are the same:

::

    $ mkdir /localwrk/$USER/triton
    $ sshfs triton.aalto.fi:/triton/tfy/work/$USER  /localwrk/$USER/triton
    $ cd /localwrk/$USER/triton
    ... (do what you need, and then unmount when there is no need any more)
    $ fusermount -u /localwrk/$USER/triton

**Easy access with Nautilus**

The SSHFS method described above works from any console. Though in case
of Linux desktops, when one has a GUI like Gnome or Unity (read all
Ubuntu users) one may use Nautilus – default file manager -- to mount
remote SSH directory. Click \ ``File -> Connect to Server``\  choose
\ ``SSH``\ , input triton.aalto.fi as a server and directory
\ ``/triton/PATH/TO/DIR``\  you'd like to mount, type your name. Leave
password field empty if you use SSH key. As soon as Nautilus will
establish connection it will appear on the left-hand side below Network
header. Now you may access it as it would be your local directory. To
keep it as a bookmark click on the mount point and press ``Ctrl+D``, it
will appear below Bookmark header on the same menu.

Copying files
.............

If your workstatios has no NFS mounts from Triton (CS and NBE have,
consult with your local admins for exact paths), you may always use
SSH.  Either copy your files from triton to a local directory on your
workstation, like::

    $ sftp user1@triton.aalto.fi:/triton/path/to/dir/* .


How can I copy Triton files from outside of Aalto?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

It is an extension of the previous question. In case you are outside
of Aalto and has neither direct access to Triton nor access to NFS
mounted directories on your directory servers. Say you want to copy
your Triton files to your home workstation. It could be done by
setting up an SSH tunnel to your department SSH server. A few steps to
be done: set tunnel to your local department server, then from your
department server to Triton, and then run any rsync/sftp/ssh command
you want from your client using that tunnel. The tunnel should be up
during whole session.

::

    client: ssh -L9509:localhost:9509 department.ssh.server
    department server: ssh -L9509:localhost:22 triton.aalto.fi
    client: sftp -P 9509 localhost:/triton/own/dir/* /local/dir

Note that port 9509 is taken for example only. One can use any other
available port. Alaternatively, if you have a Linux or Mac OS X machine,
you can setup a "proxy command", so you don't have to do the steps above
manually everytime. On your home machine/laptop, in the file
~/.ssh/config put the lines

::

    Host triton
        ProxyCommand /usr/bin/ssh DEPARTMENTUSERNAME@department.ssh.server "/usr/bin/nc -w 10 triton.aalto.fi 22"
        User TRITONUSERNAME

This creates a host alias "triton" that is proxied via the department
server. So you can copy a file from your home machine/laptop to triton
with a command like:

::

    rsync filename triton:remote_filename


.. _faq-connecttoserveronnode:

I need to connect to some server on a node
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Let's say you have some server (e.g. debugging server, notebook server,
...) running on a node.

Why are my jobs waiting in the queue with reason AssocGrpMemRunMinutes/AssocGrpCPURunMinutes or such
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Accounts are limited in how much the can run at a time, in order to
prevent a single or a few users from hogging the entire cluster with
long-running jobs if it happens to be idle (e.g. after a service break).
The limit is such that it limits the maximum remaining runtime of all
the jobs of a user. So the way to run more jobs concurrently is to run
shorter and/or smaller (less CPU's, less memory) jobs. For an in-depth
explanation see
http://tech.ryancox.net/2014/04/scheduler-limit-remaining-cputime-per.html
and for a graphical simulator you can play around with:
https://rc.byu.edu/simulation/grpcpurunmins.php . You can see the
exact limits of your account with

::

    sacctmgr -s show user $USER format=user,account,grptresrunmins%70

Why are my jobs in state "launch failed requeued held"
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Slurm is configured such that if a job fails due to some outside reason
(e.g. the node where it's running fails rather than the job itself
crashing due to a bug in the job) the job is requeued in a held state.
If you're sure that everything is ok again you can release the job for
scheduling with "scontrol release JOBID". If you don't want this
behavior (i.e. you'd prefer that such failed jobs would just disappear)
then you can prevent the requeuing with

::

    #SBATCH --no-requeue

Invalid account ... error message
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

While submitting a job you receive an error message like

::

    sbatch: error: Batch job submission failed: Invalid account or account/partition combination specified

Most probably your account is missing from SLURM database, to check it
out run

::

    $ sacctmgr show user $USER
          User   Def Acct     Admin 
    ---------- ---------- --------- 
      YOUR_LOGIN     YOUR_DEPART      None

That should return your login and associated department/school. If
empty, please contact your `local support team <../help>`
member and ask to add your account to SLURM db.

How can I find out the remaining runtime of my job/allocation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can find out the remaining time of any job that is running with

::

    squeue -h -j  -o %L

Inside a job script or *sinteractive* session you can use the
environment variable SLURM\_JOB\_ID to refer to the current job ID.

``Disk quota exceeded`` error
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

*Main article: `Triton Quotas <quotas>`\ * *and*

::

    space exceeded but I have plenty of space

Everyone should have a group quota, but no user quota. All files need to
be in a proper group (either a shared group with quota, or your "user
private group"). First of all, use the 'quota' command to make sure that
neither disk space nor number of files are exceeded. Also, make sure
that you use $WRKDIR for data and not $HOME. If you actually need more
quota, ask us.

*Solution:* add to your main directory and all your subdirectories to
the right group, and make sure all directories have the group s-bit set,
(SETGID bit, see ``man chmod``). This means "any files created within
this directory get the directory's group". Since your default group is
"domain users" which has no quota, if the s-bit is not set, you get an
immediate quota exceeded by default.

::

    # Fix everything
    #  (only for $WRKDIR or group directories, still in testing):
    /share/apps/bin/quotafix -sg --fix /path/to/dir/

    # Manual fixing:
    # Fix sticky bit:
    lfs find $WRKDIR -type d --print0 | xargs -0 chmod g+s
    # Fix group:
    lfs find /path/to/dir  ! --group $GROUP -print0 | xargs -0 chgrp $GROUP

*Why this happens:* $WRKDIR directory is owned by the user and user's
group that has the same name and GID as UID. Quota is set per group, not
per user. That is how it was implemented since 2011 when we got Lustre
in use. Since spring 2015 Triton is using Aalto AD for the
authentication which sets everyone a default group ID to 'domain users'.
If you copy anything to $WRKDIR/subdirectory that has no +s bit you copy
as a 'domain users' member and file system refuses to do so due to no
quota available. If g+s bit is set, all your directories/files
copied/created will get the directory's group ownership instead of that
default group 'domain users'. There can be very confusing interactions
between this and user/shared directories.

While copying to $WRKDIR with rsync or cp I'm getting 'Disk quota exceeded' error, though my quota is fine.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

It is related to the above mentioned issue, something like rsync -a ...
or cp -p ... are trying to save original group ownership attribute,
which will not work. Try this instead:

::

    ## mainly one should avoid -g (as well as -a) that preserves group attributes
    $ rsync -urlptDxv --chmod=Dg+s somefile triton.aalto.fi:/path/to/work/directory

    ## avoid '-p' with cp, or if you want to keep timestapms, mode etc, then use '--preserve='
    $ cp -r --preserve=mode,timestamps  somefile /path/to/mounted/triton/work/directory

Can I change zsh to bash?
^^^^^^^^^^^^^^^^^^^^^^^^^

Yes. Change shell to your Aalto account and re-login to Triton to get
your newly changed shell to work. For Aalto account changes one can
login to ``kosh.aalto.fi``, run ``kinit`` first
and then run ``chsh``, then type /bin/bash. To find out what is your
current shell, run ``echo $SHELL``

For the record: your default shell is not set by Triton environment but
by your Aalto account.

Job fails due to missed module environment variables.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You have included 'module load module/name' but job still fails due to
missing shared libraries or that it can not find some binary etc. That
is a known ZSH related issue. In your sbatch script please use ``-l``
option (aka ``--login``) which forces bash to read all the
initialization files at /etc/profile.

::

    #!/bin/bash -l
    ...

Alternatively, one can change shell from ZSH to BASH to avoid this
hacks, see the post above.

There seems to be running a lot of jobs in the short queue that has gone for longer than 4 hours. Should that be possible?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

SLURM kills jobs based on the partition's TimeLimit + OverTimeLimit
parameter. The later in our case is 60 minutes. If for instance queue
time limit is 4 hours, SLURM will allow to run on it 4 hours, plus 1
hour, thus no longer than 5 hours. Though OverTimeLimit may vary, don't
rely on it. Partition's (aka queue's) TimeLimit is the one that end user
should take into account when submit his/her job. Time limits per
partiton one can check with ``slurm p`` command.

For setting up exact time frame after which you want your job to be
killed anyway, set ``--time`` parameter when submitting the job. When
the time limit is reached, each task in each job step is sent SIGTERM
followed by SIGKILL. If you run a parallel job, set ``--time`` with
``srun`` as well. See '``man srun'`` and '``man sbatch``' for details.

::

    #SBATCH --time=1:00:00
    ...
     
    srun --time=1:00:00 ...

How can I print my text file to a local department printer?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We don't have local department printers configured anywhere on Triton.
But one can use SSH magic to send a file or command output to a remote
printer. Run from your local workstation, insert the target printer
name:

::

    ... printing text file
    $ ssh user@triton.aalto.fi "cat file.txt" | enscript -P printer_name
    ... printing a PostScript file
    $ ssh user@triton.aalto.fi "cat file.ps" | lp -d printer_name -
    ... printing a man page
    $ ssh user@triton.aalto.fi "man -t sbatch" | lp -d printer_name -

How can I access my Triton files from outside?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If your workstatios has no NFS mounts from Triton (CS and NBE have,
consult with your local admins for exact paths), you may always use
SSH.  Either copy your files from triton to a local directory on your
workstation, like

::

    $ rsync -pr user1@triton.aalto.fi:/triton/path/to/dir .

or use SSHFS – filesystem client based on SSH. Most Linux workstations
have it installed by default, if not, install it or ask your local IT
support to do it for you. For setting up your SSHFS mount from your
local workstation: create a local directory and mount remote directory
with sshfs

::

    $ mkdir /LOCALDIR/triton
    $ sshfs user1@triton.aalto.fi:/triton/PATH/TO/DIR /LOCALDIR/triton

Replace \ ``user1``\  with your real username and \ ``/LOCALDIR``\  with
a real directory on your local drive. After successful mount, use you
/LOCALDIR\ ``/triton``\  directory as it would be local. To unmount it,
run \ ``fusermount -u /LOCALDIR/triton``\  .

PHYS users example, assuming that Triton and PHYS accounts are the same:

::

    $ mkdir /localwrk/$USER/triton
    $ sshfs triton.aalto.fi:/triton/tfy/work/$USER  /localwrk/$USER/triton
    $ cd /localwrk/$USER/triton
    ... (do what you need, and then unmount when there is no need any more)
    $ fusermount -u /localwrk/$USER/triton

**Easy access with Nautilus**

The SSHFS method described above works from any console. Though in case
of Linux desktops, when one has a GUI like Gnome or Unity (read all
Ubuntu users) one may use Nautilus – default file manager -- to mount
remote SSH directory. Click \ ``File -> Connect to Server``\  choose
\ ``SSH``\ , input ``triton.aalto.fi`` as a
server and directory \ ``/triton/PATH/TO/DIR``\  you'd like to mount,
type your name. Leave password field empty if you use SSH key. As soon
as Nautilus will establish connection it will appear on the left-hand
side below Network header. Now you may access it as it would be your
local directory. To keep it as a bookmark click on the mount point and
press ``Ctrl+D``, it will appear below Bookmark header on the same menu.

How can I copy Triton files from outside of Aalto?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

It is an extension of the previous question. In case you are outside
of Aalto and has neither direct access to Triton nor access to NFS
mounted directories on your directory servers. Say you want to copy
your Triton files to your home workstation. It could be done by
setting up an SSH tunnel to your department SSH server. A few steps to
be done: set tunnel to your local department server, then from your
department server to Triton, and then run any rsync/sftp/ssh command
you want from your client using that tunnel. The tunnel should be up
during whole session.

::

    client: ssh -L9509:localhost:9509 department.ssh.server
    department server: ssh -L9509:localhost:22 triton.aalto.fi
    client: sftp -P 9509 localhost:/triton/own/dir/* /local/dir

Note that port 9509 is taken for example only. One can use any other
available port. Alaternatively, if you have a Linux or Mac OS X machine,
you can setup a "proxy command", so you don't have to do the steps above
manually everytime. On your home machine/laptop, in the file
~/.ssh/config put the lines

::

    Host triton
        ProxyCommand /usr/bin/ssh DEPARTMENTUSERNAME@department.ssh.server "/usr/bin/nc -w 10 triton.aalto.fi 22"
        User TRITONUSERNAME

This creates a host alias "triton" that is proxied via the department
server. So you can copy a file from your home machine/laptop to triton
with a command like:

::

    rsync filename triton:remote_filename

I need to connect to some server on a node
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Let's say you have some server (e.g. debugging server, notebook server,
...) running on a node. As usual, you can do this with ssh using port
forwarding. It is the same principle as in several of the above
questions.

For example, you want to connect from your own computer to port ``AAAA``
on node ``nnnNNN``. You run this command:

::

    ssh -L BBBB:nnnNNN:AAAA username@triton.aalto.fi

Then, when you connect to port ``BBBB`` on your own computer
(``localhost``, it gets forwarded straight to port ``AAAA`` on node
``nnnNNN``. Thus only one ssh connection gets us to any node. It is
possible for ``BBBB`` to be the same as ``AAAA``. By the way, this works
with any type of connection. The node has to be listening on any
interface, not just the local interface. To connect to
``localhost:AAAA`` on a node, you need to repeat the above steps twice
to forward from workstation->login and login->node, with the second
``nnnNNN`` being ``localhost``.

Why all of the files on triton cluster are in one color? How can I make them colorful? Like green for execution files, blue for folds
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

That is made intentionally due to high load on Lustre filesystem. Being
a high performance filesystem Lustre still has its own bottlenecks, and
one of the common Lustre troublemakers are ``ls -lr`` or ``ls --color``
which generate lots of requests to Lustre meta servers which regular
usage by all users may get whole system in stuck. Please follow the
recommendations given at the last section at :doc:`Data storage on the Lustre
file system <lustre>`

How do I subscribe to triton-users maillist?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Having a user account on Triton also means being on the
triton-users at aalto.fi mailist. That is where support team sends
all the Triton related announcements. All the Triton users MUST be
subscibed to the list. It is automatically kept up to date these days,
but just in case you are not yet there, please send
an email to your local team member and ask to add your email.

How to unsubscribe? You will be removed from the maillist as soon as
your Triton account is deleted from the system. Otherwise no way,
since we can't notify about urgent things that affect data integrity
or other issues.

I can't save anything to my ``$HOME`` directory, get some fsync error.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Most probably your quota has exceeded, check it out with ``quota``
command.

``quota`` is a wrapper at ``/usr/local/bin/quota`` on front end which
merges output from classic quota utility that supports NFS and Lustre's
``lfs quota``. NFS ``$HOME`` directory is limited to 10GB for everyone
and intended for initialization files mainly. Grace period is set to 7
days and "hard" quota is set to 11GB, which means you may exceed your
10GB quota by 1GB and have 7 days to go below 10GB again. However none
can exceed 11GB limit.

Note: Lustre mounted under ``/triton`` is the right place for your
simulation files. It is fast and has large quotas.

What node names like cn[01-224] mean?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

All the hardware delivered by the vendor has been labeled with some
short name. In particular every single compute node has a label like
Cn01 or GPU001 etc. we used this notation to name compute nodes, that is
cn01 is just a hostname for Cn01, gpu001 is a hostname for GPU001 etc.
Shorthands like cn[01-224] mean all the hostnames in the range cn01,
cn02, cn03 .. cn224. Same for gpu[001-008], tb[003-008], fn[01-02].
Similar notations can be used with SLURM commands like:

::

    $ scontrol show node cn[01-12]

What is a good scaling factor for parallel applications? What is the recommended number of processors for parallel jobs?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

| The good scaling factor is 1.5 or higher. It means that your program
  is running 1.5 times faster when you double the number of nodes.
| There is no way to know in advance the exact "universal" optimal
  number of CPUs. It dependes on many factors, like the application
  itself, type of MPI libraries, the initial input, I/O volume and the
  current network state. Certainly, you must not expect that, as many
  CPUs your application has got, that faster it will run. In general the
  scaling on Triton is good since we have Infiniband for nodes
  interconnect and DDN / Lustre for I/O.

Few recommendations about CPU number:

-  benchmark your applications on different number of CPU cores 1, 2,
   12, 24, 36, and larger. Check out with the developers, your
   application may have ready scalability benchmarks and recommendations
   for compiler, MPI libraries choice.
-  benchmark on shared memory i.e. up to 12 CPU cores within one node
   and then on different nodes (distributed memory): involving
   interconnect make have huge difference
-  if you are not sure about program scalability and you have no time
   for testing, don't run on more than 12 CPU cores within one node
-  be considerate! it is not you against others! do not try to fill up
   the cluster just for being cool

Can you recovery some files from my ``$HOME`` or ``$WRKDIR`` directory?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Short answer: yes for $HOME directory and no for $WRKDIR.

| $HOME is slow NFS with small quota mounted through Ethernet. Intended
  mainly for user initialization files and for some plain configs. We
  make regular backups from ``$HOME``.
| ``$WRKDIR`` (aka ``/triton``) is fast Lustre, has large quota, mounted
  through InfiniBand. Though no backups made from ``/triton``, the DDN
  storage system as such is secure and safe place for your data, though
  you can always loose your data deleting them by mistake. Every user
  must take care about his work files himself. We provide as much
  diskspace to every user, as one needs and the amount of data is
  growing rapidly. That is the reason why the user should manage his
  important data himself. Consider backups of your valuable data on
  DVDs/ USB drives or other resources outside of Triton.

The cluster has a few compiler sets. Which one I suppose to use? What are the limits for commercial compilers?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Currently there are two different sets of compilers: (i) GNU compilers,
native for Linux, installed by default, (ii) Intel compilers plus MKL, a
commercial suite, often the fastest compiler on Xeons.

FGI provides all FGI sites with 7 Intel licenses, thus only 7 users can
compile/link with Intel at once.

Code is compiled with shared libraries and it stops with an error message: ``error while loading shared libraries: libsome.so: cannot open shared object file: No such file or directory``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

That means your program can't find libraries which has been used at
linking/compiling time. You may always check shared library
dependencies:

::

    $ ldd YOUR_PROGRAM # print the list of libraries required by program

| If some of libraries is marked as not found, then you should first (i)
  find the exact path to that lib (suppose it is installed), then second
  (ii) explicitly add it to your environment variable
  $LD\_LIBRARY\_PATH.
| For instance, if your code has been previously compiled with the
  ``libmpi.so.0`` but on SL6.2 it reports an error like
  ``error while loading shared libraries: libmpi.so.0`` try to locate
  the library:

::

    $ locate libmpi.so.0
    /usr/lib64/compat-openmpi/lib/libmpi.so.0
    /usr/lib64/compat-openmpi/lib/libmpi.so.0.0.2

and the add it to your ``$LD_LIBRARY_PATH``

::

    export LD_LIBRARY_PATH=/usr/lib64/compat-openmpi/lib:$LD_LIBARY_PATH # export the lib in BASH environment

or, as in case of ``libmpi.so.0`` we have ready
module config, just run

::

    module load compat-openmpi-x86_64

In case your code is missing some specific libs, not installed on Triton
(say you got a binary compiled from somewhere else), you have a few
choices: (i) get statically linked program or (ii) find/download missing
libs (for instance from developers' site). For the second, copy libs to
your $WRKDIR and add paths to ``$LD_LIBRARY_PATH``, in the same maner as
described above.

See also:

::

    ldconfig -p # print the list of system-wide available shared libraries

While compiling should I use static or shared version of some library?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

One can use both, though for shared libs all your linked libs must be
either in your ``$WRKDIR`` in ``/shared/apps`` or must be installed by
default on all the compute nodes like vast majority of GCC and other
default Linux libs.

I've got a binary file, may I find out somehow whether it is 32-bit or 64-bit compiled?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Use ``file`` utility:

::

    # file /usr/bin/gcc
    /usr/bin/gcc: ELF 64-bit LSB executable, AMD x86-64, version 1 (SYSV),
    for GNU/Linux 2.4.0, dynamically linked (uses shared libs), not stripped

it displays the type of an executable or object file.


Graphical programs don't work (X11, -X)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
In order for graphical programs on Linux to work, a file
``~/.Xauthority`` has to be written.  If your home directory quota
(check with ``quota``) is exceeded, then this can't be written and
graphical programs can't open.  If your quota is exceeded, clean up
some files, close connections, and log in again.  You can find where
most of your space goes with ``du -h $HOME | sort -hr | less``.

This is often the case if you get ``X11 connection rejected because of
wrong authentication``.
