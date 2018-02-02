Jupyter notebooks
=================

Jupyter notebooks are a way of interactive, web-based computing:
instead of either scripts or interactive shells, the notebooks allow
you to see a whole script + output and experiment interactively and
visually.  They are good for developing and testing things, but once
things work and you need to scale up, it is best to put your code into
proper programs.  You must do this if you are going to large parallel
computing.

You can try them online at `try.jupyter.org
<http://try.jupyter.org/>`_ (there is no long-term saving here).

You can always run notebooks yourself, but on Triton we have some
facilities already set up for this.

.. note::

   Start ``sjupyter`` by using ``/share/apps/bin/sjupyter`` for now.


How jupyter notebooks work
--------------------------
* Start a notebook
* Enter some code into a cell.
* Run it with the buttons or ``Control-enter`` or ``Shift-enter`` to
  run a cell.
* Edit/create new cells, run again.  Repeat indefinitely.
* You have a visual history of what you have run, with code and
  results nicely interspersed.  With certain languages such as Python,
  you can plots and other things embedded, too so that it becomes a
  complete story.



How to use
----------
You can always install notebooks yourself on your own computers - this
is a good strategy if you don't have very demanding requirements.  To
use on Triton, do the following things:

Initial setup
~~~~~~~~~~~~~

When running Jupyter on another system, the biggest problem is always
making the conenction securely.  To do this here, we use a browser
extension and SSH Proxy.

* Install the proxy extension

  * Install the extension FoxyProxy Standard (Firefox or Chrome).
    Some versions do not work properly: the 5.x series for Firefox may
    not work, but older and newer does.

* Create a new proxy rule with the pattern ``*int.triton.aalto.fi*``

  * Proxy type: SOCKS5, Proxy URL: ``localhost``, port ``8123``.

* SSH to triton and use the ``-D 8123``.  This starts a proxy on your
  computer on port 8123.  This has to always be running whenever you
  connect to the notebook.

Now, when you go to any of the ``*.int.triton.aalto.fi*`` addresses,
you will *automatically* connect to the right place on Triton.  You
can use jupyter like normal.

Starting jupyter
~~~~~~~~~~~~~~~~

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
--------------------------

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



Notes
-----
The notebooks can be great for starting projects and interactive
exploration.  In a cluster environment, they have limited use for
high-performance calculations (though it is certainly possible,
especially with the IPython cluster support).

Notebooks are harder to version control.  As a project gets more
advanced, eventually you *may* want to switch to a more traditional
system.  It can be good to put the backend, fixed code into a library
and keep the exploration in Jupyter.  It can be tricky to know where
this point is and how to do a split.



See also
--------
* https://jupyter.org
  * Online demo: https://try.jupyter.org/
* Jupyter basic tutorial: https://www.youtube.com/watch?v=HW29067qVWk
  (first link on youtube - many more too)
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
    python -m bash_kernel.install
