Science-IT department data principles
=====================================

.. note::

   Need a place to store your data?  This is the place to look.
   First, we expect you to read and understand this information, at
   least in general. Then, see :doc:`requesting`.

This page is about how to handle data - not the raw storage part, which
you can find at :doc:`data storage <aalto-details>`.  Aalto has high-level
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
<science-it-data-policy>`.

Information on all physical locations how to use them is on the :doc:`storage
page <aalto-details>`.

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
   the necessary information (see bottom of page).
-  Each group has an owner, quota on filesystems, and some other
   metadata (see below).
-  Group membership is per-account, not tied to employment contracts
   or HR group membership.
   If you want someone to lose access to a group you manage, they have
   to be explicitly removed by the same method they were added (asking
   someone or self-service, see bottom of page).
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


See :doc:`data storage <aalto-details>` for full info.

.. _instructions:

Requesting data storage space
-----------------------------


See :doc:`requesting`.
