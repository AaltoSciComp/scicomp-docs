Creating an environment with GPU enabled Tensorflow
"""""""""""""""""""""""""""""""""""""""""""""""""""

To create an environment with GPU enabled Tensorflow you can use an
environment file like this
:download:`tensorflow-env.yml </triton/examples/tensorflow/tensorflow-env.yml>`:

.. literalinclude:: /triton/examples/tensorflow/tensorflow-env.yml

Here we install the latest tensorflow from ``conda-forge``-channel with an additional
requirement that the build version of the ``tensorflow``-package must contain
a reference to a CUDA toolkit. For a specific version replace the ``=*=*cuda*`` with e.g. ``=2.8.1=*cuda*`` for version ``2.8.1``.


