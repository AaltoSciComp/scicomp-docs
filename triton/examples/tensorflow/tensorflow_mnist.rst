Simple Tensorflow/Keras model
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Let's run the MNIST example from
`Tensorflow's tutorials <https://github.com/tensorflow/docs/blob/master/site/en/tutorials/_index.ipynb>`_:

.. literalinclude:: /triton/examples/tensorflow/tensorflow_mnist.py
	 :lines: 24-29
	 :language: python

The full code for the example is in
:download:`tensorflow_mnist.py</triton/examples/tensorflow/tensorflow_mnist.py>`.
One can run this example with ``srun``:

.. code-block:: console

  $ wget https://raw.githubusercontent.com/AaltoSciComp/scicomp-docs/master/triton/examples/tensorflow/tensorflow_mnist.py
  $ module load scicomp-python-env
  $ srun --time=00:15:00 --gres=gpu:1 python tensorflow_mnist.py

or with ``sbatch`` by submitting
:download:`tensorflow_mnist.sh</triton/examples/tensorflow/tensorflow_mnist.sh>`:

.. literalinclude:: /triton/examples/tensorflow/tensorflow_mnist.sh
   :language: slurm

Do note that by default Keras downloads datasets to ``$HOME/.keras/datasets``.
