============
Data storage
============

This page outlines the storage options available for your data. There
are many options available, some provided by CSIT, some provided by
Aalto IT Services, and some provided by Science IT. For clarity, this
page describes them all, so that you can have an easy reference.

When starting a new project, please first consider the big picture of
good Research Data Management: See the :doc:`general data management
pages here <../data/index>` and `Aalto's
page <https://www.aalto.fi/en/services/research-data-management-rdm-and-open-science>`__. On
Aalto's page, there are links to solutions for Opening, Collaborating
and Archiving. Our department's resources are just one part of that.

This page is currently a bit Linux-centric, because Linux is best
supported.

**Other operating systems:** Windows and OSX workstations do not
currently have any of these paths mounted. In the future, project and
archive may be automatically mounted. You can always remote mount via
sshfs or SMB. See the :doc:`remote access <../aalto/remoteaccess>` page for
Linux, Mac, and Windows instructions for home,project, and archive. In
OSX, there is a shortcut in the launcher for mounting home. In Windows
workstations, this is Z drive.  On your own computers, you may need to
use ``AALTO\username`` as your username for any of the SMB mounts.

**Laptops:** Laptops have their own filesystems, including home
directories. These are not backed up automatically. Other directories
can be mounted as described on the :doc:`remote
access <../aalto/remoteaccess>` page.

Summary table
~~~~~~~~~~~~~

This table lists all available options in Science-IT departments, including those not managed by
departments. In general, **project** is for most research data that requires
good backups. For big data, use **scratch**. Request **separate
projects** when needed to keep things organized.INLINE

+--------------+--------------+--------------+--------------+--------------+--------------+
| Filesystem   | Path (Linux) | Triton?      | Quota        | Backups?     | Notes        |
+==============+==============+==============+==============+==============+==============+
| home         | /u/.../$user | no           | 40 GiB       | yes,         | Used for     |
|              | name/unix    |              |              | $HOME/../.sn | personal and |
|              |              |              |              | apshot/      | non-research |
|              |              |              |              |              | files        |
+--------------+--------------+--------------+--------------+--------------+--------------+
| project      | /m/$dept/proj| some         | per-project, | Yes,         |              |
|              | ect/$project/|              | up to 100s   | hourly/daily |              |
|              |              |              | of GiB       | /weekly.     |              |
|              |              |              |              | (.snapshot)  |              |
+--------------+--------------+--------------+--------------+--------------+--------------+
| archive      | /m/$dept/arch| some         | per-project, | Yes,         |              |
|              | ive/         |              | up to 100s   | hourly/daily |              |
|              | $project/    |              | of GiB       | weekly.      |              |
|              |              |              |              | + off-site   |              |
|              |              |              |              | tape         |              |
|              |              |              |              | backups.     |              |
|              |              |              |              | (.snapshot)  |              |
+--------------+--------------+--------------+--------------+--------------+--------------+
| scratch      | /m/$dept/scr | yes          | per-project, | RAID6, but   | Don't even   |
|              | atch/$pro    |              | 2 PiB        | no backups.  | think about  |
|              | hect/        |              | available    |              | leaving      |
|              |              |              |              |              | irreplaceabl |
|              |              |              |              |              | e            |
|              |              |              |              |              | files here!  |
|              |              |              |              |              | Need Triton  |
|              |              |              |              |              | account.     |
+--------------+--------------+--------------+--------------+--------------+--------------+
| work         | /m/$dept/wor | yes          | 200GB        | RAID6, but   | same as      |
|              | k/$username/ |              | default      | no backups.  | scratch.     |
|              |              |              |              |              | Need Triton  |
|              |              |              |              |              | account.     |
+--------------+--------------+--------------+--------------+--------------+--------------+
| local        | /l/$username | yes          | usually a    | No, and      | Directory    |
|              | /            |              | few 100s GiB | destroyed if | needs to be  |
|              |              |              | available    | computer     | created and  |
|              |              |              |              | reinstalled. | permissions  |
|              |              |              |              |              | should be    |
|              |              |              |              |              | made         |
|              |              |              |              |              | reasonable   |
|              |              |              |              |              | (quite       |
|              |              |              |              |              | likely       |
|              |              |              |              |              | 'chmod 700   |
|              |              |              |              |              | /l/$USER',   |
|              |              |              |              |              | by default   |
|              |              |              |              |              | has read     |
|              |              |              |              |              | access for   |
|              |              |              |              |              | everyone!)   |
|              |              |              |              |              |              |
|              |              |              |              |              | Space usage: |
|              |              |              |              |              | \`du -sh     |
|              |              |              |              |              | /l/\`. Not   |
|              |              |              |              |              | shared among |
|              |              |              |              |              | computers.   |
+--------------+--------------+--------------+--------------+--------------+--------------+
| tmpfs        | /run/user/$u | yes          | local memory | No           | Not shared.  |
|              | id/          |              |              |              |              |
+--------------+--------------+--------------+--------------+--------------+--------------+
| webhome      | $HOME/public | no           | 1 GiB        |              | `https://use |
|              | \_html/      |              |              |              | rs.aalto.fi/ |
|              |              |              |              |              | ~USER/ <http |
|              | (/m/webhome/ |              |              |              | s://users.aa |
|              | ...)         |              |              |              | lto.fi/~USER |
|              |              |              |              |              | />`__        |
+--------------+--------------+--------------+--------------+--------------+--------------+
| custom       |              |              |              |              | Contact us   |
| solutions    |              |              |              |              | for special  |
|              |              |              |              |              | needs, like  |
|              |              |              |              |              | sensitive    |
|              |              |              |              |              | data, etc.   |
+--------------+--------------+--------------+--------------+--------------+--------------+

General notes
~~~~~~~~~~~~~

-  The table below details the types of filesystems available.
-  The path /**m/$dept/** is designed to be a standard location for mounts.
   In particular, this is shared with Triton.
-  The server ``magi`` is ``magi.cs.aalto.fi`` and is for the CS
   department. Home directory is mounted here without kerberos
   protection but directories under /m/ need active kerberos ticket
   (that can be acquired with 'kinit' command) . ``taltta`` is
   ``taltta.aalto.fi`` and is for all Aalto staff. Both use normal
   Aalto credentials.
-  **Common problem:** The Triton ``scratch``/``work`` directories are
   automounted. If you don't see it, enter the *full name* then tab
   complete and it will appear. It will appear after you try accessing
   with the *full name*.
-  **Common problem:** These filesystems are protected with Kerberos,
   which means that you must be authenticated with *Kerberos tickets* to
   access them. This normally happens automatically, but they expire
   after some time. If you are using systems remotely (the shell
   servers) or have stuff running in the background, this may become a
   problem. To solve, run ``kinit`` and it will refresh your tickets..

Filesystem list
~~~~~~~~~~~~~~~

-  **home:** your home directory

   -  Shared with the Aalto environment, for example regular Aalto
      workstations, Aalto shell servers, etc.
   -  Should not be used for research work, personal files only. Files
      are lost once you leave the university.

      -  Instead, use project for research files, so they are accessible
         to others after you leave.

   -  Quota 20 GiB.
   -  Backups recoverable by ``$HOME/../.snapshot/`` (on linux
      workstations at least).
   -  SMB mounting: ``smb://home.org.aalto.fi/``

-  **project:** main place for shared, backed-up project files

   -  ``/m/$dept/project/$project/``
   -  Research time storage for data that requires backup. Good for e.g.
      code, articles, other important data. Generally for small amount
      (10s-100s GiB) of data per project.
   -  This is the normal place for day to day working files which need
      backing up.
   -  Multi user, per-group.
   -  Quotas: from 10s to 100s of GiB
   -  Quotas are not designed to hold extremely large research data
      (TiBs). Ideal case would be 10s of GiB, and then bulk intermediate
      files on scratch.
   -  Weekly backup to tape (to recover from major failure) + snapshots
      (recover accidentally deleted files). Snapshots go back:

      -  hourly last 26 working hours (8-20)
      -  daily last 14 days
      -  weekly last 10 weeks
      -  Can be recovered using ``.snapshot/`` within project
         directories

   -  Accessible on ``magi``/``taltta`` at the same path.
   -  SMB mounting: ``smb://tw-cs.org.aalto.fi/project/$group/``

-  **archive:**

   -  ``/m/$dept/archive/$project/``
   -  For data that should be kept accessible for 1-5 years after the
      project has ended. Alternatively a good place to store a copy of a
      large original data (backup).
   -  This is practically the same as project, but retains snapshots
      for longer so that data is ensured to be written to tape
      backups.
   -  This is a disk system, so does have reasonable performance.
      (Actually, same system as project, but separation makes for easier
      management).
   -  Quotas: 10s to 1000s of GiB
   -  Backups: same as project.
   -  Accessible on ``magi``/``taltta`` at the same path.
   -  SMB mounting: ``smb://tw-cs.org.aalto.fi/archive/$group/``

-  **scratch:** large file storage and work, not backed up (Triton).

   -  ``/m/$dept/scratch/$group/``
   -  Research time storage for data that does not require backup. Good
      for temporary files and large data sets where the backup of
      original copy is somewhere else (e.g. archive).
   -  This is for massive, high performance file storage. Large reads
      are extremely fast (1+ GB/s).
   -  This is a lustre file system **as part of triton** (which is in
      Keilaniemi).
   -  Quotas: 10s to 100s of TiB. The university has 2 PB available
      total.
   -  In order to use this, **you must have a triton account**. If you
      don't, you get "input/output error" which is extremely confusing.
   -  On workstations, this is **mounted via NFS** (and accessing it
      transfers data from Keilaniemi on each access), so it is **not**
      fast on workstations, just large file storage. For high
      performance operations, work on triton and use the workstation
      mount for convenience when visualizing.
   -  This is RAID6, so is pretty well protected against single disk
      failures, but not backed up at all. It is possible that all data
      could be lost. **Don't even think about leaving irreplaceable
      files here.** CSC actually had a problem in 2016 that resulted in
      data loss. It is extremely rare (decades) thing, but it can
      happen. (still, it's better than your laptop or a drive on your
      desk. Human error is the greatest risk here).
   -  Accessible on ``magi``/``taltta`` at the same path.
   -  SMB mounting:
      ``smb://data.triton.aalto.fi/scratch/$dept/$dir/``.  (Username
      may need to be ``AALTO\yourusername``.)

-  **Triton work:** personal large file storage and work (Triton)

   -  ``/m/$dept/work/$username/``
   -  This is the equivalent of scratch, but per-person. Data is lost
      once you leave.
   -  Accessible on ``magi``/``taltta`` at the same path.
   - SMB mounting: ``smb://data.triton.aalto.fi/work/$username``.
     (Username may need to be ``AALTO\yourusername``.)

-  **local:** local disks for high performance

   -  You can use local disks for day to day work. These are not
      redundant or backed up at all. Also, if your computer is
      reinstalled, all data is lost.
   -  Performance is much higher than any of the other network
      filesystems, especially for small reads. Scratch+Triton is still
      faster for large reads.
   -  If you use this, make sure you set UNIX permissions to restrict
      the data properly. Ask if you are not sure.
   -  If you store sensitive data here, you are responsible for physical
      security of your machine (as in no one taking a hard drive). Unix
      permissions should protect most other cases.
   -  When you are done with the computer, you are also responsible for
      secure management/wiping/cleanup of this data.
   -  See the note about disk wiping under :doc:`Aalto
      Linux <../aalto/linux>` (under "when you are done with your
      computer"). IT should do this, but if it's important you must
      mention it, too.

-  **tmpfs**: in-memory filesystem

   -  This is a filesystem that stores all data in memory. It is
      extremely high performance, but extremely temporary (lost on each
      reboot). Also shares RAM with your processes, so don't use too
      much and clean up when done.
   -  TODO: are these available everywhere?

-  **webhome:** web space for `users.aalto.fi <https://users.aalto.fi>`__

   -  This is the space for `users.aalto.fi <https://users.aalto.fi>`__
      space can be accessed from the ``public_html`` link in your home
      directory.
   -  This is not a real research filesystem, but convenient to note
      here.
   -  Quota (2015) is 1 GiB. (``/m/webhome/webhome/``)
   -  `https://users.aalto.fi/~USER/ <https://users.aalto.fi/~USER/>`__

-  **triton home**: triton's home directories

   -  Not part of departments, but documented here for convenience
   -  The home directory on Triton.
   -  Backed up daily.
   -  Not available on workstations.
   -  Quota: 1 GB

* **Aalto work**: Aalto's general storage space

  - Not often used within Science-IT departments: we use project and
    archive above, which are managed by us and practically
    equivalent.  You could request space from here, but expect less
    personalized service.
  - Aalto home directories are actually here now.
  - You may request storage space from here, email the Aalto
    servicedesk and request space on work.  The procedures are not
    very well established.
  - Data is snapshotted and backed up offsite for disaster recovery.
  - Search https://it.aalto.fi for "work.org.aalto.fi" for the latest
    instructions.
  - SMB mounting via ``smb://work.org.aalto.fi``

* **Aalto teamwork**: Aalto's general storage space

  - Not used directly within Science-IT departments: we have our own
    direct interfaces to this, and ``project`` and ``archive``
    directories are atually here.
  - For information on getting teamwork space (outside of Science-IT
    departments), contact servicedesk.
  - Teamwork is unique in that it is arbitrarily extensible, and you
    may buy the space from the vendor directly.  Thus, you can use
    external grant money to buy storage space here.
  - SMB mounting via ``smb://teamwork.org.aalto.fi``

Quota errors
~~~~~~~~~~~~

**Use the ``quota`` command to see your quota**. If you have scratch or
work mounted, the quota command will hang and produce errors. For now,
check your scratch/work quotas on Triton.

The scratch and work directories do quotas by unix group, and **there is
a strange error about quota exceeded** that you may get sometimes when
the unix group of the file or directory is wrong. See the full
information at :doc:`Quotas <../triton/usage/quotas>` and summary below. You
may have to fix this on Triton if the things below don't work.

-  Symptoms: "Quota exceeded" when you are trying to make a new file in
   scratch or work directory.
-  Root cause: quotas are by groups, and if a directory is not
   setgroupid (chmod g+s), then files being created will have a
   different group (with no quota for that location), thus quota
   exceeded by default. This often happens when you copy a directory
   from one place to another, and then *later* try to make new files in
   that directory.
-  Solution: ``chmod g+s $directory`` or
   ``find $directory -type d -exec chmod g+s {} \;`` (you don't
   want to make regular files g+s mode).


