======================
Singularity Containers
======================

For more information see: http://singularity.lbl.gov/


Basic Idea
~~~~~~~~~~

The basic idea behind Singularity containers is that software is packaged
into a container (basically an entire self-contained operating system!)
that is based on a Docker image that can then be run by the
user.  This allows hard to install software to be easily packaged and
used - because you are packaging the entire OS!

During runtime, the root file system ``/`` is changed to the one inside the
image and file systems are brought into the container through bind
mounts. This sounds complicated, but in practice this is easy due to
singularity_wrapper written for Triton.


Basic Usage
~~~~~~~~~~~

While the image itself is read-only, remember that ``/home``, ``/m``, ``/scratch``
and ``/l`` etc. are not. If you edit/remove files in these locations within
the image, that will happen outside the image as well.


On Triton, you just need to load the proper module.  This will set
some environment variables and enable the use of
``singularity_wrapper``.  If you want to look yourself, all different
images can be found from ``/share/apps2/singularity/images``.


singularity_wrapper
~~~~~~~~~~~~~~~~~~~

``singularity_wrapper`` is written so that when you load a module written
for a singularity image, all the important options are already handled
for you.  It has three basic commands:

#. ``singularity_wrapper shell <shell>`` - Gives user a shell
   within the image (specify ``<shell>`` to say which shell you want).
#. ``singularity_wrapper exec <cmd>`` - Executes a program within the
   image.
#. ``singularity_wrapper run <parameters>`` - Runs the singularity image. What this
   means depends on the image in question - each image will define a
   "run command" which does something.  If you don't know what this
   is, use the first two instead.

Under the hood, ``singularity_wrapper` does this:

#. Choosing appropriate image based on module version
#. Binding of basic paths (``-B /l:/l``, ``/m:/m``, ``/scratch:/scratch``)
#. Loading of system libraries within images (if needed) (e.g. ``-B
   /lib64/nvidia:/opt/nvidia``)
#. Setting working directory within image (if needed)


Power usage
~~~~~~~~~~~

These are the "raw" singularity commands.  If you use these, you have
to configure the images and bind mounts yourself (which is done
automatically by ``singularity_wrapper``).  If you ``module show`` the
module you can get hints about what happens.

Singularity enables three base commands to user:

#. ``singularity shell <image>`` - Gives user a shell within the image (see
   ``singularity shell --help`` for more information on flags etc.)
#. ``singularity exec <image> <cmd>`` - Executes a program within the image
   (see ``singularity exec --help`` for more information on flags etc.)
#. ``singularity run <image> <parameters>`` - Runs the singularity image.
   What this means depends on the image in question. (see ``singularity
   run --help`` for more information on flags etc.)


Creating your own Singularity images to run in Triton
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

All images used in Triton are done using a templating scheme described
in `this repository <https://github.com/AaltoScienceIT/singularity-templating>`_.
Definition templates will be shared on `Aalto GitLab <https://version.aalto.fi/gitlab/AaltoScienceIT>`_ or on `GitHub <https://github.com/AaltoScienceIT>`_. Build environment is
reserved for admins, but we can take pull requests if you want to
contribute to the definitions.
