Detectron
=========

In this image Detectron has been installed to /detectron.

Usage
~~~~~

This example shows how you can launch Detectron on a gpu node. To run example
given in 
`Detectron repository <https://github.com/facebookresearch/Detectron/blob/master/GETTING_STARTED.md>`
one can use the following :download:`Slurm script </triton/examples/openfoam/paraview.slrm>`:

.. literalinclude:: /triton/examples/detectron/detectron.slrm


Simply running:: 
    sbatch detectron.slrm

Will run the example on a GPU node.
