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

.. _itsr: https://www.aalto.fi/en/services/it-services-for-research


Aalto service units
===================

Understanding all the Aalto services can be quite confusing.  Here are
some of the key players:

* **Department IT**: Only a few departments (mainly in SCI) have their
  own IT staff.  Others have people such as laboratory managers which
  may be able to provide some useful advice.  Known links: `CS
  <cs-it_>`_, `NBE <nbe-it_>`_, `PHYS <phys-it_>`_.
* **Science-IT**: Overlaps with SCI department IT groups.  They run the
  Triton cluster and support scientific computing.  Their services may
  be used throughout the entire university, but support is organized from
  the departments which fund them.
  The core Science-IT departments are CS, NBE, and
  PHYS.  Science-IT runs a weekly :doc:`SciComp garage
  <../news/garage>`, where we provide hands on support for anything
  related to scientific computing.
  :doc:`This site (scicomp.aalto.fi) <../index>` is the user
  instructions, but there is also an `official site <sci-it_>`_.
* **Aalto ITS** (IT Services): Provides central IT infrastructure.
  Their support for complicated research situations and special
  scientific software is limited, but they may be the first place to
  contact if not in the School of Science.  Their infrastructure is
  used in all schools including SCI,
  but supported by department teams.  Their instructions are on `Aalto
  Inside <its_instr_>`_, but most importantly the already-mentioned
  `IT Services for Research <itsr_>`_ page.  Contact via `servicedesk
  <https://it.aalto.fi/contact>`__.
* **Research and Innovation Services**: Administrative-type support.
  Provides support for grantwriting, innovation and commercialization,
  sponsored projects, legal services for research, and research
  infrastructures.  (From 2019, they are split into Research Services
  and Innovation Services)
* **CSC** is the Finnish academic computing center (and more).  They provide a
  lot of basic infrastructure you use without knowing it, as well as
  computing and data services to researchers (all for free).

.. _its_instr: https://inside.aalto.fi/display/ITServices/Home
.. _sci-it: http://science-it.aalto.fi/
.. _cs-it: https://wiki.aalto.fi/display/CSdept/IT
.. _nbe-it: https://wiki.aalto.fi/display/NBE/IT+Information
.. _phys-it: https://wiki.aalto.fi/display/TFYintra/PHYS+IT

Also, currently Aalto has information scattered on websites
everywhere:

* `aalto.fi <http://aalto.fi>`__ is the normal homepage, but doesn't
  have much practical information for researchers.  As of late 2018,
  information from inside and into is supposed to move here.  The new
  site is very hard to navigate (sorry, we can't do anything about
  that) and the old site can be accessed at old.aalto.fi for a while.
  This site is "not designed to have a logical structure and instead,
  you are expected to search for information" (actual quote).
  Some information is randomly hidden unless you log in.
* `it.aalto.fi <https://it.aalto.fi>`__ is a new location for IT
  instructions, and somewhat replaces the old IT instructions on
  inside.aalto.fi and into.aalto.fi.  These generally relate to how to
  do a specific task -
  but not necessarily what is the best thing to do.
* `inside.aalto.fi <https://inside.aalto.fi>`__ is the *former* typical
  "official" staff documentation area, where most service units have
  their homepages.  In the 2018 redesign, this is supposed to be
  merged to aalto.fi, but we don't know how that is going.  It may not
  be updated anymore.  (Former info: This is
  perhaps the most important place to look,
  but is *not* visible in any public search engines or on the search
  engine on the Aalto homepage - you have to go directly here to
  search (so most people never find the Aalto official information).)
* `into.aalto.fi <https://into.aalto.fi>`__ is the student official
  information.  It contains a lot of duplicate information compared to
  Inside and is public, so if you search things at Aalto you tend to
  find answers here.  We heard it is also supposed to merge with
  aalto.fi - we have no idea how that is going, it was re-developed
  in 2018.
* `wiki.aalto.fi <https://wiki.aalto.fi>`__ is obviously the Aalto
  wiki space.  Anyone can make a space here, and many departments'
  internal sites are here.  Searching can randomly find useful
  information.  Most sites aren't publically searchable.
* :doc:`scicomp.aalto.fi <../index>` is where you are now.  Scicomp
  was started by the Science-IT team from the Triton (HPC cluster)
  documentation, and scicomp is slowly taking over from our
  departments'
  research IT instructions.  Now it is our general guidance to
  researchers and the best place to find information on research and
  scientific computing - as opposed to general "staff computing" you
  find other places.



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
ready (and somewhat similar to Triton).  We have some limited
instructions and pointers to the main instructions for :doc:`mac
<../aalto/mac>` and :doc:`windows <windows>` computers.

Managed laptops are usable in and out of the Aalto networks, and you
can become "primary user" which allows you to install some software
yourself (Linux at least).



Computing
=========

You have two primary Aalto options: workstations and Triton.  The
Aalto workstations have basic scientific software installed.  From the
workstations, you can use the :doc:`HTCondor <../aalto/htcondor>`
distributed computing framework.

Most demanding computing at Aalto is performed on :doc:`Triton
<../triton/index>`, the
Aalto high performance computing cluster.  It is a fairly standard
medium-sized cluster, and
it's main advantage is the close integration into the Aalto
environment: it shares Aalto accounts, its data storage (2PB) is
also available on workstations, and has local support.  If
you need dedicated resources, you can purchase them and they can be
managed by us as part of Triton so that you get dedicated resources
and can easily scale to the full power of Triton.  Triton is part of
the Finnish Grid and Cloud Infrastructure.  Triton is the largest
publically known computing cluster in Finland after the CSC clusters.
Triton provides a web-based interface via :doc:`JupyterHub
<../triton/apps/jupyter>`.

`CSC <https://csc.fi>`_ (the Finnish IT Center for Science) is a
government-owned organization which provides a lot of services, most
notably HPC, data, and IT infrastructure services to the academic
sector.  All of their services are free to the academic community
(paid directly by the state of Finland).  They also coordinate the
Finnish Grid and Cloud Infrastructure.  They have the largest known
clusters in Finland.



Data
====

Data management isn't just storage: if data is just put somewhere, you
get a massive mess and data isn't usable in even 5 years.  Funders now
require "data management plans".  Thus data management is not just a
*hot* topic, it's an *important* one.  We have a :doc:`whole section
on data <../data/index>`, and also there are higher level `guides from
Aalto <aaltordm_>`_.  If you just want to get something done, you
should start with our :doc:`Aalto-specific guideline for Science-IT
data storage <aaltodata>` (used in CS, NBE, PHYS) - if you follow our
plan, you will be doing better than most people..  If you have
specific questions, there is an official service email address you can
use (see the Aalto pages), or you can ask the Science-IT team.

.. _aaltordm: http://www.aalto.fi/en/research/research_data_management/

Aalto has many data storage options, most free.  In general, you
should put your data in some centralized location shared with your
group: if you keep it only on your own systems, the data dies when you
leave.  We manage data by *projects*: a group of people
with shared access and a leader.  Groups provide flexibility,
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
data to these systems from lab equipment.  (In general, "work" is
organized by the Aalto hierarchy, while "teamwork" is flatter.  If you
consider yourself mainly Aalto staff who fits in the hierarchy, work
is probably better.  If you consider yourself a research who
collaborates with whoever, teamwork is better.)

CSC provides both high-performance Lustre filesystems (like Triton)
and archive systems.

In our :doc:`data management section <../data/index>`, we provide many
more links to long-term data repositories, archival, and so on.  The
`OpenScience.fi <https://openscience.fi>`_ project is state-supported
and has a lot more information on data (maybe `fairdata.fi
<https://www.fairdata.fi>`__ is the new site?).  They also provide some
data storage focused on safety and longer-term storage (like `IDA
<ida>`__), though they are not very used at Aalto because we provide
such good services locally.

.. _ida: https://www.fairdata.fi/en/ida/

Aalto provides, with Aalto accounts, `Google Drive <gdrive_>`_
(unlimited, also Team Drives), `Dropbox <dropbox_>`_ (unlimited), and
`Microsoft OneDrive <onedrive_>`_ (5TB).  Be aware that once you leave
Aalto, this data will disappear!

.. _gdrive: https://it.aalto.fi/instructions/google-drive-registration-and-closing-account
.. _dropbox: https://it.aalto.fi/instructions/aalto-dropbox-quick-guide
.. _onedrive: https://it.aalto.fi/instructions/onedrive-quick-guide

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
installed, check the :doc:`windows page <windows>`.

Triton and Aalto workstations have the central software available,
currently for laptops you are on your own.

On Triton and Linux workstations, type ``module spider $name`` to
search for available software.  We are working to unify the software
stack available on Triton and Aalto workstations.

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

- Think about how you'll manage data.  It's always easy to just start
  working, but it can be worth getting all project members on the same
  page about where data will be stored and what you want to happen to
  it in the end.  Having a very short thing written will also help a
  lot to get newcomers started.  The :doc:`"practical DMP" section
  here <../data/plans>` can help a lot - try filling out that A4 page
  to consider the big sections.

- Request a data group (see above) if you don't already have a shared
  storage location.  This will keep all of your data together, in the same
  place.  As people join, you can easily give them access.

  - If you already have a data group that is suitable (similar
    members), you can use that.  But there's no limit to the number of
    projects, so think about if it's better to keep things apart earlier.

  - Mail your department IT support and request a group.  Give the
    info requested at the bottom of :doc:`data outline page
    <../data/outline>`.

  - In the same message, request the different data storage
    locations, e.g. scratch, project, archive.  Quotas can always be
    increased later.



Training
========

Of course you want to get straight to research.  However, we come from
a wide range of backgrounds and we've noticed that missing basic
skills (computer as a tool) can be a research bottleneck.  We have
constructed a :doc:`multi-level training plan <../training/index>` so
that you can find the right courses for your needs.  These courses are
selected by researchers for researchers, so we make sure that
everything is relevant to you.

Check our `upcoming training page
<http://science-it.aalto.fi/scip/>`__ for a list of upcoming courses.
If you do anything computational or code-based at all, you should
consider the twice-yearly `CodeRefinery <http://coderefinery.org/>`__
workshops (announced on our page).  If you have a Triton account or do
high-performance computing or intensive computing or data-related
tasks, you should come to the Summer (3 days) or Winter (1 day)
kickstart, which teaches you the basics of Triton and HPC usage (we
say it is "required" if you have a Triton account).



Other notes
===========

Remember to keep the `IT Services for Research page close <itsr_>`_
close at hand!

Research is usually collaborative, but sometimes you can feel
isolated - either because you are lost in a crowd, or far away from
your colleagues.  Academic courses don't teach you everything you need
to be good at scientific computing - put some effort into working
together with, learning from, and teaching your colleagues and you
will get much further.

There are some good `cheatsheets
<https://users.aalto.fi/~darstr1/cheatsheets/>`__ which our team
maintains.  They are somewhat sepcialized, but useful in the right
places.

It can be hard to find your way around Aalto, the official campus maps
and directions are known for being confusing confusing.  Try
`UsefulAaltoMap <http://usefulaaltomap.fi>`_ instead.
