======================
Singularity Containers
======================


For more information see: http://singularity.lbl.gov/

Singularity
===========

Before usage
~~~~~~~~~~~~

Due to the 'work in progress'-designation, singularity containers are
not available by default to all users. To start using them you need to
run::

    module use /share/apps2/singularity/modules/

Basic Idea
~~~~~~~~~~

Basic Idea behind Singularity containers is that software is packaged
into a container that is based on a Linux image or Docker image that can
then be run by the user.

During runtime the root file system "/" is changed to the one inside the
image and file systems are brought into the container through bind
mounts. This sounds complicated, but in practice this is easy due to
singularity_wrapper written for Triton.

Basic Usage
~~~~~~~~~~~

While the image itself is read-only, remember that /home, /m, /scratch
and /l etc. are not. If you edit/remove files in these locations within
the image, that will happen outside the image as well.

Singularity enables three base commands to user:

#. ``singularity shell <image>`` - Gives user a shell within the image (see
   ``singularity shell --help`` for more information on flags etc.)
#. ``singularity exec <image> <cmd>`` - Executes a program within the image
   (see ``singularity exec --help`` for more information on flags etc.)
#. ``singularity run <image> <parameters>`` - Runs the singularity image.
   What this means depends on the image in question. (see ``singularity
   run --help`` for more information on flags etc.)

These commands can be used, but we recommend using ``singularity_wrapper``
instead.

All different images can be found from ``/share/apps2/singularity/images``

singularity_wrapper
~~~~~~~~~~~~~~~~~~~

``singularity_wrapper`` is written so that when you load a module written
for a singularity image, singularity_wrapper knows what parameters to
use. Differences include:

#. Choosing version appropriate image
#. Binding of basic paths (-B /l:/l, -B /m:/m, /scratch:/scratch)
#. Setting working directory within image (if needed)
#. Loading of system libraries within images (if needed) (e.g. -B
   /lib64/nvidia:/opt/nvidia)

singularity_wrapper enables the three base commands, but with small
differences:

#. ``singularity_wrapper shell <shell>`` - Gives user the requested shell
   within the image
#. ``singularity_wrapper exec <cmd>`` - Executes a program within the
   image.
#. ``singularity_wrapper run <parameters>`` - Runs the singularity image. What this
   means depends on the image in question.

.. include:: ../examples/openfoam/openfoam.rst

.. include:: ../examples/openpose/openpose.rst
