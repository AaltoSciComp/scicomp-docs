.. hint::

    During installation conda will
    `try to verify <https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-virtual.html>`_
    what is the maximum version of CUDA installed graphics cards can support
    and it will install non-CUDA enabled versions by default if none are found
    (as is the case on the login node, where environments are normally built).
    This can be usually overcome by setting explicitly that the packages should
    be the CUDA-enabled ones. It might however happen, that the environment
    creation process aborts with a message similar to:

    .. code-block:: bash

       nothing provides __cuda needed by tensorflow-2.9.1-cuda112py310he87a039_0

    In this instance it might be necessary to override the CUDA settings used by
    conda/mamba.
    To do this, prefix your environment creation command with ``CONDA_OVERRIDE_CUDA=CUDAVERSION``,
    where CUDAVERSION is the CUDA toolkit version you intend to use as in:

    .. code-block:: bash

       CONDA_OVERRIDE_CUDA="11.2" mamba env create -f cuda-env.yml

    This will allow conda to assume that the respective CUDA libraries will be
    present at a later point and so it will skip those requirements during
    installation.

    For more information, see this
    `helpful post in Conda-Forge's documentation <https://conda-forge.org/docs/user/tipsandtricks.html#installing-cuda-enabled-packages-like-tensorflow-and-pytorch>`_.
