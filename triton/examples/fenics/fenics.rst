Fenics
======

This uses :doc:`Singularity containers </triton/usage/singularity>`,
so you should refer to that page first for general information.

Fenics-images are based on `these images <https://quay.io/repository/fenicsproject/stable?tab=tags>`_.

Usage
~~~~~

This example shows how you can run a fenics example. To run example one should 
first copy the examples from the image to a suitable folder::

    mkdir -p $WRKDIR/fenics
    cd $WRKDIR/fenics
    module load singularity-fenics
    singularity_wrapper exec cp -r /usr/local/share/dolfin/demo demo

The examples try to use interactive windows to plot the results. This is not
available in the batch queue so to fix this one needs to specify an
alternative matplotlib backend. 
:download:`This </triton/examples/fenics/fenics_matplotlib.patch>` patch file
fixes example *demo_poisson.py*. Download it into ``$WRKDIR/fenics`` and run

.. code-block:: bash

    patch -d demo -p1 < fenics_matplotlib.patch 

to fix the example. After this one can run the example with the following
:download:`Slurm script </triton/examples/fenics/fenics.slrm>`:

.. literalinclude:: /triton/examples/fenics/fenics.slrm

To submit the script one only needs to run::

    sbatch fenics.slrm

Resulting image can be checked with e.g.::

    eog demo/documented/poisson/python/poisson.png
