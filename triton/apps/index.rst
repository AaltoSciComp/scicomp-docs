==========================
Applications: General info
==========================

.. seealso::

   Intro tutorial: :doc:`../tut/applications` (this is assumed
   knowledge for all software instructions)

When you need software, check the following for instructions (roughly in this order):

* This page.
* Search the SciComp site using the search function.
* Check ``module spider`` and ``module avail`` to see if something is
  available but undocumented.
* The `issue tracker
  <https://version.aalto.fi/gitlab/AaltoScienceIT/triton>`__ for other
  people who have asked - some instructions only live there.

If you have difficulty, it's usually a good idea to search the issue
tracker anyway, in order to learn from the experience of others.


Modules
-------
See :doc:`../tut/modules`.  Modules are the standard way of loading
software.


Singularity
-----------
See :doc:`../usage/singularity`.  Singularity are software containers
that provide an operating system within an operating system.  Software
will tell you if you need to use it via Singularity.


Software installation and policy
--------------------------------

We want to support all software, but unfortunately time is limited.
In the chart below, we have these categories (which don't really mean
anything, but in the future should help us be more transparent about
what we are able to support):

* A: Full support and documentation, should always work
* B: We install and provide best-effort documentation, but may be out
  of date.
* C: Basic info, no guarantees

If you know some application which is missing from this list but is
widely in use (anyone else than you is using it) it would make sense
install to ``/share/apps/`` directory and create a module file. Send
your request to the tracker.  We want to support as much software as
possible, but unfortunately we don't have the resources to do
everything centrally.

Software is generally easy to install if it is in `Spack
<https://packages.spack.io/>`__ (check
that package list page), a scientific software management and building
system.  If it has easy-to-install Ubuntu packages,
it will be easy to do via :doc:`singularity <../usage/singularity>`.




Software documentation pages
----------------------------

.. csv-table::
   :delim: |


   Name          | |
   Python        |A|


.. toctree::
   :maxdepth: 1
   :glob:

   *
