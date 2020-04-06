=======
Jupyter
=======

.. note:: Quick link

   Triton's JupyterHub is available at
   https://jupyter.triton.aalto.fi.

.. note:: For new users

   Are you new to Triton and want to access JupyterHub?  Triton is a
   high-performance computing cluster, and JupyterHub is just one of
   our services - one of the easiest ways to get started.  You still
   need a Triton account.  This site has many instructions, but you
   should read at least:

   * :doc:`About us <../tut/intro>`, :doc:`how to get help
     <../help>`, and :doc:`acknowledging Triton
     usage<../acknowledgingtriton>` (this JupyterHub is part of
     Triton, and thus Science-IT must be acknowledged in publications).
   * :doc:`The accounts page <../accounts>`, in order to request a
     Triton account.
   * Possibly the :doc:`storage page <../tut/storage>` to learn about
     the places to store data and how to transfer data.
   * The JupyterHub section of this page (below).

   If you want to use Triton more, you should finish the entire
   :ref:`tutorials section <tutorials>`.

.. figure:: /images/jupyter_demo.gif
   :scale: 60%
   :align: center
   :alt: alternate text
   :figclass: align-center

   < Triton JupyterHub Demo >

Jupyter notebooks are a way of interactive, web-based computing:
instead of either scripts or interactive shells, the notebooks allow
you to see a whole script + output and experiment interactively and
visually.  They are good for developing and testing things, but once
things work and you need to scale up, it is best to put your code into
proper programs (:doc:`more info </scicomp/jupyter-pitfalls>`).  You
must do this if you are going to large parallel
computing.

Triton's JupyterHub is available at https://jupyter.triton.aalto.fi.
You can try them online at `try.jupyter.org
<https://try.jupyter.org/>`_ (there is a temporary notebook with no
saving).

You can always run notebooks yourself on your own (or remote)
computers, but on Triton we have some facilities already set up to
make it easier.


How Jupyter notebooks work
==========================
* Start a notebook
* Enter some code into a cell.
* Run it with the buttons or ``Control-enter`` or ``Shift-enter`` to
  run a cell.
* Edit/create new cells, run again.  Repeat indefinitely.
* You have a visual history of what you have run, with code and
  results nicely interspersed.  With certain languages such as Python,
  you can plots and other things embedded, so that it becomes a
  complete reproducible story.

JupyterLab is the next iteration of this and has many more features,
making it closer to an IDE or RStudio.

Notebooks are without a doubt a great tool.  However, they are only
one tool, and you need to know their limitations.  See our other page
on :doc:`limitations of notebooks </scicomp/jupyter-pitfalls>`.



JupyterHub
==========

.. note::

   JupyterHub on Triton is still under development, and features will
   be added as they are needed or requested.  Please use the `Triton
   issue tracker
   <https://version.aalto.fi/gitlab/AaltoScienceIT/triton/issues>`__.

The easiest way of using Jupyter is through JupyterHub - it is a
multi-user jupyter server which takes a web-based login and spawns
your own single-user server.  This is available on Triton.

Connecting and starting
-----------------------
Currently jupyterHub is available only within Aalto networks, or from
the rest of the internet after a first Aalto login:
https://jupyter.triton.aalto.fi.

..
    If you are not within the Aalto
    networks (aalto open is not), either connect to the Aalto VPN (see
    `it.aalto.fi <https://it.aalto.fi>`__ or
    :doc:`../../aalto/remoteaccess`, this is the easiest and best
    supported) or
    set up a SSH proxy as described right below.
    You must also have a :doc:`Triton account <../accounts>`.

Once you log in, you must start your single-user server.  There are
several options available that trade off between long run time and
short run time but more memory available.  Your server runs in the
Slurm queue, so the first start-up takes a few seconds but after that
it will stay running even if you log out.  The resources you request
are managed by slurm: if you go over the memory limit, your server
will be killed without warning or notification (but you can see it in
the output log, ``~/'jupyterhub_slurmspawner_*.log``).  The Jupyter
server nodes are oversubscribed, which means that we can allocate more
memory and CPU than is actually available.  We will monitor the nodes
to try to ensure that there are enough resources available, so do
report problems to us.  **Please request the minimum amount of memory
you think you need** - you can always restart with more memory.  You
can go over your memory request a little bit before you get problems.

When you use Jupyter via this interface, the slurm billing weights are
lower, so that the rest of your Triton priority does not decrease by
as much.

..
    Proxy for remote access
    ~~~~~~~~~~~~~~~~~~~~~~~

    When connecting to JupyterHub outside of Aalto networks, you need to
    connect somehow.  This describes how you can do it using SSH.  Using
    the Aalto VPN is easier (Aalto laptops have it set up by default).  In
    a few weeks, this should no longer be needed.

    If you use the proxy instead of the VPN:

    * Install the proxy extension

    * Install the extension FoxyProxy Standard (Firefox or Chrome).
      Some versions do not work properly: the 5.x series for Firefox may
      not work, but older and newer does.

      * Create a new proxy rule with the pattern ``*jupyter.triton.aalto.fi*``.

    * Proxy type: SOCKS5, Proxy URL: ``localhost``, port ``8123``.

      * SSH to kosh or some other Aalto computer and use the ``-D 8123``.
    This starts a proxy on your computer on port 8123.  This has to
      always be running whenever you connect to the notebook.

      * ``ssh -D 8123
	username@kosh.aalto.fi``.

    Now, when you go to ``jupyter.triton.aalto.fi``, you will
    *automatically* connect to the right place on Triton via FoxyProxy and
    the SSH proxy and can use Jupyter like normal.  But if the ssh
    connection goes down, then you can't connect and will get errors, and
    you will have to remember to restart it.  You should also remember
    that it will require SSH *inside* of Aalto too: it's simplest disable
    FoxyProxy inside of Aalto networks and enable only when you need.


Usage
-----
Once you get to your single-user server Jupyter running as your own
user on Triton.  You begin in a convenience directory which has links to
``home``, ``scratch``, etc.  You can not make files in this directory
(it is read-only), but you can navigate to the other folders to create
your notebooks.  You have access to all the Triton filesystems (not
project/archive) and all normal software.

We have some basic extensions installed:

* Jupyterlab (to use it, change ``/tree`` in the URL to ``/lab``).
  Jupyterlab will eventually be made the default.
* modules integration
* jupyter_contrib_nbextensions - check out the variable inspector
* diff and merge tools (currently does not work somehow)

The log files for your single-user servers can be found in, see
``~/jupyterhub_slurmspawner_*.log``.  When a new server starts, these
are automatically cleaned up when they are one week old.

For `reasons of web security
<https://jupyterhub.readthedocs.io/en/latest/reference/websecurity.html>`__,
you can't install your own extensions (but you can install your own
kernels).  Send your requests to us instead.

Problems?  Requests?
--------------------
This service is currently in beta and under active development.  If
you notice problems or would like any more extensions or features, let
us know.  If this is useful to you, please let us know your user
store, too.  In the current development stage, the threshold for
feedback should be very low.

Currently, the service level is best effort.  The service may go down
at any time and/or notebooks may be killed whenever there is a
shortage of resources or need of maintenance.  However, notebooks
auto-save and do survive service restarts, and we will try to avoid
killing things unnecessarily.



Software and kernels
====================
We have various kernels automatically installed (these instructions
should apply to both JupyterHub and ``sjupyter``):

* Python (2 and 3 via some recent anaconda modules + a few
  more Python modules.)
* Matlab (latest module)
* Bash kernel
* R (a default R environment you can get by ``module load r-triton``.
  ("R (safe)" is similar but tries to block some local user configuration
  which sometimes breaks things, see FAQ for more hints.)
* Julia: currently doesn't seem to play nicely with global
  installations (if anyone knows something otherwise, let us know).
  Just load two modules: ``module load julia``, ``module
  load jupyterhub/live``, and then install the kernel ``julia`` and
  ``Pkg.add("IJulia")`` and it will install locally for you.
* We do not yet have a kernel management policy.  Kernels may be added
  or removed over time.  We would like to keep them synced with the
  most common Triton modules, but it will take some time to get this
  automatic.  Send requests and problem reports.

Since these are the normal Triton modules, you can submit installation
requests for software in these so that it is automatically available.

Installing kernels from virtualenvs or Anaconda environments
------------------------------------------------------------
You can do this::

  module load jupyterhub/live
  envkernel conda --user --name INTERNAL_NAME --display-name="My conda" /path/to/conda_env

Or for Python virtualenvs::

  module load jupyterhub/live
  envkernel virtualenv --user --name INTERNAL_NAME --display-name="My virtualenv" /path/to/conda_env

You have to have the package ``ipykernel`` installed in the
environment: activate the environment and do ``pip install
ipykernel``.

Installing a different R module as a kernel
-------------------------------------------

Load your R modules, install R kernel normally (to some ``NAME``),
use envkernel as a wrapper to re-write the kernel (reading the
``NAME`` and rewriting to the same ``NAME``), after it loads the
modules you need::

  # Load jupyterhub/live, and R 3.6.1 with IRkernel.
  module load r-irkernel/1.1-python3
  module load jupyterhub/live

  # Use Rscript to install jupyter kernel
  Rscript -e "library(IRkernel); IRkernel::installspec(name='NAME', displayname='R 3.6.1')"

  # Use envkernel to re-write, loading the R modules.
  envkernel lmod --user --kernel-template=NAME --name=NAME r-irkernel/1.1-python3

Install your own kernels from other Python modules
--------------------------------------------------

This works if the module has Python installed and working.  This has
to be done once in any Triton shell::

  module load jupyterhub/live
  envkernel lmod --user --name INTERNAL_NAME --display-name="Singularity my kernel" MODULE_NAME
  module purge

Install your own kernels from Singularity image
-----------------------------------------------
First, find the ``.simg`` file name.  If you are using this from one
of the Triton modules, you can use ``module show MODULE_NAME`` and
look for ``SING_IMAGE`` in the output.

Then, install a kernel for your own user using envkernel.  This has to
be done once in any Triton shell::

  module load jupyterhub/live
  envkernel singularity --user --name KERNEL_NAME --display-name="Singularity my kernel" SIMG_IMAGE
  module purge


Install your own non-Python kernels
-----------------------------------
* First, ``module load jupyterhub/live``.  This loads
  the anaconda environment which contains all the server code and
  configuration.  (This step may not be needed for all kernels)
* Follow the instructions you find for your kernel.  You may need to
  specify ``--user`` or some such to have it install in your user
  directory.
* You can check your own kernels in
  ``~/.local/share/jupyter/kernels/``.

If your kernel involves loading a :doc:`module </triton/tut/modules>`,
you can either a) load the modules within the notebook server
("softwares" tab in the menu), or b) update your ``kernel.json`` to
include the required environment variables (see `kernelspec
<https://jupyter-client.readthedocs.io/en/stable/kernels.html>`__).
(We need to do some work to figure out just how this works).  Check
``/share/apps/jupyterhub/live/miniconda/share/jupyter/kernels/ir/kernel.json``
for an example of a kernel that loads a module first.

..
  This one-liner might help: ``( echo "  \"env\": {" ; for x in LD_LIBRARY_PATH LIBRARY_PATH MANPATH PATH PKG_CONFIG_PATH ; do echo "    \"$x\": \"${!x}\"", ; done ; echo "  }" ) >> ~/.local/share/jupyter/kernels/ir/kernel.json`` + then edit the JSON to make it valid.




Git integration
===============

You can enable git integration on Triton by using the following
lines from inside a git repository.  (This is normal nbdime, but uses
the centrally installed one so that you don't have to load a
particular conda environment first.  The ``sed`` command fixes
relative paths to absolute paths, so that you use the tools no matter
what modules you have loaded)::

  /share/apps/jupyterhub/live/miniconda/bin/nbdime config-git --enable
  sed --in-place -r 's@(= )[ a-z/-]*(git-nb)@\1/share/apps/jupyterhub/live/miniconda/bin/\2@' .git/config



FAQ/common problems
===================
* **Jupyterhub won't spawn my server: "Error: HTTP 500: Internal
  Server Error (Spawner failed to start [status=1]."**.  Is your home
  directory quota exceeded?  If that's not it, check the
  ``~/jupyterhub_slurmspawner_*`` logs then contact us.

* **My server has died mysteriously.**  This may happen if resource
  usage becomes too much and exceed the limits - Slurm will kill your
  notebook.  You can check the ``~/jupyterhub_slurmspawner_*`` log
  files for jupyterhub to be sure.

* **My server seems inaccessible / I can't get to the control panel to
  restart my server.  Especially with JupyterLab**.  In JupyterLab,
  use File→Hub Control Panel.  If you can't get there, you can change
  the URL to ``/hub/home``.

* **My R kernel keeps dying**.  Some people seem to have global R
  configuration, either in ``.bashrc`` or ``.Renviron`` or some such
  which globally, which even affects the R kernel here.  Things we
  have seen: pre-loading modules in ``.bashrc`` which conflict with
  the kernel R module; changing ``RLIBS`` in ``.Renviron``.  You can
  either (temporarily or permanently) remove these changes, or you
  could `install your own R kernel <https://irkernel.github.io/>`__.
  If you install your own, it is up to you to maintain it (and
  remember that you installed it).

* "Spawner pending" when you try to start - this is hopefully fixed in `issue
  #1534/#1533
  <https://github.com/jupyterhub/jupyterhub/issues/1534>`__ in
  JupyterHub.  Current recommendation: wait a bit and return to
  JupyterHub home page and see if the server has started.  Don't click
  the button twice!


See also
========
* https://jupyter.org

  * Online demos and live tutorial: https://jupyter.org/try (use the
    Python one)

* Jupyter basic tutorial: https://www.youtube.com/watch?v=HW29067qVWk
  (this is just the first link on youtube - there are many more too)

* More advanced tutorial: `Data Science is Software
  <https://www.youtube.com/watch?v=EKUy0TSLg04>`__ (this is not just a
  Jupyter tutorial, but about the whole data science workflow using
  Jupyter.  It is annoying long (2 hours), but *very* complete and
  could be considered good "required watching")

* :doc:`/scicomp/jupyter-pitfalls`

* CSC has this service, too, however there is no long term storage yet
  so there is limited usefulness for research: https://notebooks.csc.fi/

Our configuration is available on Github.  Theoretically, all the
pieces are here but it is not yet documented well and not yet
generalizable.  The Ansible role is a good start but the jupyterhub
config and setup is hackish.

* Ansible config role:
  https://github.com/AaltoScienceIT/ansible-role-fgci-jupyterhub
* Configuration and automated conda environment setup:
  https://github.com/AaltoScienceIT/triton-jupyterhub

..
  Matlab support:
    pip install matlab_kernel
    cd $MATLABROOT/extern/engines/python/
    python setup.py
