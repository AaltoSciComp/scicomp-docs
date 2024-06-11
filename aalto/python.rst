=====================
Python on Aalto Linux
=====================

The scientific python ecosystem is also available on Aalto Linux
workstations (desktops),
including the anaconda (Python 3) and anaconda2 (Python 2) modules providing
the Anaconda python distribution. For a more indepth description see the
generic `python page under scientific computing docs </scicomp/python>`.

On Aalto Linux Laptops, these instructions don't work.  Instead, we'd
recommend installing Anaconda or Miniconda yourself and then you can
manage packages via environments.  You can also install Python
packages through the package manager, but that can have problems with
installing your own libraries if not managed carefully.

.. highlight:: console


Anaconda on Aalto Linux
=======================

You can mostly use Python like normal - see :doc:`/scicomp/python`.

To create your own anaconda environments, first load the Anaconda module::

   $ module load anaconda

then you get the ``conda`` command.  If you get an error such as::

  NotWritableError: The current user does not have write permissions to a required path.
  path: /m/work/modules/automatic/anaconda/envs/aalto-ubuntu1804-generic/software/anaconda/2020-04-tf2/1b2b24f2/pkgs/cache/18414ddb.json

Try the following to solve it (this prevents conda from trying to
store its downloaded files in the shared directory)::

   $ conda config --prepend pkgs_dirs ~/.conda/pkgs



The "neuroimaging" environment
==============================

On the Aalto Linux workstations and Triton, there is a conda environment which
contains an extensive collection of Python packages for the analysis of
neuroimaging data, such as fMRI, EEG and MEG.

To use it on Aalto Ubuntu workstations and VDI::

    $ ml purge
    $ ml anaconda3
    $ source activate neuroimaging

To use it on the new Triton (as of May 2024)::

    $ ml purge
    $ ml neuroimaging-env

Note that the module name has changed on the new Triton, to make it clearer that this is *not* the same neuroimaging environment as it was in the old Triton. If you need exactly the same old environments, please get in touch. **This it not working anymore:** To see the full list of packages what are installed in the environment, use::

    $ conda list

Some highlights include:

- Basic scientific stack

  - numpy
  - scipy
  - matplotlib
  - pandas
  - statsmodels

- fMRI:

  - nibabel
  - nilearn
  - nitime
  - pysurfer

- EEG/MEG:

  - mne
  - pysurfer

- Machine learning:

  - scikit-learn
  - tensorflow
  - pytorch

- R:

  - rpy2 (bridge between Python and R)
  - tidyverse

Finally, if you get binaries from the wrong environment (check with
``which BINARYNAME``) you may need to update the mappings with::

    $ rehash

MNE Analyze
-----------

Note: this was tested only for NBE workstations. If you wish to run
``mne_analyze`` from your workstation you should follow this procedure. Open a
new terminal and make sure you have the *bash* shell (``echo $SHELL``, if you
do not have it, just type ``bash``) and then::

    $ module load mne
    $ source /work/modules/Ubuntu/14.04/amd64/common/mne/MNE-2.7.4-3434-Linux-x86_64/bin/mne_setup_sh
    $ export SUBJECTS_DIR=PATHTOSUBJECTFOLDER
    $ export SUBJECT=SUBJECTID
    $ mne_analyze

Please note that the path of the "source" command might change with most up to
date versions of the tool. Please note that the "PATHTOSUBJECTFOLDER" and
"SUBJECTID" are specific to the data you have. Please refer to MNE
documentation for more help on these.


Mayavi
------
If you experience problems with the 3D visualizations that use Mayavi (for
example MNE-Python's brain plots), you can try forcing the graphics backend to
Qt5:

- For the Spyder IDE, set Tools -> Preferences -> Ipython console -> Graphics
  -> Backend: Qt5
- For the ipython consoles, append ``c.InteractiveShellApp.matplotlib = 'qt5'``
  to the ``ipython_config.py`` and ``ipython_kernel_config.py`` configuration
  files. By default, these can be found in ``~/.ipython/profile/default/``.
- In Jupyter notebooks, execute the magic command ``%matplotlib qt5`` at the
  beginning of your notebook.

Installation of additional packages
-----------------------------------
The "neuroimaging" environment aims to provide everything you need for the
analysis of neuroimaging data. If you feel a package is missing that may be
useful for others as well, contact `Marijn van Vliet
<marijn.vanvliet@aalto.fi>`_. To quickly install a package in your home folder,
use ``pip install <package-name> --user``.
