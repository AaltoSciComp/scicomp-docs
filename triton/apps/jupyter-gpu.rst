Jupyter with GPUs
=================

.. warning::

   Jupyter with GPUs are only available for certain projects which
   have funded the GPUs.  More information below.

The normal OnDemand Jupyter does not include GPUs, because they are
very expensive and Jupyter interactive work by its nature has lots of
idling.  However, some projects have ordered GPUs specifically for
interactive work.

When we have GPUs available for Jupyter.  They are divided into separate
virtual GPUs with less GPU-memory.  We hope it's enough to do basic
testing while not having the cost while minimizing the amount of
wasted resources.



How it works
------------

* Use the normal OnDemand Jupyter app,
  https://ondemand.triton.aalto.fi , as described in :doc:`jupyter`.
* Select one of the interactive partitions (see below)
* Your Jupyter session will start.  Note it has shorter timeouts that
  other Jupyter sessions, to prevent inefficiency.  Once you have
  resources, don't forget to use them.
* There is no service guarantee, resources may be adjusted anytime
  without warning.  Save often.


.. list-table::
   :header-rows: 1

* * Resources
  * Who has access
  * Resources

* * Ellis H200 GPU
  * ELLIS project staff (``ellis`` unix group), contact XXX for access.
  * 4 H200 GPUs split into 56 vGPUs with 18G mem each

* * General H200 GPU
  * Anyone, but sessions will be stopped without warning if a higher
    priority user comes.
  * Same as above

Remember, Jupyter+GPUs are designed to be used for testing and
development, not production runs.  You should plan (from the
beginning) how you will transition to batch jobs for your main
computations, otherwise you may have a bad time.

The virtual GPUs have much less memory than full GPUs.  Please contact
us if it doesn't serve your needs and we can try to adjust to make it
better.  Resources and availability may change at any time - including
restarting for maintenance without warning.



Contact
-------

Contact ASC/Science-IT us via the normal means, or the people in the
table above for access to the resources.
