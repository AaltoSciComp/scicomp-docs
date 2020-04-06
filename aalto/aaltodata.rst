==================================================
Data: outline, requesting space, requesting access
==================================================

.. note::

   Need a place to store your data?  This is the place to look.
   First, we expect you to read and understand the top information.
   Then, see the :ref:`instructions <instructions>` at bottom.

This page is about how to handle data - not the raw storage part, which
you can find at :doc:`data storage <../aalto/aaltostorage>`.  Aalto has high-level
information on `research data management <aaltordm_>`_, too.

.. _aaltordm: https://www.aalto.fi/en/services/research-data-management-rdm-and-open-science

What is data management?
------------------------

Data management is much more than just storage. It concerns everything
from data collection, to data rights, to end-of-life (archival,
opening, etc). This may seem far-removed from research practicalities,
but funding agencies are beginning to require advanced
planning. Luckily, there are plenty of resources at Aalto (especially
in SCI), and it's just a matter of connecting the dots.

Oh, and data management is also important because without data management,
data becomes disorganized, you lose track, and as people come and go,
you lose knowledge of what you have. Don't let this happen to you or
your group!

Another good starting point is the `Aalto research data management pages
<aaltordm_>`_. These pages can also help with preparing a data
management plan.

**Data management is an important part of modern science! We are here
to help.** These pages both describe the resources available at Aalto
(via Science-IT), and provide pointers to issues that may be relevant
to your research.

Data storage at Aalto SCI (principles and policies)
---------------------------------------------------

.. note::

   This especially applies to CS, NBE, and PHYS (the core Science-IT
   departments).  The same is true for everyone using Triton storage.  These
   policies are a good idea for everyone at Aalto, and are slowly
   being developed at the university level.

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
used, and why it's needed, it's probably managed well for these
purposes.

Read the full :doc:`Science-IT data management policy here
<datapolicy>`.

Information on all physical locations how to use them is on the :doc:`storage
page <../aalto/aaltostorage>`.

Groups
~~~~~~

Everywhere on this page, "group" refers to a certain file access group
groups (such as a unix group), not an organizational (research) group. They will often be the
same, but there can be many
more access groups made for more fine-grained data access.

Data is stored in group directories. A group may represent a real
research group, a specific project, or specific access-controlled data.
These are easy to make, and they should be extensively used to keep data
organized.  If you need either finer-grained or more wide data access,
request that more groups are made.

Please note, that by design all project data is accessible to every
member in the group. This means that, when needed, IT can fix all
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
-  To see all members of a group: ``getent group $groupname``

Common data management considerations
-------------------------------------

Organizing data
~~~~~~~~~~~~~~~

This may seem kind of obvious, but you want to keep data organized.
Data is always growing in volume and variety, so if you don't organize
it as it is being made, you have no chance of doing it later.
Organize by:

* Project
* To be backed up vs can be recreated
* Original vs processed.
* Confidential or not confidential
* To be archived long-term vs to be deleted

Of course, make different directories to sort things.  But also the
group system described above is one of the pillars of good data
organization: sort things by group and storage location based on how
it needs to be handled.

Backups
~~~~~~~

Backups are extremely important, not just for hardware failure, but
consider user error (delete the wrong file), device lost or stolen, etc. Not all
locations are backed up. It is your responsibility to make sure that
data gets stored in a place with sufficient backups. Note that personal
workstations and mobile devices (laptops) are not backed up.

Confidential or sensitive data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note::

   The following description is written for the CS department, but
   applies almost equally to NBE and PHYS.  This is being expanded and
   generalized to other department as well.  Regardless of your
   department, these are good steps to follow for any confidential
   data at Aalto.

.. note::

   This meets the requirements for "Confidential" data, which covers
   most use cases.  If you have extreme requirements, you will need
   something more (but be careful about making custom solutions).

Aalto has some `guidelines for classification of confidential
information <https://inside.aalto.fi/display/ArchiveandRegistryServices/Guidelines+-+Classification+of+Information>`__,
but they tend to deal with documents as opposed to practical guidelines
for research data. If you have data which needs special attention, you
should put it in a separate group and tell us when creating the
group.

The following paragraph is a "summary for proposals", which can be
used when the CS data security needs to be documented.  This is for
the CS department, but similar thing can be created for other
departments.  A longer description is also available.

    Aalto CS provides secure data storage for confidential data. This data
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
   accessed from CS computers, see :doc:`data
   storage <../aalto/aaltostorage>`.
-  To access data from laptops (Aalto or your own), use :doc:`network drive
   mounting <../aalto/remoteaccess>`, not copying. Also consider if
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
research <https://www.aalto.fi/en/services/how-to-handle-personal-data-in-research>`__,
which is basically a research-oriented summary of the Personal Data Act.
Depending on the type of project, approval from the `Research Ethics
Committee <https://inside.aalto.fi/display/AboutAalto/Research+Ethics+Committee>`__
may be needed (either for publication, or for human interaction. The
second one would not usually cover pure data analysis of existing data).
Personal data handling procedures are currently not very well defined at
Aalto, so you will need to use your judgment.

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

Aalto strongly encourages to share the data openly or under controlled
access with a goal of 50% data shared by 2020 (see
`The Aalto RDM pages <https://www.aalto.fi/en/services/research-data-management-rdm-and-open-science>`__).
In short, Aalto says that you "must" make
strategic decisions about openness for the best benefits (which
practically probably means you can do what you would like).
Regardless, being open is usually a good idea when you can: it builds
impact for your work and benefits society more.

Zenodo (https://zenodo.org/) is an excellent platform for sharing data, getting
your data cited (it provides a DOI), and control what you share with
different policies (https://about.zenodo.org/policies/).  For
larger data, there are other resources, such as IDA/AVAA provided by CSC
(see below).

There are lists of data repositories:
`r3data <https://www.re3data.org/>`__, and `Nature Scientific Data's
list <https://www.nature.com/sdata/policies/repositories>`__.

Datasets can and should also be listed on `ACRIS
<https://acris.aalto.fi>`__, just like papers - this allows you to get
credit for them in the university's academic reporting.

Data management plans
~~~~~~~~~~~~~~~~~~~~~

Many funders now require data management plans when submitting
grants.  (Aside from this, it's useful to do a practical consideration
of how you'll deal with data)

Please see:

* :ref:`The DMP section on this site <scicomp_dmp>`
* The `Aalto data management plan
  page <https://www.aalto.fi/en/services/data-management-plan-dmp>`__

Long-term archival
~~~~~~~~~~~~~~~~~~

Long-term archival is important to make sure that you have ability to
access your group's own data in the long term. Aalto resources are not
currently intended for long-term archival. There are other resources
available for this, such as

-  the EU-funded `Zenodo <https://zenodo.org/>`__ for open published
   data (embargoed data and closed data is also somewhat supported).
-  Finland's `IDA <https://www.fairdata.fi/en/ida/>`__ (for large data,
   closed or open). There are :doc:`Aalto-specific instructions
   for IDA here <../data/ida>`.
-  There is supposed to be an alternate `Finnish digital preservation
   service <https://www.fairdata.fi/en/fairdata-pas/>`__ coming in
   2017, and it's unclear what the intention of IDA is in light of that.

Archival when you leave
~~~~~~~~~~~~~~~~~~~~~~~

Unfortunately, everyone leaves Aalto sometime. Have you considered
what will happen to your data?  Do you want to be remembered? This
section currently is written from the perspective of a researcher, not
a professor-level staff member, but if you are a group leader you need
to make sure your data will stay available! Science-IT (and most of
these resources) are focused on research needs, not archiving a
person's personal research data  (if we archive it for a person who
has left, it's not accessible anyway!  Our philosophy is that it
should be part of a group as described above.). In general, we can archive data as
part of a professor's group data (managed in the group directories the
normal ways), but not for individuals.

-  Remember that your home directories get removed when your account
   expires (we think in only two weeks!).
-  Data in the group directories it won't be automatically deleted. But
   you should clean up all your junk and leave only what is needed for
   future people. Remember, if you don't take care of it, it becomes
   extremely hard for anyone else to. The owner of the group (professor)
   will be responsible for deciding what to do with the data, so make
   sure to discuss with them and easy for them to do the right thing!
-  Make sure that the data is documented well.  If it's undocemented,
   then it's unusable anyway.
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
   (`PAS <https://www.avointiede.fi/en/digital-preservation>`__), but this is
   probably not intended for own data, only well-curated data. Anyway,
   if you need something
   that long and it isn't confidential, consider opening it.

Summary of data locations
-------------------------

Below is a summary of the core Science-IT data storage locations.


.. list-table::
   :header-rows: 1

   * * Solution
     * Purpose
     * Where available?
     * Backup?
     * Group management?
   * * project
     * Research time storage for data that requires backup. Good for
       e.g. code, articles, other important data.  Generally for a
       small amount of data per project.
     * Workstations, triton login node
     *  Weekly backup to tape (to recover from major failure)
	+ snapshots (recover accidentally deleted files).

	Snapshots go back

	- hourly last 26 working hours (8-20)
	- daily last 14 days
	  - weekly last 10 weeks
     * yes
   * * Archive
     * Data which a longer life that project.  Practically the same,
       but better to sort things out early.  Also longer snapshot and
       guaranteed to get backed up to tape.
     * Workstations, Triton login node.  /m/$dept/project/$group.
     * Same as above
     * yes
   * * Scratch (group based)/work (per-user)
     * Large research data that doesn't need backup.  Temporary
       working storage.  Very fast access on Triton.
     * /m/$dept/$scratch/$groupname, /m/$dept/work/$username.
     * no
     * scratch: yes, work: no


See :doc:`data storage <../aalto/aaltostorage>` for full info.

.. _instructions:

Instructions for storage and access
-----------------------------------

.. note::

   This applies to the Science-IT departments.  If you want to apply
   for storage space from Aalto-IT, you can use these instructions as
   a model, but their processes are not yet fully developed.

   You and users must accept the :doc:`data policy <datapolicy>`
   (summary above).


Existing data groups and responsible contacts:

* CS: `Existing groups <https://wiki.aalto.fi/display/CSdept/Data+groups>`__
  and `CS-IT (guru) email here <http://do.cs.aalto.fi>`__
* NBE: `Existing groups <https://wiki.aalto.fi/display/NBE/Data+groups>`__ and
  `NBE IT (it-nbe) email here <https://wiki.aalto.fi/display/NBE/IT+Information>`__
* PHYS:
* Aalto: Aalto IT servicedesk


Requesting to be added to a group
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note::

   **CS department**: New!  Group owners/managers can add members to
   their groups self-service.  Go to https://domesti.cs.aalto.fi from
   Aalto networks, over VPN, or remote desktop at
   https://vdi.aalto.fi, and it should be obvious.

Send an email to the responsible contact (see above) and **CC the
group owner or responsible person**, and include this information:

-  Group name that you request to join
-  copy and paste this statement, or something similar: "I am aware that
   all data stored here is managed by the group's owner and have read
   the data management policies."
-  Ask the group owner to reply with confirmation.
-  Do you need access to scratch or work? If so, you need a Triton
   account and you can request it now. If you don't, you'll get
   "input/output error" and be *very* confused.
-  Example:

     Hi, I (account=omes1) would like to join the group ``myprof``.  I
     am aware that all data stored here is managed by the group's
     owner and have read the data management policies.
     ``$professor_name``, please reply confirming my addition.

Requesting a new group
~~~~~~~~~~~~~~~~~~~~~~

Send an email to the responsible contact (see above) with the following information. Group
owners should be long-term (e.g. professor level) staff.

-  Requested group name (you can check the name from the lists below)
-  Owner of data (prof or long-term staff member)
-  Other responsible people who can authorized adding new members to the
   group. (they can reply and say "yes" when someone asks to join the
   group.)
-  Who is responsible for data should you become unavailable (default:
   supervisor who is probably head of department).
-  Initial members
-  Expiration time (default=max 2 years, extendable. max 5 years
   archive). We will ping you for management/renewal then.
-  Which filesystems and what quota. (project, archive, scratch). See
   the :doc:`the storage page <../aalto/aaltostorage>`.
-  Basic description of purpose of group.
-  Is there any confidential or personal data (see above for disclaimer).
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

