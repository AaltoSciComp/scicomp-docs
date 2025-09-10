.. csv-table::
   :delim: |
   :header-rows: 1

   Card                 | Slurm partition (``--partition=``) | Slurm feature name (``--constraint=``) | Slurm gres name (``--gres=gpu:NAME:n``) | total amount   | nodes        | architecture   | compute threads per GPU   | memory per card   | CUDA compute capability
   NVIDIA V100          | ``gpu-v100-32g``                   | ``volta``                              | ``v100``                                | 40             | gpu[1-10]    | Volta          | 5120                      | 32GB              | 7.0
   NVIDIA V100          | ``gpu-v100-32g``                   | ``volta``                              | ``v100``                                | 40             | gpu[28-37]   | Volta          | 5120                      | 32GB              | 7.0
   NVIDIA V100          | ``gpu-v100-16g``                   | ``volta``                              | ``v100``                                | 176            | dgx[1-2,8-27]| Volta          | 5120                      | 16GB              | 7.0
   NVIDIA V100          | ``gpu-v100-32g``                   | ``volta``                              | ``v100``                                | 32             | dgx[3,5-7]   | Volta          | 5120                      | 32GB              | 7.0
   NVIDIA A100          | ``gpu-a100-80g``                   | ``ampere``                             | ``a100``                                | 56             | gpu[11-17,38-44] | Ampere     | 7936                      | 80GB              | 8.0
   NVIDIA H100          | ``gpu-h100-80g``                   | ``hopper``                             | ``h100``                                | 16             | gpu[45-48]   | Hopper         | 16896                     | 80GB              | 9.0
   NVIDIA H200          | ``gpu-h200-35g-ia``                | ``hopper``                             | ``h200-35g``                            | 24             | gpu[49]      | Hopper         |                           | 35GB              | 9.0
   NVIDIA H200(*)       | ``gpu-h200-141g-ellis``, ``gpu-h200-141g-short``  | ``hopper``              | ``h200``                                | 112            | gpu[50-63]   | Hopper         |                           | 141GB             | 9.0
   AMD MI100            | ``gpu-amd``                        |    features not supported              | ``-p gpu-amd --gres=gpu:mi100``         | 1              | gpuamd[1]    |                |                           |                   |
   AMD MI210            | ``gpu-amd``                        |    features not supported              | ``-p gpu-amd --gres=gpu:mi210``         | 2              | gpuamd[1]    |                |                           |                   |

(*) These GPUs have a priority queue for the ellis project, since they were procured for this project. 
Any job submitted to the short queue might be preempted if a job requiring the resources comes in from the ellis queue. 
They are not allocated automatcally unless you specifically request a job on their partition.
