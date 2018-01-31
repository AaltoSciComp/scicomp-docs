.. csv-table::
   :delim: |
   :header-rows: 1

   Name                            | Path                                  | Quota                       | Backup    | Locality                       | Purpose
   Home                            | ``$HOME`` or ``/home/$username/``             | hard quota 1GB              | Nightly   | all nodes                      | Small user specific files, no calculation data.
   Work                            | ``$WRKDIR`` or ``/scratch/work/$username/``   | 200GB and 1 million files   | x         | all nodes                      | Personal working space for every user. Calculation data etc. Quota can be increased on request.
   Scratch                         | ``/scratch/$dept/$project/``              | on request                  | x         | all nodes                      | Department/group specific project directories.
   Local temp                      | ``/tmp/``                                 | limited by disk size        | x         | single-node                    | Primary (and usually fastest) place for single-node calculation data.  Removed once user's jobs are finished on the node.
   XDG Runtime Directory (ramfs)   | ``$XDG_RUNTIME_DIR``                    | limited by memory           | x         | single-node                    | Ramfs on the compute nodes with files cached in the memory.  Small random-access data (https://standards.freedesktop.org/basedir-spec/basedir-spec-latest.html).
   Local persistent                | ``/l/``                                   | varies                      | x         | dedicated group servers only   | Local disk persistent storage.  On servers purchased for a specific group.  Not backed up.
