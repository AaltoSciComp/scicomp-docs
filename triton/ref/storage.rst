.. csv-table::
   :delim: |
   :header-rows: 1

   Name                            | Path                                  | Quota                       | Backup    | Locality                           | Purpose
   Home                            | ``$HOME`` or ``/home/$username/``             | hard quota 10GB              | Nightly   | all nodes                  | Small user specific files, no calculation data.
   Work                            | ``$WRKDIR`` or ``/scratch/work/$username/``   | 200GB and 1 million files   | x         | all nodes                  | Personal working space for every user. Calculation data etc. Quota can be increased on request.
   Scratch                         | ``/scratch/$dept/$project/``              | on request                  | x         | all nodes                      | Department/group specific project directories.
   Local temp                      | ``/tmp/``                                 | limited by disk size        | x         | single-node                    | Primary (and usually fastest) place for single-node calculation data.  Removed once user's jobs are finished on the node.
   Local persistent                | ``/l/``                                   | varies                      | x         | dedicated group servers only   | Local disk persistent storage.  On servers purchased for a specific group.  Not backed up.
   ramfs (login nodes only)        | ``$XDG_RUNTIME_DIR``                    | limited by memory           | x         | single-node                      | Ramfs on the *login node only*, in-memory filesystem
