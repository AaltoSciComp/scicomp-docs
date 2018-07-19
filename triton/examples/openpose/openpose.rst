OpenPose
========

This uses :doc:`Singularity containers </triton/usage/singularity>`,
so you should refer to that page first for general information.

OpenPose has been compiled against system OpenBLAS and most recent
Caffe, CUDA and cuDNN. Image is based on a Ubuntu 16.04 base image.

Within the container OpenPose is installed under /opt/openpose. Due to
the way the examples are organized, the singularity\_wrapper changes the
working directory to /opt/openpose.

Example :download:`script </triton/examples/openpose/openpose.slrm>` to be run with srun can
be seen below.

Usage
~~~~~

.. literalinclude:: /triton/examples/openpose/openpose.slrm
