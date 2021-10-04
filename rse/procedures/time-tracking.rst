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

## Time tracking

(This section is for our RSEs)

* Be aware that it takes some time to get up to speed with a project.
  This should be considered when making the initial estimate, during
  the first consultation.
* No one can work at 100% at a specific task.  Instead of
  micro-managing time, our RSE should assume 75% efficiency for the
  time billed to any given project, with the rest for overhead tasks.
  This also covers the time spent by other SciComp members spending
  consulting on projects, and time spent after the project is done
  with follow-up consultations.
* When being paid by projects, we need to *only* record time actually
  spent on that project.  Thus, daily garages and other RSE meetings
  need to recorded to the common RSE project/cost center.  These
  overhead work times are managed separately.

Gitlab commands:
* Use these within the issue as a comment, to control the time
  allocation.
* ``TIME-RECORD`` has the form ``XXmoYYwZZdUUhVVm`` for ``XX`` month, ``YY`` 
  weeks ``ZZ`` days ``UU`` hours and ``VV`` minutes.
* Time units: Months (``mo``), Weeks (``w``), Days (``d``), Hours (``h``), 
  Minutes (``m``). Default conversion rates are 1mo = 4w, 1w = 5d, and 1d = 8h.  
* ``/estimate TIME-RECORD`` - estimate total time a project make take.  
  Used as
  soon as possible at beginning of a project, can always be updated
* ``/spend TIME-RECORD [YYYY-MM-DD]`` - announce that you have spent a 
  certain amount of time
  on the project, you can give an optional date for the spent time.
* ``/timesaved TIME-RECORD [YYYY-MM-DD]`` - estimate total researcher time 
  saved, this is important for us to see how efficient we are.

## Project management and results:

Most projects should have a few details associated with them, like contact 
details of the requesting researcher and potentially also their supervisor.

Gitlab commands for project details:
* ``/contacts EMAIL[, EMAIL [...]]`` - who we usually communicate with, 
  note that these people will get update emails, when the project is updated.
* ``/supervisor EMAIL[, EMAIL [...]]`` - PI(s) responsible for research (not
   usually contacted)
* ``/summary TEXT`` - text to be added to the summary bullet points of this
  project. Takes the whole note as text, but should be a single sentence.


For an overview of our work we try to keep track on what kind of results are 
supported by it. For this we keep a record of associated publications either
in the form of papers, software or datasets. It is also interesting to see 
how many researchers benefited from any given project, so we keep track of 
those, this number can easily increase at a later point if software we 
produced or systems we set in place are used by more people. 

Gitlab commands for project outcomes:
* ``/projects INT`` - number of researcher projects supported by this RSE project
* ``/publications INT`` - number of publications supported by this RSE project
* ``/software INT`` - number of software packages supported by this RSE project
* ``/datasets INT`` - datasets supported by this RSE project
* ``/outputs INT`` - number of open science outputs produced other than the categories above





