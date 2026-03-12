Grace Hopper Super Chips
========================


Hardware in Triton
------------------

Triton has currently two compute nodes (gpuarm[1,2]) with the Grace-Hopper superchip.
To gain access, please use the slurm partition: ``--partition gpu-grace-h200-141g``.

Super chip
----------

The Grace-Hopper is a tightly coupled system of a CPU build with the ARM architecture, and a GPU chip. There is a high-bandwidth connection between the CPU and GPU, so applications that can use both the CPU and GPU benefit from it.

The ARM architecture means, that code compiled for the "normal" x86 does not run on Grace-Hopper. All binary programs must be specifically compiled for ARM.

Software on triton
------------------

At the moment, SciComp provides only very minimal set of software for Grace-Hopper. It is intended that users download and use containers from nvidia.

A very basic example could be::

    apptainer exec --nv docker://nvidia/cuda:13.0.1-base-ubuntu22.04 nvidia-smi

Or a full slurm batch file::

    #!/bin/bash
    #SBATCH --partition=gpu-grace-h200-141g
    #SBATCH --gpus=1
    apptainer exec --nv docker://nvidia/cuda:13.0.1-base-ubuntu22.04 nvidia-smi


