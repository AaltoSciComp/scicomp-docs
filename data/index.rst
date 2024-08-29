Data
====

Data connects most research together.  It's easy to make in short
term, but in the long term it can become so chaotic it loses its
value.  Can you access your research group's data from 5 years ago and
use it?

Summary for Triton data
-----------------------

If you use Triton or go beyond your own device/simple cloud services,
you have the following basic options:

.. list-table::
   :header-rows: 1

   * *
     * Shared
     * Size / backups
     * When you leave
     * Usage
   * * Triton Work
     * no
     * 100s GB+

       no

     * deleted
     * Small projects, testing work, or getting started.  Switch to a
       Triton project directory when a project becomes large.

       ``/scratch/work/USER``
   * * Triton project
     * yes
     * No limit

       no
     * stays
     * The most recommended place for large data.  Make sure you back
       up irreplaceable data (see below).

       ``/scratch/DEPT/PROJECT/``
       Needs to be requested as described :doc:`here </data/requesting/>`

   * * (Aalto/Dept) Project directory
     * yes
     * GBs-TBs

       yes
     * stays
     * Recommend to have a copy here for original or irreplaceable
       data.  Only available on login nodes, so you need a Scratch/Work
       directory also to copy

       ``/m/DEPT/PROJECT/``


You *really should* talk to your group leader about data storage
locations - data is important and your group leader needs to be aware
of where all the group's data is stored so they can coordinate all the
use.


Data storage in Aalto
---------------------

* Quick summary: `What file storage to use? <https://www.aalto.fi/en/services/what-file-storage-to-use-when>`__
* `Teamwork storage space <https://www.aalto.fi/en/services/file-storage-space-for-research-and-groups-teamwork>`__ (Aalto project directories)
* `Storage services for research data <https://www.aalto.fi/en/services/storage-services-for-research-data>`__
* `Summary of storage locations <https://www.aalto.fi/en/services/data-storage-file-services>`__
* `Guidelines for classification of confidential information <https://www.aalto.fi/en/information-processing/classification-of-information>`__,


Data in Science-IT departments
------------------------------

(CS, NBE, PHYS).

Getting space:

.. toctree::
   :maxdepth: 1

   requesting
   principles

More details:

.. toctree::
   :maxdepth: 1


   aalto-details
   confidential-data
   archival
   leaving-aalto
   organization
   science-it-data-policy



Data on Triton
--------------

:doc:`Triton </triton/index>` is a computer cluster that provides
large and fast data storage connected to significant computing power,
but it is not backed up.

* Tutorial: :doc:`/triton/tut/storage`
* Tutorial: :doc:`/triton/tut/remotedata`
* Triton quick reference: :ref:`ref-storage` and :ref:`ref-remote-data`
* Overview with checklist: :doc:`/triton/usage/storage`
* :doc:`/triton/usage/localstorage`
* :doc:`/triton/usage/lustre`
* :doc:`/triton/usage/quotas`
* :doc:`/triton/usage/smallfiles`



Data management
---------------

This section covers administrative and organizational matters about data.

* `Aalto Research Data Management pages
  <https://www.aalto.fi/en/services/research-data-management-rdm-and-open-science>`__,
  and here we focus on the practical side of things.



Other
-----

* :doc:`/scicomp/git-annex`



Summary table
--------------

This is a broad summary of many of the locations mentioned above.

O = good, x  = bad


Requirements table
~~~~~~~~~~~~~~~~~~

Different data has different needs.

.. csv-table::
   :delim: |
   :header-rows: 1
   :stub-columns: 1

                              | Large        | Fast         | Confidential | Frequent backups | Long-term archival  | Shareable
     Code                     |              |              |              | OO               | OO                  | O
     Original data            | O            | O            | OO?          | OO               | OO                  | O
     Intermediate files       | OO           | OO           | OO?          |                  |                     | 
     Final results/open data  |              |              |              |                  | OO                  | OO


Storage location table
~~~~~~~~~~~~~~~~~~~~~~

.. csv-table::
   :delim: |
   :header-rows: 1
   :stub-columns: 2

             |                   | Large     | Fast      | Confidential | Backups   |Long-term archival  | Shareable
   Triton    | :doc:`Triton project </triton/usage/lustre>`    | OO        | OO*       | O            | x         | x                  | O
             | :doc:`work </triton/usage/lustre>`              | OO        | OO*       | O            | x         | x                  |
             | :doc:`Triton home </triton/usage/lustre>`       | x         |           | O            | OO        |                    |
             | :doc:`Local disks </triton/usage/localstorage>` | O         | OO        | O            |           |                    |
             | :ref:`ramfs <ramfs-description>`                |           | OOO       | OO           |           |                    |
   Depts     | /m/.../project    | O         | O         | OO           | OO        |                    | O
             | /m/.../archive    | O         | O         | OO           | OO        | O                  | O
   Aalto     | Aalto home        |           |           | OO           | OO        |                    |
             | Aalto work        | O         | O         | OO           | OO        |                    | O
             | Aalto teamwork    | O         | O         | OO           | OO        |                    | O
             | Aalto laptops     |           |           | x            | x         | X                  |
             | Aalto webspace    |           |           |              |           |                    | OO
             | version.aalto.fi  |           |           | OO           | OO        | O                  | OO
             | ACRIS             |           |           | O            | O         |                    |
             | Eduuni            |           |           |              |           |                    |
             | Aalto Wiki        |           |           |              |           |                    |
   Finland   | Funet filesender  |           |           | O            |           |                    | OO
             | CSC cPouta        | O         | O         |              |           |                    | O
             | CSC Ida           | OOO       | x         |              | OO        | O                  | O
             | FSD               |           |           | OO           | O         | OO                 | O
   Public    | github            |           |           | x            |           |                    | OO
             | Zenodo            |           |           |              |           | OO                 | OO
             | Google drive      |           |           | x            |           |                    | O
             | OneDrive          |           |           |              |           |                    |
             | Own computers     |           |           | x            | x         | x                  |
             | Emails            |           |           | x            | x         | x                  |
             | EUDAT B2SHARE     |           |           |              | O         | O                  | O

(*) For details check out the description of :doc:`the lustre file system </triton/usage/lustre>` and the issue of :doc:`small Files</triton/usage/smallfiles>` on Triton.

