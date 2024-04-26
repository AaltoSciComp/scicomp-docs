.. list-table::
   :header-rows: 1

   * * Command
     * Description
   * * ``module load mamba``
     * Load module that provides conda/mamba Triton, for use making
       your own environments.  ``mamba`` is a faster drop-in
       replacement for ``conda``.
   * * :ref:`conda-first-time-setup`
     * See link for six commands to run once per user account on
       Triton (to avoid filling up all space on your home directory).
   * * .. code-block:: yaml

         name: conda-example
         channels:
           - conda-forge
         dependencies:
           - numpy
           - pandas
     * Minimal ``environment.yml`` example.  By defining our requirements
       in one place, our environment becomes reproducible and we can
       solve problems by re-creating it.  "Dependencies" lists
       packages that will be installed.
   * * **Environment management:**
     *
   * * ``mamba env create --file environment.yml``
     * Create environment from yaml file.  Use ``-n NAME`` to set or
       override the name from the .yml file.  Environments with ``-n``
       are stored in ``conda config --show envs_dirs``.
   * * ``source activate NAME``
     * Activate environment of name NAME.  Note we use this and *not*
       ``conda init``/``conda activate`` to avoid changing Python for your whole
       account.
   * * ``source deactivate``
     * Deactivate conda from this session.
   * * ``conda env list``
     * List all environments.
   * * ``conda env remove -n NAME``
     * Remove the environment of that name.
   * * **Package management:**
     * Inside the activate environment
   * * ``conda list``
     * List packages in currently active environment.
   * * ``conda install --freeze-installed --channel CHANNEL PACKAGE_NAME``
     * Install packages in an environment with minimal changes to what
       is already installed.  Usually you would want to go at add them
       to environment.yml if it is a dependency.  Better: add to
       environment.yml and then see next line.
   * * ``conda env update --file environment.yml``
     * Update an environment file based on environment.yml
   * * ``conda env export``
     * Export an environment.yml that describes the current
       environment.  Add ``--no-builds`` to make it more portable
       across operating systems.  Add ``--from-history`` to list only
       what you have explicitly requested in the past.
   * * ``conda search [--channel conda-forge] NAME``
     * Search for a package.  List includes name, version, build
       version (often including linked libraries like Python/CUDA), and
       channel.
   * * **Other:**
     *
   * * ``mamba ...``
     * Use ``mamba`` instead of ``conda`` for faster operations.
       ``mamba`` is a drop-in replacement.  It should be installed in
       the environment.
   * * ``conda clean -a``
     * Clean up cached files to free up space (not environments or
       packages in them).
   * * ``CONDA_OVERRIDE_CUDA="11.2" conda ..``
     * Used when making CUDA environment on login node (choose right
       CUDA version for you). Used with ``... env create`` or
       ``... install`` to indicate that CUDA will be available when
       the program runs.
   * * Channel ``conda-forge``

       Package selection ``tensorflow=*=*cuda*``
     * Package selection for tensorflow.  The first ``*`` can be
       replaced with the Tensorflow version specification
   * * Channels ``pytorch`` and ``conda-forge``

       Package selection ``pytorch=*=*cuda*``
     * Package selection for pytorch.  The first ``*`` can be replaced
       with the pytorch version specification.
   * * CUDA
     * In channel conda-forge, automatically selected based on
       software you need.  For manual compilation, package
       ``cudatoolkit`` in conda-forge.
