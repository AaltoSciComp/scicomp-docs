Detectron
=========

Detectron uses :doc:`Singularity containers </triton/usage/singularity>`,
so you should refer to that page first for general information.

Detectron-image is based on a 
`Dockerfile <https://github.com/facebookresearch/Detectron/blob/master/docker/Dockerfile>`_ 
from Detectron's repository. In this image Detectron has been installed to /detectron.

Usage
~~~~~

This example shows how you can launch Detectron on a gpu node. To run example
given in 
`Detectron repository <https://github.com/facebookresearch/Detectron/blob/master/GETTING_STARTED.md>`_
one can use the following :download:`Slurm script </triton/examples/detectron/detectron.slrm>`:

.. literalinclude:: /triton/examples/detectron/detectron.slrm

Now example can by run on GPU node with::

    sbatch detectron.slrm


In typical usage one does not want to download models for each run. To use 
stored models one needs to:

1. Copy detectron sample configurations from the image to your own configuration folder::

    module load singularity-detectron
    mkdir -p $WRKDIR/detectron/
    singularity_wrapper exec cp -r /detectron/configs $WRKDIR/detectron/configs
    cd $WRKDIR/detectron

2. Create data directory and download example models there::

    mkdir -p data/ImageNetPretrained/MSRA
    mkdir -p data/coco_2014_train:coco_2014_valminusminival/generalized_rcnn
    wget -O data/ImageNetPretrained/MSRA/R-101.pkl \
        https://s3-us-west-2.amazonaws.com/detectron/ImageNetPretrained/MSRA/R-101.pkl
    wget -O data/coco_2014_train:coco_2014_valminusminival/generalized_rcnn/model_final.pkl \
        https://s3-us-west-2.amazonaws.com/detectron/35861858/12_2017_baselines/e2e_mask_rcnn_R-101-FPN_2x.yaml.02_32_51.SgT4y1cO/output/train/coco_2014_train:coco_2014_valminusminival/generalized_rcnn/model_final.pkl

4. Edit the weights-parameter in configuration file *12_2017_baselines/e2e_mask_rcnn_R-101-FPN_2x.yaml*::

    33c33
    <   WEIGHTS: $WRKDIR/detectron/data/ImageNetPretrained/MSRA/R-101.pkl
    ---
    >   WEIGHTS: https://s3-us-west-2.amazonaws.com/detectron/ImageNetPretrained/MSRA/R-101.pkl

5. Edit :download:`Slurm script </triton/examples/detectron/detectron2.slrm>` to
   point to downloaded weigths and models:

.. literalinclude:: /triton/examples/detectron/detectron2.slrm

6. Submit job::

    sbatch detectron.slrm

