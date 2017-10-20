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

O = good, x  = bad

.. csv-table::
   :delim: |
   :header-rows: 1
   :stub-columns: 2

             |           | Large     | Fast      | Confidential | Backups|Long-term archival | Shareable
   Triton    | scratch   | OO        | OO        | O         | ➖         | x         | O
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
   Finland   | funet fileshare|      |           | O         |           |           | OO
             | CSC cPouta| O         | O         |           |           |           | O
             | CSC Ida   | OOO       | x         |           | OO        | O         | O
   Public    | github    |           |           | x         |           |           | OO
             | Zenodo    |           |           |           |           | OO        | OO
             | Google drive|         |           | x         |           |           | O
             | Own computers|        |           | x         | x         | x         |
             | Emails    |           |           | x         | x         | x         |

Information
===========

* Triton

  * The filesystems by :doc:`Triton <../triton/index>`.  Primarily
    scratch and work, which are very large, very fast on Triton, but
    only for scratch data.

* Departments

  * CS,NBE,PHYS provide storage logically divided into project and
    archive.  These are the counterparts of Triton and are backed up.

* Aalto

  * Information available from Aalto ITS, some `here
    <https://inside.aalto.fi/display/ITServices/IT+Services+for+Research>`_.

* 
