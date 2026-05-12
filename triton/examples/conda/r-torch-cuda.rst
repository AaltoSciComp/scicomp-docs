To create an environment with GPU enabled Torch you can use an
environment file like this:

.. code-block:: yaml

    name: r-torch-cuda
    channels:
      - conda-forge
    dependencies:
      - r-torch
      - cudatoolkit

Here we include cudatoolkit in the environment. The
r-torch installer should find the CUDA toolking and
enable GPU support in Torch.

Once the environment is created, install Torch in
R with

.. code-block:: r

    > library(torch)
    > install_torch()