.. csv-table::
   :header-rows: 1
   :delim: |

   Command                | Description
   ``sbatch``             | submit a job to queue (see standard options below)
   ``srun``               | Within a running job script/environment: Run code using the allocated resources (see options below)
   ``srun``               | On frontend: submit to queue, wait until done, show output. (see options below)
   ``sinteractive``       | Submit job, wait, provide shell on node for interactive playing (X forwarding works, default partition interactive).  Exit shell when done. (see options below)
   ``srun --pty bash``    | (advanced) Another way to run interactive jobs, no X forwarding but simpler.  Exit shell when done.
   ``scancel`` *<jobid>*  | Cancel a job in queue
   ``salloc``             | (advanced) Allocate resources from frontend node.  Use ``srun`` to run using those resources, ``exit`` to close shell when done. Read :doc:`the description <../usage/general>`! (see options below)
   ``scontrol``           | View/modify job and slurm configuration


.. csv-table::
   :header-rows: 1
   :delim: !

   Command                  ! Option                          ! Description
   ``sbatch``/``srun``/etc  ! ``-t``, ``--time=``\ *hh:mm:ss* ! **time limit**
                            ! ``-t, --time=``\ *dd-hh*        ! **time limit, days-hours**
                            ! ``-p, --partition=``\ *partition*! **job partition.  Usually leave off and things are auto-detected.**
                            ! ``--mem-per-cpu=``\ *n*         ! **request n MB of memory per core**
                            ! ``--mem=``\ *n*                 ! **request n MB memory per node**
                            ! ``-c``, ``--cpus-per-task=``\ *n*  ! **Allocate *n* CPU's for each task. For multithreaded jobs. (compare ``--ntasks``: ``-c`` means the number of cores for each process started.)**
                            ! ``-N``, ``--nodes=``\ *n-m*        ! allocate minimum of n, maximum of m nodes.
                            ! ``-n``, ``--ntasks=``\ *n*         ! allocate resources for and start *n* tasks (one task=one process started, it is up to you to make them communicate. However the main script runs only on first node, the sub-processes run with "srun" are run this many times.)
                            ! ``-J``, ``--job-name=``\ *name*    ! short job name
                            ! ``-o`` *output*                ! print output into file *output*
                            ! ``-e`` *error*                 ! print errors into file *error*
                            ! ``--exclusive``                ! allocate exclusive access to nodes.  For large parallel jobs.
                            ! ``--constraint=``\ *feature*   ! request *feature* (see ``slurm features`` for the current list of configured features, or Arch under the :ref:`hardware list <hardware-list>`).  Multiple with ``--constraint="hsw|skl"``.
                            ! ``--array=``\ *0-5,7,10-15*    ! Run job multiple times, use variable ``$SLURM_ARRAY_TASK_ID`` to adjust parameters.
                            ! ``--gres=gpu``                 ! request a GPU, or ``--gres=gpu:``\ *n* for multiple
                            ! ``--gres=spindle``             ! request nodes that have disks, ``spindle:``\ *n*, for a certain number of RAID0 disks
                            ! ``--mail-type=``\ *type*       ! notify of events: ``BEGIN``, ``END``, ``FAIL``, ``ALL``, ``REQUEUE`` (not on triton) or ``ALL.`` MUST BE used with ``--mail-user=`` only
                            ! ``--mail-user=``\ *your@email* ! whome to send the email
   ``srun``                 ! ``-N`` *<N_nodes>* hostname    ! Print allocated nodes (from within script)
