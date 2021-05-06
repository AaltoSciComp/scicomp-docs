Compiling CUDA code while using conda environments
==================================================

:supportlevel:
:pagelastupdated: 2021-05-05
:maintainer:

.. highlight:: bash

Conda is a powerful package manager that is commonly used to create Python
environments. It is ofter used to install GPU-accelerated code such as PyTorch
or Tensorflow. Many models built on top of these frameworks often extend the
available operators / CUDA kernels by compiling extensions. These extensions
are sometimes built beforehand and sometimes they are done using JIT
(just-in-time) compilation. When dealing with such models one can often
encounter many pitfalls that make it hard to compile of said extensions.

This document tries to explain how one should approach and debug CUDA compiling
while using conda environments. The example uses PyTorch, but the basic ideas
work for other frameworks as well.

TL;DR is provided at the end of the document.

Our example case
----------------

In this example we'll use PyTorch's
`example repo <https://github.com/pytorch/extension-cpp>`_ on C++/CUDA
extensions.

::

  git clone https://github.com/pytorch/extension-cpp.git pytorch-extension-cpp
  cd pytorch-extension-cpp/cuda
  module load miniconda
  conda create --name pytorch-env --channel pytorch pytorch torchvision torchaudio cudatoolkit=10.2
  source activate pytorch-env

Here we:

1. Cloned the extension repository and moved into its CUDA-examples folder
2. Loaded a miniconda module that gives us the conda-command
3. Created a new environment for our pytorch installation and activated it

One could of course use the already existing ``anaconda``-environment, but when
dealing with extensions one often needs a specific version of a toolkit and/or
framework, so here were using a custom environment.

How conda packages the CUDA libraries
-------------------------------------

During the installation procedure you might have noticed that we obtained a
package called ``cudatoolkit``. In fact, during the environment creation we
explicitly wanted a specific version of this toolkit (``cudatoolkit=10.2``).
This requirement only specified the major version, so to see what is the
full version of our toolkit, we need to run

::

  conda list cudatoolkit

End result is something like this::

  (pytorch-env) [tuomiss1@login3 cuda]$ conda list cudatoolkit
  # packages in environment at /home/tuomiss1/.conda/envs/pytorch-env:
  #
  # Name                    Version                   Build  Channel
  cudatoolkit               10.2.89              hfd86e86_1

So the version we have installed is ``10.2.89``. This is important, as all
packages installed by conda that use this toolkit have been compiled to use
the specific version of the toolkit. If we run

::

  conda list pytorch

We see something like this::

  (pytorch-env) [tuomiss1@login3 cuda]$ conda list pytorch
  # packages in environment at /home/tuomiss1/.conda/envs/pytorch-env:
  #
  # Name                    Version                   Build  Channel
  pytorch                   1.8.1           py3.8_cuda10.2_cudnn7.6.5_0    pytorch

Here we can see that the version of our ``pytorch``-package is ``1.8.1``, the
build of the package is ``py3.8_cuda10.2_cudnn7.6.5_0`` and it comes from a
channel called ``pytorch``. Looking at the build-string we can see that our
version of ``pytorch`` has been compiled against CUDA 10.2 and cuDNN 7.6.5.

For more information on the build, we can run

::

  conda search --channel pytorch --info pytorch=1.8.1=py3.8_cuda10.2_cudnn7.6.5_0

which will show all of the dependencies that the package has. For now, we're
only interested in the version of the ``cudatoolkit``.

If you're installing multiple different CUDA-enabled frameworks into a
single environment it is recommended to do the installation in a single
command as otherwise you might get competing builds with competing
``cudatoolkit``-requirements. This can break some of your installations.

Why is the version of ``cudatoolkit`` so important? That is because the
``cudatoolkit`` that comes via conda is not the full CUDA SDK (software
development kit). It is missing, among other things, the ``nvcc`` compiler
that is used to compile CUDA code. The package ``cudatoolkit`` only contains
**runtime** libraries, not **development** headers etc. It is done in
this way to save space. Most use cases for CUDA code do not compile their
own CUDA code and thus packaging the minimal amount of files to the toolkit
will greatly reduce the network bandwidth and storage needed by environments.

However, when we're compiling CUDA extensions, we need the CUDA compiler
and the development headers. These we will find from the module system.

Obtaining CUDA SDK from the module system
-----------------------------------------

Our module system contains various installations of the CUDA toolkit.
In order to use them properly, we also need to load a compatible compiler.

Let's first try to run a JIT-compiled extension without loading the correct
modules. We can (in the ``pytorch-extension-cpp/cuda``-folder) try the
JIT-compiled code on a GPU node.

::

  srun --gres=gpu:1 --mem=4G --time=00:15:00 python jit.py

This will fail with error such as

::

  RuntimeError: Error building extension 'lltm_cuda'

This happens because we are missing the required development files. To load
said files we can run

::

  module load gcc/8.4.0
  module load cuda/10.2.89

Here we do the following:

1. We load a compiler that is supported by our version of CUDA-toolkit.
2. We load a CUDA SDK with **exactly the same version** as the one installed in
   our conda environment.

If we try our ``srun``-command again after loading the modules, we get (after
some compilation output) the following::

  Loading extension module lltm_cuda...
  Help on module lltm_cuda:

  NAME
      lltm_cuda

  FUNCTIONS
      backward(...) method of builtins.PyCapsule instance
          backward(arg0: at::Tensor, arg1: at::Tensor, arg2: at::Tensor, arg3: at::Tensor, arg4: at::Tensor, arg5: at::Tensor, arg6: at::Tensor, arg7: at::Tensor, arg8: at::Tensor) -> List[at::Tensor]
          
          LLTM backward (CUDA)
      
      forward(...) method of builtins.PyCapsule instance
          forward(arg0: at::Tensor, arg1: at::Tensor, arg2: at::Tensor, arg3: at::Tensor, arg4: at::Tensor) -> List[at::Tensor]
          
          LLTM forward (CUDA)

  FILE
      /scratch/work/tuomiss1/cache/torch_extensions/lltm_cuda/lltm_cuda.so


This means that our compilation was successful.

During these steps it is important to notice few things.

Firstly, different versions of CUDA only support a range of compilers. In case
of CUDA 10.2, GCC 8.4.0 is within the supported range. To find out what are the
supported versions for specific CUDA toolkit one needs to find out
`this table <https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#system-requirements>`_
hidden in the CUDA toolkit's installation requirements. It lists the minimum
and maximum version numbers for the compiler. However, for modern versions of
the CUDA toolkit the version used as a base compiler for Triton should be good
enough (e.g. ``gcc/8.4.0`` at the time of writing).

Secondly, it is recommended to exactly match the module version of the CUDA
toolkit with version of the CUDA toolkit that is within the conda environment.
If we're missing a module version of CUDA toolkit that you have installed via
conda, please let us know. Changes in second minor version might not affect
the stability or results of a compiled program, but it is not worth the risk
to try different versions. Installing various CUDA-toolkits as modules is very
easy for us.

TL;DR
-----

1. Install cuda-enabled code in your conda environment and activate it
2. Find out what version of ``cudatoolkit`` was installed with

::

  conda list cudatoolkit

3. Load compiler and CUDA SDK with the same version with

::

  module load gcc/8.4.0
  module load cuda/"exact same version as in conda environment"
