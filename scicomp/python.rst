======
Python
======

The scientific python ecosystem is also available on Aalto Linux
workstations, including the anaconda2 and anaconda3 modules providing
the Anaconda python distribution. For a more indepth description see
`python page under triton docs </triton/apps/python>`.


The "brain" environment with mayavi
===================================

On the Aalto Linux workstations there exists a conda environment under
the anaconda2 module called "brain" which contains the mayavi
visualization tool, mne, and pysurfer. Many of the packages in this
environment are older than those in the main "root" environment
because mayavi is incompatible with many newer packages. Thus it's not
possible to install mayavi to the main root environment, and a
separate environment is needed. To use it::

    $ ml purge
    $ ml anaconda2
    $ source activate brain

If you wish to use mayavi from the ipython terminal console or from
the qtconsole, you need to additionally set the environment variable::

    $ export ETS_TOOLKIT=wx

If you use the spyder IDE, then you need to set Tools -> Preferences
-> Ipython console -> Graphics -> Backend: Qt.

Finally, if you get binaries from the wrong environment (check with
"which BINARYNAME") you may need to update the mappings with::

    $ rehash


Installation (for admins)
-------------------------

The environment was created with the commands::

    $ ml purge
    $ ml anaconda2
    $ conda create -n brain mayavi anaconda wxpython
    $ source activate brain
    $ pip install mne pysurfer

DO NOT TRY TO UPGRADE THE ENVIRONMENT (conda upgrade --all), at least
spyder breaks.
