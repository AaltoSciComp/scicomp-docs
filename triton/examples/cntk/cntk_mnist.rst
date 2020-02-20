Simple CNTK model
~~~~~~~~~~~~~~~~~

Let's run the MNIST example from
`CNTK's tutorials <https://github.com/microsoft/CNTK/blob/release/latest/Examples/Image/Classification/MLP/Python/SimpleMNIST.py>`_:

.. literalinclude:: /triton/examples/cntk/cntk_mnist.py
	 :lines: 58-65

The full code for the example is in
:download:`cntk_mnist.py</triton/examples/cntk/cntk_mnist.py>`.
One can run this example with ``srun``::

  wget https://raw.githubusercontent.com/AaltoScienceIT/scicomp-docs/master/triton/examples/cntk/cntk_mnist.py
  module load anaconda
  srun -t 00:15:00 --gres=gpu:1 python cntk_mnist.py

or with ``sbatch`` by submitting
:download:`cntk_mnist.sh</triton/examples/cntk/cntk_mnist.sh>`:

.. literalinclude:: /triton/examples/cntk/cntk_mnist.sh

Do note that datasets in the code come from ``/scratch/scip/data/cntk/MNIST``.
Thus model won't run outside of Triton. Check the
`CNTK GitHub repo <https://github.com/microsoft/CNTK>`_ for the whole example.
