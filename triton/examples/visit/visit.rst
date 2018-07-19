VisIT
=====

This uses :doc:`Singularity containers </triton/usage/singularity>`,
so you should refer to that page first for general information.

Visit has been compiled using the build_visit-script from the VisIT page on an
Ubuntu image. It has minimal amount of other software installed.

Parallelization is done against Triton's OpenMPI, so using this container
with other OpenMPI modules is discouraged.

Within the container VisIT is installed under ``/opt/visit/``. PATH is
automatically appended with their respective paths so all program calls are 
available automatically.

Usage
~~~~~

This example shows how you can launch visit on the login node for small
visualizations or launch it in multiprocess state on a reserved node. Firstly, 
let's load the module::

    module use /share/apps2/singularity/modules
    module load Visit

Now you can run VisIT with::

    singularity_wrapper exec visit

If you want to run VisIT with multiple CPUs, you should reserve a node with
``sinteractive``::

    sinteractive -t 00:30:00 -n 2 -N 1-1
    singularity_wrapper exec visit -np 2

Do note the flag ``-N 1-1`` that ensures that all of VisITs processes end up
on the same node. Currently VisIT encounters problems when going across the
node lines.
