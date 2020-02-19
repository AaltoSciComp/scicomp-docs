Your own notebooks via ``sjupyter``
===================================

.. note::

   Now that :doc:`Triton Jupyterhub <jupyter>` exists, this method of
   running Jupyter is not
   so important.  It is only needed if you need more resources than
   JupyterHub can provide.

We provide a command ``sjupyter`` which automates launching your own
notebooks in the Slurm queue.  To use this, ``module load sjupyter``.
This gives you more flexibility in
choosing your nodes and resources than Jupyterhub, but also will after
your and your department's Triton priority more because you are
blocking others from using these resources.


.. _jupyter-proxy-setup:

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
  (or ``jupyter.triton.aalto.fi`` if you want to connect to that using
  the proxy).

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
can use Jupyter like normal.  But if the ssh connection goes down,
then you can't connect and will get errors, so be aware (especially
with jupyter.triton.aalto.fi which you might expect to always work).

Starting sjupyter
-----------------

We have the custom-built command ``sjupyter`` for
starting Jupyter on Triton.

First, you must load the ``sjupyter`` module::

  module load sjupyter

To run in the Triton queue (using more resources), just use
``sjupyter``.  This will start a notebook on the interactive Slurm
queue.  All the normal rules apply: timelimits, memory limits, etc.
If you want to request more resources, use the normal Slurm options
such as ``-t``, ``--mem``, etc.  Notebooks can only last as long as
your job lasts, and you will need to restart them.  Be efficient with
resource usage: if you request a lot of resources and leave the
notebook idle, no one else can use them.  Thus, try to use the
(default) interactive partition, which handles this automatically.

To run on the login node, run ``sjupyter --local``.  This is good for
small testing and so on, which doesn't use too much CPU or memory.


