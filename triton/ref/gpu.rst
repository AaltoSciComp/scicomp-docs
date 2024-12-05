.. csv-table::
   :delim: |
   :header-rows: 1

   Card                | Slurm partition (``--partition=``) | Slurm feature name (``--constraint=``) | Slurm gres name (``--gres=gpu:NAME:n``) | total amount   | nodes        | architecture   | compute threads per GPU   | memory per card   | CUDA compute capability
   Tesla K80\*         |  *Not available*                                  | ``kepler``                             | ``teslak80``                            | 12             | gpu[20-22]   | Kepler         | 2x2496                    | 2x12GB            | 3.7
   Tesla P100          | ``gpu-p100-16g``                   | ``pascal``                             | ``teslap100``                           | 20             | gpu[23-27]   | Pascal         | 3854                      | 16GB              | 6.0
   Tesla V100          | ``gpu-v100-32g``                   | ``volta``                              | ``v100``                                | 40             | gpu[1-10]    | Volta          | 5120                      | 32GB              | 7.0
   Tesla V100          | ``gpu-v100-32g``                   | ``volta``                              | ``v100``                                | 40             | gpu[28-37]   | Volta          | 5120                      | 32GB              | 7.0
   Tesla V100          | ``gpu-v100-16g``                   | ``volta``                              | ``v100``                                | 16             | dgx[1-2]     | Volta          | 5120                      | 16GB              | 7.0
   Tesla V100          | ``gpu-v100-32g``                   | ``volta``                              | ``v100``                                | 16             | dgx[3-7]     | Volta          | 5120                      | 32GB              | 7.0
   Tesla A100          | ``gpu-a100-80g``                   | ``ampere``                             | ``a100``                                | 56             | gpu[11-17,38-44] | Ampere     | 7936                      | 80GB              | 8.0
   Tesla H100          | ``gpu-h100-80g``                   | ``hopper``                             | ``h100``                                | 16             | gpu[45-48]   | Hopper         | 16896                     | 80GB              | 9.0
   Tesla H200          | ``gpu-h200-18g-ia``                | ``hopper``                             | ``h200-18g``                            | 56             | gpu[49]      | Hopper         |                           | 18GB              | 9.0
   Tesla H200          | ``gpu-h200-141g``                  | ``hopper``                             | ``h200``                                | 16             | gpu[50-51]   | Hopper         |                           | 141GB             | 9.0
   AMD MI100 (testing) |   *Not yet installed*              | ``mi100``                              | Use ``-p gpu-amd`` only, no ``--gres``  |                | gpuamd[1]    |
