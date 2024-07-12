.. _python-ipyparallel:

IPython Parallel
================

`ipyparallel <https://ipyparallel.readthedocs.io/en/latest/>`__ is a
tool for running embarrassingly parallel code using Python.   The
basic idea is that you have a *controller* and *engines*.  You have a
*client* process which is actually running your own code.

Preliminary notes: ipyparallel is installed in the
``scicomp-python-env/latest`` modules.

Let's say that you are doing some basic interactive work:

* Controller: this can run on the frontend node, or you can put it on
  a script.  To start: ``ipcontroller --ip="*"``
* Engines: ``srun -N4 ipengine``: This runs the four engines in slurm
  interactively.  You don't need to interact with this once it is
  running, but remember to stop the process once it is done because it
  is using resources.  You can start/stop this as needed.
* Start your Python process and use things like normal:

  .. code-block:: python

    import os
    import ipyparallel
    client = ipyparallel.Client()
    result = client[:].apply_async(os.getpid)
    pid_map = result.get_dict()
    print(pid_map)

This method lets you turn on/off the engines as needed.  This isn't the
most advanced way to use ipyparallel, but works for interactive use.

See also: :doc:`../examples/python/ipyparallel/ipyparallel` for a version
which goes in a slurm script.
