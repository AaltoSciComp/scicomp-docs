=======
Jupyter
=======

Jupyter notebooks are a way of interactive, web-based computing:
instead of either scripts or interactive shells, the notebooks allow
you to see a whole script + output and experiment interactively and
visually.  They are good for developing and testing things, but once
things work and you need to scale up, it is best to put your code into
proper programs.  You must do this if you are going to large parallel
computing.

You can try them online at `try.jupyter.org
<http://try.jupyter.org/>`_ (there is no long-term saving here).

You can always run notebooks yourself on your own (or remote)
computers, but on Triton we have some facilities already set up to
make it easier.


How jupyter notebooks work
==========================
* Start a notebook
* Enter some code into a cell.
* Run it with the buttons or ``Control-enter`` or ``Shift-enter`` to
  run a cell.
* Edit/create new cells, run again.  Repeat indefinitely.
* You have a visual history of what you have run, with code and
  results nicely interspersed.  With certain languages such as Python,
  you can plots and other things embedded, too so that it becomes a
  complete story.


Jupyterhub
==========

.. note::

   Jupyterhub on Triton is still under development, and features will
   be added as they are needed or requested.

The easiest way of using Jupyter is through JupyterHub - it is a
multi-user jupyter server which takes a web-based login and spawns
your own single-user server.  This is available on Triton.

Connecting
----------
Currently jupyterhub is available only available within Triton, so you
have to set up the :ref:`proxy described in the section below
<jupyter-proxy-setup>`.  Once this is done, connect to
``https://jupyter01.int.triton.aalto.fi``.

Usage
-----
It is just Jupyter.  You begin in a convenience directory which has links to
``home``, ``scratch``, etc.  You can not make files in this directory
(it is read-only), but you can navigate to the other folders to create
your notebooks.

We have some basic extensions installed:

* Jupyterlab (to use it, change ``/tree`` in the URL to ``/lab``).
  Jupyterlab will eventually be made the default.
* Python (2 and 3 via ``anaconda/latest`` modules. + a few
  more.)
* Matlab (latest module)
* Bash kernel
* R: coming soon

The log files for your single-user servers can be found in, see
``~/jupyterhub_slurmspawner_*.log``.  These will eventually be cleaned
up when they are more than 1 week old.

For `web security reasons
<https://jupyterhub.readthedocs.io/en/latest/reference/websecurity.html>`__,
you can't install your own extensions (but you can install your own
kernels).  Send your requests to us instead.

Installing your own kernels
---------------------------
* First, ``source
  /share/apps/jupyterhub/live/miniconda/bin/activate``.  This loads
  the anaconda environment which contains all the servers.  (May not
  be needed for all kernels*
* Follow the instructions you find for your kernel.  You may need to
  specify ``--user`` or some such to have it install in your user
  directory.
* You can check your own kernels in ``~/.local/share/jupyter/kernels/``.

If your kernel involves loading a module, you can either a) load the
modules within the notebook server ("softwares" tab in the tree menu),
or b) update your ``kernel.json`` to include the required environment
variables (see `kernelspec
<https://jupyter-client.readthedocs.io/en/stable/kernels.html>`__).

..
  This one-liner might help: ``( echo "  \"env\": {" ; for x in LD_LIBRARY_PATH LIBRARY_PATH MANPATH PATH PKG_CONFIG_PATH ; do echo "    \"$x\": \"${!x}\"", ; done ; echo "  }" ) >> ~/.local/share/jupyter/kernels/ir/kernel.json`` + then edit the JSON to make it valid.

Problems?  Requests?
--------------------
This service is currently in beta and under active development.  If
you notice problems or would like any more extensions or features, let
us know.  If this is useful to you, you can let us know too.  In the
current development stage, the threshold for feedback should be very
low.


Your own notebooks via ``sjupyter``
===================================

.. note::

   Start ``sjupyter`` by using ``/share/apps/bin/sjupyter`` for now.

.. note::

   This is currently not integrated into the Jupyterhub setup above.


.. jupyter-proxy-setup:

Set up the proxy
----------------

When running Jupyter on another system, the biggest problem is always
making the conenction securely.  To do this here, we use a browser
extension and SSH Proxy.

* Install the proxy extension

  * Install the extension FoxyProxy Standard (Firefox or Chrome).
    Some versions do not work properly: the 5.x series for Firefox may
    not work, but older and newer does.

* Create a new proxy rule with the pattern ``*int.triton.aalto.fi*``

  * Proxy type: SOCKS5, Proxy URL: ``localhost``, port ``8123``.

  * DNS through the proxy: on.

* SSH to triton and use the ``-D 8123``.  This starts a proxy on your
  computer on port 8123.  This has to always be running whenever you
  connect to the notebook.

  * If you are in Aalto networks: ``ssh -D 8123
    username@triton.aalto.fi``.
  * If you are not in Aalto networks, you need to do an extra hop
    through another Aalto server: ``ssh -D 8123
    username@triton.aalto.fi -o ProxyCommand='ssh
    username@kosh.aalto.fi -W %h:%p'``.

Now, when you go to any address matching ``*.int.triton.aalto.fi*``,
you will *automatically* connect to the right place on Triton.  You
can use Jupyter like normal.

Starting jupyter
----------------

We have the custom-built command ``sjupyter`` for starting Jupyter on
Triton.

To run on the login node, run ``sjupyter --local``.  This is good for
small testing and so on, which doesn't use too much CPU or memory.

To run in the Triton queue (using more resources), just use
``sjupyter``.  This will start a notebook on the interactive Slurm
queue.  All the normal rules apply: timelimits, memory limits, etc.
If you want to request more resources, use the normal Slurm options
such as ``-t``, ``--mem``, etc.  Notebooks can only last as long as
your job lasts, and you will need to restart them.  Be efficient with
resource usage: if you request a lot of resources and leave the
notebook idle, no one else can use them.  Thus, try to use the
(default) interactive partition, which handles this automatically.



Other kernels and software
==========================

Jupyter isn't just Python - you can run other programming languages
with the same notebook interface.  See the `full list of kernels here
<https://github.com/jupyter/jupyter/wiki/Jupyter-kernels>`_.

We support the following kernels already:

* **Python 2**: ``module load anaconda2`` first.
* **Matlab**: ask us, we need matlab 2017b and the Jupyter connector
  needs to be installed.
* **R**: Supported, ask us to install.
* **Bash**: Installed, but may be unstable.  Note, that if you do
  anything that has external effects to the filesystem, things are not
  re-runable!  Probably best for exploring how bash scripting works.

If you need other software installed to use in these environments, you
can within the python/R/matlab/etc environment: just do it outside of
Jupyter and it should be there inside, as long as you use the same
environment.



Notes and limitations
=====================
The notebooks can be great for starting projects and interactive
exploration.  However, as a project gets more advanced, you will
eventually find that the linear nature of notebooks is a limitation
because code can not really be reused.  It is possible to define
functions/classes within the notebook, but you lose the power of
inspection (they are just seen as single blocks) and can't share code
across notebooks (and copy and paste is bad).  This doesn't mean to
not use notebooks: but do keep this in mind, and once your methods are
mature enough (you are using the same code in multiple places), try to
move the core functions and classes out into a separate library, and
import this into the day-to-day exploration notebooks.

In a cluster environment, notebooks have limited use for
high-performance calculations, because you must reserve your resources
in advance but the notebooks are usually not using them.  It is
possible to do multi-node parallel calculations through things like
IPython Cluster, but it will end up inefficient.  Instead, use
notebooks for exploration.  When you need to run on the cluster,
create actual programs (start, run, end) and :doc:`submit those to the
queue </triton/tut/serial>`.  Use notebooks to explore and process the
output.

Notebooks are hard to :doc:`version control </scicomp/git>`, so you
should look at the `Jupyter diff and merge tools
<https://github.com/jupyter/nbdime>`__.  Just because notebooks is
interactive doesn't mean version control is any less important!  The
"split core functions into a library" is also related: that library
should be in version control at least.



See also
========
* https://jupyter.org
  * Online demo: https://try.jupyter.org/
* Jupyter basic tutorial: https://www.youtube.com/watch?v=HW29067qVWk
  (this is just the first link on youtube - there are many more too)
* CSC has this service, too, however there is no long term saving yet
  so there is limited research usefulness: https://notebooks.csc.fi/


..
  Matlab support:
    pip install matlab_kernel
    cd $MATLABROOT/extern/engines/python/
    python setup.py

  R support:
    https://irkernel.github.io/installation/
    ``module load anaconda3 R/3.4.1-iomkl-triton-2017a``.


  Bash:
    ml load anaconda3
    python -m bash_kernel.install
