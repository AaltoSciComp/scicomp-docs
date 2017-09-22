===================================
Outline of academic data management
===================================

This page is about how to use data - not the raw storage part, which
you can find at `data storage <aaltostorage>`_.  Aalto has high-level
information on `research data management <aaltordm>`_, too.

.. _aaltordm: http://www.aalto.fi/en/research/research_data_management/

What is data management?
------------------------

Data management is much more than just storage. It concerns everything
from data collection, to data rights, to end-of-life (archival,
opening, etc). This may seem far-removed from research practicalities,
but funding agencies are beginning to require advanced
planning. Luckily, there are plenty of resources at Aalto (especially
in SCI), and it's just a matter of connecting the dots.

Oh, also, data management is important, because without data management,
data becomes disorganized, you lose track, and as people come and go,
you lose knowledge of what you have. Don't let this happen to you or
your group!

A good starting point is the `Aalto research data management pages
<aaltordm>`_. These pages can also help with preparing a data
management plan.

**Data management is an important part of modern science! We are here
to help.** These pages both describe the resources available at Aalto
(via Science-IT), and provide pointers to issues that may be relevant
to your research.

Data storage at Aalto SCI (principles and policies)
---------------------------------------------------

.. note::

   This especially applies to CS, NBE, and PHYS (the core Science-IT
   departments).  The same is true for everyone using Triton.  These
   policies are a good idea for everyone at Aalto.

Most data should be stored in a **group (project) directory**, so that
multiple people can access it and there is a plan for after you leave.
Ask your supervisor/colleagues what your group's existing groups are and
where the data is stored. **Work data should always be stored in a
project directory, not personal home directories.** See below for how to
create or join a group. Home directory data can not be accessed by IT
staff, according to law and policy - data there dies when you leave.

All data in group directories is considered accessible to all members
(see below).

All data stored should be Aalto or research related. Should there
be questions, ask. Finnish law and Aalto policies must be followed (in
that order), including by IT staff. Should there be agreements with
third-parties regarding data rights, those will also be followed by
IT staff, but these must be planned in advance.

All data must have an owner and lifespan. We work with large amount of
data from many different people, and data without clear ownership
becomes a problem. ("ownership" refers to decision-making
responsibility, not IPR ownership). Also, there must be a clear
successor for when people leave or become unavailable. By default, this
is supervisor.

Personal workstations are considered stateless and, unless there is
special agreement, could be reinstalled at any time and are not backed
up. This should not concern day to day operations, since by default all
data is stored on network filesystems.

We will, in principle, make space for whatever data is
needed. However, it is required that it be managed well. If you can
answer what the data contains, why it's stored, and how the space is
used, and why it's needed, it's probably managed well.

Read the full data management policy here (TODO).

Information on all physical locations how to use them is on the `storage
page <aaltostorage>`_.

Groups
~~~~~~

*Please see the bottom of this page for instructions on requesting and
managing groups, including getting access to data.*

Everywhere on this page, "group" refers to unix groups, not
organizational groups. They will often overlap, but there can be many
more unix groups made for more fine-grained data access.

Data is stored in group directories. A group may represent a real
research group, a specific project, or specific access-controlled data.
These are easy to make, and they should be extensively used to keep data
organized.

Please note, that by design all project data is accessible to every
member in the project. This means that, when needed, IT can fix all
permissions so that all group members can read all data. For limiting
the access more fine-grained than these project groups, please have a
separate group created. Data in a group is considered "owned and
managed" by the group owner on file. The owner may grant access to
others and change permissions as needed. Unless otherwise agreed, any
group member may also request permissions to be corrected so that
everyone in the group has access.

-  **Access control is provided by unix groups** (managed in the Aalto
   active directory). There can be one group per group leader, project,
   or data that needs isolation. You should use many groups, they make
   overall management easier. A group can be a sub-group of another.
-  **Each group can get its own quota** and fileystem directories
   (project, archive, scratch, etc). Quota is per-filesystem. Tell us
   requested quota when you set up a project.

   -  A typical setup would be: one unix group for a research group,
      with more groups for specific project when that is helpful. If
      there are fixed multi-year projects, they can also get a group.

-  Groups are managed by IT staff. To request a group, mail us with
   the necessary information (see next point).
-  Each group has an owner, quota on filesystems, and some other
   metadata (see below),
-  **To have a group created and storage space allocated**, see below.
-  **To get added to a group**, see instructions below.
-  To see your groups: use the ``groups`` command or
   ``groups $username``
-  To see all members of a group: ``gentent group $groupname``

Common data management considerations
-------------------------------------

Backups
~~~~~~~

Backups are extremely important, not just for hardware failure, but
consider user error (rm the wrong file), device loss, etc. Not all
locations are backed up. It is your responsibility to make sure that
data gets stored in a place with sufficient backups. Note that personal
workstations and mobile devices (laptops) are not backed up.

Confidential or sensitive data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Aalto has some `guidelines for classification of confidential
information <https://inside.aalto.fi/display/ArchiveandRegistryServices/Guidelines+-+Classification+of+Information>`__,
but they tend to deal with documents as opposed to practical guidelines
for research data. If you have data which needs special attention, you
must mention this to us first. The following paragraph can be used as a
summary of data security for proposals, and a longer description is
available on request.

Aalto SCI provides secure data storage for confidential data. This data
is stored centrally in protected datacenters and is managed by dedicated
staff. All access is through individual Aalto accounts, and all data is
stored in group-specific directories with per-person access control.
Access rights via groups is managed by IT, but data access is only
provided upon request of the data owner. All data is made available only
through secure, encrypted, and password-protected systems: it is
impossible for any person to get data access without a currently active
user account, password, and group access rights. Backups are made and
also kept confidential. All data is securely deleted at the end of life.
CS-IT provides training and consulting for confidential data management.

If you have confidential data at CS, follow these steps. CS-IT takes
responsibility that data managed this way is secure, and it is your
responsibility to follow CS-IT's rules. Otherwise you are on your own:

-  Request a new data folder in the project from CS-IT. Notify them that
   it will hold confidential data and any special considerations or
   requirements. Consider how fine-grained you would like the group: you
   can use an existing group, but consider how many people will have
   access.
-  Store data only in this directory on the network drive. It can be
   accessed from CS computers, see `data
   storage <aaltostorage>`__.
-  To access data from laptops (Aalto or your own), use `network drive
   mounting <LINK/Remote%20access>`__, not copying. Also consider if
   temporary files: don't store intermediate work or let your programs
   save temporary files to your own computer.
-  Don't transfer the data to external media (USB drives, external hard
   drives, etc) or your own laptops or computers. Access over the
   network.
-  All data access should go through Aalto accounts. Don't send data to
   others and or create other access methods. Aalto accounts provide
   central auditing and access control.
-  Realize that you are responsible for the day to day management of
   data and using best practices. You are also responsible for ensuring
   that people who have access to the data follow this policy.
-  In principle, one can store data on laptops or external devices with
   full disk encryption. However, in this case we does not take
   responsibility unless you ask us first.you must ask us about this. In
   general it's best to try to adapt to the network drive workflow.
   (Laptop full disk encryption is a good idea anyway).

We can assist in creating more secure data systems, as can Aalto IT
security. It's probably more efficient to contact us first.

Personal data (research data about others, not about you)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"Personal data" is any data concerning an identifiable person. Personal
data is very highly regulated (mainly by the Personal Data Act, soon by
the General Data Protection Regulation). Aalto has a `document that
describes what is needed to process personal data for
research <https://into.aalto.fi/display/enregulations/The+processing+of+personal+data+in+scientific+research>`__,
which is basically a research-oriented summary of the Personal Data Act.
Depending on the type of project, approval from the `Research Ethics
Committee <https://inside.aalto.fi/display/AboutAalto/Research+Ethics+Committee>`__
may be needed (either for publication, or for human interaction. The
second one would not usually cover pure data analysis of existing data).
Personal data handling procedures are currently not very well defined at
Aalto, so you will need to use your judgement.

However, most research does not need data to be personally identifiable,
and thus research is made much simpler. Thus, you want to try to always
make sure that data is not identifiable, even to yourself using any
technique (anonymization). The legal requirement is "reasonable
likelihood of identification", which can include technical and
confidentiality measures, but in the end is still rather subjective.
Always anonymize before data arrives at Aalto, if possible. Let us know
when you have personal data, so we can make a note of it in the data
project.

However, should you need to use personal data, the process is not
excessively involved beyond what you might expect (informed consent,
ethics, but then a notification of personal data file). Contact us for
initial help in navigating the issues and RIS for full advice.

Openness
~~~~~~~~

You should consider releasing data openly when possible. Aalto
encourages this. See the research data management web pages (at top) for
some basic information. For small data, `Zenodo <https://zenodo.org>`__ is a
good way to open it (and provides DOIs so that it can be cited). For
larger data, there are other resources, such as IDA/AVAA provided by CSC
(see below).

There are lists of data repositories:
`r3data <http://www.re3data.org/>`__, and `Nature Scientific Data's
list <http://www.nature.com/sdata/policies/repositories>`__.

Datasets can and should also be listed on `ACRIS
<https://acris.aalto.fi>`__, just like papers - this allows you to get
credit for them in the university's academic reporting.

Data management plans
~~~~~~~~~~~~~~~~~~~~~

The `Aalto data management plan
page <http://www.aalto.fi/en/research/research_data_management/data_management_planning/>`__
combined with this page should provide a starting point for creating a
data management plan. Should you need more advice, please ask, we can
help here.

We hope to have some standard texts which can be used for grants and
data management plans.

Long-term archival
~~~~~~~~~~~~~~~~~~

Long-term archival is important to make sure that you have ability to
access your group's own data in the long term. Aalto resources are not
currently intended for long-term archival. There are other resources
available for this, such as

-  the EU-funded `Zenodo <https://zenodo.org/>`__ for open published
   data (embargoed data, or closed data is also somewhat supported).
-  Finland's `IDA <http://openscience.fi/ida>`__ (for large data, long
   term storage, closed or open). There are `Aalto-specific instructions
   for IDA here <LINK/IDA>`__.
-  There is supposed to be an alternate `Finnish digital preservation
   service <http://openscience.fi/digital-preservation>`__ coming in
   2017, and it's unclear what the intention of IDA is in light of that.

Archival when you leave
~~~~~~~~~~~~~~~~~~~~~~~

Unfortunately, everyone leaves Aalto sometime. Have you considered
what will happen to your data?  Do you want to be remembered? This
section currently is written from the perspective of a researcher, not
a professor-level staff member, but if you are a group leader you need
to make sure your data will stay available! Science-IT (and most of
these resources) are focused on research needs, not archiving a
person's personal research data. In general, we can archive data as
part of a professor's group data (managed in the group directories the
normal ways), but not for individuals.

-  Remember that your home directories get removed when your account
   expires (we think in only two weeks!).
-  Data in the group directories it won't be automatically deleted. But
   you should clean up all your junk and leave only what is needed for
   future people. Remember, if you don't take care of it, it becomes
   extremely hard for anyone else to. The owner of the group (professor)
   will be responsible for deciding what to do with the data, so make
   sure to discuss with them!
-  Can your data be released openly? If you can release something as
   open data on a reputable archive site like Zenodo, you can ensure
   that you will always have access to it.  (The best way to back up
   is to let the whole internet do it for you.)
-  For lightweight archival (~5 years past last use, not too big), the
   archive filesystem is suitable. The data must be in a group directory
   (probably your professor's). Make sure that you discuss the plans
   with them, since they will have to manage it.
-  IDA (see above) could be used for archival of any data, but you will
   have to maintain a CSC account (TODO: can this work, and how?). Also,
   these projects have to be owned by a senior-level staff person, so
   you have to transfer it to a group anyway.
-  Finland aims to have a long-term archival service by 2017
   (`PAS <http://openscience.fi/digital-preservation>`__), but this is
   probably not intended for own data. Anyway, if you need something
   that long and it isn't confidential, consider opening it.

Summary of data locations
-------------------------

Below is a summary table that describes the primary options for research
data:

+----------------+----------------+----------------+----------------+----------------+
| Solution       | Purpose        | Visible on     | Backup         | Group          |
|                |                | workstations   |                | management     |
+================+================+================+================+================+
| project        | Research time  | /m/cs/project/ | Weekly backup  | yes            |
| directories    | storage for    | $group/        | to tape (to    |                |
|                | data that      |                | recover from   |                |
|                | requires       |                | major failure) |                |
|                | backup. Good   |                | + snapshots    |                |
|                | for e.g. code, |                | (recover       |                |
|                | articles,      |                | accidentally   |                |
|                | other          |                | deleted        |                |
|                | important      |                | files).        |                |
|                | data.          |                |                |                |
|                | Generally for  |                | Snapshots go   |                |
|                | small amount   |                | back           |                |
|                | (<500GB) of    |                |                |                |
|                | data per       |                | -  hourly last |                |
|                | project.       |                |    26 working  |                |
|                |                |                |    hours       |                |
|                |                |                |    (8-20)      |                |
|                |                |                | -  daily last  |                |
|                |                |                |    14 days     |                |
|                |                |                | -  weekly last |                |
|                |                |                |    10 weeks    |                |
+----------------+----------------+----------------+----------------+----------------+
| archive        | For data that  | /m/cs/archive/ | Same as above  | yes            |
| directories    | should be kept | $group/        |                |                |
|                | accessible for |                |                |                |
|                | 1-5 years      |                |                |                |
|                | after the      |                |                |                |
|                | project has    |                |                |                |
|                | ended.         |                |                |                |
|                | Alternatively  |                |                |                |
|                | a good place   |                |                |                |
|                | to store a     |                |                |                |
|                | copy of a      |                |                |                |
|                | large original |                |                |                |
|                | data (backup). |                |                |                |
+----------------+----------------+----------------+----------------+----------------+
| Science-IT     | Research time  | /m/cs/scratch/ | No backup (but | yes            |
| scratch/work   | storage for    | $group/        | RAID6)         |                |
| (Triton        | data that does |                |                |                |
| storage)       | not require    | /m/cs/work/$us |                |                |
|                | backup. Good   | ername/        |                |                |
|                | for temporary  |                |                |                |
|                | files and      |                |                |                |
|                | large data     |                |                |                |
|                | sets where the |                |                |                |
|                | backup of      |                |                |                |
|                | original copy  |                |                |                |
|                | is somewhere   |                |                |                |
|                | else (e.g.     |                |                |                |
|                | archive or     |                |                |                |
|                | version        |                |                |                |
|                | control        |                |                |                |
|                | system).       |                |                |                |
+----------------+----------------+----------------+----------------+----------------+
| Custom         | Ask us         |                |                |                |
| solution       |                |                |                |                |
+----------------+----------------+----------------+----------------+----------------+

See `data storage <aaltostorage>`_ for full info.

Instructions
------------

Responsible contacts:

* CS: `CS-IT (guru) email here <http://do.cs.aalto.fi>`_
* NBE: `NBE IT (it-nbe) email here <https://wiki.aalto.fi/display/NBE/IT+Information>`_
* PHYS:

Requesting to be added to a group
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Send an email to the responsible contact (see above) and **CC the
group owner or responsible person**, and include this information:

-  Group name that you request to join
-  copy and paste this statement, or something similar: "I am aware that
   all data stored here is managed by the group's owner and have read
   the data management policies."
-  Ask the group owner to reply with confirmation.
-  Do you need access to scratch or work? If so, you need a Triton
   account and you can request it now. If you don't, you'll get
   "input/output error" and be confused.
-  Example:

     Hi, I (account=omes1) would like to join the group ``myprof``.  I
     am aware that all data stored here is managed by the group's
     owner and have read the data management policies.
     ``$professor_name``, please reply confirming.

Requesting a new group
~~~~~~~~~~~~~~~~~~~~~~

Send an email to the responsible contact (see above) with the following information. Group
owners should be long-term (e.g. professor level) staff.

-  Requested group name (you can check the name from the lists below)
-  Owner of data (prof or long-term staff member)
-  Other responsible people who can authorized adding new members to the
   group. (these can reply and say "yes" when someone asks to join the
   group.)
-  Who is responsible for data should you become unavailable (default:
   supervisor who is probably head of department).
-  Initial members
-  Expiration time (default=max 2 years, extendable. max 5 years
   archive). We will ping you for management/renewal then.
-  Which filesystems and what quota. (project, archive, scratch). See
   the `the storage page <aaltostorage>`__.
-  Basic description of purpose of group.
-  Is there any confidential or secret data (see above for disclaimer).
-  Any other notes that CS-IT should enforce, for example check NDA
   before giving access.
-  Example:

       I would like to request a new group ``coolproject``. I am the
       owner, but my postdoc Tiina Tekkari can also approve adding
       members.  (Should I become unavailable, my colleague Anna
       Algorithmi (also a professor here) can provide advice on what
       to do with the data)

       We would like 20GB on the ``project`` filesystem.

       This is for our day to day work in algorithms development, we
       don't expect anything too confidential.

Existing data groups
--------------------

Here are some lists of existing data groups, listing group names,
owners, and so on. Refer to it should you need to get access to
existing data (although best is to ask your supervisor).

* `CS list <https://wiki.aalto.fi/display/CSdept/Data+groups>`_
* `NBE list <https://wiki.aalto.fi/display/NBE/Data+groups>`_


