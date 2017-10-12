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

O = best, o = acceptable, x = bad, X = very bad

.. csv-table::
   :delim: |
   :header-rows: 1
   :stub-columns: 1

                  | Large        | Fast         | Confidential | Frequent backups| Long-term archival
     Code         |              |              |              | ++           | ++
     Original     | +            | +            | ++?          | ++           | ++
     data         |              |              |              |              |
     Intermediate | ++           | ++           | ++?          |              |
     files        |              |              |              |              |
     Final        |              |              |              |              | ++
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

O = best, o = acceptable, x = bad, X = very bad

.. csv-table::
   :delim: |
   :header-rows: 1
   :stub-columns: 2

             |           | Large     | Fast      | Confidential | Backups|Long-term archival | Shareable
   Triton    | scratch   | ++        | ++        | +         | -         | -         | +
             | work      | ++        | ++        | +         | -         | -         |
             |Triton home| -         |           | +         | ++        |           |
             |Local disks| +         | ++        | +         |           |           |
             | ramfs     |           | +++       | ++        |           |           |
   Depts     | /m/.../project| +     | +         | ++        | ++        |           | +
             | /m/.../archive| +     | +         | ++        | ++        | +         | +
   Aalto     | Aalto home|           |           | ++        | ++        |           |
             | Aalto laptops |       |           | -         | -         | X         |
             | Aalto webspace|       |           |           |           |           | ++
             | version.aalto.fi|     |           | ++        | ++        | +         | ++
   Finland   | funet fileshare|      |           | +         |           |           | ++
             | CSC cPouta| +         | +         |           |           |           | +
             | CSC Ida   | +++       | -         |           | ++        | +         | +
   Public    | github    |           |           | -         |           |           | ++
             | Zenodo    |           |           |           |           | ++        | ++
             | Google drive|         |           | -         |           |           | +
             | Own computers|        |           | -         | -         | -         |
             | Emails    |           |           | -         | -         | -         |

Information
===========

TODO
