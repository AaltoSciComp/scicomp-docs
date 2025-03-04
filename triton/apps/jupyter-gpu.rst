Jupyter with GPUs
=================

.. warning::

   Certain projects have funded hardware for Jupyter with GPUs.  The resources
   are available to all Triton users, with priority given to the project
   members.  Others can attempt to use in a preemptible queue (the jobs are
   killed with no warning if a higher-priority user comes).

   We are still tuning the parameters (run time, resources available,
   etc.) to balance usefulness vs resource wastage.  There is no service
   guarantee.  Let us know what is useful or not working.

The normal OnDemand Jupyter does not include GPUs, because they are very
expensive and Jupyter interactive work by its nature has lots of idling.
However, some projects have ordered GPUs specifically for interactive work. The
GPUs that have been dedicated for interactive Jupyter work are divided into
separate virtual GPUs with less GPU-memory.


.. highlight:: console


Expected use case
-----------------

Remember, Jupyter+GPUs are designed to be used for testing and
development, not production runs or real computation.  The GPU memory
is limited, so you can test code but probably not even run
moderately-sized models.  This is because any resources allocated to a
Jupyter job are mostly idle.

You should plan (from the beginning) how you will transition to batch
jobs for your main computations.  For example, write and verify code
in Jupyter with tiny data, then from the command line submit the code
to run in the batch queue with much more resources::

   $ sbatch --gpus=1 --wrap 'jupyter nbconvert --to notebook --execute mynotebook.ipynb --output mynotebook.$(date -Iseconds).ipynb'



How it works
------------

* Use the normal OnDemand Jupyter app,
  https://ondemand.triton.aalto.fi, as described in :doc:`jupyter`.
* Select one of the interactive partitions (see below)
* Your Jupyter session will start.  Note it has shorter timeouts that
  other Jupyter sessions, to prevent inefficiency.  Once you have
  resources, don't forget to use them.
* When you are done with using the resources, remember to stop the session via
  File > Shut Down.
* There is no service guarantee, resources may be stopped or adjusted
  anytime without warning.  Save often.

.. list-table::
   :header-rows: 1

* * Name
  * Who has access
  * Resources

* * Ellis H200 GPU
  * ELLIS project staff (``ellis`` unix group). Still being formed, contact ASC
    for access for now.
  * 8 H200 GPUs split into a total of 56 vGPUs with 18G mem each.

* * General H200 GPU
  * Anyone, but sessions can be stopped without warning if a higher
    priority user comes and needs the resources.
  * Same as above

Time limits and other parameters are visible in OnDemand (and not
copied here since they may change).



Contact
-------

Contact ASC/Science-IT us via the normal means, or the people in the
table above for access to the resources.
