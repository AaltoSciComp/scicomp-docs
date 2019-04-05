OpenPose
========

This uses :doc:`Singularity containers </triton/usage/singularity>`,
so you should refer to that page first for general information.

OpenPose has been compiled against Atlas and Caffe, CUDA and cuDNN. 
Image is based on a `bvlc/caffe:gpu <https://hub.docker.com/r/bvlc/caffe>`_ base image.

Dockerfile for this image is available
`here <https://github.com/AaltoScienceIT/scienceit-dockerfiles/blob/master/OpenPose/Dockerfile>`_.

Within the container OpenPose is installed under `/opt/openpose-master`. Due to
the way the examples are organized, the `singularity_wrapper` changes the
working directory to `/opt/openpose-master`.

Example :download:`sbatch script </triton/examples/openpose/openpose.slrm>` is
shown below.

Usage
~~~~~

.. literalinclude:: /triton/examples/openpose/openpose.slrm
