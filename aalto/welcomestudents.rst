==================
Welcome, students!
==================

Welcome to the Aalto!  We are glad you are interested in scientific
computing and data.  These pages may be useful to you, but are
somewhat targeted to research usage.  However, these pages can still
serve as a good introduction to resources for scientific and
data-intensive computing at Aalto if you are a student.

If you are involved in a research group or doing researcher for a
professor/group leader, you are a researcher!  You should acquaint
yourself with all information on this site, starting with
:doc:`welcomeresearchers` and use whatever you need.

There are general IT instructions for students: `FI <itsFI_>`_ `SV
<itsSV_>`_ `EN <itsEN_>`_.  There is an `introduction to IT services
for students <itsrv_std_>`_ (`FI <itsrv_std_fi_>`_) There are also
`research-focused instructions <itsr_>`_.

.. _itsFI: https://into.aalto.fi/display/fiit/Etusivu
.. _itsSV: https://into.aalto.fi/display/svit/Startsida
.. _itsrv_std: https://into.aalto.fi/display/fiit/IT-pikaopas+opiskelijoille
.. _itsrv_std_fi: https://into.aalto.fi/display/fiit/IT-pikaopas+opiskelijoille
.. _itsrv_std_sv: https://into.aalto.fi/pages/viewpage.action?pageId=17334253
.. _itsEN: https://into.aalto.fi/display/enit/Homepage



Accounts
========

In general, your Aalto account is identical to that which researchers
have --- the only difference is departmental affiliation.


Getting help
============

As a student, the `ITS servicedesks <https://it.aalto.fi/contact>`__
are the first place to go for help.  The site https://it.aalto.fi is
the new central site for IT instructions.  Previously, some public
instructions were on ``https://into.aalto.fi`` (studies focused) and
``https://inside.aalto.fi`` (staff focused) and finding information
was a great challenge.  Note that in 2018, all of these are being
updated.

This site, http://scicomp.aalto.fi, is intended for scientific
computing support and might be useful to you.


Computation
===========

TODO: Aalto workstations and default scientific software.

The `shell servers
<https://inside.aalto.fi/display/ITServices/Servers+for+light+computing>`_
``brute`` and ``force`` are for light computing, and generally for
students.  You may find them useful, but can often be overloaded. :doc:`Learn how to launch Jupyter notebook on there <../aalto/remotejupyter>`.

For GPU computing, the `Paniikki Linux computer lab
<http://usefulaaltomap.fi/#!/select/paniikki>`_ has GPUs in all
workstations and various software.  The instructions for :doc:`Aalto
workstations <../aalto/linux>` apply there as well (mostly). Read the
:doc:`Paniikki cheatsheet here <../aalto/paniikki>`. The
software on these machines is managed by the Aalto-IT team.  This is
the place if you need to play with GPUs, deep learning, etc.

The use of :doc:`Triton <../triton/index>` is primarily for research
purposes.  Some very advanced courses may use this, but it generally
only available for research purposes.  Please ask your instructor
first, before asking us.



Data storage
============

Aalto home directories have a 20GB quota, and this is suitable for
small use.  Note that files here are lost once you leave Aalto, so
make sure you back up.

The `IT Services for Research <itsr_>`_ page contains some other cloud
services which may be useful for data storage.

.. _itsr: https://inside.aalto.fi/display/ITServices/IT+Services+for+Research



Software
========

ITS has a `software and licenses <its_sw_>`_ (`FI <its_sw_fi_>`_)
page, and also a `full list of licenses <its_sw_list_>`_.  There is
also http://download.aalto.fi/.  Various scientific software can be
found for your own use via the Aalto software portals.


.. _its_sw: https://inside.aalto.fi/display/ITServices/Software+and+licenses
.. _its_sw_fi: https://inside.aalto.fi/display/ITPK/Ohjelmistot+ja+lisenssit
.. _its_sw_list: https://inside.aalto.fi/display/ITServices/University+software+licenses


The Lmod (``module``) system provides more software on
``brute``/``force`` and in Paniikki.  For example, to access a bunch
of scientific Python software, you can do ``module load anaconda3``.
The :doc:`researcher-focused instructions are here
</triton/tut/modules>`, but like many things on this site you may have
to adapt to the student systems.



Other notes
===========
It can be hard to find your way around Aalto, the official campus maps
and directions are known for being confusing confusing.  Try
`UsefulAaltoMap <http://usefulaaltomap.fi>`_ instead.

Do you have suggestions for this page?  Please leave on `issue on
Github <scicomp_github_issues_>`_ (make sure you have a good title
that mentions the audience is students, so we can put the information
in the right place).  Better yet, send a pull request to us yourself.

.. _scicomp_github_issues: https://github.com/AaltoScienceIT/scicomp-docs/issues
