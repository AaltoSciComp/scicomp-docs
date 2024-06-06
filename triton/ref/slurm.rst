.. csv-table::
   :header-rows: 1
   :delim: |

   Command                | Description
   ``sbatch``             | submit a job to queue (see standard options below)
   ``srun``               | Within a running job script/environment: Run code using the allocated resources (see options below)
   ``srun``               | On frontend: submit to queue, wait until done, show output. (see options below)
   ``sinteractive``       | Submit job, wait, provide shell on node for interactive playing (X forwarding works, default partition interactive).  Exit shell when done. (see options below)
   ``srun --pty bash``    | (advanced) Another way to run interactive jobs, no X forwarding but simpler.  Exit shell when done.
   ``scancel`` *JOBID*  | Cancel a job in queue
   ``salloc``             | (advanced) Allocate resources from frontend node.  Use ``srun`` to run using those resources, ``exit`` to close shell when done (see options below)
   ``scontrol``           | View/modify job and slurm configuration


.. csv-table::
   :header-rows: 1
   :delim: !

   Command                  ! Option                          ! Description
   ``sbatch``/``srun``/etc  ! ``-t``, ``--time=``\ *HH:MM:SS* ! **time limit**
                            ! ``-t, --time=``\ *DD-HH*        ! **time limit, days-hours**
                            ! ``-p, --partition=``\ *PARTITION*! **job partition.  Usually leave off and things are auto-detected.**
                            ! ``--mem-per-cpu=``\ *N*         ! **request n MB of memory per core**
                            ! ``--mem=``\ *N*                 ! **request n MB memory per node**
                            ! ``-c``, ``--cpus-per-task=``\ *N*  ! **Allocate *n* CPU's for each task. For multithreaded jobs. (compare ``--ntasks``: ``-c`` means the number of cores for each process started.)**
                            ! ``-N``, ``--nodes=``\ *N-M*        ! allocate minimum of n, maximum of m nodes.
                            ! ``-n``, ``--ntasks=``\ *N*         ! allocate resources for and start *n* tasks (one task=one process started, it is up to you to make them communicate. However the main script runs only on first node, the sub-processes run with "srun" are run this many times.)
                            ! ``-J``, ``--job-name=``\ *NAME*    ! short job name
                            ! ``-o`` *OUTPUTFILE*            ! print output into file *output*
                            ! ``-e`` *ERRORFILE*             ! print errors into file *error*
                            ! ``--exclusive``                ! allocate exclusive access to nodes.  For large parallel jobs.
                            ! ``--constraint=``\ *FEATURE*   ! request *feature* (see ``slurm features`` for the current list of configured features, or Arch under the :ref:`hardware list <hardware-list>`).  Multiple with ``--constraint="hsw|skl"``.
                            ! ``--constraint=localdisk``     ! request nodes that have local disks
                            ! ``--array=``\ *0-5,7,10-15*    ! Run job multiple times, use variable ``$SLURM_ARRAY_TASK_ID`` to adjust parameters.
                            ! ``--gres=gpu``                 ! request a GPU, or ``--gres=gpu:``\ *n* for multiple
                            ! ``--mail-type=``\ *TYPE*       ! notify of events: ``BEGIN``, ``END``, ``FAIL``, ``ALL``, ``REQUEUE`` (not on triton) or ``ALL.`` MUST BE used with ``--mail-user=`` only
                            ! ``--mail-user=``\ *YOUR@EMAIL* ! whome to send the email
   ``srun``                 ! ``-N`` *N_NODES* hostname    ! Print allocated nodes (from within script)
