==============
Triton cluster
==============

Triton is the Aalto high-performance computing cluster.  It serves all
researchers
of Aalto, but is currently coordinated from within the School of
Science.  Access is free for researchers (students not doing research
should check out our :doc:`intro for students
<../aalto/welcomestudents>`).  It is similar to the CSC
clusters, though CSC clusters are larger and Triton is easier to use
because it is more integrated into the Aalto environment.

Quick contents and links
========================

.. list-table::

   * * **Triton contents**

       * About Triton

         * :doc:`overview`
         * :doc:`usagepolicy`
	 * :doc:`acknowledgingtriton`

       * :doc:`Getting Help/Contact <help>`

	 * `Triton issue tracker <https://version.aalto.fi/gitlab/AaltoScienceIT/triton/issues>`_
	   (most requests here, login with HAKA)
	 * `Suggestions for good support requests
	   <https://docs.csc.fi/support/support-howto/>`_

       * :doc:`Quick Reference <ref/index>`
       
.. _triton_tutorial_link:

       * Tutorials (start here)

	 * :doc:`accounts`
	 * :doc:`tut/intro`
	 * :doc:`tut/connecting`
	 * :doc:`tut/applications`
	 * :doc:`tut/modules`
	 * :doc:`tut/storage`
	 * :doc:`tut/interactive`
	 * :doc:`tut/serial`
         * :doc:`tut/array`
         * :doc:`tut/dependency`
	 * :doc:`tut/monitoring`
	 * :doc:`tut/gpu`
	 * :doc:`tut/parallel`

       * Cluster usage details

	 * Parallel jobs (coming, for now see :doc:`usage/general`)
	 * :doc:`usage/gpu`

       * :ref:`Applications <apps>`

       For full contents, see below.

     * **News**

       **Shortcuts**

       * `Issue tracker <https://version.aalto.fi/gitlab/AaltoScienceIT/triton/issues>`_
       * `Quick Reference <ref/index>`
       * `Triton Cheatsheet <https://aaltoscicomp.github.io/cheatsheets/triton-cheatsheet.pdf>`_
       * `Triton FAQ <usage/faq>`
       * `Scicomp Garage </help/garage>`

       **Scientific computing resources**

       * :doc:`SCIP – Scientific Computing in Practice courses
	 </training/scip/index>`: organized
	 by SciComp. Including Triton kickstarts and many others
       * `Parallel computing <https://wiki.aalto.fi/download/attachments/65022076/parallel_computing.2012-04-12.pdf?version=1&modificationDate=1334828664000&api=v2>`_
       * `Aalto IT Services for Research <https://www.aalto.fi/en/services/it-services-for-research>`_
       * `Hands-on Scientific Computing <hosc_>`__: map of important
	 computing skills
       * `Software Carpentry <https://software-carpentry.org/>`_
	 (scientific computation basics) and
	 `Code Refinery <https://coderefinery.org/>`_ (more focused on
	 programming techniques)

       **General links**

       * `CSC <https://www.csc.fi/>`_ - Finland's academic computing center.
       * `FGCI user's guide
	 <https://docs.csc.fi/cloud/fgci/fgci-user-guide-overview/>`_ at CSC: That is a
	 general Guide to FGCI resources. Triton is one of them.
       * `CSC HPC guides
	 <https://research.csc.fi/guides>`_ at CSC: a
	 Triton like cluster at CSC. Similar setup, thus examples and
	 instructions can be useful.
       * `Aalto research data management information <https://www.aalto.fi/en/services/research-data-management-rdm-and-open-science>`_



Overview
========

.. toctree::
   :maxdepth: 1

   overview.rst
   help.rst
   accounts.rst
   usagepolicy.rst
   acknowledgingtriton.rst

.. _tutorials:

Tutorials
=========
These are designed to be read (or `watched <tutorial-playlist_>`__) in-order by every Triton user when they
get their accounts (except maybe the last ones).  In order to use
Triton well, in the `Hands-on SciComp roadmap <hosc_>`__ you should
also know the `Basics (A) <hosc-a_>`__ and `Linux (C) <hosc-c_>`__
levels as a prerequisite.

.. _tutorial-playlist: https://www.youtube.com/playlist?list=PLZLVmS9rf3nN_tMPgqoUQac9bTjZw8JYc
.. _hosc: https://hands-on.coderefinery.org/
.. _hosc-a: https://hands-on.coderefinery.org/#a-basics
.. _hosc-c: https://hands-on.coderefinery.org/#c-linux-and-shell

.. toctree::
   :maxdepth: 1

   tut/about-tutorials.rst
   tut/intro.rst
   tut/connecting.rst
   tut/applications.rst
   tut/modules.rst
   tut/storage.rst
   Interactive jobs: running your first command <tut/interactive>
   Serial jobs: running in the queue <tut/serial>
   tut/monitoring.rst
   tut/array.rst
   tut/gpu.rst
   tut/parallel.rst
   tut/dependency.rst

Detailed instructions
=====================
.. toctree::
   :maxdepth: 1
   :glob:

   usage/*

.. _application-list:
.. _apps:

Applications
============

See our :doc:`general information <apps/index>` and the full list below:

.. toctree::
   :maxdepth: 1
   :glob:

   apps/index
   apps/*


Reference and Examples
======================
.. toctree::
   :maxdepth: 1

   ref/index
   examples/index
