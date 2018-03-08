=======================
Remote Jupyter Notebook
=======================

Here we describe how you can utilise Aalto computing resources for Jupyter Notebook remotely. The guide is targeted for UNIX users at the moment.

Aalto provides two “light computing” servers: ``brute.org.aalto.fi``, ``force.org.aalto.fi``. We demonstrate how to launch a Jupyter Notebook on ``brute`` and access it on your laptop.

.. figure:: /images/brute_htop.png
  :align: center
  :alt: alternate text
  :figclass: align-center

  < System activity on Brute > 


.. code-block:: bash
	
	ssh username@brute.org.aalto.fi

	# Create your Kerberos ticket
	kinit

	# Create a session. I use tmux
	tmux

	# Load Anaconda
	module use /work/modules/modulefiles/common/; module refresh; module load anaconda3

	# Create your env
	conda create -n env-name python=3.6 jupyter
	
	# Activate your python environment
	source activate env-name

	# Launch jupyter notebook in headless mode and a random port number
	jupyter notebook --no-browser --port=12520

Now back to your laptop

.. code-block:: bash
	
	# Forward the port 
	ssh -L 12520:localhost:12520 -N -f -l username brute.org.aalto.fi

Now launch your browser and go to http://localhost:12520 with your token.



