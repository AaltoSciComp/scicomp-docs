=====================
Data storage services
=====================


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
   repository such as Zenodo.

+--------------+--------------+--------------+--------------+--------------+--------------+
|              | Large        | Fast         | Confidential | Backups      | Long-term    |
|              |              |              |              |              | archival     |
+==============+==============+==============+==============+==============+==============+
| Code         |              |              |              | O            | O            |
+--------------+--------------+--------------+--------------+--------------+--------------+
| Original     | o            | o            | O?           | O            | O            |
| data         |              |              |              |              |              |
+--------------+--------------+--------------+--------------+--------------+--------------+
| Intermediate | O            | O            | O?           |              |              |
| files        |              |              |              |              |              |
+--------------+--------------+--------------+--------------+--------------+--------------+
| Final        |              |              |              |              | O            |
| results/open |              |              |              |              |              |
| data         |              |              |              |              |              |
+--------------+--------------+--------------+--------------+--------------+--------------+

Types of storage
================

There are different qualities we want in filesystems: large, fast,
confidential, highly available, backed up, mounted everywhere, lasts
forever. It is expensive to have all of these together, so there are
different places with different benefits. It is up to you to balance
their use so that you can accomplish what you need. Compare this table
to the types of data above. Use the right place for the right data.

+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+
|           |           | Large     | Fast      | Confident | Backups   | Long-term | Shareable |
|           |           |           |           | ial       |           | archival  |           |
+===========+===========+===========+===========+===========+===========+===========+===========+
| Triton    | scratch   | O         | O         | o         | X         | X         | O         |
+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+
|           | work      | O         | O         | o         | X         | X         |           |
+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+
|           | Triton    | X         |           | o         | O         |           |           |
|           | home      |           |           |           |           |           |           |
+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+
|           | Local     | o         | OO        | o         |           |           |           |
|           | disks     |           |           |           |           |           |           |
+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+
|           | ramfs     |           | OOO       | O         |           |           |           |
+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+
| Depts     | /m/.../pr | o         | o         | O         | O         |           | o         |
|           | oject     |           |           |           |           |           |           |
+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+
|           | /m/.../ar | o         | o         | O         | O         | o         | o         |
|           | chive     |           |           |           |           |           |           |
+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+
| Aalto     | Aalto     |           |           | O         | O         |           |           |
|           | home      |           |           |           |           |           |           |
+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+
|           | Aalto     |           |           | x         | X         | X         |           |
|           | laptops   |           |           |           |           |           |           |
+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+
|           | Aalto     |           |           |           |           |           | O         |
|           | webspace  |           |           |           |           |           |           |
+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+
|           | version.a |           |           | O         | O         | o         | O         |
|           | alto.fi   |           |           |           |           |           |           |
+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+
| Finland   | funet     |           |           | o         |           |           | O         |
|           | fileshare |           |           |           |           |           |           |
+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+
|           | CSC       | o         | o         |           |           |           | o         |
|           | cPouta    |           |           |           |           |           |           |
+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+
|           | CSC Ida   | OO        | x         |           | O         | o         | o         |
+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+
| Public    | github    |           |           | X         |           |           | O         |
+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+
|           | Zenodo    |           |           |           |           | O         | O         |
+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+
|           | Google    |           |           | X         |           |           | o         |
|           | drive     |           |           |           |           |           |           |
+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+
|           | Own       |           |           | X         | X         | X         |           |
|           | computers |           |           |           |           |           |           |
+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+
|           | Emails    |           |           | X         | X         | X         |           |
+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+
