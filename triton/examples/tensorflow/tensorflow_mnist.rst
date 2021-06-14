Simple Tensorflow/Keras model
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Let's run the MNIST example from
`Tensorflow's tutorials <https://github.com/tensorflow/docs/blob/master/site/en/tutorials/_index.ipynb>`_:

.. literalinclude:: /triton/examples/tensorflow/tensorflow_mnist.py
	 :lines: 24-29
	 :language: python

The full code for the example is in
:download:`tensorflow_mnist.py</triton/examples/tensorflow/tensorflow_mnist.py>`.
One can run this example with ``srun``::

  wget https://raw.githubusercontent.com/AaltoSciComp/scicomp-docs/master/triton/examples/tensorflow/tensorflow_mnist.py
  module load anaconda
  srun --time=00:15:00 --gres=gpu:1 python tensorflow_mnist.py

or with ``sbatch`` by submitting
:download:`tensorflow_mnist.sh</triton/examples/tensorflow/tensorflow_mnist.sh>`:

.. literalinclude:: /triton/examples/tensorflow/tensorflow_mnist.sh
   :language: slurm

Do note that by default Keras downloads datasets to ``$HOME/.keras/datasets``.

For users of Kale and Turso, Tensorflow requires the use of a virtual environment on the ``gpu`` node. You will be able to run the example through the default node but to run using ``--gres=gpu:1`` you need to set up a virtual environment. Instructions for setting one up can be found `here <https://wiki.helsinki.fi/display/it4sci/Module+System>`__, under *Virtual Environments*.
