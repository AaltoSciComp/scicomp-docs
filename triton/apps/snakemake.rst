=========
Snakemake
=========

`Snakemake <https://snakemake.readthedocs.io/en/stable/>`_ is a workflow management tool. It is used to create reproducible and scalable data processing workflows (pipelines). 

Workflows are described via a human readable, Python based language. 

---------------
Example project
---------------

To get started using Snakemake on Triton, we have prepared `a git repo with a small example project <https://github.com/AaltoRSE/snakemake-triton-example>`_. 

You can clone the repo, follow the instructions in ``README.md`` to run the project on Triton, and use it as a starting point for your own workflow.

The project

#. follows the `recommended Snakemake project structure <https://snakemake.readthedocs.io/en/stable/snakefiles/deployment.html>`_,
#. uses conda environments for `integrated package management <https://snakemake.readthedocs.io/en/stable/snakefiles/deployment.html>`_,
#. uses the `Slurm executor plugin <https://snakemake.github.io/snakemake-plugin-catalog/plugins/executor/slurm.html>`_ to submit the workflow steps as cluster jobs,
#. decouples the workflow and Slurm resource configurations using a `Snakefile <https://snakemake.readthedocs.io/en/stable/snakefiles/rules.html>`_ and a `profile configuration file <https://snakemake.readthedocs.io/en/stable/executing/cli.html#profiles>`_, respectively.

