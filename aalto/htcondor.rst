========
HTCondor
========

.. note::

    -  SCIP courses: look for `Introduction to distributed computing with
       HTCondor <http://science-it.aalto.fi/scip>`__
    -  HTCondor official manuals: https://research.cs.wisc.edu/htcondor/manual/

Introduction
------------

HTCondor (formerly known as just Condor) is a computing scheduler
developed at University of Wisconsin-Madison. This allows users to run
their binaries on Aalto Linux workstations without explicit logging to
desktop machines. Condor takes care of choosing the right workstation,
setting correct job priority and taking care of cleaning the output.
Condor distributes, schedules, executes and returns the result. So
handmade farming is not needed.

HTCondor status at Aalto and support
------------------------------------

Condor installations are department specific. Here is a list of
departments that have HTCondor software installed on their Ubuntu
workstations.

+-----------------------+------------------------------------+----------------------------------------------------------------+
| Department / school   | Support contact                    | Comments                                                       |
+=======================+====================================+================================================================+
| PHYS & NBE / SCI      | Aalto IT servicedesk *             | joint installation, installed on all the Ubuntu workstations   |
+-----------------------+------------------------------------+----------------------------------------------------------------+
| CS / SCI              | Aalto IT servicedesk *             | installed on all the Ubuntu workstations                       |
+-----------------------+------------------------------------+----------------------------------------------------------------+
| MATH / SCI            | Matti Harjula and Kenrick Bingham  | installed on about 50 newer Ubuntu workstations                |
+-----------------------+------------------------------------+----------------------------------------------------------------+

The instructions below are common to all the departments if not
mentioned otherwise.

\* Getting help: your department IT guys have responsibility over the
HTCondor installation. Best way to reach them is to drop an email to
the Aalto IT servicedesk including info like: your department, Linux
workstation name and type of problem.

HTCondor official manuals
-------------------------

The detailed manual can be found from
https://research.cs.wisc.edu/htcondor/manual/. Current version of Condor we have
can be checked with ``condor_q -version``.

Before you run with Condor
--------------------------

It is recommended that you compile you binary statically. If you have
used shared libs (or you get from someone code that has not been
compiled statically), make sure that you set your environment correctly
and use ``getenv = true`` option in Condor submit script.

No large MPI jobs (over the net) are allowed with Condor. For any large
MPI or multithread job, please either run on your local workstation only
or on other resources like :doc:`Triton <../triton/index>`.

Condor is well suited for short time serial runs (like overnight), or
for small (2-4 CPUs) parallel runs that can be run within one machine.
Long runs (over 12 hours) are possible, but remember that Condor runs on
local workstations, and uses only idle CPU cycles, i.e. some currently
unused workstation during the day and all of them during night. Local
usage is of higher priority and thus submitted Condor job that hurts
local user will be suspended.

Always use ``should_transfer_files = yes`` in your Condor submit script.
This way you make sure that all IOs will go to local directory assigned
to HTCondor on a local worker instead of shared NFS (be it /home or
alike).

Run your code with Condor
-------------------------

-  Discover condor pool status with ``condor_status`` or with
   ``condor_status -available`` to find out which machines are
   available for jobs. This step is to make sure that condor pool is
   available.
-  Compile a statically linked binary.
-  Create a condor submission script, like job\ ``.cond`` below

-  Submit the job to condor pool with ``condor_submit job.cond``
-  Manage your job(s) with ``condor_q``, ``condor_rm``

It may take several minutes for code to start running. Check out
``condor.log`` for any useful log information.

Job script examples
~~~~~~~~~~~~~~~~~~~

CS users should use ``universe = local``

::

    # job_1.cond -- ready to run serial code example

    executable = serial.bin
    universe = vanilla
    output = serial.out
    error = serial.err
    log = condor.log
    should_transfer_files = YES
    queue

::

    # job_2.cond -- Condor serial job submission script example

    # define job specific vars to be used later in this script
    # this should be an absolute path, or path from current working dir
    DIR=myrun

    # setting up base directory for input, output, error and log files, executable path is not affected
    initialdir = $(DIR)

    # Define executable to run, it can be arch specific, or just some generic code
    executable = mycode

    # memory requirements, if any
    #request_memory = 512 MB

    # Condor universe. Default Vanilla, others haven't been configured/tested
    universe = vanilla

    # the file name specified with 'input' should contain any keyboard input the program requires
    # note, that command-line arguments are specified by the 'arguments' command below
    input = input.txt

    # and output files
    # note, that input, output, log and error files will/should be in 'initialdir' directory
    output = $(cluster).out

    # Errors, if any, will go here
    error = $(cluster).err

    # Always define log file, so that you know what haapened to your job(s)
    log = condor.log

    # email for job notifications, when it is completed or finished with errors
    #notify_user = firstname.lastname@aalto.fi
    #notification = Complete
    # Additional environment vars
    #environment = "PATH=$ENV(PATH):/home/user/bin"

    # replicate your current working environment on the worker node
    # useful when you have some specific vars like PATH, LD_LIBRARY_PATH or other defined with 'module'
    getenv = true

    # code arguments, if any
    #arguments = -c cmd_input.conf

    # Trasferring your files to a system the job is going to run on
    # that is the recommended method, to avoid NFS traffic
    should_transfer_files = yes
    transfer_input_files = cmd_input.conf,input.txt
    when_to_transfer_output = ON_EXIT_OR_EVICT

    # Some specific requirements, if any. By default Condor will run job on a machine which has
    # the same architecture and operating system family as the machine from which it was submitted.
    # Here is we want the worker node would be Ubuntu 12.04 with 4 CPU cores or more
    #requirements = (OpSysLongName >= "Ubuntu 12.04") && (TotalCPus >= 4)

    queue

Condor commands
~~~~~~~~~~~~~~~

-  ``condor_q -analyze <condor_job_id>`` # your
   running/pending jobs diagnostics (for all your jobs at once if
   ``job_id`` is missing)
-  ``condor_q -global`` # list all/everyone's jobs at pool
-  ``condor_q -version`` # find out installed condor version
-  ``condor_status -available`` # list available computers for your job
-  ``condor_status -state -total`` # Condor pool resources in total
-  ``condor_status HOSTNAME`` # show status for a specific host
   (HOSTNAME.hut.fi in this case), where number
   of slots gives number of CPU cores available
-  ``condor_status -long vesku`` # show all details for a specific host
-  ``condor_status -constraint 'OpSysLongName>="Ubuntu 12.04"'`` # list
   Ubuntu 12.04 workstations only
-  ``condor_rm <condor_job_id>`` # remove particular job
-  ``condor_rm -all`` # remove all user jobs
-  ``condor_rm -constraint 'JobStatus =!= 2'`` # remove all user jobs
   that are not currently running
-  ``condor_hold <job_id>`` # hold your Condor job(s) in the queue
-  ``condor_release <job_id>`` # release job(s) previously holded in the
   queue
-  (NOTE: doesn't work on Ubuntu, so anywhere at Aalto)
   ``condor_compile`` ``[cc \| f77 \| g++ \| make \| ...]`` #
   relink an executable for checkpointing with Standard universe; not
   installed on Ubuntu 12.04, see Checkpointing section below
-  ``condor_history`` # list the completed jobs submitted from the
   workstation you run this command on

Startup script ``requirements=`` can be always tested with
``condor_status -constraint``. Like in the above ``job_2.cond`` example:

-  ``condor_status -constraint '(OpSysLongName>="Ubuntu 12.04") && (TotalCPus >= 4)' -available``

More commands and their usage examples you can find at `Condor User
Manual <https://research.cs.wisc.edu/htcondor/manual/v7.9/index.html>`__.

Additional "requirements"/"constraints" options that have been
configured on PHYS workstations only: CPUModel, CPUModelName,
TotalFreeMemory. The later one in MB, reports currently available free
memory according to /proc/meminfo. Can be useful for large memory jobs,
see example below.

::

    # ask for machine with more than 4GB of free memory
    requirements = (TotalFreeMemory >= 4000)

Checkpointing and condor\_compile
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

HTCondor has no checkpoitning or remote system calls support on Ubuntu
(according to\ `manual
pages <https://research.cs.wisc.edu/htcondor/manual/v8.0/1_5Availability.html>`__).

HTCondor config
---------------

Machine in considered to be free if: no user activity within 15 min
(keyboard or mouse), average load < 30%, and no condor job already
running.

Running job will be suspended if: local workstation user became active
(on hold) or CPU busy for more than 2 min and job has been running more
than 90 sec.

Suspended job will be resumed if: machine has been free for 5 min.

Suspended job is killed if: it has been suspended for 4 hours (Vanilla
universe) or hasn't completed checkpointing within 10 min (Standard
universe) or higher priority job is waiting in the queue.

Job will be preempted if: it uses more memory than available for its
slot (killed and send back to queue).

FAQ
---

Condor has support on running jobs under shared filesystem. Should I use this?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is a bad idea. Keep using Condor's default local directory
(somewhere on the local harddrive, department specific settings),
otherwise, several jobs using NFS constantly (either home or any other
remotely mounted) would make it really slow. Use

::

    should_transfer_files  = YES
    transfer_input_files   = file1.dat,file2.txt

options instead. Then condor will copy all required (specified) files
to its local spool directory and run jobs locally. Only when finished,
it will return files back to the original submitting directory.  This
original submitting directory should *not* be a NFS mounted directory
such as your home directory, as in the Aalto environment those are
mounted with Kerberos security, and if the Kerberos ticket has expired
because you aren't working on your workstations, condor will not be
able to access this directory and your job results will be lost.

My job is in 'Idle' state, while there are resources available
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Job may take several minutes to start, if it takes longer, check out job
log (defined with ``log =`` directive in the submit script) and then run
``condor_q -analyze <job_id>`` to see possible reasons. More debugging
options at `condor\_q
manual <https://research.cs.wisc.edu/htcondor/manual/v7.9/condor_q.html>`__.

I've copy/pasted example files from this page, but when try to run they produce some errors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Should be this wiki specific. Noticed (with ``cat -A filename``) that
copy/pasted text includes bunch of non-ascii characters.

Got it fixed with ``perl -pi -e 's/[[:^ascii:]] //g' filename``

Additional files/scripts
------------------------

Files that may be useful with condor:

-  ``cq`` – A script that works as ``condor_q``\ but also prints the
   executing host

   ::

       #!/usr/bin/perl

       use POSIX;

       $user=$ENV{'LOGNAME'};
       $now=`date +%s`;
       $now=~s/\n//;

       $str=" -cputime -submitter $user ";
       for $i (0..$#ARGV) {
        $str.=" $ARGV[$i-1]";
       }

       if($ARGV[0] eq "all") {$str=" -global -cputime -currentrun";}
       if($ARGV[0] eq "j") {system("condor_q -global -cputime -currentrun -submitter $user|egrep '(jobs|Schedd)'");exit(0);}
       if($ARGV[0] eq "rm") {$str=`condor_q -submitter $user -format \"%d\\n\" ClusterId|xargs`;print "condor_rm $str";exit(0);}

       foreach(`condor_q -long $str`) {
         s/\n//;
         s/\"//g;

         if(m/^Iwd\s*=\s*(\S+)/) { $iwd=$1; }
         if(m/^RemoteHost\s*=\s*(\S+)/) { $rh=$1; }

         if(m/ServerTime/) {
           $iwd=~s/.*\/(.*\/.*)$/$1/;
           push(@iwds, "$rh\t $iwd");
         }

       }

       foreach(`condor_q $str`) {
         s/\n//;
         if(/^\s*\d+\.\d/) {
           $iwd=shift(@iwds);
           $_.=" ".$iwd;
         }
         print "$_\n";
       }

       sub runtime() {

         my($now, $st)=@_;
         $str=localtime($now-$st-7200);
         $str=~s/\t/ /g;
         $str=~s/^\s*//g;
         $str=~s/\s+/ /g;
         split(/ /,$str);
         $d=$_[2]-1;
         $t=$_[3];

         if($d>0) {$ret="$d+$t";}else{$ret=$t;}

         return $ret;

       }

-  ``turbomole.cond``, ``run_ridft510_condor.scr``– pair of scripts for
   running TurboMole or AMBER (thanks to Markus Kaukonen)

   ::

       # turbomole.cond
       Executable = ./run_ridft510_condor.scr
       Universe = vanilla
       Error = err.$(cluster)
       Output = out.$(cluster)
       Log = log.$(cluster)
       environment = "OMP_NUM_THREADS=1"

       Requirements = Memory > 1000

       should_transfer_files = YES
       when_to_transfer_output = ON_EXIT
       transfer_input_files = run_ridft510_condor.scr, auxbasis, basis, control, coord,
       mos

       #Arguments =
       Queue

   and run\_ridft510\_condor.scr

   ::

       #!/bin/sh
       source /etc/profile
       source /etc/bashrc
       source /etc/profile.d/fyslab-env.sh

       AMBERHOME=${HOME}/bin/Amber10
       TURBODIR=${HOME}/bin/Turbo5.10/

       PATH=$PATH:$TURBODIR/scripts
       PATH=$PATH:$TURBODIR/bin/`sysname`

       export PATH
       export PATH="${AMBERHOME}/exe:${AMBERHOME}/bin:${PATH}"
       export PATH="${HOME}/bin:${PATH}"

       ulimit -s unlimited
       #ulimit -a > mylimits.out

       jobex -ri -c 200 > jobex.out


