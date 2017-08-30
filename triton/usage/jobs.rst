===============
Monitoring jobs
===============

Monitoring jobs
===============

Before you start, if you have SLURM experience but new to Triton, you
may want to check out '``slurm`` command on Triton' paragraph below.
There we introduce Triton specific tool that is widely used for jobs
monitoring and many other issues.

There are two quick ways to see your own jobs. One is to list every job
and their current priority in the queues.

::

    $ slurm q
    PRIORITY  JOBID   PARTITION  NAME      ST  TIME      START_TIME        NODELIST(REASON)
    12971826           batch-wsm DA_vk_400k_5M         0:00              N/A  PENDING (Priority)
    12971825           batch-wsm DA_vk_400k_50M        0:00              N/A  PENDING (Priority)
    12971818           batch-hsw DA_vk_400k_5M         0:06 2016-10-17T15:12  RUNNING ivb28
    12971817           short-ivb update.12.sh          0:06 2016-10-17T15:12  RUNNING ivb13
    12971816           batch-ivb FI_vk_2000k_50        0:07 2016-10-17T15:12  RUNNING ivb28
    ...

But mostly a simple overview will do. Here is the same information as
above, only this time formatted for brevity. The leftmost value is the
combined job count.

::

    $ slurm qq
    1    PARTITION  CPUS  NODES  MIN_MEM  FEATURES  QOS     STATE    REASON
    1    batch-wsm  1     1      4G       ivb|wsm|  normal  PENDING  AssocGrpMemRunMinutes
    1    batch-wsm  1     1      8G       ivb|wsm|  normal  PENDING  AssocGrpMemRunMinutes
    242  batch-wsm  1     1      25G      (null)    normal  PENDING  AssocGrpMemRunMinutes
    2    coin       1     1      4G       (null)    normal  RUNNING  None
    15   batch-wsm  1     1      4G       (null)    normal  RUNNING  None
    2    coin       1     1      4G       (null)    normal  RUNNING  None
    ...

For "watching" your jobs progress, use 'watch' option

::

    slurm watch q

Since the cluster is in heavy use most of the time, there are other
users whose jobs will of course affect what happens with yours. The
state of the entire queue, including running either ``slurm short`` or
``slurm ss``.

::

    slurm s

With the ``s`` or ``short`` option, the output is sorted by priority and
reflects the scheduler's execution order as nodes become available. The
queue position can change at any time, either from new or submissions or
based on historical usage accounting.

You can choose to display the one partition you are interested in:

::

    slurm ss gpu

Show detailed information about running job(s):

::

    slurm j 

Job status while pending
------------------------

There are a number of reasons that your job may be sitting in the queue.
Listing your pending jobs with ``squeue -u $USER -t PD`` will help
determine why your job is not running. Look at the ``NODELIST(REASON)``.
A pending job may have these reasons:

-  ``(Priority)``: Other jobs have priority over your job. Just wait.
-  ``(Resources):`` Your job has enough priority to run, but there
   aren’t enough free resources to run it. Just wait.

-  ``(ReqNodeNotAvail)``: You request something that is not available.
   Check memory requirements per CPU, CPUs per node. Possibly time limit
   is the issue. Could be that due to scheduled maintenance break, all
   nodes are reserved and thus your ``-t`` parameter can't be larger
   than time left till the break.
-  ``(QOSResourceLimit)``: Your job exceeds the QOS limits. The QOS
   limits include wall time, number of jobs a user can have running at
   once, number of nodes a user can use at once, etc. This may or may no
   be a permanent status. If your job requests a wall time greater than
   what is allowed or exceeds the limit on the number of nodes a single
   job can use, this status will be permanent. However, your job may be
   in this status if you currently have jobs running and the total
   number of jobs running or aggregate node usage is at your limits. In
   this case, jobs in this state will become eligible when your existing
   jobs finish.
-  (AssociationResourceLimit): The job exceeds some limit set on the
   association. On triton, this in practice means the per-user
   GrpCPURunMins limit, which currently is 1.5M minutes per user. Wait a
   while for running jobs to proceed, so that new jobs may start. Also,
   shorter job time limits help. See `GrpCPURunMins
   visualizer <https://marylou.byu.edu/simulation/GrpCPURunMins-Visualizer/index.html>`__
   .

In case of the first two one can check currently estimated time the job
will be started. Run ``slurm j <jobid>``, look at ``StartTime=``

Job states
----------

Possible states for jobs are:
``PENDING  (PD), RUNNING (R), SUSPENDED (S), COMPLETING (CG), COMPLETED (CD),  CONFIGURING (CF), CANCELLED (CA), FAILED (F), TIMEOUT (TO), PREEMPTED  (PR), NODE_FAIL (NF)``.

Modifying the job after submission
----------------------------------

The question asked time to time: "Can one modify job parameters after it
hass been submitted?". The answer is, yes it is possible, but only some
parameters. For instance change memory/CPU requirements for pending job
or set another time limit ofr running/pending job. Think carefully
before you submit a job, but if you ended up in the situation that
modification is needed, please contact your `Triton support team
member <../help>`__.

Needless to say that there is no way to impact on your job priority and
make sure that it goes to run asap?

Viewing finished jobs
---------------------

Information about finished and cancelled jobs are available via the
``slurm history `` command. Most notable pieces are memory use and also
exit code, in case the jobs did not finish cleanly.

::

    $ slurm history 2hours
    JobID          JobName    Start             MaxVMem  MaxRes     TotalCPU     Elapsed Tasks CPUs Nodes ExitCode State
    1052748        helloe.sh  2012-04-10T19:05        -       -    00:00.015    00:00:00  none    1     1      1:0 FAILED
     └──batch      *          2012-04-10T19:05        -       -    00:00.015    00:00:00     1    1     1      1:0 FAILED
    1052751        testarr    2012-04-10T19:07        -       -    00:00.074    00:02:30  none    5     1      0:0 COMPLETED
     └──batch      *          2012-04-10T19:07     393M      6M    00:00.055    00:02:30     1    1     1      0:0 COMPLETED
        1052751.0  runtask    2012-04-10T19:07      99M      1M    00:00.002    00:00:30     1    1     1      0:0 COMPLETED
        1052751.1  runtask    2012-04-10T19:08      99M      1M    00:00.003    00:00:30     1    1     1      0:0 COMPLETED
        1052751.2  runtask    2012-04-10T19:08      99M      1M    00:00.003    00:00:30     1    1     1      0:0 COMPLETED
        1052751.3  runtask    2012-04-10T19:09      99M      1M    00:00.003    00:00:30     1    1     1      0:0 COMPLETED
        1052751.4  runtask    2012-04-10T19:09      99M      1M    00:00.003    00:00:30     1    1     1      0:0 COMPLETED

Recognized time forms are *n* min, *n* hours, *n* days, *n* weeks
(without space).

*Elapsed* is the wall clock time from job start to finish.

*MaxVMem* is the highest amount of virtual memory your program allocated
during its lifetime. If the slurm job's memory limit is set below it,
your job would be killed.

*MaxRes* is the resident (physical) memory the program actually used of
its virtual memory allocation, which may be of interest when monitoring
program behavior.

Cancelling jobs
---------------

::

    $ scancel                       # cancel a job
    $ scancel `echo {5205484..5205533}`    # cancel jobs in the range
    $ scancel --state=PENDING --user=$USER --partition=debug  # kill all of your pending jobs on debug queue

Job priority
============

The running job priority in general has many factors to consider. In
addition to job time, requested nodes number and QoS, there are others,
like how much CPU time the user has burn already all together on the
cluster, partition priority, for how long a particular job has been
sitting n the queue and others. While your job is pending in the queue
SLURM checks those metrics regularly and recount job priority constanly.
If you are interested in details, take a look at `Ticket-based
multifactor priority
plugin <https://slurm.schedmd.com/priority_multifactor.html>`__ page,
that is the one we use on Triton for jobs scheduling.

::

    $ slurm s                # list of jobs per user with their current priorities
    $ slurm full             # as above but almost all of the job parameters are listed
    $ slurm shares           # displays usage values per user
    $ slurm p gpu            # shows partition parameters incl. Priority=
    $ slurm j <jobid>        # shows <jobid> detailed info incl. QoS, requested nodes etc.

``slurm`` command on Triton
===========================

A nice tool originally developed by Tapio Leipälä specifically for
Triton user needs and developed by Triton support team nowadays.

The ``slurm`` command can show most often needed information about jobs,
resources and the cluster state. It's a wrapper script to the native
SLURM commands. New features are added from time to time. Running it
without parameters prints a list of available commands. Most have some
soft of shortcuts for convenience.

.. include:: ../ref/slurm_status.rst

Native slurm commands
=====================

While Triton has a ``slurm`` utility that hides most of original SLURM
commands, you still may want to learn more. If need something else that
``slurm`` can not do, the native commands with their full functionality
are at your service. For the details, please consult corresponding man
pages (``man squeue`` , etc).

-  `` squeue ``– view information about jobs located in the Slurm
   scheduling queue

   ::

       $ squeue -n gpu[1-22]         # reports only jobs allocated to specific nodes
       $ squeue -t PD -i 5 -u $USER  # reports your pending jobs, with the 5s interval

-  `` sinfo `` – view node & partition information
-  `` sshare `` – show statistics from the accounting database
-  `` scontrol `` – various function, end user mostly interested in
   ``scontrol show`` ...

   ::

       scontrol show node ivb1    # show specific node config

-  **sprio** - Show calculated priority factors for jobs waiting in the
   queue
-  **sacct** - Historical info about jobs

Customizable output for ``slurm``
---------------------------------

The ``slurm`` command output can be customized. Look in the for variable
names in /usr/local/bin/slurm and place them into your own
$HOME/.config/slurmvars file.

For example, more detailed node info for those interested to know if
either Xeon or Opteron machines are free. This changes the look of
``slurm partitions``.

::

    fmt_s_parts="%10P %.10l %.15F %8f %N"
