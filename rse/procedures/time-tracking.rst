Time tracking
=============

.. warning::

   This page is still in draft form and being discussed and
   developed - it is *only a proposal*.  See the note on the parent
   page.

   This proposal may turn out to be especially bad... please comment.

Unfortunately (fortunately?), we have to track our time some, in order
to justify the benefits of what we do.



Finance time tracking
---------------------

For projects funded by groups (external or internal funding), they
should me marked in Halli.  All other projects (funded by the
department's/school's basic funding) is marked to the standard RSE
project (ask for it), and this time is accounted for at the end of
each year (using the system below)



Internal time tracking
----------------------

In addition to the financial tracking above, it seems we have to keep
a separate tracking of what projects we work on because not every
project is reportable via Halli.

Right now we propose that time tracking is done through Gitlab, within
the issue opened for each "project".

Gitlab commands:

* Use these within the issue as a comment, to control the time
  allocation.
* ``/estimate NNw`` - estimate total time a project make take.  Used as
  soon as possible at beginning of a project, can always be updated
* ``/spend NNh`` - announce that you have spent a certain amount of time
  on the project
* Units: Months (``mo``), Weeks (``w``), Days (``d``), Hours (``h``), Minutes
  (``m``). Default conversion rates are 1mo = 4w, 1w = 5d, and 1d = 8h.
* Use the labels to record the sponsoring department, funding source
  (project or basic), and state.



Reporting
---------

RSEs should be able to produce tabular data matching this semantic
model.  Each row should be one (project, day) work report.

* **username** of the RSE
* **unit** hosting the research (Aalto acronym: SCI, (CS, NBE, PHYS,
  MS, DIEM), ARTS, BIZ, CHEM, ELEC, ENG)
* **day** of work (YYYY-MM-DD)
* **hours** of work on that day.
* **funding**: ``project`` or ``basic`` funding - who is paying for
  this project?  If ``project``, this implies that it was billed to
  Halli.  If ``basic``, it's assumed that it was billed to the RSE
  project and accounting will be done at the end of the year.
* **project-id**: Issue number from Gitlab (optional? - or some other
  ID?).  Note that, from Gitlab, project issue number can give us the
  **unit**, but not the **funding** since most likely initial
  consultations occur before Halli is set up, so can't be billed to
  that.
* **comment**

Things do not have to be exact for every day, but when aggregated over
months, it should asymptotically approach the right values.



Other notes
-----------

Be aware:

* Be aware that it takes some time to get up to speed with a project.
  This should be considered when making the initial estimate, during
  the first consultation.
* When being paid by projects, we need to *only* record time actually
  spent on that project.  Thus, daily garages and other RSE meetings
  need to recorded to the common RSE project/cost center.  These
  overhead work times are managed separately.
