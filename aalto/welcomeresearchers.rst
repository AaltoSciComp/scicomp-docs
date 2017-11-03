=====================
Welcome, researchers!
=====================

Welcome to Aalto, researchers.  Aalto has excellent resources for you,
but it can be quite hard to learn of them.  These pages will provide a
good overview of IT services for researchers for you (focused on
computation and data-using researchers).

These aren't generic IT instructions - ITS has an introduction for
staff somewhere (TODO: find it online).  There is also a handy list of
`research-focused services <itsr_>`_ provided by ITS.

.. _itsr: https://inside.aalto.fi/display/ITServices/IT+Services+for+Research

.. note::

   Under construction

Aalto service units
===================

Understanding all the Aalto services can be quite confusing.  Here are
some of the key players:

* **Department IT**: Only a few departments (mainly in SCI) have their
  own IT staff.  Others have people such as laboratory managers which
  may be able to provide some useful advice.
* **Science-IT**: Overlaps with SCI department IT groups.  They run the
  Triton cluster and support scientific computing.  The main target
  audience is the departments which fund them, but can assist anyone
  in the university.  The core Science-IT departments are CS, NBE, and
  PHYS.  Science-IT runs a weekly :doc:`SciComp garage
  <../news/garage>`, where we provide hands on support for anything
  related to scientific computing.   `Official site <sci-it>`_, but
  :doc:`this site <../index>` is its day-to-day guidance.
* **Aalto ITS** (IT Services): Provides central IT infrastructure.
  Their support for complicated research situations and special
  scientific software is limited, but they are the first place to
  contact if not in SCI.  Their infrastructure is also used in SCI,
  but supported by department teams.  Their instructions are on `Aalto
  Inside <its_instr_>`_
* **Research and Innovation Services**: Administrative-type support.
  Provides support for grantwriting, innovation and commercialization,
  sponsored projects, legal services for research, and research
  infrastructures.
* **CSC** is the Finnish academic computing center.  They provide a
  lot of basic infrastructure you use without knowing it, as well as
  computing and data services to researchers (all for free).

.. _its_instr: https://inside.aalto.fi/display/ITServices/Home
.. _sci-it: http://science-it.aalto.fi/



End-user systems
================
Aalto provides computers to it's employees, obviously.  You can choose
a managed system or standalone.  If it's standalone, you are on your
own.  If managed, login is through your Aalto account.  You can get
laptop or desktop, and Linux, Mac, or Windows.

Desktops are connected directly to the wired networks.  :doc:`Linux
desktops <../aalto/linux>` have fast and automatic access to all of
the university data storage systems, including Triton and department
storage.  They also have a wide variety of scientific software already
ready (and somewhat similar to Triton).

Managed laptops are usable in and out of the Aalto networks, and you
can become "primary user" which allows you to install some software
yourself (Linux at least).



Computing
=========

You have two primary Aalto options: workstations and Triton.  The
Aalto workstations have basic scientific software installed.  From the
workstations, you can use the :doc:`HTCondor <../aalto/htcondor>`
distributed computing framework.

Most HPC at Aalto is performed on :doc:`Triton <../triton/index>`, the
Aalto HPC cluster.  It is a fairly standard medium-sized cluster, and
it's main advantage is the close integration into the Aalto
environment: it shares Aalto accounts and its data storage (2PB) is
also available on workstations.  Triton is part of the Finnish Grid
and Cloud Infrastructure.

`CSC <https://csc.fi>`_ (the Finnish IT Center for Science) is a
government-owned organization.  They provide a lot of services, most
notably HPC and data management services to the.  All of their
services are free to the academic community (paid directly by the
state of Finland).  They also coordinate the Finnish Grid and Cloud
Infrastructure.  They have the largest known cluster in Finland.



Data
====

Data management isn't just storage: if data is just put somewhere, you
get a massive mess and data isn't usable in even 5 years.  Funders now
require "data management plans".  Thus data management is not just a
*hot* topic, it's an *important* one.  We have a :doc:`whole section
on data <../data/index>`, and also there are higher level :doc:`guides from
Aalto <aaltordm_>`_.  If you have specific questions, there is an
official service email address you can use, or you can ask the
Science-IT team.

.. _aaltordm: http://www.aalto.fi/en/research/research_data_management/

Aalto has many data storage options, most free.  In general, you
should put your data in some centralized location shared with your
group: if you keep it only on your own systems, the data dies when you
leave.

Triton has 2PB of non-backed up data storage on the high-performance
Lustre filesystem.  This is used for large active computation
purposes.  The Triton nodes have an incredible bandwidth to this and
it is very fast and parallel.  This is mounted by default at
Science-IT departments, and can be by default in other departments
too.

Aalto provides "work" and "teamwork" centralized filesystems.
Teamwork is managed by the Science-IT departments and provided to its
researchers.  For other schools/departments, both are provided by
Aalto ITS but you will have to figure out your school's system
yourself.  These systems are snapshotted, backed up, shareable, and
easily available on Aalto workstations.  It's even possible to
directly collect data to these systems from lab equipment.

CSC provides both high-performance Lustre filesystems (like Triton)
and archive systems.

In our :doc:`data management section <../data/index>`, we provide many
more links to long-term data repositories, archival, and so on.  The
`OpenScience.fi <https://openscience.fi>`_ project is state-supported
and has a lot more information on data.  They also provide some
data storage focused on safety and longer-term storage, though they
are harder to use.



Software
========

Triton and :doc:`Aalto Linux workstations <../aalto/linux>` come with
a lot of scientific software installed, with in the :doc:`Lmod system
<../triton/tut/modules>`.  If you are the primary user of a
workstation, you can install Ubuntu packages yourself (and if you
aren't, you should ask to be).  If you use Triton or are in a Science-IT department, it
can be worth asking Science-IT about software you need - we are
experts in this.  Windows workstations can have things automatically
installed, but you'll have to find the method from the ITS
instructions above.

`ITS software and licenses
<https://inside.aalto.fi/display/ITServices/Software+and+licenses>`__.

CSC also has `a lot of software
<https://research.csc.fi/software>`__.  Some is on CSC computers, some
is exported to Triton.



Other notes
===========

Remember to keep the `IT Services for Research page close <itsr_>`_
close at hand!
