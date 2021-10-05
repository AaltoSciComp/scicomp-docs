.. Triton user guide documentation master file, created by
   sphinx-quickstart on Thu Jun 15 12:18:55 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

==================================================
Welcome to the Pages of Aalto Scientific Computing
==================================================

We are here to offer Aalto users support with scientific programming 
questions, usage of the triton cluster and data management.
For these topics we have created several `Tutorials</triton/#Tutorials>`__ offer a daily support 
`Garage</help/garage/>`__ and provide `Training courses</Training/>`__ throught the year. 


:doc:`Aalto Scientific Computing
</about/index>` maintains these pages with the :doc:`help of the Aalto community <README>`.
[`twitter <https://twitter.com/SciCompAalto>`__]  We consist of
Science-IT (HPC, the Triton cluster and RSEs), certain department ITs, and
other friends.  :doc:`You can join us </about/join>`.
Along with general Welcome guide:

.. toctree::
   :maxdepth: 1

   aalto/welcomeresearchers
   aalto/welcomestudents

we have created a quick-guide to set up your system, access and use triton

.. toctree::
   :maxdepth: 1
   
   triton/quickstart
   
News
====
.. include:: /news/index.rst
   :start-line: 3
   :end-line: 7

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
management.  Concrete information: :doc:`main Aalto services
<aalto/aaltostorage>` and :doc:`global services <data/services>`.
Main Theoretical information: :doc:`Aalto-specific summary
<data/outline>` and `Aalto's
Research Data Management pages
<https://www.aalto.fi/en/services/research-data-management-rdm-and-open-science>`_.

.. toctree::
   :maxdepth: 2

   data/index

Cheatsheets: `Data <ch-data_>`_, `A4 Data management plan <ch-dmpA4_>`_.

.. _ch-dmpA4: https://aaltoscicomp.github.io/cheatsheets/DMP-A4-both.pdf



Triton
======
Triton is the Aalto high performance computing cluster.  It is your
go-to resources for anything that exceeds your desktop computer's
capacity.

.. toctree::
   :maxdepth: 2

   triton/index

Cheatsheets: `Triton <ch-triton_>`_

.. _ch-triton: https://aaltoscicomp.github.io/cheatsheets/triton-cheatsheet.pdf



Aalto Research Software Engineering
===================================

Skills to do science are different than skills to write good research
code.  The Aalto Research Software Engineering group provides support
and mentoring to those using computing and data.

.. toctree::
   :maxdepth: 2

   rse/index


Scientific computing
====================
In this section, you find general (not Aalto specific) scientific
computing resources.

.. toctree::
   :maxdepth: 2

   scicomp/index

Cheatsheets: `git for normal people <ch-gfnp_>`_, `Gitlab (produced by Gitlab, with Aalto link) <ch-gitlab_>`_

.. _ch-gfnp: https://aaltoscicomp.github.io/cheatsheets/git-for-normal-people-cheatsheet_1.0.pdf
.. _ch-gitlab: https://aaltoscicomp.github.io/cheatsheets/git-cheatsheet.pdf



Training
========

We have various recommended training courses for researchers who deal
with computation and data.  These courses are selected by researchers,
for researchers and grouped by level of skill needed.

.. toctree::
   :maxdepth: 2

   training/index



About
========

.. toctree::
   :maxdepth: 2
   :titlesonly:

   help/index
   about/index

These docs are open source: all content is licensed under CC-BY 4.0
and all examples under CC0 (public domain).  Additionally, this is an
*open project* and we *strongly* encourage anyone to :doc:`contribute
<README>`.  For information, see the :doc:`README` and the Github
links at the top of every page.  Either make Github issues, pull
requests, or ask for direct commit access.  Be bold: the biggest
problem is missing information, and mistakes can always be fixed.


* :ref:`genindex`
* :ref:`search`

