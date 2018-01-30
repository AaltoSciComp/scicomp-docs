.. csv-table::
   :header-rows: 1
   :delim: |

   Command                                  | Description
   ``slurm q`` ; ``slurm qq``               | Status of your queued jobs (long/short)
   ``slurm partitions``                     | Overview of partitions (A/I/O/T=active,idle,other,total)
   ``slurm cpus`` *<partition>*             | list free CPUs in a partition
   ``slurm history`` *[1day,2hour,...]*     | Show status of recent jobs
   ``seff`` *<jobid>*                       | Show percent of mem/CPU used in job
   ``slurm j`` *<jobid>*                    | Job details (only while running)
   ``slurm s`` ; ``slurm ss`` *<partition>* | Show status of all jobs
   ``sacct``                                | Full history information (advanced, needs args)

**Full slurm command help:**

::

    $ slurm

    Show or watch job queue:
     slurm [watch] queue     show own jobs
     slurm [watch] q   show user's jobs
     slurm [watch] quick     show quick overview of own jobs
     slurm [watch] shorter   sort and compact entire queue by job size
     slurm [watch] short     sort and compact entire queue by priority
     slurm [watch] full      show everything
     slurm [w] [q|qq|ss|s|f] shorthands for above!
     slurm qos               show job service classes
     slurm top [queue|all]   show summary of active users
    Show detailed information about jobs:
     slurm prio [all|short]  show priority components
     slurm j|job      show everything else
     slurm steps      show memory usage of running srun job steps
    Show usage and fair-share values from accounting database:
     slurm h|history   show jobs finished since, e.g. "1day" (default)
     slurm shares
    Show nodes and resources in the cluster:
     slurm p|partitions      all partitions
     slurm n|nodes           all cluster nodes
     slurm c|cpus            total cpu cores in use
     slurm cpus   cores available to partition, allocated and free
     slurm cpus jobs         cores/memory reserved by running jobs
     slurm cpus queue        cores/memory required by pending jobs
     slurm features          List features and GRES

    Examples:
     slurm q
     slurm watch shorter
     slurm cpus batch
     slurm history 3hours

**Other advanced** commands (many require lots of parameters to be
useful):

.. csv-table::
   :header-rows: 1
   :delim: |

   Command           | Description
   ``squeue``        | Full info on queues
   ``sinfo``         | Advanced info on partitions
   ``slurm nodes``   | List all nodes
