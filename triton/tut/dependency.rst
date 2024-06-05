================
Job dependencies
================

.. highlight:: console

.. admonition:: Abstract

   * Sometimes, several jobs need to be run in sequence (for example,
     different parts that require different types of resources).  This
     can be done with job dependencies.

   * This can be done with the ``--dependency`` Slurm option.

Introduction
============

Job dependencies are a way to specify dependencies between jobs.  The
most common use is to launch a job only after a previous job has
completed successfully.  But other kinds of dependencies are also
possible.


Basic example
=============

Dependencies are specified with the ``--dependency=DEPENDENCY_LIST``
option. E.g. ``--dependency=afterok:123:124`` means that the job can
only start after job ID's 123 and 124 have both completed
successfully.


Automating job dependencies
===========================

A common problem with job dependencies is that you want job B to start
only after job A finishes successfully.  However, you cannot know the
job ID of job A before it has been submitted.  One solution is to
catch the job id of job A when submitting it and store it as a shell
variable, and using the stored value when submitting job B. Like::

    $ idA=$(sbatch jobA.sh | awk '{print $4}')
    $ sbatch --dependency=afterok:${idA} jobB.sh


Exercises
=========

.. exercise:: Dependencies-1: read the docs

   Look at ``man sbatch`` and investigate the ``--dependency`` parameter.

.. exercise:: Dependencies-2: Chain of jobs

   Create a chain of jobs A -> B -> C each depending on the successful
   completion of the previous job.  In each job run e.g. ``sleep 60``
   to give you time to investigate the status of the queue.
   
   .. solution::
   
      You should all of your jobs in queue. Jobs with dependency on a 
      previous job will have a status on pending, stating a dependency 
      as the reason.

.. exercise:: Dependencies-3: First job fails

   Continuing from the previous exercise, what happens if at the end
   of the job A script you put ``exit 1``. What does it mean?
   
   .. solution::
   
      Putting ``exit 1`` at the end of your job script means it returns 
      a unix exit code indicating a failure. Next jobs in your depedency 
      list will sit in queue forever, since as far as they know the previous 
      job never completed successfully.
      
      
