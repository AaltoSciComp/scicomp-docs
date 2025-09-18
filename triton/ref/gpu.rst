.. csv-table::
   :delim: |
   :header-rows: 1
   :class: scicomp-table-dense

   GPU brand name       | GPU name in Slurm (``--gpus=NAME:n``)  | VRAM GB (``--gres=gpu-vram:NNg``) | CUDA compute capability (``--gres=min-cuda-cc=NN``) | total amount   | nodes            | GPUs per node | Compute threads per GPU   | Slurm partition (``--partition=``)               |
   NVIDIA H200(*)       | ``h200``                               | ``141``                           | 9.0 (``90``)                                        | 112            | gpu[50-63]       | 8             | 16896                     | ``gpu-h200-141g-ellis``, ``gpu-h200-141g-short`` |
   NVIDIA H200(**)      | ``h200_2g.35gb``                       | ``35``                            | 9.0 (``90``)                                        | 24             | gpu[49]          | 24            | 4224                      | ``gpu-h200-35g-ia-ellis``, ``gpu-h200-35g-ia``   |
   NVIDIA H100          | ``h100``                               | ``80``                            | 9.0 (``90``)                                        | 16             | gpu[45-48]       | 4             | 16896                     | ``gpu-h100-80g``                                 |
   NVIDIA A100          | ``a100``                               | ``80``                            | 8.0 (``80``)                                        | 56             | gpu[11-17,38-44] | 4             | 7936                      | ``gpu-a100-80g``                                 |
   NVIDIA V100          | ``v100``                               | ``32``                            | 7.0 (``70``)                                        | 40             | gpu[28-37]       | 4             | 5120                      | ``gpu-v100-32g``                                 |
   NVIDIA V100          | ``v100``                               | ``32``                            | 7.0 (``70``)                                        | 40             | gpu[1-10]        | 4             | 5120                      | ``gpu-v100-32g``                                 |
   NVIDIA V100          | ``v100``                               | ``32``                            | 7.0 (``70``)                                        | 32             | dgx[3,5-7]       | 8             | 5120                      | ``gpu-v100-32g``                                 |
   NVIDIA V100          | ``v100``                               | ``16``                            | 7.0 (``70``)                                        | 176            | dgx[1-2,8-27]    | 8             | 5120                      | ``gpu-v100-16g``                                 |
   AMD MI210            | ``mi210`` with  ``-p gpu-amd``         | ``32``                            |                                                     | 2              | gpuamd[1]        | 2             | 7680                      | ``gpu-amd``                                      |
   AMD MI100            | ``mi100`` with  ``-p gpu-amd``         | ``64``                            |                                                     | 1              | gpuamd[1]        | 1             | 6656                      | ``gpu-amd``                                      |

Since 2025, the main way to request certain types of GPUs is with
``--gres``, for example ``--gpus=1 --gres=min-vram:32``.  Only one
``--gres`` option is allowed, so to combine gres, use a comma
separated list: ``--gres=gpu-vram:32g,min-cuda-cc=80``.

(*) These GPUs have a priority queue for the Ellis project, since they were
procured for this project. Any job submitted to the short queue might be
preempted if a job requiring the resources comes in from the Ellis queue.

(**) These GPUs are split from a single GPU with NVIDIA's
`Multi-Instance GPU <https://docs.nvidia.com/datacenter/tesla/mig-user-guide/index.html>`__-feature.
