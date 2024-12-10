==========
Bioscience
==========

Neuroimaging environment on Triton
----------------------------------
On the Aalto Linux workstations and Triton, there is a conda environment which
contains an extensive collection of Python packages for the analysis of
neuroimaging data, such as fMRI, EEG and MEG.

Since the module system got an update along with the last overhaul of Triton in 2024, there are currently two versions of this module in use. 
On the workstations and VDI, the old module can be obtained by:: 

    $ ml purge
    $ ml anaconda3
    $ source activate neuroimaging

To see the full list of packages installed in the environment, use::

    $ conda list

An update of the module system for the workstations and VDI is currently (as of November 2024) under development. If you need the new module on the workstations, contact us.

On Triton, you load the neuroimaging environment by:: 

    $ ml purge
    $ ml neuroimaging-env



snakemake
---------

Snakemake is a workflow management system, that is it is a tool to make your workflow reproducible and, more importantly, scalable with minimal effort. Documentation for snakemake on Triton is at :doc:`Snakemake  <../apps/snakemake>`.

In addition to building your own environment for snakemake, as described in the documentation above, both the neuroimaging module and the scicomp-python module include snakemake, which you can get via::

    $ ml purge
    $ ml neuroimaging-env

or::

    $ ml purge
    $ ml scicomp-python-env

If for some reason using an environemnt is not possible, you can load a standalone module via:: 
 
    $ ml snakemake

