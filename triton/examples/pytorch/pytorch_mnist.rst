Simple PyTorch model
--------------------

Let's run the MNIST example from
`PyTorch's tutorials <https://github.com/pytorch/examples/blob/master/mnist/main.py>`_:

.. literalinclude:: /triton/examples/pytorch/pytorch_mnist.py
   :lines: 45-61
   :language: python

The full code for the example is in
:download:`pytorch_mnist.py</triton/examples/pytorch/pytorch_mnist.py>`.
One can run this example with ``srun``:

.. code-block:: console

  $ wget https://raw.githubusercontent.com/AaltoSciComp/scicomp-docs/master/triton/examples/pytorch/pytorch_mnist.py
  $ module load scicomp-python-env
  $ srun --time=00:15:00 --mem=4G --gpus=1 python pytorch_mnist.py

or with ``sbatch`` by submitting
:download:`pytorch_mnist.sh</triton/examples/pytorch/pytorch_mnist.sh>`:

.. literalinclude:: /triton/examples/pytorch/pytorch_mnist.sh
   :language: slurm

The new module ``scicomp-pytorch-env/2026.1`` can also be used to run the example, but you will need to specify the min CUDA version in your batch script.

:download:`pytorch_mnist_min_cuda.sh</triton/examples/pytorch/pytorch_mnist_min_cuda.sh>`:

.. literalinclude:: /triton/examples/pytorch/pytorch_mnist_min_cuda.sh
   :language: slurm


The Python-script will download the MNIST dataset to ``data`` folder.
