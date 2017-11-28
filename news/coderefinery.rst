CodeRefinery
============

The NeIC sponsored CodeRefinery project is being hosted in `Otaniemi
from 12-14 December <cre_>`_.  We highly recommend this workshop.
(note: It is full and registration is closed).

.. _cre: http://coderefinery.org/workshops/2017-12-12-espoo/

If you have an Aalto centrally-managed laptop, this page gives hints
on software installation.  (These are not needed if you have your own
computer you administer yourself, or if you have an Aalto standalone
computer you administer yourself).  You have to use these instructions
along with the CodeRefinery instructions.



Linux
=====

You need to be primary user in order to install your own packages.
Ask your IT support to make you if you aren't already.  You can check
with the ``groups`` command (see if you are in
``COMPUTERNAME-primaryuser``).

Install the required packages this way.  If you are primary user, you
will be asked to enter your own password::

  pkcon install bash git git-gui gitk git-cola meld gfortran gcc g++ build-essential cmake sphinx-doc python-pytest python-pep8 python-cffi

  pkcon install python-numpy python-scipy python-matplotlib python-pandas python-seaborn cython

TODO: jupyter, possibly use anaconda instead.



Mac
===

You also need to be primary user to install software.

If you are, in the software center you can install "Get temporary
admin rights".  This will allow you to become an administrator for 30
minutes at a time.  Then, you can install ``.dmg`` files yourself
(Use this for git, meld, cmake).

Anaconda: you should be able to do "Install for me only".

Xcode can be installed via the software center.

Jupyter: use it via Anaconda



Windows
=======

No instructions yet.
