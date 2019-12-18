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

Please contact us via the support email address **esupport-triton** *_at_* **aalto.fi** (not
personal email) and we will set up your account.  Please tell us your
department, supervisor, Aalto account, and see the conditions below.
(For future help, you should probably use our issue tracker: see the
:doc:`help` page.)

A few prerequisites:

-  you must have valid Aalto account
-  you must have working email address (Aalto)
-  you must accept :doc:`Triton usage
   policies <usagepolicy>`: requesting access to
   Triton cluster at Aalto University, you accept all the conditions
   listed in the Triton usage policies, including the data and privacy
   policies.
-  You should tell us your department/school in your account creation
   request.
-  Accounts are for

   - Researchers (as in, affiliated with a research PI in any way).
     Please tell us who your supervisor is in your account request.
   - Students coming to one of our `Scientific Computing in Practice
     courses <scip_>`_ which uses Triton.  You will be specifically
     told if this is the case
   - Other students not doing research needing computational
     facilities should check out our :doc:`introduction for students
     <../aalto/welcomestudents>`.  **This includes most student
     projects as part of courses, unless you are effectively joining a
     research group to do a project.**

.. _scip: http://science-it.aalto.fi/scip/

You know that you have Triton access if you are in the ``triton-users``
group at Aalto: ``groups`` shows this on Aalto linux machines.

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

Your account currently lasts as long as your Aalto account does. If
you want to end your account early, contact your local support via the
esupport-triton email address. This way, you will also be unsubscribed
from the triton-users maillist (the mailing list is required for
everyone who has an account).

Before you leave, please clean up your home/work/scratch directories
data. Consider who should have your data after you are done: does your
group still need access to it?. You won't have access to the files
after your account is deactivated. Note that scratch/work directory
data are unrecoverable after deleting, which will happen eventually.

Terms of use/privacy policy
~~~~~~~~~~~~~~~~~~~~~~~~~~~

See the :doc:`usagepolicy` page.
