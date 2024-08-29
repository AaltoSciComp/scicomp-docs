JupyterHub (jupyter.cs) for instructors
=======================================

.. seealso::

   Main article with general usage instructions: :doc:`Jupyterhub for
   Teaching <../jupyterhub>`.  For research purposes, see :doc:`Triton
   JupyterHub </triton/apps/jupyter>`.

`Jupyter <https://jupyter.org>`__ is an open-source web-based system
for interactive computing in "notebooks", highly known for its
features and ease of use.  `Nbgrader
<https://nbgrader.readthedocs.io/en/latest/user_guide/highlights.html>`__
("notebook grader") is a Jupyter extension to support automatic
grading via notebooks.  The primary advantage (and drawback) is its
simplicity: there is very little difference between the notebook
format for research work and automatic grading.  This lowers the
barrier to creating assignments and means that the interface students
(and you) learn is directly applicable to (research) projects that may
come later.

Nbgrader documentation is at https://nbgrader.readthedocs.io/, and
is necessary reading to understand how to use it.  For a quickstart in
the notebook format, see `the highlights page
<https://nbgrader.readthedocs.io/en/latest/user_guide/highlights.html>`__.
However, the Noteable service documentation
(https://noteable.edina.ac.uk/documentation/) is generally much
better, and most of it is applicable to here as well.  The
information included in these is not duplicated here, and is
*required* in order to use jupyter.cs.

Below, you mostly find documentation specific to jupyter.cs and
important notes you do not find other places.


.. toctree::
   :maxdepth: 1

   news
   overview
   system-environment
   request-course
   course-data
   nbgrader
   testing-a-course
   nbgrader-hints
   autograding
   exporting-grades
   public-copy
   faq-hints



Contact
-------
CS-IT. (students, always contact your course instructors first.)

* Chat via :ref:`scicomp chat <chat>`,
  https://scicomp.zulip.cs.aalto.fi, stream ``#jupyter.cs`` for quick
  questions (don't send personal data here, it is public).
* Issues needing action (new courses, autograding, software
  installation, etc) via the CS IT email alias guru @ cs dot aalto.fi
* Realtime support via :ref:`garage` every day at 13:00, focus days on
  Wednesdays but some help might be possible on other days (good for
  screensharing to show a problem, you can prepare us by mentioning
  your issue in the chat first).  You can coordinate by chat to be
  sure.



.. _jupyterhub-instructors-more-info:

More info
---------

* The `Noteable <https://noteable.edina.ac.uk/>`__ is a commercial
  service using nbgrader and has some good documentation:
  https://noteable.edina.ac.uk/documentation/
* For source code and reporting issues, see the main jupyterhub page.
