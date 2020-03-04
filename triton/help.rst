===================
Getting Triton help
===================

There are many ways to get help, and you should try them all.  If you
are just looking for the most important link, it is :ref:`our issue
tracker <issuetracker>`.

Whatever you do, these `guidelines for making good support requests
<https://research.csc.fi/support-request-howto>`__ are very useful.

.. seealso::

   Are you just looking for a Triton account?  See :doc:`accounts`.

Give enough information
~~~~~~~~~~~~~~~~~~~~~~~

We get many requests for help which are too vague to give a useful
response.  So, when sending us a question, always answer these
questions and you'll get the fastest useful response:

* **Has it ever worked?**  (If so, what has changed?)
* **What are you trying to accomplish?**  (Your `ultimate goal
  <https://en.wikipedia.org/wiki/XY_problem>`_, not current technical
  obstacle.)
* **What did you do?**  (Be specific enough to be reproducible - copy and
  paste exact commands you run, scripts, inputs, output messages, etc.)

If you don't know something, it's OK, just do your best and we'll help
from there!  You can also chat with us to brainstorm about issues in
general.  A much more detailed guide is available from `Sigma2 documentation
<https://documentation.sigma2.no/help/how_to_write_good_support_requests.html>`_.


The Triton docs
~~~~~~~~~~~~~~~
In case you got to this page directly, you are now on the Triton and
Science-IT (CS, NBE, PHYS at least)
documentation site. See `the main page <index>`
for the index.


Your colleagues
~~~~~~~~~~~~~~~
Science is a collaborative process, even if it doesn't seem so.
Academic courses don't teach you everything you need to know, so it's
worth trying to work together and learn from each other - your group
is the expert in it's work, after all.


.. _issuetracker:

Issue tracker
~~~~~~~~~~~~~

We keep track of cluster issues
at https://version.aalto.fi/gitlab/AaltoScienceIT/triton/issues. Feel
free to post your issue there. Either admins or other
users can reply --- and you should feel free to reply and help others,
too. The system is accessible from anywhere in the world,
but you need to login with HAKA (using the button). All newly
created issues are reported to admins by email.

This is primary support channel and meant for general issues like
general help, troubleshooting, problems with code, new software
requests, problems that may affect several users.

.. note::

   If you get a message that you are blocked from version.aalto.fi,
   send the email to servicedesk.  It's not your fault: it
   automatically blocks people when their organizational unit
   changes.  Yes, this is bad but it's not in our control...

   If you have an Aalto visitor account, login with HAKA won't work -
   use your email address and Aalto password.


.. _esupport-triton-address:

Email ticketing system
~~~~~~~~~~~~~~~~~~~~~~

For private issues you can also contact us via `our email alias (on
our wiki pages, login required)`__. This is primarily
intended for specific issues such as requesting new accounts, quotas,
etc.  Please avoid sending personal mails directly to admins, because
it is best for all admins to be aware of issues, people may be absent,
and personal emails are likely to be lost.

Most general issues should be reported to the issue tracker instead,
not by email.  Email is primarily for accounts related queries.

__ https://wiki.aalto.fi/display/Triton/Getting+help

Users' mailing list
~~~~~~~~~~~~~~~~~~~

All cluster users are on the triton-users mailing list (automagically
kept in sync with those who have Triton access).  It is for
announcements and open discussions mainly, for problem solving please
try the tracker.

If you do not receive list emails, you'd better check out with your
local Triton admin that you are on the list. Otherwise you miss all the
announcements including critical ones about maintenance breaks.

In person
~~~~~~~~~

Come by one of the :doc:`Scientific computing garages
<../news/garage>` any week.  It's the best place to get problems
solved fast.

You can also come and talk to us face-to-face, but of course we have to
be in-office.  This is especially useful when there is an open-ended
question where we have to discuss what is the best solution.  We may
then ask you to open a ticket once there is an answer, so that we can
track the progress and not forget.

Triton support team
~~~~~~~~~~~~~~~~~~~

Most of us are members of your department's support teams, so can
answer questions about balancing use of Triton and your department's
computers.  We also like it when people drop by and talk with us, so
that we can better plan our services.  In general, don't mail us
directly - use either the issue tracker above or the support email
address.  You can address your request to a specific person.

.. csv-table::
   :header-rows: 1
   :delim: |

   Dept       | Name             | Location
   CS/NBE     | Mikko Hakala     | T-building A243 / Otakaari 3, F354
   CS         | Simo Tuomisto    | T-building A243
   ELEC       | Tarmo Simonen    | Otakaari 3, F417
   PHYS       | Ivan Degtyarenko | Otakaari 1, Y415a
   CS/SCI     | Richard Darst    | T-building A243


Science-IT trainings
~~~~~~~~~~~~~~~~~~~~
We have regular training in topics relevant to HPC and scientific
computing.  In particular, each January and June we have a "kickstart"
course which teaches you everything you need to know to do HPC work.
Each Triton user should come to one of these.  For the schedule, see
`our training page <http://science-it.aalto.fi/scip/>`__.


Getting a detailed bug report with triton-record-environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We have a script named ``triton-record-environment`` which will record
key environment variables, input, and output.  This greatly helps in
debugging.

To use it to run a single command that gives an error::

  triton-record-environment YOUR_COMMAND
  Saving output to record-environment.out.txt
  ...

Then, just check the output of ``record-environment.out.txt`` (it
shouldn't have any confidential information, but make sure) and send
it to us/attach it to the bug report.

If you use Python, add the ``-p`` option, matlab should use ``-m``,
and graphical programs should use ``-x`` (these options have to go
*before* the command you execute).

