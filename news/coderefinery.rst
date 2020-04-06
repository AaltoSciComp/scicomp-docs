:orphan:

CodeRefinery
============

The NeIC sponsored CodeRefinery project is being hosted in `Otaniemi
from <cre2_>`_ (previously we had one in `Otaniemi from 12-14 December
<cre_>`_).  We highly recommend this workshop.  (note: It is full and
registration is closed).

.. _cre: https://coderefinery.org/workshops/2017-12-12-espoo/
.. _cre2: https://coderefinery.org/workshops/2018-05-29-espoo/

If you have an Aalto centrally-managed laptop, this page gives hints
on software installation.  You have to use these instructions
along with the CodeRefinery instructions.

.. note::

  These are only for the Aalto centrally managed laptops.  They are
  not needed if you have your own computer you administer yourself, or
  if you have an Aalto standalone computer you administer yourself).

.. warning::

   You should request primary user rights early, or else it won't be
   ready on time and you will have trouble installing things.  For
   Windows computers, request a wa (workstation admin) account.



Linux
=====

You need to be primary user in order to install your own packages.
Ask your IT support to make you if you aren't already.  You can check
with the ``groups`` command (see if you are in
``COMPUTERNAME-primaryuser``).

Install the required packages this way.  If you are primary user, you
will be asked to enter your own password::

  pkcon install bash git git-gui gitk git-cola meld gfortran gcc g++ build-essential snakemake sphinx-doc python3-pytest python3-pep8

For Python, we strongly recommend using Anaconda to get the latest
versions of software and to have things set up mostly automatically.

You should install Anaconda to your home directory like normal (this
is the best way to get the latest versions of the Python packages).
If your
default shell is ``zsh`` (this is the Aalto default, unless you changed
it yourself), then Anaconda won't be automatically put into the path.
Either: copy the relevant lines from ``.bashrc`` to ``.zshrc`` (you may
have to make this file), or just start ``bash`` before starting the
Anaconda programs.

Jupyter: use via Anaconda.

PyCharm: the "snap package" installer requires root, which most people
don't have.  Instead, download the standalone community file
(``.tar.gz``), unpack it, and then just run it using
``./pycharm.../bin/pycharm.sh``.  The custom script in ``/usr/loca/bin``
won't work since you aren't root, but you can make an alias in
``.bashrc`` or ``.zshrc``: ``alias pycharm=...`` (path here).

Docker: you can't easily do this on the Aalto laptops, but it is optional.

Mac
===

You also need to be primary user to install software.

If you are the primary user, in the Software Center you can install
"Get temporary admin rights".  This will allow you to become an
administrator for 30 minutes at a time.  Then, you can install
``.dmg`` files yourself (Use this for git, meld, cmake, docker).

Anaconda: you should be able to do "Install for me only".

Xcode can be installed via the Software Center.

Jupyter: use it via Anaconda, no need to install.


Windows
=======

You should request a workstation-admin account ("``wa account``"),
then you can install everything.  Note: these instructions are not
extensively tested.

Git and bash can be installed according to the instructions.

Visual diff tools: Needs wa-account.

Mingw: Not working, but seems to be because of download failing.

Cmake: Needs wa-account.

Docker: untested, likely requires wa-account.
