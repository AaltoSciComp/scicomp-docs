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

Building a simple PyTorch environment
-------------------------------------

Nvidia provides ARM containers for PyTorch, which you can use as a starting point for your own containers.
This example shows how you can extend such a container by installing additional packages from pip.

A new PyTorch container is built each month, you can browse the selection
in the `Nvidia PyTorch catalog <https://catalog.ngc.nvidia.com/orgs/nvidia/containers/pytorch>`__.
The following container definition file selects the February 2026 Nvidia PyTorch container with PyTorch
version 2.11 as a starting point:

.. code-block:: none

  Bootstrap: docker
  From: nvcr.io/nvidia/pytorch:26.02-py3

  %post
    pip install transformers==4.57.6 pyyaml==6.0.1

  %help
    An apptainer image based on Nvidia's PyTorch container with ARM CPU architecture.

    The bootstrapped container runs on Ubuntu 24.04, and contains CUDA version 13.1,
    OpenMPI 4.1.7, Python 3.12 and PyTorch 2.11.

    This image extends the bootstrapped PyTorch container with transformers package
    from HuggingFace.

    PyYAML is a package required by transformers that has already been installed by the
    operating system package manager in the container. Pip will try to update PyYAML
    (to 6.0.3 at the time this image was created), which will fail the build because
    pip cannot change packages installed by the system package manager.
    Thus, PyYAML has to be pinned to the version used by the system package manager.


You can add other packages you need to the ``pip install`` command in the container definition above.
We also recommend documenting your container in the ``%help`` section
(which packages you have added and why).
Save your container definition to a file (here we will use ``pytorch-transformers-arm.def``) and
track it with version control to back it up for reproducibility.

Next, you need to build the container image (SIF-file) from the definition file.
Building needs to happen on an ARM-device, which you can achieve for example with
the following sbatch script ``build-pytorch-transformers-arm-container.sh`` like so:

.. code-block:: slurm

  #!/bin/bash
  #SBATCH --job-name=build-arm-container
  #SBATCH --partition=gpu-grace-h200-141g
  #SBATCH --cpus-per-task=4
  #SBATCH --gpus=1
  #SBATCH --time=01:00:00
  #SBATCH --mem=128G

  # You can replace $WRKDIR with $PWD to create the cache in your current working dir
  mkdir -p "$WRKDIR/apptainer_cache"
  export APPTAINER_CACHEDIR="$WRKDIR/apptainer_cache"

  apptainer build pytorch-transformers-arm.sif pytorch-transformers-arm.def

After you have successfully built your container, you can start using it in your scripts.
Here is a simple example of how to run an imaginary Python training script with two arguments
using the container:

.. code-block:: sh

  #!/bin/bash
  #SBATCH --job-name=train-script
  #SBATCH --partition=gpu-grace-h200-141g
  #SBATCH --cpus-per-task=8
  #SBATCH --gpus=1
  #SBATCH --time=04:00:00
  #SBATCH --mem=256G

  # The --nv argument makes the GPU available within the container
  apptainer exec --nv pytorch-transformers-arm.sif \
    python train_script.py \
      --arg1 foo \
      --arg2 bar

You simply need to prepend calls to your scripts with the apptainer exec command.
For a more comprehensive tutorial on apptainer, please see
`the third lesson <https://coderefinery.github.io/hpc-containers/>`__ of our
`Tuesday Tools & Techniques for HPC (TTT4HPC) course <../../training/scip/ttt4hpc-2024.rst>`__.
Just keep in mind when reading the lesson that it assumes x86 architecture instead of ARM,
so adjust the examples in the tutorial to use ARM.
In other words, be sure to select an ARM container as your starting point,
and run the building script on ARM hardware as shown above.
And if you want or need any help setting up your ARM containers,
you can always join `SciComp garage <../../help/garage.rst>`__ for help.

