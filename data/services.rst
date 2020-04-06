===============================
Data storage services available
===============================

This page provides a list of common data storage services, and can
help you select the right service for the type of data you have (see
:doc:`organization`).  But before we talk about services, you have to
consider what your needs are.


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

Service index
=============

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
             | Aalto work| O         | O         | OO        | OO        |           | O
             | Aalto teamwork| O     | O         | OO        | OO        |           | O
             | Aalto laptops |       |           | x         | x         | X         |
             | Aalto webspace|       |           |           |           |           | OO
             | version.aalto.fi|     |           | OO        | OO        | O         | OO
             | ACRIS           |     |           | O         | O         |           |
             | Eduuni          |     |           |           |           |           |
             | Aalto Wiki      |     |           |           |           |           |
   Finland   | Funet filesender|     |           | O         |           |           | OO
             | CSC cPouta| O         | O         |           |           |           | O
             | CSC Ida   | OOO       | x         |           | OO        | O         | O
             | FSD       |           |           | OO        | O         | OO        | O
   Public    | github    |           |           | x         |           |           | OO
             | Zenodo    |           |           |           |           | OO        | OO
             | Google drive|         |           | x         |           |           | O
             | OneDrive    |         |           |           |           |           |
             | Own computers|        |           | x         | x         | x         |
             | Emails    |           |           | x         | x         | x         |
             | EUDAT B2SHARE |       |           |           | O         | O         | O

Service details
===============

.. note::

   This list is still under development (2018-03-07)

In general, if you need to

* **archive and open**, consider hosting data on Zenodo (and put a
  record of it in ACRIS, so you can get internal Aalto credit.  If you
  have a discipline-specific repository, use that instead (with
  metadata still in ACRIS)
* For **day to day work** within Aalto, Aalto network drives are a
  good service and (different options below).
* For **making a data management plan**, DMPTuuli along with :doc:`our
  info <plans>` is good.



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

* See the **work** and **teamwork** notes below in the next section.
  In some cases, these are managed by departments.

Aalto
~~~~~
* See :doc:`../aalto/aaltostorage`.

* Also information is available from Aalto ITS, some `here
  <https://www.aalto.fi/en/services/it-services-for-research>`_.

* **Aalto home directories** are small and intended mainly for personal
  stuff.  Once you leave, this data dies, so don't put important
  stuff here.

* Aalto has **work** and **teamwork** storage systems.  These are
  actually provided at the Aalto level, but how you request space, how
  you use them, and what the are called varies and is not always very
  well defined.  A little bit of info at
  :doc:`../aalto/aaltostorage`.

* **Aalto laptops** are not a good place to store data because they are
  usually not backed up, and data is not shareable.  (Even if data is
  backed up, once you leave, no one will even be able to get access).
  Most people who use laptops have the most valuable data stored on
  network drives.

* **Aalto webspace** can share data.  See
  :doc:`../aalto/aaltostorage`.  This isn't suitable for archival or
  long-term anything, since it is tied to user accounts.  If you
  want to share here, maybe you could do a bit more work and
  handle it forever at Zenodo?

* https://version.aalto.fi is the Aalto Gitlab.  It is used for small
  version controlled files.  It is a great place for day to day work
  of private files, but not for permanent archival.  See
  :doc:`../aalto/git`.

* **ACRIS** is the Aalto "research information system", meaning it's a
  record of things that everyone is doing research-wise.  You should
  make records for datasets there as a research output.
  (`ACRIS + research data instructions
  <https://wiki.aalto.fi/display/ACRIShelp/ACRIS+and+research+data>`__)

  Summary: try to host the actual data elsewhere, but always make a
  report of the data in ACRIS so you get credit.

  ACRIS has support for storing data itself, but that isn't
  recommended most of the time since ACRIS in it's current form isn't
  guaranteed to stay around forever.  However, if data needs to be
  kept internal, it might be OK since you can set confidentiality and
  share with certain people.  However, you *should* always make a
  report of your datasets in ACRIS even if they are hosted elsewhere,
  so that you can get academic credit for it.

  What data sets should be included in ACRIS?  We think: a) anything that
  is independently published with DOI. b) any paper which serves as a
  formal dataset description in a data journal, even if there is also
  an entry as an ACRIS article.  c) any paper which serves as an
  informal dataset description.

  As for different roles: creator=who is involved in creating it,
  distributor=who can be contacted about access (if not public),
  owner=who has ultimate responsibility (often the PI but project
  dependent).

* **Eduuni** is a Finnish service for educational collaboration.  It's
  reported to be more secure than either Google Drive or OneDrive, but
  we know of few people who use it.

* The **Aalto Wiki** is sometimes mentioned as a place to store data.
  It's really better for collaboration, but you can put little bits of
  data there if you want.

Finnish services
~~~~~~~~~~~~~~~~
* The **FUNET filesender** (https://filesender.funet.fi) can share
  files with others.  You log in with your Aalto account, and then you
  can upload files and send a link by email.  Or, you can send an
  email that allows others to upload.  Run by CSC and recommended for
  sharing (instead of email).

* **IDA**, **Etsin**, and **AVAA** are CSC-provided services (funded
  by the ministry as part of the Open Science project, ATT), which
  provide some data services to researchers.

  * **Etsin** is the Finnish metadata catalog.  The intention is that
    all research data eventually gets cataloged here (open or not),
    but we are quite far from that goal.  Ideally, there would be
    bidirectional imports to and from ACRIS (the Aalto system) and
    other repositories, but it's not there yet.  We should recommend
    that you make a note of your data here, but realistically do ACRIS
    and wait for a link.

  * **IDA** is a storage service. (`instructions
    <https://openscience.fi/ida>`__) It is based on iRODS, a data
    management layer on top of filesystems.  Thus, you have to access
    it using a special API, command line interfaces, or other tools.
    Because of this, the learning curve is very steep.  Currently, we
    think IDA would be good if your university doesn't provide large
    enough free, properly backed up storage that is shareable within
    Finland.  For long-term public storage, Zenodo is probably overall
    easier to use.  We have some practical notes on using it
    :doc:`here <ida>`, because it takes quite a few steps to get started.

    It is said to be a safe place to store your data, but if you read
    closely a different "long-term preservation" service `is coming
    <https://www.fairdata.fi/en/fairdata-pas/>`__, so IDA isn't that.  IDA
    might have a use case for confidential data which can't leave
    Finland, but it says `it claims it is not suitable for such
    <https://www.fairdata.fi/en/ida/>`__.  They also say that metadata
    "`shall
    <https://sui.csc.fi/web/guest/terms-of-use/-/asset_publisher/FMMBc3VntxT0/content/id/465885>`__"
    be added, which makes you think it is only for data which is
    prepared enough for putting in Etsin.

    If you are dealing with a large amount of data and want to use an
    API to handle it, this could be good.

    IDA is being `renewed <https://openscience.fi/ida-renewal>`__ in
    2018, and will need reevaluation then.

  * **AVAA** is basically a merging of IDA and Etsin.  You can set
    some metadata in IDA so that your data is available via the web.
    There are some instruction in the IDA user guide (`browser
    <https://www.fairdata.fi/en/ida/user-guide/>`__, `command line
    <https://www.fairdata.fi/en/ida/user-guide/>`__).  Overall,
    having to use three different services for publishing a file takes
    a fair amount of work, so if you want to open data, Zenodo is
    faster.

* **The FSD Finnish Social Data Archive / Tietoarkisto** is run from
  the University of Tampere.  It is a full-service archive for social
  data, so they can help in data preparation and curation..  It is one
  of the few places in Finland allowed to archive personally
  identifiable data.

* **DMPTuuli** (`dmptuuli.fi <https://dmptuuli.fi>`__) is a service
  for making data management plans.  It is primarily targeted at
  funder DMPs, so it won't help you plan your actual research (and
  even for funder DMPs, you need to know what to say).  You can check
  our :doc:`data management plans <plans>` page, including the
  "emergency DMP" section.  Aalto also has a `little bit of guidance
  <https://www.aalto.fi/en/services/data-management-plan-dmp>`__.

EU services
~~~~~~~~~~~

* **Zenodo** (https://zenodo.org) is a long-term data repository.  It
  is the largest (thus the most stable long-term) and also has a great
  user interface.  You get a DOI if you archive here.  We recommend
  this service unless you have another
  domain-specific repository that fits your data better.  If you
  publish data here, also make a metadata entry in ACRIS (see above).

  Zenodo is a good service, but there is little curation, so you need
  to make sure that your data is described well (both in the
  structured catalog information and within the data, so that it is
  usable).

  When you put data in Zenodo, also make an ACRIS dataset entry linked
  with the DOI.

* **EUDAT** (https://eudat.eu) provides a lot of different services:
  B2share is a lot like Zenodo, but smaller and last we checked the
  user interface wasn't as good (and it didn't provide DOIs).  B2Drop
  is a Dropbox-like file sharing service (powered by nextcloud), which
  can be quite nice.  B2Find is a metadata catalog that lets you
  search for data.  The other services are mostly target to other
  large infrastructures.  (EUDAT will be re-evaluated in 2018)

Global services (with special Aalto support)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **Google Drive** is a cloud storage solution (but you probably
  already knew that...).  You can register your Aalto account as a
  Google account, which gives you unlimited storage (note that this
  does not mean your personal account gets unlimited... a Gsuite
  account does.  This account ends when you leave Aalto, so this
  should not be used for permanent storage).  You have to enable your
  account using `ITS instructions here
  <https://www.aalto.fi/en/services/google-drive-registration-and-closing-of-an-account>`__.
  Access the Aalto Google Drive from https://gdrive.aalto.fi.  This
  service can be great for sharing, but because it is tied to your
  Aalto account, you should not store valuable research data here.

  Google Drive (organizations only) has a "shared drive" concept, which will allow you to
  put data into groups which can easily be inherited as time goes on,
  even if the original people move on.

* **Microsoft OneDrive** is like Google Drive, and Aalto has a special
  agreement.  You can find
  `instructions from ITS here
  <https://www.aalto.fi/en/services/onedrive-quick-guide>`__.
  Theoretically, OneDrive has a higher security rating than Google
  Drive, but it is still not suitable for legally confidential data.

* **Dropbox** is like the above two.  You can find `ITS instructions
  here
  <https://www.aalto.fi/en/services/aalto-dropbox-quick-guide>`_.  You
  can sign up using a detailed procedure there.  Again, this isn't
  suitable for confidential/personal data, and everything vanishes
  once you leave Aalto.

Global services
~~~~~~~~~~~~~~~

* **Github** is a code-sharing and collaboration service (using git,
  obviously).  If you have an open source project, this is a
  well-known place to put it.  The only downside is if you have
  objections to proprietary services.  Github should not be used as a
  permanent archive, but there is Zenodo integration so that your code
  can be archived permanently (and even has integration with the
  Github "release" feature).

This is by no means a complete list...
