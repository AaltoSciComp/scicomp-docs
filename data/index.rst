Data
====

Data connects most research together.  It's easy to make in short
term, but in the long term it can become so chaotic it loses its
value.  Can you access your research group's data from 5 years ago and
use it?



Data in Aalto
-------------

* Main page: `Research Data Management <https://www.aalto.fi/en/services/research-data-management-rdm-and-open-science>`__
* Quick summary: `What file storage to use? <https://www.aalto.fi/en/services/what-file-storage-to-use-when>`__
* `Summary of storage locations <https://www.aalto.fi/en/services/data-storage-file-services>`__
* `Guidelines for classification of confidential information <https://www.aalto.fi/en/information-processing/classification-of-information>`__,



Data in Science-IT departments
------------------------------

.. toctree::
   :maxdepth: 1

   requesting
   principles
   aalto-details
   confidential-data
   archival
   leaving-aalto
   organization
   science-it-data-policy



Data on Triton
--------------

Triton provides large and fast data storage connected to significant
computing power, but it is not backed up.

* :doc:`/triton/tut/storage`
* :doc:`/triton/tut/remotedata`



Data management
---------------

* `Aalto Research Data Management pages
  <https://www.aalto.fi/en/services/research-data-management-rdm-and-open-science>`__,
  and here we focus on the practical side of things.



Other
-----

* :doc:`/scicomp/git-annex`



Summary table
--------------

O = good, x  = bad

.. csv-table::
   :delim: |
   :header-rows: 1
   :stub-columns: 1

                  | Large        | Fast         | Confidential | Frequent backups| Long-term archival
     Code         |              |              |              | OO           | OO
     Original data | O            | O            | OO?          | OO           | OO
     Intermediate files | OO           | OO           | OO?          |              |
     Final results/open data |              |              |              |              | OO


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
