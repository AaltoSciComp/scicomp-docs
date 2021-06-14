Troubleshooting
====

Here is a list of common issues and errors you may come across when using Triton or your own cluster. 

Common issues
-----------------------

``srun: Required node not available (down, drained or reserved)``
#####


This error usually occurs when the default specified node is down, drained or reserved which can happen if the cluster is undergoing some work. If this error occurs then the shell will usually hang after the job has been submitted if the job is still waiting for memory allocation. To find which nodes are available for us to run jobs we can use ``sinfo`` and under the ``STATE`` column you will see for each partition the states of the nodes. 

To fix this we can either wait for the default node to be available or choose a different partition with the ``--partition=`` command, using one of the partitions from ``sinfo`` which has free and available (``idle``) nodes. 


