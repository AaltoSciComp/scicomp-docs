Master-Worker Example
---------------------

Following example shows how to manage host list using the
python-hostlist package and run different tasks for master task and
worker task.

This kind of structure might be needed if one wants to create a e.g.
Spark cluster or use some other program that uses
master-worker-paradigm, but does not use MPI.

It is important to make sure that in case of job cancellation all
programs started by the scripts will be killed gracefully. In case of
Spark or other programs that initialize a cluster using SSH and then
forking a process, these forked processes must be killed after job
allocation has ended.

``hostlist-test.slrm``::

    #!/bin/bash
    #SBATCH -t 00:10:00
    #SBATCH -N 3
    #SBATCH -n 5
    #SBATCH -p batch
    #SBATCH -o hostlist-test.out

    # An example of a clean_up-routine if the master has to take e.g. ssh connection to start program on workers 
    function clean_up {
        echo "Got SIGTERM, will clean up my workers and exit."
        exit
    }
    trap clean_up SIGHUP SIGINT SIGTERM

    # Actual script that defines what each worker will do
    srun bash run.sh

``run.sh``::

    #!/bin/bash

    # Get a list of hosts using python-hostlist
    nodes=`hostlist --expand $SLURM_NODELIST|xargs`

    # Determine current worker name
    me=$(hostname)

    # Determine master process (first node, id 0)
    master=$(echo $nodes | cut -f 1 -d ' ')

    # SLURM_LOCALID contains task id for the local node
    localid=$SLURM_LOCALID

    if [[ "$me" == "$master" && "$localid" -eq 0 ]] 
    then
       # Run these if the process is the master task
       echo "I'm the master with number "$localid" in node "${me}". My subordinates are "$nodes
    else
       # Run these if the process is a worker
       echo "I'm a worker number "$localid" in node "${me}
    fi

Example output::

    I'm a worker number 1 in node opt469
    I'm a worker number 2 in node opt469
    I'm the master with number 0 in node opt469. My subordinates are opt469 opt470 opt471
    I'm a worker number 0 in node opt471
    I'm a worker number 0 in node opt470
