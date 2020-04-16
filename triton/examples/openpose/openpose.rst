OpenPose
========

This uses :doc:`Singularity containers </triton/usage/singularity>`,
so you should refer to that page first for general information.

OpenPose has been compiled against OpenBlas, Caffe, CUDA and cuDNN.
Image is based on a `nvidia/cuda:10.1-cudnn7-devel-ubuntu18.04 <https://hub.docker.com/r/nvidia/cuda/tags>`_ docker image.

Dockerfile for this image is available
`here <https://raw.githubusercontent.com/AaltoScienceIT/scienceit-dockerfiles/master/OpenPose/v1.5.1/Dockerfile>`_.

Within the container OpenPose is installed under ``/opt/openpose``. Due to
the way the libraries are organized, ``singularity_wrapper`` changes the
working directory to ``/opt/openpose``.

Running OpenPose example
~~~~~~~~~~~~~~~~~~~~~~~~

One can run this example with ``srun``::

  wget https://raw.githubusercontent.com/AaltoScienceIT/scicomp-docs/master/triton/examples/openpose/openpose.sh
  module load singularity-openpose
  sbatch openpose.slrm

Example :download:`sbatch script </triton/examples/openpose/openpose.sh>` is
shown below.

.. literalinclude:: /triton/examples/openpose/openpose.sh
