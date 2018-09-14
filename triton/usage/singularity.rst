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
``singularity_wrapper``.

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

All images used in Triton are built from Docker images stored in
our private Docker registry in
`exoti.cs.aalto.fi <https://exoti.cs.aalto.fi>`_. They build
automatically from Docker pushes using our continuous integration builder. If
you want to build your own Singularity image to Triton, we can create a user
for you to the registry and add your image to the automatic build.

.. code-block:: none

  Even though the system is in production it is still being tested.
  Thus there might be changes in the future.

Steps to get your images building are outlined below. You'll need to do steps
1 to 3 only once.

Step 1: Ask us for access to exoti.cs.aalto.fi
----------------------------------------------

Create a new issue to
`our issue tracker <https://version.aalto.fi/gitlab/AaltoScienceIT/triton/issues>`_
where you explain that you require access to our registry. We'll create an
account for you. After this you'll need to go to
`exoti.cs.aalto.fi <https://exoti.cs.aalto.fi>`_ and request a password change.
You'll get an automatic email with a link to the password reset page.

**DO NOT** use your Aalto password as your password. When you do a
``docker login`` Docker will save your password in plaintext into your
home directory.

In the future we'll remove this step.

Step 2: Create an application token
---------------------------------------------------------------

For added security you should not use your main password for ``docker login``.
By clicking on your username, you'll get to your user settings. From there, do
the following:

  1. Click ``Create new token`` in the Application tokens-section.
  2. Choose name for the token and click create.
  3. Copy the application token that is visible on the right side of your
     screen.

Step 3: Docker login
--------------------

On your own workstation run::

  docker login exoti.cs.aalto.fi

Your username is same as your Aalto username. As a password give the
application token you created in step 2.

Step 4: Push your images to registry
------------------------------------

If you have an existing image in Dockerhub, you can run::

  docker pull <dockerhub user>/<image>:<tag>
  docker tag <dockerhub user>/<image>:<tag> exoti.cs.aalto.fi/<your username>/<image>:<tag>
  docker push exoti.cs.aalto.fi/<your username>/<image>:<tag>

For example::

  docker pull library/ubuntu:latest
  docker tag library/ubuntu:latest exoti.cs.aalto.fi/$USER/ubuntu:latest
  docker push exoti.cs.aalto.fi/$USER/ubuntu:latest

If you are building your image from Dockerfile, you can run::

  docker build -it exoti.cs.aalto.fi/$USER/my_image:latest /path/to/my/dockerfile
  docker push exoti.cs.aalto.fi/$USER/my_image:latest

Step 5: Let us know what image you want to have in Triton
---------------------------------------------------------

We need the following information for the automatic build:

  - What is the Docker url of the image
    (e.g. ``exoti.cs.aalto.fi/$USER/my_image``)?
  - What tags do you want built (we recommend you use ``latest`` and ``dev``)?
  - Does the image utilize GPUs?

After that we'll set up the automated build. Every time you push a newer
version of said ``image:tag`` the image will update in Triton if the build
was successful.

After the build has been done you can load up your new image in Triton with::

  module use /share/apps/singularity-ci/centos/modules/$USER
  module load my_image:latest

and launch the programs within using the ``singularity_wrapper exec``.
