=====================
Welcome, researchers!
=====================

Welcome to Aalto, researchers.  Aalto has excellent resources for you,
but it can be quite hard to learn of them.  These pages will provide a
good overview of IT services for researchers for you (focused on
computation and data-using researchers).

These aren't generic IT instructions - ITS has an introduction for
staff somewhere (but apparently not online).  There is also a handy list of
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
  may be able to provide some useful advice.  Known links: `CS
  <cs-it_>`_, `NBE <nbe-it_>`_, `PHYS <phys-it_>`_.
* **Science-IT**: Overlaps with SCI department IT groups.  They run the
  Triton cluster and support scientific computing.  The main target
  audience is the departments which fund them, but can assist anyone
  in the university.  The core Science-IT departments are CS, NBE, and
  PHYS.  Science-IT runs a weekly :doc:`SciComp garage
  <../news/garage>`, where we provide hands on support for anything
  related to scientific computing.   `Official site <sci-it_>`_, but
  :doc:`this site <../index>` is its day-to-day guidance.
* **Aalto ITS** (IT Services): Provides central IT infrastructure.
  Their support for complicated research situations and special
  scientific software is limited, but they are the first place to
  contact if not in the School of Science.  Their infrastructure is also used in SCI,
  but supported by department teams.  Their instructions are on `Aalto
  Inside <its_instr_>`_, but most importantly the already-mentioned
  `IT Services for Research <itsr_>`_ page.
* **Research and Innovation Services**: Administrative-type support.
  Provides support for grantwriting, innovation and commercialization,
  sponsored projects, legal services for research, and research
  infrastructures.
* **CSC** is the Finnish academic computing center.  They provide a
  lot of basic infrastructure you use without knowing it, as well as
  computing and data services to researchers (all for free).

.. _its_instr: https://inside.aalto.fi/display/ITServices/Home
.. _sci-it: http://science-it.aalto.fi/
.. _cs-it: https://wiki.aalto.fi/display/CSdept/IT
.. _nbe-it: https://wiki.aalto.fi/display/NBE/IT+Information
.. _phys-it: https://wiki.aalto.fi/display/TFYintra/PHYS+IT

Also, currently Aalto has information is scattered everywhere:

* `aalto.fi <http://aalto.fi>`__ is the normal homepage, but doesn't
  have much practical information for researchers.
* `inside.aalto.fi <https://inside.aalto.fi>`__ is the typical
  "official" staff documentation area, where most service units have
  their homepages. This is perhaps the most important place to look,
  but is *not* visible in any public search engines or on the search
  engine on the Aalto homepage - you have to go directly here to
  search (so most people never find the Aalto official information).
* `into.aalto.fi <https://into.aalto.fi>`__ is the student official
  information.  It contains a lot of duplicate information compared to
  Inside and is public, so if you search things at Aalto you tend to
  find answers here.
* `wiki.aalto.fi <https://wiki.aalto.fi>`__ is obviously the Aalto
  wiki space.  Anyone can make a space here, and many department's
  internal sites are here.  Searching can randomly find useful
  information.  Most sites aren't publically searchable.
* :doc:`scicomp.aalto.fi <../index>` is where you are now.  Scicomp
  was started by the Science-IT group from the Triton (HPC cluster)
  documentation, which is slowly taking over from our department's
  research IT instructions.  Now is is our general guidance to
  researchers.  We would rather combine with other official sites, but
  currently there's nothing standard-based and open.



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
environment: it shares Aalto accounts, its data storage (2PB) is
also available on workstations, and has responsive local support.  If
you need dedicated resources, you can purchase them and they can be
managed by us as part of Triton.  Triton is part of the Finnish Grid
and Cloud Infrastructure.

`CSC <https://csc.fi>`_ (the Finnish IT Center for Science) is a
government-owned organization.  They provide a lot of services, most
notably HPC, data, and IT infrastructure services to the academic
sector.  All of their services are free to the academic community
(paid directly by the state of Finland).  They also coordinate the
Finnish Grid and Cloud Infrastructure.  They have the largest known
cluster in Finland.



Data
====

Data management isn't just storage: if data is just put somewhere, you
get a massive mess and data isn't usable in even 5 years.  Funders now
require "data management plans".  Thus data management is not just a
*hot* topic, it's an *important* one.  We have a :doc:`whole section
on data <../data/index>`, and also there are higher level `guides from
Aalto <aaltordm_>`_, or you can check :doc:`our guide for researchers
<../data/outline/>`.  If you have specific questions, there is an
official service email address you can use (see the Aalto pages), or
you can ask the Science-IT team.

.. _aaltordm: http://www.aalto.fi/en/research/research_data_management/

Aalto has many data storage options, most free.  In general, you
should put your data in some centralized location shared with your
group: if you keep it only on your own systems, the data dies when you
leave.  We manage data by *projects*: a group of people
with shared access and a manager.  Groups provide flexibility,
sharing, and long-term management (so that you don't lose or forget
about data every time someone leaves).  You can request as many
projects as you need, and each can have its own access control and
quota.  You can read about the :doc:`storage locations available
<../aalto/aaltostorage>` and :doc:`storage service policy
<../data/datapolicy>`.

Triton has 2PB of non-backed up data storage on the high-performance
Lustre filesystem.  This is used for large active computation
purposes.  The Triton nodes have an incredible bandwidth to this and
it is very fast and parallel.  This is mounted by default at
Science-IT departments, and can be by default in other departments
too.

Aalto provides "work" and "teamwork" centralized filesystems which are
large, backed up, snapshotted, shared: everything you may want.
Within the Science-IT departments, Science-IT and department IT
manages it and provides access.  For other schools/departments, both
are provided by Aalto ITS but you will have to figure out your
school's policies yourself.  It's even possible to directly collect
data to these systems from lab equipment.

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
experts in this and working to simplify the mess that scientific
software is.  Windows workstations can have things automatically
installed, but you'll have to find the method from the ITS
instructions above.

Triton and Aalto workstations have the central software available,
currently for laptops you are on your own.

On Triton, type ``module spider $name`` to search for available
software.  We are working to unify the software stack available on
Triton and Aalto workstations.

ITS has a `software and licenses <its_sw_>`_ (`FI <its_sw_fi_>`_)
page, and also a `full list of licenses <its_sw_list_>`_.  There is
also https://download.aalto.fi/.

.. _its_sw: https://inside.aalto.fi/display/ITServices/Software+and+licenses
.. _its_sw_fi: https://inside.aalto.fi/display/ITPK/Ohjelmistot+ja+lisenssit
.. _its_sw_list: https://inside.aalto.fi/display/ITServices/University+software+licenses
.. _sw_download: http://download.aalto.fi/

CSC also has `a lot of software
<https://research.csc.fi/software>`__.  Some is on CSC computers, some
is exported to Triton.



Starting a project
==================
Each time you start a project, it's worth putting a few minutes into
planning so that you create a good base (and don't end up with chaos
in a few years).

- Do the normal Aalto bureaucratic work.  We don't know about that, and
  this guide does *not* relate to that.  You also don't have to do
  that stuff in order to do the steps below.

- Request a data group (see above) if you don't already have a good
  location.  This will keep all of your data together, in the same
  place.

  - If you already have a data group that is suitable (similar
    members), you can use that.  But there's no limit to the number of
    projects, so think about if it's better to keep things apart earlier.

  - Mail your department IT support and request a group.  Give the
    info requested at the bottom of :doc:`data outline page
    <../data/outline>`.

  - In the same message, request the different data storage
    locations, e.g. scratch, project, archive.  Quotas can always be
    increased later.

- Think about how you'll manage data.  It's always easy to just start
  working, but it can be worth getting all project members on the same
  page about where data will be stored and what you want to happen to
  it in the end.  Having a very short thing written will also help a
  lot to get newcomers started.  The :doc:`"practical DMP" section
  here <../data/plans>` can help a lot - try filling out that A4 page
  to consider the big sections.



Training
========

Of course you want to get straight to research.  However, we come from
a wide range of backgrounds and we've noticed that missing basic
skills (computer as a tool) can be a research bottleneck.  We have
constructed a :doc:`multi-level training plan <../training/index>` so
that you can find the right courses for your needs.  These courses are
selected by researchers for researchers, so we make sure that
everything is relevant to you.



Other notes
===========

Remember to keep the `IT Services for Research page close <itsr_>`_
close at hand!

There are some good `cheatsheets
<https://users.aalto.fi/~darstr1/cheatsheets/>`__ which our team
maintains.  They are somewhat sepcialized, but useful in the right
places.

It can be hard to find your way around Aalto, the official campus maps
and directions are known for being confusing confusing.  Try
`UsefulAaltoMap <http://usefulaaltomap.fi>`_ instead.
