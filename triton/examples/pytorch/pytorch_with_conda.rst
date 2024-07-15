Creating an environment with GPU enabled PyTorch
""""""""""""""""""""""""""""""""""""""""""""""""

To create an environment with GPU enabled PyTorch you can use an
environment file like this
:download:`pytorch-env.yml </triton/examples/pytorch/pytorch-env.yml>`:

.. literalinclude:: /triton/examples/pytorch/pytorch-env.yml

Here we install the latest pytorch version from ``pytorch``-channel and
the ``pytorch-cuda``-metapackage that makes certain that the

Additional packages required by pytorch
are installed from ``conda-forge``-channel.
