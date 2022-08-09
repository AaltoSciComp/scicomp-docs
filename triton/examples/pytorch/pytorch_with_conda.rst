Creating an environment with GPU enabled PyTorch
------------------------------------------------

To create an environment with GPU enabled PyTorch you can use an
environment file like this
:download:`pytorch-env.yml </triton/examples/pytorch/pytorch-env.yml>`:

.. literalinclude:: /triton/examples/pytorch/pytorch-env.yml

Here we install the latest pytorch vesion from ``pytorch``-channel with an additional
requirement that the build version of the ``pytorch``-package must contain
a reference to a cuda toolkit. Additional packages required by pytorch
are installed from ``conda-forge``-channel. For a specific version replace the 
``=*=*cuda*`` with e.g. ``=1.12=*cuda*`` for version ``1.12``.
