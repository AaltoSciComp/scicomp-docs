.. csv-table::
   :delim: |
   :header-rows: 1

   Card                | Slurm feature name (``--constraint=``) | Slurm gres name (``--gres=gpu:NAME:n``) | total amount   | nodes        | architecture   | compute threads per GPU   | memory per card   | CUDA compute capability
   Tesla K80\*         | ``kepler``                             | ``teslak80``                            | 12             | gpu[20-22]   | Kepler         | 2x2496                    | 2x12GB            | 3.7
   Tesla P100          | ``pascal``                             | ``teslap100``                           | 20             | gpu[23-27]   | Pascal         | 3854                      | 16GB              | 6.0
   Tesla V100          | ``volta``                              | ``v100``                                | 40             | gpu[1-10]    | Volta          | 5120                      | 32GB              | 7.0
   Tesla V100          | ``volta``                              | ``v100``                                | 40             | gpu[28-37]   | Volta          | 5120                      | 32GB              | 7.0
   Tesla V100          | ``volta``                              | ``v100``                                | 16             | dgx[1-7]     | Volta          | 5120                      | 16GB              | 7.0
   Tesla A100          | ``ampere``                             | ``a100``                                | 28             | gpu[11-17]   | Ampere         | 7936                      | 80GB              | 8.0
   AMD MI100 (testing) | ``mi100``                              | Use ``-p gpu-amd`` only, no ``-gres``   |                | gpuamd[1]    |
