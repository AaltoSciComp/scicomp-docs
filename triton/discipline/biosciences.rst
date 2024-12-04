==========
Bioscience
==========

neuroimaging environment on Triton
----------------------------------
On the Aalto Linux workstations and Triton, there is a conda environment which
contains an extensive collection of Python packages for the analysis of
neuroimaging data, such as fMRI, EEG and MEG.

Since the module system got an update along with the last overhaul of Triton in 2024, there are currently two versions of this module in use. 
On the workstations and VDI, the old module can be obtained by:: 

    $ ml purge
    $ ml anaconda3
    $ source activate neuroimaging

To see the full list of packages what are installed in the environment, use::

    $ conda list

An update of the module system for the workstations and VDI is currently (as of November 2024) under development. If you need the new module on the workstations, contact us.

On Triton, you load the neuroimaging environment by:: 

    $ ml purge
    $ ml neuroimaging-env



snakemake
---------

Snakemake is a workflow management system, that is it is a tool to make your workflow reproducible and especially scalable with minimal effort. Documentation can be found at https://snakemake.readthedocs.io/en/stable/index.html 

On Triton, Aalto workstations and VDI you can load a standalone module via:: 
 
    $ ml snakemake