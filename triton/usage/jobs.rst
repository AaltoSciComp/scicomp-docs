===============
Monitoring jobs
===============

Basics
======

Before you start, if you have SLURM experience but new to Triton, you
may want to check out the ``slurm`` command on Triton' paragraph below.
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
-  ``(AssociationResourceLimit)``: The job exceeds some limit set on the
   association. On triton, this in practice means the per-user
   GrpCPURunMins limit, which currently is 1.5M minutes per user. Wait a
   while for running jobs to proceed, so that new jobs may start. Also,
   shorter job time limits help. See `GrpCPURunMins
   visualizer <https://rc.byu.edu/simulation/GrpCPURunMins-Visualizer/index.html>`__
   .

In case of the first two one can check currently estimated time the job
will be started. Run ``slurm j <jobid>``, look at ``StartTime=``

Job states
----------

Possible states for jobs are:

  * PENDING  (PD)
  * RUNNING (R)
  * SUSPENDED (S)
  * COMPLETING (CG)
  * COMPLETED (CD)
  * CONFIGURING (CF)
  * CANCELLED (CA)
  * FAILED (F)
  * TIMEOUT (TO)
  * PREEMPTED  (PR)
  * NODE_FAIL (NF)``.

Modifying the job after submission
----------------------------------

The question asked time to time: "Can one modify job parameters after it
hass been submitted?". The answer is, yes it is possible, but only some
parameters. For instance change memory/CPU requirements for pending job
or set another time limit ofr running/pending job. Think carefully
before you submit a job, but if you ended up in the situation that
modification is needed, please contact your `Triton support team
member <../help>`.

Needless to say that there is no way to impact on your job priority and
make sure that it goes to run asap?

Viewing finished jobs
---------------------

Information about finished and cancelled jobs are available via the
``slurm history`` command. Most notable pieces are memory use and also
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

Output time information is displayed as days-hours:minutes:seconds.

Recognized time forms for the input parameter are *n* min, *n* hours, *n* days, *n* weeks
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

Triton queues are not first-in first-out, but "fairshare".  This means
that every person has a priority.  The more you run the lower your
user priority.  As time passes, your user priority increases again.
The longer a job waits in the queue, the higher its job priority goes.
So, in the long run (if everyone is submitting an never-ending stream
of jobs), everyone will get exactly their share.

Once there are priorities, then: jobs are scheduled in order of
priority, then any gaps are backfilled with any smaller jobs that can
fit in.  So small jobs usually get scheduled fast regardless.

*Warning: from this point on, we get more and more technical, if you
really want to know the details.  Summary at the end.*

What's a share?  Currently shares are based on department and their
respective funding of Triton (``sshare``).  Shares are shared among
everyone in the department, but each person has their own priority.
Thus, for medium users, the 2-week usage of the rest of your
department can affect how fast your jobs run.  However, again, things
are balanced per-user within departments.  (However, one heavy user in
a department can affect all others in that department a bit too much,
we are working on this)

Your priority goes down via the "job billing": roughly time×power.
CPUs are billed at 1/s (but older, less powerful CPUs cost less!).
Memory costs .2/GB/s.  But: you only get billed for the max of memory
or CPU. So if you use one CPU and all the memory (so that no one else
can run on it), you get billed for all memory but no CPU.  Same for
all CPUs and little memory.  This encourages balanced use.  (this also
applies to GPUs).

GPUs also have a billing weight, currently 2/GPU/s for newer models and
1/GPU/s for the older ones.

If you submit a long job but it ends early, you are only billed for
the actual time you use (but the longer job might take longer to start
at the beginning).  Memory is always billed for the full reservation
even if you use less, since it isn't shared.

The "user priority" is actually just a record how much you have
consumed lately (the billing numbers above).  This number goes down
with a half-life decay of 2 weeks.  Your personal priority your share
compared to that, so we get the effect described above: the more you
(or your department) runs lately, the lower your priority.

If you want your stuff to run faster, the best way is to more
accurately specify your time (may make that job can find a place
sooner) and memory (avoids needlessly wasting your priority).

While your job is pending in the queue SLURM checks those metrics
regularly and recalculates job priority constantly.  If you are
interested in details, take a look at `multifactor priority plugin
<https://slurm.schedmd.com/priority_multifactor.html>`__ page (general
info) and `depth-oblivious fair-share factor
<https://slurm.schedmd.com/priority_multifactor3.html>`__ for what we
use specifically (warning: very in depth page).  On Triton, you can
always see the latest billing weights in ``/etc/slurm/slurm.conf``

Numerically, job priorities range from 0 to 2^32-1.  Higher is
sooner to run, but really the number doesn't mean much itself.

These commands can show you information about your user and job
priorities:

.. csv-table::
   :delim: |

   ``slurm s``         | list of jobs per user with their current priorities
   ``slurm full``      | as above but almost all of the job parameters are listed
   ``slurm shares``    | displays usage (RawUsage) and current FairShare weights (FairShare, higher is better) values for all users
   ``slurm j <jobid>`` | shows ``<jobid>`` detailed info including priority, requested nodes etc.

..
   ``slurm p gpu``       |     # shows partition parameters incl. Priority=


tl;dr: Just select the resources you think you need, and slurm
tries to balance things out so everyone gets their share.  The best
way to maintain high priority is to use resources efficiently so you
don't need to over-request.


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

-  ``squeue`` – view information about jobs located in the Slurm
   scheduling queue

   ::

       $ squeue -n gpu[1-22]         # reports only jobs allocated to specific nodes
       $ squeue -t PD -i 5 -u $USER  # reports your pending jobs, with the 5s interval

-  ``sinfo`` – view node & partition information
-  ``sshare`` – show statistics from the accounting database
-  ``scontrol`` – various function, end user mostly interested in
   ``scontrol show`` ...

   ::

       scontrol show node ivb1    # show specific node config

-  ``sprio`` - Show calculated priority factors for jobs waiting in the
   queue
-  ``sacct`` - Historical info about jobs

Customizable output for ``slurm``
---------------------------------

The ``slurm`` command output can be customized. Look in the for variable
names in /usr/local/bin/slurm and place them into your own
$HOME/.config/slurmvars file.

For example, more detailed node info for those interested to know
which kind of machines are free. This changes the look of ``slurm
partitions``.

::

    fmt_s_parts="%10P %.10l %.15F %8f %N"
