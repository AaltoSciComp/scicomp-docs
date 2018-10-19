IPython parallel
----------------


A example batch script that uses IPython parallel (``ipyparallel``)
within slurm.  See also the :ref:`interactive hints on the Python page
<python-ipyparallel>`.


ipyparallel uses **global state** in your home directory, so you can
only run _one_ of these at a time!  You can add the ``--profile=``
option to name different scripts (you could use ``$SLURM_JOB_ID``).
But then you will get a growing number of unneeded profile directories
at ``~/.ipython/profile_*``, so this isn't recommended.  Basically,
ipyparallel is more designed for one-at-a-time interactive use rather
than batch scripting (unless you do more work...).

:download:`ipyparallel.slrm
</triton/examples/python/ipyparallel/ipyparallel.slrm>` is an example
slurm script that sets up ipyparallel.  It assumes that most work is
done in the engines.  It has inline Python, replace this with ``python
your_script_name.py``

.. literalinclude:: /triton/examples/python/ipyparallel/ipyparallel.slrm

