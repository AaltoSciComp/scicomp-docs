Running simple PyTorch model with NVIDIA's containers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Let's run the MNIST example from
`PyTorch's tutorials <https://github.com/pytorch/examples/blob/master/mnist/main.py>`_:

.. literalinclude:: /triton/examples/pytorch/pytorch_mnist.py
	 :lines: 45-61

The full code for the example is in
:download:`pytorch_mnist.py</triton/examples/pytorch/pytorch_mnist.py>`.
One can run this example with ``srun``::

  wget https://raw.githubusercontent.com/AaltoSciComp/scicomp-docs/master/triton/examples/pytorch/pytorch_mnist.py
  module load nvidia-pytorch/20.02-py3
  srun -t 00:15:00 --gres=gpu:1 singularity_wrapper exec python pytorch_mnist.py

or with ``sbatch`` by submitting
:download:`pytorch_singularity_mnist.sh</triton/examples/pytorch/pytorch_singularity_mnist.sh>`:

.. literalinclude:: /triton/examples/pytorch/pytorch_singularity_mnist.sh

The Python-script will download the MNIST dataset to ``data`` folder.
