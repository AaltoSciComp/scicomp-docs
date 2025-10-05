.. csv-table::
   :header-rows: 1
   :delim: |

   Command                | Description
   ``sbatch``             | submit a job to queue (see standard options below)
   ``srun``               | Within a running job script/environment: Run code using the allocated resources (see options below)
   ``srun``               | On frontend: submit to queue, wait until done, show output. (see options below)
   ``sinteractive``       | Submit job, wait, provide shell on node for interactive playing (X forwarding works, default partition interactive).  Exit shell when done. (see options below)
   ``srun --pty bash``    | (advanced) Another way to run interactive jobs, no X forwarding but simpler.  Exit shell when done.
   ``scancel JOBID``      | Cancel a job in queue
   ``salloc``             | (advanced) Allocate resources from frontend node.  Use ``srun`` to run using those resources, ``exit`` to close shell when done (see options below)
   ``scontrol``           | View/modify job and slurm configuration


.. csv-table::
   :header-rows: 1
   :delim: !

   Command                  ! Option                         ! Description
   ``sbatch``/``srun``/etc  ! ``-t``, ``--time=HH:MM:SS``    ! **time limit**
                            ! ``-t``, ``--time=DD-HH``           ! **time limit, days-hours**
                            ! ``-p PARTITION``, ``--partition=PARTITION``  ! **job partition.  Usually leave off and things are auto-detected.**
                            ! ``--mem-per-cpu=N``            ! **request N MB of memory per core**
                            ! ``--mem=N``                    ! **request N MB memory per node**
                            ! ``-c``, ``--cpus-per-task=N``  ! **Allocate *n* CPU's for each task. For multithreaded jobs. (compare ``--ntasks``: ``-c`` means the number of cores for each process started.)**
                            ! ``-N``, ``--nodes=N-M``        ! allocate minimum of N, maximum of M nodes.
                            ! ``-n``, ``--ntasks=N``         ! allocate resources for and start *n* tasks (one task=one process started, it is up to you to make them communicate. However the main script runs only on first node, the sub-processes run with "srun" are run this many times.)
                            ! ``--gpus=1``                   ! request a GPU, or ``--gpus=N`` for multiple
                            ! ``--gres=min-vram:NNg``        ! request GPUs with at least ``NN`` GB of VRAM.  To combine with other ``--gres`` options, use ``--gres=min-vram:NNg,min-cuda-cc=NN``.
                            ! ``--gres=min-cuda-cc:NN``      ! request GPUs with CUDA compute capability of at least N.N.  See above for combining with other GRES.
                            ! ``-J``, ``--job-name=NAME``    ! short job name
                            ! ``-o OUTPUTFILE``              ! print output into file *output*
                            ! ``-e ERRORFILE``               ! print errors into file *error*
                            ! ``--exclusive``                ! allocate exclusive access to nodes.  For large parallel jobs.
                            ! ``--constraint=FEATURE``       ! request *feature* (see ``slurm features`` for the current list of configured features, or Arch under the :ref:`hardware list <hardware-list>`).  Multiple with ``--constraint="hsw|skl"``.
			    ! ``--tmp=nnnG``                 ! request a node with a :doc:`local disk storage space </triton/usage/localstorage>` and ``nnn`` GB of space on it.
                            ! ``--array=0-5,7,10-15``        ! Run job multiple times, use variable ``$SLURM_ARRAY_TASK_ID`` to adjust parameters.
                            ! ``--mail-type=TYPE``           ! notify of events: ``BEGIN``, ``END``, ``FAIL``, ``ALL``, ``REQUEUE`` (not on triton) or ``ALL.`` MUST BE used with ``--mail-user=`` only
                            ! ``--mail-user=first.last@aalto.fi`` ! Aalto email to send the notification about the job. External email addresses doesn't work.
   ``srun``                 ! ``-N N_NODES hostname``        ! Print allocated nodes (from within script)
