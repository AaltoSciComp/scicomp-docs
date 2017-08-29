Singularity Containers
----------------------

For more information see: http://singularity.lbl.gov/

Before usage
~~~~~~~~~~~~

Due to the 'work in progress'-designation, singularity containers are
not available by default to all users. To start using them you need to
run

bash

::

    module use /share/apps/singularity/modules/

Basic Idea
~~~~~~~~~~

Basic Idea behind Singularity containers is that software is packaged
into a container that is based on a Linux image or Docker image that can
then be run by the user.

During runtime the root file system "/" is changed to the one inside the
image and file systems are brought into the container through bind
mounts. This sounds complicated, but in practice this is easy due to
singularity\_wrapper written for Triton.

Basic Usage
~~~~~~~~~~~

While the image itself is read-only, remember that /home, /m, /scratch
and /l etc. are not. If you edit/remove files in these locations within
the image, that will happen outside the image as well.

Singularity enables three base commands to user:

#. singularity shell <image> - Gives user a shell within the image (see
   "singularity shell --help" for more information on flags etc.)
#. singularity exec <image> <cmd> - Executes a program within the image
   (see "singularity exec --help" for more information on flags etc.)
#. singularity run <image> <parameters> - Runs the singularity image.
   What this means depends on the image in question. (see "singularity
   run --help" for more information on flags etc.)

These commands can be used, but we recommend using singularity\_wrapper
instead.

All different images can be found from /share/apps/singularity/images

singularity\_wrapper
~~~~~~~~~~~~~~~~~~~~

singularity\_wrapper is written so that when you load a module written
for a singularity image, singularity\_wrapper knows what parameters to
use. Differences include:

#. Choosing version appropriate image
#. Binding of basic paths (-B /l:/l, -B /m:/m, /scratch:/scratch)
#. Setting working directory within image (if needed)
#. Loading of CUDA libraries within images (if needed) (-B
   /lib64/`nvidia:/libhost <http://nvidia/libhost>`__)

singularity\_wrapper enables the three base commands, but with small
differences:

#. singularity\_wrapper shell <shell> - Gives user the requested shell
   within the image
#. singularity\_wrapper exec <cmd> - Executes a program within the
   image.
#. singularity run <parameters> - Runs the singularity image. What this
   means depends on the image in question.

Applications
------------

OpenFOAM and ParaView
~~~~~~~~~~~~~~~~~~~~~

OpenFOAM and ParaView have been installed from the Ubuntu 16.04 Docker
image provided by OpenFOAM people. It has minimal amount of other
software installed.

Within the container OpenFOAM is installed under /opt/openfoam4/ and
ParaView under /opt/paraviewopenfoam50/. PATH is automatically appended
with their respective paths so all program calls are available
automatically.

Usage
^^^^^

This example shows how you can run damBreak example. Firstly, let's load
the OpenFOAM module and create a folder for the example

bash

::

    module use /share/apps/singularity/modules
    module load OpenFOAM
    mkdir damBreak
    cd damBreak

Secondly, let's use singularity shell to copy example data files to the
folder and to initialize the simulation.

bash

::

    cp -r /opt/openfoam4/tutorials/multiphase/interFoam/laminar/damBreak/damBreak/0 .
    cp -r /opt/openfoam4/tutorials/multiphase/interFoam/laminar/damBreak/damBreak/system .
    cp -r /opt/openfoam4/tutorials/multiphase/interFoam/laminar/damBreak/damBreak/constant .
    blockMesh
    decomposePar
    exit

After this one can submit the following slurm script with sbatch to
solve the problem:

 

bash

::

    #!/bin/bash
    #SBATCH -p short
    #SBATCH -t 00:30:00
    #SBATCH -n 4
    #SBATCH --mem=4G

    module purge
    module load OpenFOAM

    srun singularity_wrapper exec interFoam -parallel

Paraview can be started similarly.

::

    #!/bin/bash
    #SBATCH -p short
    #SBATCH -t 00:10:00
    #SBATCH -n 1
    #SBATCH --mem=8G

    module purge
    module load OpenFOAM

    singularity_wrapper exec paraview

 

OpenPose
~~~~~~~~

OpenPose has been compiled against system OpenBLAS and most recent
Caffe, CUDA and cuDNN. Image is based on a Ubuntu 16.04 base image.

Within the container OpenPose is installed under /opt/openpose. Due to
the way the examples are organized, the singularity\_wrapper changes the
working directory to /opt/openpose.

Usage
^^^^^

bash

::

    #!/bin/bash
    #SBATCH -p gpushort
    #SBATCH -t 00:10:00
    #SBATCH -n 1
    #SBATCH --gres=gpu:teslak80:1
    #SBATCH --mem=8G

    module purge
    module load OpenPose

    singularity_wrapper exec ./build/examples/openpose/openpose.bin --video examples/media/video.avi --no_display --write_video $WRKDIR/openpose.avi
