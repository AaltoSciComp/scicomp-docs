Running simple Tensorflow/Keras model with NVIDIA's containers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Let's run the MNIST example from
`Tensorflow's tutorials <https://github.com/tensorflow/docs/blob/master/site/en/tutorials/_index.ipynb>`_:

.. literalinclude:: /triton/examples/tensorflow/tensorflow_mnist.py
	 :lines: 24-29

The full code for the example is in
:download:`tensorflow_mnist.py</triton/examples/tensorflow/tensorflow_mnist.py>`.
One can run this example with ``srun``::

  wget https://raw.githubusercontent.com/AaltoSciComp/scicomp-docs/master/triton/examples/tensorflow/tensorflow_mnist.py
  module load nvidia-tensorflow/20.02-tf1-py3
  srun -t 00:15:00 --gres=gpu:1 singularity_wrapper exec python tensorflow_mnist.py

or with ``sbatch`` by submitting
:download:`tensorflow_singularity_mnist.sh</triton/examples/tensorflow/tensorflow_singularity_mnist.sh>`:

.. literalinclude:: /triton/examples/tensorflow/tensorflow_singularity_mnist.sh

Do note that by default Keras downloads datasets to ``$HOME/.keras/datasets``.
