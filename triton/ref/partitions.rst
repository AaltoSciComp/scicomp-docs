.. csv-table::
   :delim: |
   :header-rows: 1

   Partition  |Max job size|Mem/core (GB)|Tot mem (GB)| Cores/node | Limits     | Use
   <default>  |            |            |            |            |            | If you leave off all possible partitions will be used (based on time/mem)
   debug      | 2 nodes    | 2.66 - 12  | 32-256     | 12,20,24   | 15 min     | testing and debugging short interactive. work.  1 node of each arch.
   batch      | 16 nodes   | 2.66 - 12  | 32-256     | 12, 20,24  | 5d         | **primary partition**, all serial & parallel jobs
   short      | 8 nodes    | 4 - 12     | 48-256     | 12, 20,24  | 4h         | short serial & parallel jobs, +96 dedicated CPU cores
   hugemem    | 1 node     | 43         | 1024       | 24         | 3d         | huge memory jobs, 1 node only
   gpu        | 1 node, 2-8GPUs   | 2 - 10     | 24-128     | 12         | 5d         | :doc:`GPU computing <../usage/gpu>`
   gpushort   | 4 nodes, 2-8 GPUs  | 2 - 10     | 24-128     | 12         | 4h         | :doc:`GPU computing <../usage/gpu>`
   interactive| 2 nodes    | 5          | 128        | 24         | 1d         | for ``sinteractive`` command, longer interactive work

Use ``slurm partitions`` to see more details.
