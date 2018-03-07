===============================
Data storage services available
===============================

This page provides a list of common data storage services, and can
help you select the right service for the type of data you have (see
:doc:`organization`).


Types of data
=============

There are different broad categories of data:

-  **Code/papers** **drafts/**: These are absolutely critical, but quite
   small. You want a full history that is easy to use, too. Put in
   version control and in Aalto gitlab.
-  **Original data:** Your original, irreplaceable data. You want this
   in two places: a fast, large, available place for day-to-day work,
   and also somewhere backed up for a fairly long time.
-  **Intermediate working files:** This is what you get when you run
   code on original data. It's OK if this is lost, because you have the
   code and original data to re-create it, right? It can go in the
   large, fast location.
-  **Final published results/data:** You want this backed up and
   available for a very long time (forever?). Put in an open-access
   repository such as Zenodo.  Once it's in the archival, backups
   should be done there.

O = good, x  = bad

.. csv-table::
   :delim: |
   :header-rows: 1
   :stub-columns: 1

                  | Large        | Fast         | Confidential | Frequent backups| Long-term archival
     Code         |              |              |              | OO           | OO
     Original     | O            | O            | OO?          | OO           | OO
     data         |              |              |              |              |
     Intermediate | OO           | OO           | OO?          |              |
     files        |              |              |              |              |
     Final        |              |              |              |              | OO
     results/open |              |              |              |              |
     data         |              |              |              |              |

Storage services
================

There are different qualities we want in filesystems: large, fast,
confidential, highly available, backed up, mounted everywhere, lasts
forever. It is expensive to have all of these together, so there are
different places with different benefits. It is up to you to balance
their use so that you can accomplish what you need. Compare this table
to the types of data above. Use the right place for the right data.

You often need to use different types of services, for example
version.aalto.fi for day to day code management, but archive to Zenodo
at the end of a project.

O = good, x  = bad

.. csv-table::
   :delim: |
   :header-rows: 1
   :stub-columns: 2

             |           | Large     | Fast      | Confidential | Backups|Long-term archival | Shareable
   Triton    | scratch   | OO        | OO        | O         | x         | x         | O
             | work      | OO        | OO        | O         | x         | x         |
             |Triton home| x         |           | O         | OO        |           |
             |Local disks| O         | OO        | O         |           |           |
             | ramfs     |           | OOO       | OO        |           |           |
   Depts     | /m/.../project| O     | O         | OO        | OO        |           | O
             | /m/.../archive| O     | O         | OO        | OO        | O         | O
   Aalto     | Aalto home|           |           | OO        | OO        |           |
             | Aalto laptops |       |           | x         | x         | X         |
             | Aalto webspace|       |           |           |           |           | OO
             | version.aalto.fi|     |           | OO        | OO        | O         | OO
             | ACRIS           |     |           | O         | O         |           |
             | Eduuni          |     |           |           |           |           |
             | Aalto Wiki      |     |           |           |           |           |
   Finland   | funet filesender|     |           | O         |           |           | OO
             | CSC cPouta| O         | O         |           |           |           | O
             | CSC Ida   | OOO       | x         |           | OO        | O         | O
             | FSD       |           |           | OO        | O         | OO        | O
   Public    | github    |           |           | x         |           |           | OO
             | Zenodo    |           |           |           |           | OO        | OO
             | Google drive|         |           | x         |           |           | O
             | OneDrive    |         |           |           |           |           |
             | Own computers|        |           | x         | x         | x         |
             | Emails    |           |           | x         | x         | x         |
             | EUDAT B2SHARe |       |           |           | O         | O         | O

Information
===========

.. note::

   This list is still under development (2018-03-07)

Science-IT services
~~~~~~~~~~~~~~~~~~~
* The filesystems by :doc:`Triton <../triton/index>`.  Primarily
  scratch and work, which are very large, very fast on Triton, but
  only for scratch data because they are not backed up.

Departments
~~~~~~~~~~~
* **CS,NBE,PHYS** provide storage logically divided into project and
  archive.  These are the counterparts of Triton and are backed up.
  They are actually Aalto "teamwork", but the departments do the
  day-to-day interfacing.  See :doc:`../aalto/aaltostorage`.

Aalto
~~~~~
* See :doc:`../aalto/aaltostorage`.

* Also information is available from Aalto ITS, some `here
  <https://inside.aalto.fi/display/ITServices/IT+Services+for+Research>`_.

* **Aalto home directories** are small and intended mainly for personal
  stuff.  Once you leave, this data dies, so don't put important
  stuff here.

* **Aalto laptops** are not a good place to store data because they are
  usually not backed up, and data is not shareable.  (Even if data is
  backed up, once you leave, no one will even be able to get access).
  Most people who use laptops have the most valuable data stored on
  network drives.

* **Aalto webspace** can share data.  See
  :doc:`../aalto/aaltostorage`.  This isn't suitable for archival or
  long-term anything, since it is tied to user accounts.  If you
  want to share here, maybe you could do a bit more work and
  handle it forever at Zenode?

* https://version.aalto.fi is the Aalto Gitlab.  It is used for small
  version controlled files.  It is a great place for day to day work
  of private files, but not for permanent archival.  See
  :doc:`../aalto/git`.

* **ACRIS** is the Aalto "research information system", meaning it's a
  record of things that everyone is doing research-wise.  You should
  make records for datasets there as a research output.  It has
  support for storing data itself, but that probably isn't recommended
  most of the time since ACRIS in it's current form isn't guaranteed
  to stay around forever.  However, if data needs to be kept internal,
  it might be OK since you can set confidentiality and share with
  certain people.  Still, consider other services which can do similar
  things.  However, you *should* always make a report of your datasets
  in ACRIS anyway, so that you can get academic credit for it.  You
  can some info about it `on ACRIShelp
  <https://wiki.aalto.fi/display/ACRIShelp/ACRIS+and+research+data>`__,
  but we should probably make some better instructions.

* **Eduuni** is a Finnish service for educational collaboration.  It's
  reported to be more secure than either Google Drive or OneDrive, but
  we know of few people who use it.

* The **aalto Wiki** is sometimes mentioned as a place to store data.
  It's really better for collaboration, but you can put little bits of
  data there if you want.

Finnish services
~~~~~~~~~~~~~~~~
* The **FUNET filesender* (https://filesender.funet.fi) can share
  files with others.  You log in with your Aalto account, and then you
  can upload files and send a link by email.  Or, you can send an
  email that allows others to upload.  Run by CSC and recommended for
  sharing (instead of email).

* **IDA**, **Etsin**, and **AVAA** are CSC-provided services (funded
  by the ministry), which provide some data services to researchers.
  We have some practical notes on using it :doc:`here <ida>`.

* **The FSD Finnish Social Data Arhive / Tietoarkisto** is run from
  the University of Tampere.  It is a full-service archive for social
  data, so they can help in data preparation and curation..  It is one of the few places allowed to archive personal data.

EU services
~~~~~~~~~~~

* **Zenodo** (https://zenodo.org) is a long-term data repository.  It
  is the largest (thus the most stable long-term) and also has a great
  user interface.  There is little curation, so make sure that your
  metadata is good.  We recommend this service unless you have another
  domain-specific repository that fits your data better.  If you
  publish data here, also make a metadata entry in ACRIS (see above).

* **EUDAT** (http://eudat.eu)

