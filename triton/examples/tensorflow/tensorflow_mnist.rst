Simple Tensorflow/Keras model
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Let's run the MNIST example from 
`Tensorflow's tutorials <https://github.com/tensorflow/docs/blob/master/site/en/tutorials/_index.ipynb>`_.
The model for the example is in 
:download:`tensorflow_mnist.py</triton/examples/tensorflow/tensorflow_mnist.py>`:

.. literalinclude:: /triton/examples/tensorflow/tensorflow_mnist.py
	 :lines: 17-

One can run this example with `srun`::

  module load anaconda3/latest
  srun -t 00:15:00 --gres=gpu:1 python tensorflow_mnist.py

or with `sbatch` by submitting
:download:`tensorflow_mnist.slrm</triton/examples/tensorflow/tensorflow_mnist.sh>`:

.. literalinclude:: /triton/examples/tensorflow/tensorflow_mnist.sh
