.. Triton user guide documentation master file, created by
   sphinx-quickstart on Thu Jun 15 12:18:55 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

:og:description: Documentation about scientific and data-intensive computing at Aalto and beyond. Targeted towards Aalto researchers, but has some useful information for everyone.
:gitstamp_ignore:

.. meta::
   :keywords: Aalto Scientific Computing, Aalto SciComp, ASC, High-performance computing, HPC, Scientific computing, scicomp, research software, Aalto Research Software Engineers, AaltoRSE, RSE, RSEng


==========================
Aalto Scientific Computing
==========================

This site contains documentation about scientific and data-intensive
computing at Aalto University and beyond.  It is targeted towards
Aalto researchers, but has some useful information for everyone.

.. toctree::
   :maxdepth: 1

   aalto/welcomeresearchers
   aalto/welcomestudents

News
====
.. include:: /news/index.rst
   :start-line: 3
   :end-line: 11

.. toctree::
   :maxdepth: 1

   news/index.rst


The Aalto environment
=====================
Aalto provides a wide variety of support for scientific computing.
For a summary, see the `IT Services for Research page
<https://www.aalto.fi/en/services/it-services-for-research>`_.
For information about data storage at Aalto, see the section on data
management below.

.. toctree::
   :maxdepth: 2

   aalto/index

Cheatsheets: `CS <ch-cs_>`_, `Data <ch-data_>`_.

.. _ch-cs: https://aaltoscicomp.github.io/cheatsheets/cs-cheatsheet.pdf
.. _ch-data: https://aaltoscicomp.github.io/cheatsheets/sci-data-cheatsheet.pdf



Data management
===============
In this section, you can find some information and instructions on data
management.

.. toctree::
   :maxdepth: 2

   data/index

Cheatsheets: `Data <ch-data_>`_, `A4 Data management plan <ch-dmpA4_>`_.

.. _ch-dmpA4: https://aaltoscicomp.github.io/cheatsheets/DMP-A4-both.pdf



Triton
======
Triton is the Aalto high performance computing cluster.  It is your
go-to resources for anything that exceeds your desktop computer's
capacity.  To get started, you could check out the :ref:`tutorials
<tutorials>` (going through all the principles) or :doc:`quickstart
guide </triton/quickstart/index>` (if you pretty much know the
basics).

.. toctree::
   :maxdepth: 2

   triton/index

Cheatsheets: `Triton <ch-triton_>`_

.. _ch-triton: https://aaltoscicomp.github.io/cheatsheets/triton-cheatsheet.pdf



Aalto Research Software Engineers
=================================

Skills to do science are different than skills to write good research
code.  The Aalto Research Software Engineers (AaltoRSE) provide
support and mentoring to those using computing and data so that
everyone can do the best possible work.

.. toctree::
   :maxdepth: 2

   rse/index


Scientific computing
====================

In this section, you find general (not Aalto specific) scientific
computing resources.  We encourage other sites to use and contribute
to this information.

.. toctree::
   :maxdepth: 2

   scicomp/index

Cheatsheets: `git the way you need it <ch-gfnp_>`_, `Gitlab (produced by Gitlab, with Aalto link) <ch-gitlab_>`_

.. _ch-gfnp: https://aaltoscicomp.github.io/cheatsheets/git-the-way-you-need-it.pdf
.. _ch-gitlab: https://aaltoscicomp.github.io/cheatsheets/git-cheatsheet.pdf



Training
========

We have various recommended training courses for researchers who deal
with computation and data.  These courses are selected by researchers,
for researchers and grouped by level of skill needed.

.. toctree::
   :maxdepth: 2

   training/index



Help
====

Don't go alone, we are there!  There is all kinds of "folk knowledge"
to efficiently use the tools of scientific computing, and we would
like to learn that.  In particular, our community is welcome to come
to our :doc:`SciComp garage <help/garage>` even for small random chats
about your work, but there are :doc:`plenty of other ways to ask for
help <help/index>`, too.

.. toctree::
   :maxdepth: 2
   :titlesonly:

   help/index



About us
========

Aalto Scientific Computing isn't a :abbr:`HPC (High Performance
Computing)` center - we provide HPC services, but our goal is to
support scientific computing no matter what resources you need.
Computing is hard, and we know that support is even more important
than the infrastructure.  If you are a unit at Aalto University,
:doc:`you can join us </about/join>`.  [`Mastodon
<https://fosstodon.org/@SciCompAalto>`__, `Twitter
<https://twitter.com/SciCompAalto>`__]

.. toctree::
   :maxdepth: 2
   :titlesonly:

   about/index

:doc:`Aalto Scientific Computing </about/index>` (ASC) maintains these
pages with the :doc:`help of the Aalto community <README>`.
This site is open source: all content is licensed under CC-BY 4.0
and all examples under CC0 (public domain).  Additionally, this is an
*open project* and we *strongly* encourage anyone to :doc:`contribute
<README>`.  For information, see the :doc:`README` and the Github
links at the top of every page.  Either make Github issues, pull
requests, or ask for direct commit access.  Be bold: the biggest
problem is missing information, and mistakes can always be fixed.


* :ref:`genindex`
* :ref:`search`

.. raw:: html

   <a rel="me" hidden href="https://fosstodon.org/@SciCompAalto">Mastodon</a>
