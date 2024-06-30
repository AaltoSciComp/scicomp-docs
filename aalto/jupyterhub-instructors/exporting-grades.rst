Exporting Grades from Nbgrader
==============================

To export grades, ``nbgrader export`` is your central point.

Default Exporter (MyCourses)
----------------------------

Running the command above will generate a CSV file (using a custom MyCourses exporter), which you can download, check, and upload to MyCourses.

- You can add the option ``--MyCoursesExportPlugin.scale_to_100=False`` to not scale points to 100.


.. note::
        
    The example below will export the grades for the assignment ``pa1`` (mandatory to set) to a CSV file named ``grades.csv`` (optional). The grades will not be scaled to 100.

    .. code:: bash

        nbgrader export --to=grades.csv --assignment pa1 --MyCoursesExportPlugin.scale_to_100=False

    You can also use the configuration file to set these arguments. See the next section for more information.

Detailed Exporter
-----------------

You could also use the detailed exporter, which exports the grades in a more detailed format. This is useful if you want to see the grades for each graded cell in notebooks.

This exporter can be used to export multiple assignments grades in a single file. The column names will include the assignment name (if exporting more than one assignment), notebook name (if the assignment contains more than one notebook) and the cell name. The cell names will look something like ``cell-fe326c8d9fe8d3a3`` unless you assign a proper name in the cell metadata while creating the assignment notebook, which we encourage you to do.

Since the default export in our environment is the MyCourses Exporter, to set the detailed exporter as your exporter, you can add the following line to the configuration file:

.. code:: python

    c.ExportApp.plugin_class = "detailed_exporter.DetailedExportPlugin"

Or if you wish to use the command line, you can use the following command:

.. code:: bash

    nbgrader export --exporter=detailed_exporter.DetailedExportPlugin --assignment {assignment name} --DetailedExportPlugin.scale_to_100=False

To export multiple assignments, you can set the ``assignment`` attribute in the configuration file:

.. code:: python

    c.ExportApp.plugin_class = "detailed_exporter.DetailedExportPlugin"
    c.DetailedExportPlugin.assignment = ["assignment_name1", "assignment_name2"]
    c.DetailedExportPlugin.scale_to_100 = False

.. seealso::

   :doc:`Nbgrader Basics <./nbgrader>` for learning more about Nbgrader and the configuration.

   :doc:`Hints <./nbgrader-hints>` for more tips, such as late submission policy.
