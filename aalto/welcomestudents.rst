==================
Welcome, students!
==================

.. seealso::

   Primary information is at Aalto's `IT Services for Students
   <https://www.aalto.fi/en/services/it-services-for-students>`_ page,
   which focuses on basic services.  This focuses on students in
   computing and data intensive programs.

Welcome to the Aalto!  We are glad you are interested in scientific
computing and data.  `scicomp.aalto.fi <https://scicomp.aalto.fi>`_
may be useful to you, but is
somewhat targeted to research usage.  However, it can still
serve as a good introduction to resources for scientific and
data-intensive computing at Aalto if you are a student.  This page is
devoted to resources which are available to students.

If you are involved in a research group or doing researcher for a
professor/group leader, you are a researcher!  You should acquaint
yourself with all information on this site, starting with
:doc:`welcomeresearchers` and use whatever you need.

General IT instructions can be found at https://www.aalto.fi/en/it-help.  There
used to be some on into.aalto.fi, but these are gone now.  There also used
to be a 2-page PDF introduction for students, but it also seems to be
gone from online.  `IT Services for Students
<https://www.aalto.fi/en/services/it-services-for-students>`_ is
now the best introduction.



Accounts
========

In general, your Aalto account is identical to that which researchers
have --- the only difference is that you don't have an departmental
affiliation.



Getting help
============

As a student, the `ITS servicedesks <https://it.aalto.fi/contact>`__
are the first place to go for help.  The site https://www.aalto.fi/en/it-help is
the new central site for IT instructions.

This site, https://scicomp.aalto.fi, is intended for research
scientific computing support but has a few page useful to you.


Computation
===========

As a student, you have access to various light computational
resources which are suitable for most courses that need extra power:

.. csv-table::
   :delim: |

   :doc:`Paniikki computer lab <paniikki>` | Linux workstations, GPUs, software via modules
   Other computer labs | workstations, different OSs
   `Shell servers <https://www.aalto.fi/en/services/linux-shell-servers-at-aalto>`_ | via ssh, software via modules, overcrowded.  `Brute and Force <https://www.aalto.fi/en/services/servers-for-light-duty-calculation>`_ are for computation, others not.
   :doc:`JupyterHub <jupyterhub>` | basic software, in web browser
   `Remote desktop <https://vdi.aalto.fi>`_ | Windows and Linux
   Own computers | Software at https://download.aalto.fi

The :doc:`Jupyter service <../aalto/jupyterhub>` at
https://jupyter.cs.aalto.fi is available to everyone with an Aalto
account.  It provides at least basic Python and R software; we try to
keep it up to date with the things people need most for courses that
use programming or data.

The `shell servers
<https://www.aalto.fi/en/services/linux-shell-servers-at-aalto>`_
``brute`` and ``force`` are for light computing, and generally for
students.  You may find them useful, but can often be
overloaded. `Light computing shell servers
<https://www.aalto.fi/en/services/servers-for-light-duty-calculation>`_. :doc:`Learn
how to launch Jupyter notebook on there <../aalto/remotejupyter>`.

For GPU computing, the :doc:`Paniikki Linux computer lab
<../aalto/paniikki>` (`map
<https://usefulaaltomap.fi/#!/select/paniikki>`_) has GPUs in all
workstations.  Software is available via ``module spider $name`` to
search and ``module load $name`` to load (and the module ``anaconda``
has Python, tensorflow, etc.).  Read the :doc:`Paniikki cheatsheet
here <../aalto/paniikki>`.  The instructions for :doc:`Aalto
workstations <../aalto/linux>` sort of apply there as well.  The
software on these machines is managed by the Aalto-IT team.  This is
the place if you need to play with GPUs, deep learning, etc, and helps
you transition to serious computing on large clusters.

A new (2018) remote desktop service is available at
https://vdi.aalto.fi (`instructions <https://www.aalto.fi/en/services/vdiaaltofi-how-to-use-aalto-virtual-desktop-infrastructure>`_).
This provides Windows and Linux desktops and is
designed to replace the need for computer classrooms with special
software installed.  You can access it via a web browser or the VMware
Horizon client.

The use of :doc:`Triton <../triton/index>` is for research purposes
and students can't get access unless you are affiliated with a
research project or (in very rare cases), a course makes special
arrangements.



Data storage
============

Aalto home directories have a 40GB quota, and this is suitable for
small use.  Note that files here are lost once you leave Aalto, so
make sure you back up.

The `IT Services for Research <itsr_>`_ page contains some other cloud
services which may be useful for data storage.  Of the cloud services,
note that everyone at Aalto can get an unlimted Google Drive account
through the Aalto Google Apps service: `instructions
<https://www.aalto.fi/en/services/google-drive-registration-and-closing-of-an-account>`__.
Your Aalto Google account will expire once you are no longer
affiliated, so your files here will become inaccessible.

.. _itsr: https://www.aalto.fi/en/services/it-services-for-research



Software
========

ITS has a `software and licenses <its_sw_>`_ (`FI <its_sw_fi_>`_)
page, and also a `full list of licenses <its_sw_list_>`_.  There is
also http://download.aalto.fi/.  Various scientific software can be
found for your own use via the Aalto software portals.


.. _its_sw: https://www.aalto.fi/en/services/softwares-for-staff-and-students-homeuse
.. _its_sw_fi: https://www.aalto.fi/fi/palvelut/ohjelmistot-henkilokunnan-ja-opiskelijoiden-kotikoneisiin
.. _its_sw_list: https://inside.aalto.fi/display/ITServices/University+software+licenses

The Lmod (``module``) system provides more software on
``brute``/``force`` and in Paniikki.  For example, to access a bunch
of scientific Python software, you can do ``module load anaconda``.
The :doc:`researcher-focused instructions are here
</triton/tut/modules>`, but like many things on this site you may have
to adapt to the student systems.

Common software:

.. csv-table::
   :delim: |

   Python | ``module load anaconda`` on Linux
   Tensorflow etc packages | same as Python, in Paniikki



Other notes
===========
It can be hard to find your way around Aalto, the official campus maps
and directions are known for being confusing confusing.  Try
`UsefulAaltoMap <https://usefulaaltomap.fi>`_ instead.

Do you have suggestions for this page?  Please leave on `issue on
Github <scicomp_github_issues_>`_ (make sure you have a good title
that mentions the audience is students, so we can put the information
in the right place).  Better yet, send a pull request to us yourself.

.. _scicomp_github_issues: https://github.com/AaltoScienceIT/scicomp-docs/issues
