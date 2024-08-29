Singularity Containers
======================

.. highlight:: shell-session

.. seealso::

  * The longer `Container on HPC with Apptainer lesson
    <https://coderefinery.github.io/hpc-containers/>`__

A **container** is basically an operating system within a file: by
including all the operating system support files, software inside of
it can run (almost) anywhere.  This is great for things like clusters,
where the operating system has to be managed very conservatively yet
users have all sorts of bleeding-edge needs.

The downside is that it's another thing to understand and manage.
Luckily, most of the time containers for the software already exists,
and using them is not much harder than other shell scripting.

**Apptainer** is the same as **Singularity**, but Apptainer is the
most open-source one that we currently use.  (``singularity`` is an
alias for ``apptainer`` on our cluster.)


What are containers?
--------------------

As stated above, the basic idea is that software is packaged into a
**container** which basically contains the entire operating system.  This
is done via a **image definition file** (``Dockerfile``, Apptainer/Singularity
definition file ``.def``) which is itself interesting because it
contains a script that makes the whole image automatically - which
makes it reproducible and shareable.  The **image** itself is the data
which contains the operating system and software.

During runtime, the root file system ``/`` is used from inside the
image and other file systems (``/scratch``, ``/home``, etc.) can be
brought into the container through **bind mounts**. Effectively, the
programs in the container are run in an environment mostly defined by
the container image, but the programs can read and write specific
files in Triton - all the data you need to operate on.  Typically,
e.g. the home directory comes from Triton.

This sounds complicated, but in practice it is not too hard once you
see an example and can copy the commands to run.  For images managed
by Triton admins themselves, this is easy due to
``apptainer_wrapper`` tool we have written for Triton.  You can also
run Apptainer on triton without the wrapper, but you may need to
e.g.  bind ``/scratch`` yourself to access your data.

The hardest part of using containers is keeping track of files inside
vs outside: You specify a command that gets run *inside* the container
image.  It mostly accesses files *inside* the image, but it can access
files *outside* if you bind-mount them in.  If you ever get confused,
use ``singularity shell`` (see below) to enter the container and see
what is going on.



About Singularity
-----------------

`Docker <https://www.docker.com/>`__ is the most commonly talked about
container runtime, but most clusters use `Apptainer
<https://apptainer.org/>`__.  The following table should make
the reasons clear:

.. list-table::
   :header-rows: 1

   * * Docker
     * Apptainer/Singularity
   * * Designed for infrastructure deployment
     * Designed for scientific computing
   * * Operating system service
     * User application
   * * In practice, gives root access to whole system
     * Does not give or need extra permissions to the system
   * * Images stored in layers in hidden operating system locations
       opaquely managed through some commands.
     * One image is one ``.sif`` file which you manage using normal
       commands.

Docker is still a standard image format, and there are ways to convert
images between the formats.  In practice, if you can use Docker, you
can also use Singularity by converting your image (commands on this
page) and running it by copying other commands on this page.



Singularity with Triton's pre-created modules
---------------------------------------------

Some of the Triton modules automatically activate a Singularity image.
On Triton, you just need to load the proper module.  This will set
some environment variables and enable the use of
``apptainer_wrapper`` (to see how it works, check ``module show
MODULE_NAME``).

While the image itself is read-only, remember that ``/home``, ``/m``,
``/scratch`` and ``/l`` etc. are not. If you edit/remove files in
these locations within the image, that will happen outside the image
as well.

``apptainer_wrapper`` is written so that when you load a module written
for a Apptainer image, all the important options are already handled
for you.  It has three basic commands:

#. ``apptainer_wrapper shell [SHELL]`` - Gives user a shell
   within the image (specify ``[SHELL]`` to say which shell you want).
#. ``apptainer_wrapper exec CMD`` - Executes a program within the
   image.
#. ``apptainer_wrapper run PARAMETERS`` - Runs the Apptainer image. What this
   means depends on the image in question - each image will define a
   "run command" which does something.  If you don't know what this
   is, use the first two instead.

Under the hood, ``apptainer_wrapper`` does this:

#. Choosing appropriate image based on module version
#. Binding of basic paths (``-B /l:/l``, ``/m:/m``, ``/scratch:/scratch``)
#. Loading of system libraries within images (if needed) (e.g. ``-B
   /lib64/nvidia:/opt/nvidia``)
#. Setting working directory within image (if needed)



Singularity commands
--------------------

This section describes using Singularity directly, with you managing
the image file and running it.


Convert a Docker image to a Singularity image
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you have a Docker image, it has to be on a registry somewhere
(since they don't exist as standalone files).  You can **pull** to
convert it to a ``.sif`` file (remember to change to a scratch folder
with plenty of space first)::

  $ cd $WRKDIR
  $ singularity build IMAGE_OUTPUT.sif docker://GROUP/IMAGE_NAME:VERSION

If you are running on your own computer with Docker and Singularity
both installed, you can use a local image like this (and then you need
to copy it to the cluser)::

  $ singularity build IMAGE_OUTPUT.sif docker-daemon://LOCAL_IMAGE_NAME:VERSION

This will store the Docker layers in ``$HOME/.singularity/cache/``,
which can result in running out of quota in your home folder.
In a situation like this, you can then clean the cache with::

  singularity cache clean

You can also use another folder for your singularity cache by setting
the ``SINGULARITY_CACHEDIR``-variable. For example, you can set it to
a subfolder of your ``WRKDIR`` with::

  export SINGULARITY_CACHEDIR=$WRKDIR/singularity_cache
  mkdir $SINGULARITY_CACHEDIR

Create your own image
~~~~~~~~~~~~~~~~~~~~~

See the `Singularity docs on this
<https://docs.sylabs.io/guides/latest/user-guide/quick_start.html#build-images-from-scratch>`__.
You create a Singularity definition file ``NAME.def``, and then::

  $ singularity build IMAGE_OUTPUT.sif NAME.def


Running containers
~~~~~~~~~~~~~~~~~~

These are the "raw" singularity commands.  If you use these, you have
to configure the images and bind mounts yourself (which is done
automatically by ``apptainer_wrapper``).  If you ``module show
NAME`` on a singularity module, you will get hints about what happens.

* ``singularity shell IMAGE_FILE.sif`` will start a shell inside of
  the image.  This is great for understanding what the image does.
* ``singularity exec IMAGE_FILE.sif COMMAND`` will run COMMAND inside
  of the image.  This is how you would script it for batch jobs, etc.
* ``singularity run IMAGE_FILE.sif`` is a lot like ``exec``, but will
  run some pre-configured command (defined as part of the image
  definition).  This might be useful when using a pre-made image.  If
  you make an image executable, you can do this by running the image
  directly: ``./IMAGE_FILE.sif [COMMAND]``
* The extra arguments ``--bind=/m,/l,/scratch`` will make the import
  Triton data filesystems available inside of the container.
  ``$HOME`` happens by default. You may want to add ``$PWD`` for your
  current working directory.
* ``--nv`` provides GPU access (though sometimes more is needed).



Examples
--------

.. admonition:: Batch script using singularity
   :class: dropdown

   .. code-block:: slurm

      #!/bin/bash
      #SBATCH --mem=10G
      #SBATCH --cpus-per-task=4

      # We would run `python /path/to/software/in-image.py
      $WRKDIR/my-input-file`, so instead we run this inside the image.
      srun singularity exec --bind /scratch YOUR_IMAGE.sif python /path/to/software/in-image.py $WRKDIR/my-input-file


.. admonition:: Writable container image that can be updated

   Sometimes, it is too much work to completely define an image before
   building it: it is more convenient to incrementally update it, just
   like your own computer.  You can make a writeable image *directory* using
   ``singularity build --sandbox`` and then when you run it you can make permanent
   changes to it by running with ``singularity [run|exec|shell]
   --writeable``.  You could, for example, pull a Ubuntu image and
   then slowly install things in it.

   But note these disadvantages:

   * The image isn't reproducible: you don't have the definition file
     to make it, so if it gets messed up you can't go back.  Being
     able to delete and reproduce is very useful.

   * There isn't an efficient, single-file image: instead, there are
     tens of thousands of files in a directory.  You get the problems
     of :doc:`many small files <smallfiles>`.  If you run this many
     times, use ``singularity build SINGLE_FILE.sif
     WRITEABLE_DIRECTORY_IMAGE/`` to convert it to a single file.



.. admonition:: MPI in singularity
   :class: dropdown

   The `Serpent code <http://montecarlo.vtt.fi>`_ is a Hybrid
   MPI/OpenMP particle following code, and can be installed into a
   container using the definition file `sss2.def
   <https://version.aalto.fi/gitlab/serpent/singularity/-/blob/master/sss2.def>`_,
   which creates a container based on Ubuntu v. 20.04. In the `build
   process
   <https://version.aalto.fi/gitlab/serpent/singularity/-/blob/master/README.md>`_,
   Singularity clones the Serpent source code, installs the required
   compilers and libraries, including the MPI library to the
   container. Furthermore, datafiles needed by Serpent are included in
   the container. Finally, a python environment with useful tools are
   also installed into the container. The Serpent code is compiled and
   the executable binaries are saved and the source code is removed.

   The container can be directly used with the Triton queue system
   assuming the datafiles are stored in the user home folder. The file
   `sss2.slurm_cmd
   <https://version.aalto.fi/gitlab/serpent/singularity/-/blob/master/sss2.slurm_cmd>`_
   can be used as an example. If scratch is used, please add ``-B
   /scratch`` after "exec" in the file.

   The key observations to make:

   #. ``mpirun`` is called in Triton, which launches multiple
      Singularity containers (one for each MPI task). Each container
      directly launches the ```sss2```-executable. Each container can
      run multiple OpenMP threads of Serpent.
   #. The openMPI library (v. 4.0.3) shipping with Ubuntu 20.04 seems
      to be compatible with the Triton module ``openmpi/4.1.5``
   #. The Ubuntu MPI library binds all the threads to the same
      CPU. This is avoided by passing the parameter ``--bind-to none``
      to mpirun.
   #. The infiniband is made available by the mpirun parameter ``--mca
      btl_openib_allow_ib``.



See also
--------

* `Containers on HPC with Apptainer
  <https://coderefinery.github.io/hpc-containers/>`__ - a longer
  lesson by our team.
* Singularity documentation: https://docs.sylabs.io/
* Singularity docs on building a container: https://docs.sylabs.io/guides/latest/user-guide/build_a_container.html
* Singularity documentation from Sigma2 (Norway):
  https://documentation.sigma2.no/software/containers.html



..
    Commented until checked through

    Creating your own Singularity images to run in Triton
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    All images used in Triton are built from Docker images stored in
    our private Docker registry in
    `registry.cs.aalto.fi <https://registry.cs.aalto.fi>`_. They build
    automatically from Docker pushes using our continuous integration builder. If
    you want to build your own Singularity image to Triton, we can create a user
    for you to the registry and add your image to the automatic build.

    .. code-block:: none

      Even though the system is in production it is still being tested.
      Thus there might be changes in the future.

    Steps to get your images building are outlined below. You'll need to do steps
    1 to 3 only once.

    Step 1: Log in to registry.cs.aalto.fi
    --------------------------------------

    Go to
    `registry.cs.aalto.fi <https://registry.cs.aalto.fi>`_ and click ``Gitlab`` under
    ``Social logins``. This will redirect you to a ``Gitlab`` page that you can use
    for authentication. In this page use your Aalto username and password to login.

    In the future we'll improve the authentication page.

    Step 2: Create an application token
    -----------------------------------

    For added security you cannot use your main password for ``docker login``.
    By clicking on your username, you'll get to your user settings. From there, do
    the following:

      1. Click ``Create new token`` in the Application tokens-section.
      2. Choose name for the token and click create.
      3. Copy the application token that is visible on the right side of your
         screen.

    Step 3: Docker login
    --------------------

    On your own workstation run::

      docker login registry.cs.aalto.fi

    Your username is same as your Aalto username. As a password give the
    application token you created in step 2.

    Step 4: Push your images to registry
    ------------------------------------

    If you have an existing image in Dockerhub, you can run::

      docker pull <dockerhub user>/<image>:<tag>
      docker tag <dockerhub user>/<image>:<tag> registry.cs.aalto.fi/<your username>/<image>:<tag>
      docker push registry.cs.aalto.fi/<your username>/<image>:<tag>

    For example::

      docker pull library/ubuntu:latest
      docker tag library/ubuntu:latest registry.cs.aalto.fi/$USER/ubuntu:latest
      docker push registry.cs.aalto.fi/$USER/ubuntu:latest

    If you are building your image from Dockerfile, you can run::

      docker build -it registry.cs.aalto.fi/$USER/my_image:latest /path/to/my/dockerfile
      docker push registry.cs.aalto.fi/$USER/my_image:latest

    Step 5: Let us know what image you want to have in Triton
    ---------------------------------------------------------

    .. warning::
      Do note that images built to Triton are visible to all users.
      Do not include sensitive code/data in the docker images. You should retreive
      such data from your project/work folder during job runtime.

    We need the following information for the automatic build:

      - What is the Docker url of the image
        (e.g. ``registry.cs.aalto.fi/$USER/my_image``)?
      - What tags do you want built (we recommend you use ``latest`` and ``dev``)?
      - Does the image utilize GPUs?

    After that we'll set up the automated build. Every time you push a newer
    version of said ``image:tag`` the image will update in Triton if the build
    was successful.

    After the build has been done you can load up your new image in Triton with::

      module use /share/apps/singularity-ci/centos/modules/$USER
      module load my_image:latest

    and launch the programs within using the ``apptainer_wrapper exec``.
