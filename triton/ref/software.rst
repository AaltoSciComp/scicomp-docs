* **Python:** ``module load scicomp-python-env`` for the Aalto Scientific
  Computing managed Python environment with common packages. :doc:`More info
  <../apps/python>`.

  * ``module load mamba`` for mamba/conda for making your own
    environments (:ref:`see below <ref-conda>`)

  .. note:: For PyTorch users: ``scicomp-python-env`` only supports older GPUs (V100s). 
     For newer GPUs (B300s), use the PyTorch-specific environment below.

* **PyTorch:** ``module load scicomp-pytorch-env/2026.1`` for the latest PyTorch environment 
  optimized for newer GPUs (B300s) with common deep learning packages. :doc:`More info
  <../apps/pytorch>`.

* **R:** ``module load r`` for a basic R package.  :doc:`More info
  <../apps/r>`.

  * ``module load scicomp-r-env`` for an R module with various
    packages pre-installed

* **Matlab:** ``module load matlab`` for the latest Matlab version.
  :doc:`More info <../apps/matlab>`.
