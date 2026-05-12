Grace Hopper Super Chips
========================

Hardware in Triton
------------------

Triton has currently two compute nodes (gpuarm[1,2]) with the Grace-Hopper superchip.
To gain access, please use the slurm partition: ``--partition gpu-grace-h200-141g``.

Run time limits
---------------

The servers are for testing and development, not for long production runs. The jobs in triton are limited to 12 gpu-hours. So a single gpu job can run for 12 hours or two gpu job for 6 hours.

Super chip
----------

The Grace-Hopper is a tightly coupled system of a CPU build with the ARM architecture, and a GPU chip. There is a high-bandwidth connection between the CPU and GPU, so applications that can use both the CPU and GPU benefit from it.

Software on triton
------------------

The ARM architecture means, that code compiled for the "normal" x86 does not run on Grace-Hopper. All binary programs must be specifically compiled for ARM.

SciComp provides only very minimal set of software for Grace-Hopper. It is intended that users download and use containers e.g. from `NVidia Catalog <https://catalog.ngc.nvidia.com/>`__.

A very basic example could be::

    apptainer exec --nv docker://nvidia/cuda:13.0.1-base-ubuntu22.04 nvidia-smi

Or a full slurm batch file::

    #!/bin/bash
    #SBATCH --partition=gpu-grace-h200-141g
    #SBATCH --gpus=1
    apptainer exec --nv docker://nvidia/cuda:13.0.1-base-ubuntu22.04 nvidia-smi

Here we compile and run a hello world app::

  #!/bin/bash
  #SBATCH --partition=gpu-grace-h200-141g
  #SBATCH --gpus=1
  #SBATCH --mem-per-cpu=10G
  #SBATCH --cpus-per-task=12

  echo Version of nvcc
  apptainer exec --nv docker://nvcr.io/nvidia/nvhpc:26.1-devel-cuda_multi-rockylinux9 nvcc --version

  ARCH=sm_90
  echo Compile within container for arch $ARCH
  apptainer exec --nv docker://nvcr.io/nvidia/nvhpc:26.1-devel-cuda_multi-rockylinux9 nvcc -arch=$ARCH hello-world.cu -o hello

  echo Run outside container
  ./hello

  echo finished


The hello-world.cu could be e.g.::

  #include <stdio.h>
  #include "cuda_runtime.h"

  __global__ void cuda_hello(){
    printf("Hello World from GPU!\n");
  }

  int main() {

    int nDevices;
    cudaGetDeviceCount(&nDevices);
    printf("We have %d GPUs.\n",nDevices);

    cuda_hello<<<1,1>>>();
    cudaDeviceSynchronize();
    return 0;
  }

