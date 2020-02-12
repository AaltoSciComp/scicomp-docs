Simple PyTorch model
~~~~~~~~~~~~~~~~~~~~

Let's run the MNIST example from
`PyTorch's tutorials <https://github.com/pytorch/examples/blob/master/mnist/main.py>`_:

.. literalinclude:: /triton/examples/pytorch/pytorch_mnist.py
	 :lines: 45-61

The full code for the example is in
:download:`tensorflow_mnist.py</triton/examples/pytorch/pytorch_mnist.py>`.
One can run this example with ``srun``::

  wget https://raw.githubusercontent.com/AaltoScienceIT/scicomp-docs/master/triton/examples/pytorch/pytorch_mnist.py
  module load anaconda
  srun -t 00:15:00 --gres=gpu:1 python pytorch_mnist.py

or with ``sbatch`` by submitting
:download:`pytorch_mnist.sh</triton/examples/pytorch/pytorch_mnist.sh>`:

.. literalinclude:: /triton/examples/pytorch/pytorch_mnist.sh

The Python-script will download the MNIST dataset to ``data`` folder.
