======
Python
======

The scientific python ecosystem is also available on Aalto Linux
workstations, including the anaconda (Python 3) and anaconda2
(Python2) modules providing
the Anaconda python distribution. For a more indepth description see
the generic `python page under scientific computing docs
</scicomp/python>`.


The "neuroimaging" environment
==============================

On the Aalto Linux workstations there exists a conda environment under the
anaconda3 module called "neuroimaging" which contains an extensive collection
of Python packages for the analysis of neuroimaging data, such as fMRI, EEG and
MEG.

To use it::

    $ ml purge
    $ ml anaconda3
    $ source activate neuroimaging

A more up-to-date yet under development version of the environment can be activated with::

    $ ml purge
    $ ml anaconda3
    $ source activate neuroimaging2

To see the full list of packages what are installed in the environment, use::

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

Note: this was tested only for NBE workstations. If you wish to run ``mne_analyze`` from your workstation you should follow this procedure. Open a new terminal and make sure you have the *bash* shell (``echo $SHELL``, if you do not have it, just type ``bash``) and then::

    $ module load mne
    $ source /work/modules/Ubuntu/14.04/amd64/common/mne/MNE-2.7.4-3434-Linux-x86_64/bin/mne_setup_sh
    $ export SUBJECTS_DIR=PATHTOSUBJECTFOLDER
    $ export SUBJECT=SUBJECTID
    $ mne_analyze

Please note that the path of the "source" command might change with most up to date versions of the tool. Please note that the "PATHTOSUBJECTFOLDER" and "SUBJECTID" are specific to the data you have. Please refer to MNE documentation for more help on these.


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

Notes for admins
----------------
The trick to getting Mayavi to play nicely with a modern Python environment is
to install it from Git::

    $ ml purge
    $ ml anaconda3
    $ source activate neuroimaging
    $ pip install git+https://github.com/enthought/traits.git@a7a83182048c08923953e302658b51b68c802132
    $ pip install git+https://github.com/enthought/pyface.git@13a064de48adda3c880350545717d8cf8929afad
    $ pip install git+https://github.com/enthought/traitsui.git@ee8ef0a34dfc1db18a8e2c0301cc18d96b7a3e2f
    $ pip install git+https://github.com/enthought/mayavi.git
