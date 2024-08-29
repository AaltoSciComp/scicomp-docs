.. csv-table::
   :delim: |
   :header-rows: 1

   Name                            | Path                                       | Quota                       | Backup    | Sharing across                 | Purpose
   Home                            | ``$HOME`` or ``/home/USERNAME/``           | hard quota 10GB             | Nightly   | all nodes                      | Small user specific files, no calculation data.
   Work                            | ``$WRKDIR`` or ``/scratch/work/USERNAME/`` | 200GB and 1 million files   | x         | all nodes                      | Personal working space for every user. Calculation data etc. Quota can be increased on request.
   Scratch                         | ``/scratch/DEPT/PROJECT/``                 | on request                  | x         | all nodes                      | Department/group specific project directories.
   Local temp                      | ``/tmp/`` (nodes with disks only)          | local disk size             | x         | single-node                    | (Usually fastest) place for single-node calculation data.  Removed once user's jobs are finished on the node.  Request with ``--constraint=localdisk``.
   ramfs                           | ``/dev/shm/`` (and ``/tmp/`` on diskless nodes) | limited by memory      | x         | single-node                    | Very fast but small in-memory filesystem
