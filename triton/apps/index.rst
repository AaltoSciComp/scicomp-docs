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
* Visit :doc:`/help/garage` to ask for advice.

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


Software installations
----------------------

We aim to help as many people as possible, but we can't do everything.
For things we can't install for everyone, we can often provide
instructions for how you can install it by yourself.

Software is generally easy to install if it is in the `conda's
conda-forge channel <https://anaconda.org/search>`__ (for almost any
software, see our :doc:`conda guide </triton/apps/python-conda>`) or the
`Spack package manager <https://packages.spack.io/>`__ (for compiled
software).  If it has easy-to-install Ubuntu packages, it will be easy
to do via :doc:`singularity <../usage/singularity>` containers.

The :ref:`Triton issue tracker <issuetracker>` should have a record of
all software we help people to install which isn't documented at
scicomp.aalto.fi.



Software documentation pages
----------------------------

.. toctree::
   :maxdepth: 1
   :glob:

   *


Software installation and policy
--------------------------------

We want to support all software, but unfortunately time is limited.
If we tried to install everything perfectly, we would in practice not
be able to support much.  Thus, we try to do the best we can for as
many people as we can by defining these levels of support.  You don't
have to know the levels: just ask for what you need, the levels are
for us to organize our support internally.

.. list-table::
   :header-rows: 1
   :stub-columns: 1

   * *
     * Installation
     * Support by ASC staff
     * Updates (new versions, etc)
     * Documentation
   * * A
     * Installed globally (with functionality checks)
     * Full support (named responsible person)
     * Automatically (every so often)
     * Always up to date
   * * B
     * Installed globally
     * Good, usually
     * Upon request (without much testing)
     * May be out of date unless we get requests
   * * C
     * Installed globally (without checks of functionality)
     * None promised (ask anyway)
     * Upon request (*if* there is time)
     * None or minimal stub page (check issue tracker/chat for more
       info or updates)
   * * E
     * User-installed
     * Good
     * n/a
     * Updated when requested
   * * F
     * User-installed
     * None promised (ask anyway)
     * n/a
     * Minimal or none: "word of mouth" or garage support.  (check
       issue tracker/chat)
