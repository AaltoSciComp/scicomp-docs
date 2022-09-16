Creating an environment with packages requiring CUDA
----------------------------------------------------

Many tools check, whether the system has a cuda capable graphics card set up
and will install non cuda enabled versions by default if none is found (as is 
the case on the login node, where environments are normally built). This can 
be overcome by loading cuda specific versions (as detailed below).
It might however happen, that the environment creation process aborts with a 
message similar to:

.. code-block:: bash

   nothing provides __cuda needed by tensorflow-2.9.1-cuda112py310he87a039_0
  
In this instance it might be necessary to override the CUDA settings used by 
conda/mamba. 
To do this, prefix your environment creation command with ``CONDA_OVERRIDE_CUDA=CUDAVERSION``, 
where CUDAVERSION is the Cuda toolkit version you intend to use as in:

.. code-block:: bash

   CONDA_OVERRIDE_CUDA="11.2" mamba env create -f cuda-env.yml

This will allow conda to assume that the respective cuda libraries will be 
present at a later point but skip those requirements during installation.

