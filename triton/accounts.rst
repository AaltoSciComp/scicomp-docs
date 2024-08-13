===============
Triton accounts
===============

You need to request Triton access separately, however, the account
information (username, password, shell,
etc) is shared with the Aalto account so there is not actually a
separate account. Triton access is available to any researcher at
Aalto for free.  Resources are funded by departments, and distributed
by a fairshare algorithm: members of departments and schools which
provide direct funding have a greater share.

Please use `the account request form
<https://selfservice.esupport.aalto.fi/ssc/app#/order/2025/>`__
("Triton: New user account") to
request the account.
(For future help, you should probably use our issue tracker: see the
:doc:`help` page.)

A few prerequisites:

- You must :doc:`check the intended use cases and agree with the
  Triton usage policies <usagepolicy>`, including the data and
  privacy policies.
- You must learn how to use a computer cluster properly.  At minimum,
  read the :ref:`Triton tutorials <tutorials>` relevant to your uses
  (scanning all tutorials if it is new to you).  Also, you might want
  to read `hands-on scientific computing
  <https://hands-on.coderefinery.org/>`__, and you should know A
  ("Basics"), C ("Linux"), and D ("HPC") well.
- You must have valid Aalto account.
- Also tell us your department/school in your account creation
  request.

.. _triton-accounts-are-for:

Account eligibility checklist (:doc:`see details <usagepolicy>`):

- **Research = yes**, for which a research supervisor can take
  responsibility. (Please tell us who your research supervisor is in your
  account request: someone Professer/Lecturer/Staff Scientist level.
  Not postdoc, doctoral researcher, etc.).

  - **Yes: for use in research work** (scholarly publications, datasets,
    research software, theses, etc.) by anyone affiliated with a
    research PI in any way.

    - ...   Triton should be :doc:`acknowledged
      and linked in ACRIS <acknowledgingtriton>`.

  - **Yes: research theses (PhD, Masters, Bachelors)**.
    However, literature review/non-research theses shouldn't use
    Triton (though these shouldn't have a need for Triton).  These
    should also be acknowledged in ACRIS.
  - **A thesis at a company** doesn't necessarily disqualify Triton use,
    but Triton should be used for the relevant research that will be
    in the thesis, not other company work.

- **Possible: Other minor staff use**

  - For example, testing computational methods, supporting other
    research, or simple usage of computational tools.  However, Triton
    isn't designed as an operative environment and has no service
    guarantees.

- **No: study projects**

  - There are other resources for this, see
    :doc:`/aalto/welcomestudents`.
  - **Yes: study projects as part of a research group.**  If you, a
    student, essentially takes part in a research group to do a study
    project, this is allowed. (It counts as research, and using Triton
    is normal in this case.)

    - (The research supervisor would evaluate this): For example, your
      work will guide future research directions.  Your work may lead to
      a publication someday, even if not an active part of this project.
      The project comes from research ideas.

    - You should be clear about your situation in your request and indicate
      *research* supervisor (Professer/Lecturer level, not course
      instructor or thesis course supervisor).  The supervisor should
      respond to an email confirming the account.

- **Yes:** Students coming to one of our :doc:`Scientific Computing in
  Practice courses </training/scip/index>` which uses Triton. You will
  be specifically told if this is the case.

Visitors, students (non-employed), and teaching assistant job titles
will have a confirmation requested from their research supervisor
before the account is created (you supervisor will have to reply
"yes", you can remind them to read their email and answer).  Others
will have their research supervisor cc:ed in the account creation
message.

You know that you have Triton access if you are in the
``triton-users`` group at Aalto: The ``groups`` command shows this on
Aalto linux machines.



Your department/unit
~~~~~~~~~~~~~~~~~~~~

When you get an account, you get added to a unit's group, which is
"billed" for your usage.  If you change Aalto units, this may need
updated.  Check ``sshare -U`` or ``sshare`` and if it's wrong, let us
know (the units are first on the line).  (These are currently by
department, so changes are not that frequent)



Password change and other issues
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Since your Triton account is a regular Aalto account, for any password
change, shell change etc use Aalto services.  You can always do these on
the server kosh.aalto.fi (at least).

If you are in doubts, in case of any account related issue your
primary point of contact is your local support team member via the
support email address. Do not post such issues on the tracker.



Account deactivation / remove from mailing list
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Your account lasts as long as your Aalto account does, and
the triton-users mailing list is directly tied to Triton account.
You will also be
unsubscribed from the mailing list (they go together, you can't just
be removed from the mailing list).

If you want to deactivate your account, send an email to the scicomp
email address (scicomp -at- aalto.fi).  You can save time by saying
something like the following in your message (otherwise we will reply
to confirm, if you have any special requests or need help, ask us): "I
realize that I will lose access to Triton, I have made plans for any
important data data and I realize that any home and work directory
data will eventually be deleted".

Before you leave, please clean up your home/work/scratch directories
data. Consider who should have your data after you are done: does your
group still need access to it?. You won't have access to the files
after your account is deactivated. Note that scratch/work directory
data are unrecoverable after deleting, which will happen eventually.
If data is stored in a group directory (/scratch/$dept/$groupname), it
won't be deleted and will stay managed by the group owner.



Terms of use/privacy policy
~~~~~~~~~~~~~~~~~~~~~~~~~~~

See the :doc:`usagepolicy` page.
