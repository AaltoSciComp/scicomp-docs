User support
============

.. seealso::

   `Video recording of this talk <https://www.youtube.com/watch?v=P1ttGhPGuN0&list=PLZLVmS9rf3nN1Rj-TAqFEzFM22Y1kJmvn>`__

   :doc:`user-support-responses`


As infrastructure providers, we are often thrust into a user support
role (as well as a teaching role).  We should look at this as a good
thing: support of top-level science requires an intimate connection to
the tools to do that science.  I see that as part of our plan.

This talk is about Aalto Scientific Computing's user support.  It is
designed as much to explain our philosophy of user support as it is to
talk about specific tools.  It takes a critical view of some existing
common practices, as discussed in CodeRefinery/NordicHPC channels.

Broad contents:

- What does "user support" even mean?
- AaltoSciComp's lines of user support
- Strategic risks and considerations

.. figure:: /about/img/scicomp-3-components.png

   The three roles of Aalto Scientific Computing are all
   interdependent on one another.


About us
--------
- We are Aalto Scientific Computing
  - Science-IT (HPC)
  - Department IT (CS, NBE, PHYS)
  - Close collaborations with Aalto ITS, CSC, FCCI

- Our collaboration used to be called "Finnish Grid and Cloud
  Infrastructure", now will be called "**Finnish Computing Competence
  Infrastructure**" so *user support is clearly more important than
  ever*.
- We are proud of our user support, but it is a multi-faceted
  approach which requires the right mindset.



Role of user support in scientific computing
--------------------------------------------

User support has a bad reputation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Customers often think it is really bad (the support staff hate me!)
- Support staff often hate doing it (the customers don't know anything!)
- Our term "issue" or "ticket" implies it's a discrete task that you
  want to end as soon as possible.

Why?

- Technology is hard
- Users usually don't give enough information to solve the issue.
- ... Users don't even know how to give enough information.
- We often pick up slack when something isn't otherwise taught
- We are disconnected from the user community
- User support may be some forced extra thing on top of our "real"
  job.


Types of support
~~~~~~~~~~~~~~~~

- How do we even answer questions people may have?  Some issues are
  system bugs that are *our* action items, but when the user themself
  needs help we can make some **hierarchy of support strategies**:

  a) "read the manual: <link>"
  b) tell them what to do
  c) give them a live demo
  d) pair program working example, you lead
  e) do the task for them, no need to teach

- Lower letters are faster to answer and traditional support.  Higher
  letters are much more time-consuming, and approach mentoring or
  Research Software Engineering services.


Why is support hard?
~~~~~~~~~~~~~~~~~~~~
- "Crisis of computing": most users skills are much less than needed.
- User interfaces are usually bad
- Lots of hidden internal state


XY problem
~~~~~~~~~~
- People ask for what they think they need (X)
- They are given X
- X isn't even a good way of doing what they actually want (Y), but we
  spend a huge amount of time doing X, when the right way Z→Y is much
  simpler.
- **XY problem** (`wikipedia
  <https://en.wikipedia.org/wiki/XY_problem>`__): people don't ask for
  the end goal, but some intermediate step.
- **XY solution** (my term): Support person wants to answer X because
  it requires less investigation and you can close the ticket and move
  on, even though they get the feeling it's not a good idea.


Be motivating
~~~~~~~~~~~~~

- "How to help someone use a computer" by Phil Agre:
  https://www.librarian.net/stax/4965/how-to-help-someone-use-a-computer-by-phil-agre/
- Hanlon's razor: "never attribute to malice that which is adequately
  explained by stupidity"
- In our case, this is **never attribute to malice or stupidity that
  which is adequately explained by having never been told something
  obvious**
- Avoid expressing unhappiness, displeasure, a condescending attitude,
  expectation that they should have known better, "damage", etc.
- Resist the temptation to blame the user.  If they actually can do
  something that harms others, it's the system's fault.  If they don't
  know something, the UI is bad or society's preparation is not
  enough.  Etc.



SciComp`s user support tools
----------------------------

Our general guidelines
~~~~~~~~~~~~~~~~~~~~~~
- "help page", :doc:`scicomp.aalto.fi/help </help/index>`

  - Describes what to do in general, key points to mention when making
    a request.

  - It links to a longer "how to ask for help"

  - Both can be a bit patronizing to link to during an issue, so we
    have to be careful.


Docs
~~~~
- https://scicomp.aalto.fi (this site)
- Open-source (CC-BY), public
- Built with `Sphinx <https://sphinx-doc.org>`__
- Findable by general web search.  This is a *big* deal - don't hide
  your docs!
- Managed by git on Github
- There will be another talk on specific Sphinx information later.


Gitlab issue tracker
~~~~~~~~~~~~~~~~~~~~
- We use Aalto Gitlab (version.aalto.fi) as issue tracker

  - University single-sign on
  - "Internal" permissions (anyone who can log in)
  - Common interface, reasonably powerful labelling, searching, etc.

- When is an issue closed?  As soon as possible, or when you are sure
  they are happy?

  - We are too much "when we are sure they are happy", which often is
    "never"
  - Closing too soon discourages asking for help.

  - Is *issue* the right term here, or is *conversation* the right term?


Email tracker
~~~~~~~~~~~~~
- Email is a bad medium, advanced issues should be *public* so that
  users can learn from each other and we don't have to type the same
  thing over and over.
- Low threshold to direct to the issue tracker instead of email.

  - Most users know this and we get few emails

- Aalto IT services uses Efecte, CS uses its own RT (much nicer).
- Three groups: scicomp, scip (teaching), rse (RSE services).


Daily Garage
~~~~~~~~~~~~
- :doc:`/help/garage`
- Online "office hours" via Zoom
- Every day, 13-14.  If no one comes, it's admin chat time.
- Amazingly good for keeping a community going.


Chat
~~~~
- :ref:`chat`
- Is chat a good idea or does it get out of hand?  Remains to be seen
- Current philosophy: we need to build community.  Chat is not for
  issues, but *chat* and determining if something should be an issue
  or not.
- Uses Aalto-hosted Zulipchat.  Believe us, just don't use Slack.


Office drop-in
~~~~~~~~~~~~~~
- Not done in pandemic time, obviously
- Mostly replaced by "daily garage" which is better anyway
- Our offices are spread around the departments we serve, and we
  accept drop-ins anytime we are there.
- This keeps us closely connected to the community.


Personal networks
~~~~~~~~~~~~~~~~~
- Most of us came from the departments we serve now
- Our existing networks are a good way of contacting us


Teaching
~~~~~~~~
- :doc:`/training/index`
- You can't just answer questions as they come in, you need to
  proactively.
- Our teaching is open and free.
- Low threshold to direct to existing material rather than answering
  new question.  Close support ↔ teaching connection.
- `CodeRefinery <https://coderefinery.org>`__ is a Nordic teaching
  collaboration.


Private email
~~~~~~~~~~~~~
- I (rkdarst) really discourage this and always direct people to one of
  the tracked means.

- My phrasing "If you send it to me personally, I am almost certain to
  eventually forget to reply, and I may not be the person who can best
  answer you anyway."  Then I usually try to give some sort of an
  attempt at an answer, since I have to give the appearance that I
  really care.



Strategic vision of support
---------------------------

Support ↔ teaching ↔ RSE
~~~~~~~~~~~~~~~~~~~~~~~~
* Support: one-to-one answering questions
* Teaching: one-to-many improving skills
* Research Software Engineering: one-to-few "I will do it for you" or
  "Let me get you started"


Strategic risks
~~~~~~~~~~~~~~~
- The middle layer of science always gets cut first: when funding goes
  down, support will get cut and researchers left more alone.
- Our load increases, and our funding doesn't

  - We become unhappy, support level goes down
  - Emphasis increases on speed of closing tickets


Strategic benefits of good support
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
These can be used to argue for good funding of our teams:

- Diversity

  - Without good support, "rich get richer" contributes to the
    increasing homogeneity of computational science.

  - Previous talk by Richard Darst:

    - Summary: Computational sciences has a crisis of demographics.
      We are on the front lines of this battle, and it's up to us 
    - `Slides <https://docs.google.com/presentation/d/1pVjFnxGzfy0DTPuc1XLQDFg0-44GUWwfSMxe5vVg-Lc/edit>`__
    - `Video <https://youtu.be/z1VS1wleN-o>`__

- Open science

  - Without good user skills, people can't make their computational
    work reproducible or shareable.
  - We need to claim our place in this problem, rather than let it go
    to administrative Open Science staff.


Exercise: problematic situations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Someone emails you privately about something they have clearly not
   even tried yet.

2. A new researcher is trying to use Triton to do some machine
   learning.  They are trying to use Python+Jupyter, but minimal
   experience managing a Python environment.


Conclusions
-----------

Open questions

- What do *you* think?
- Do we have too many lines of support?



See also
--------

- SciComp's :doc:`User help page </help/index>`
- Richard Darst's talk on `Support services vs diversity
  <https://www.youtube.com/watch?v=z1VS1wleN-o>`__
- `How to ask for help with supercomputers
  <https://cicero.xyz/v3/remark/0.14.0/github.com/bast/help-with-supercomputers/main/talk.md/#1>`__,
  the counterpoint of this from the user perspective.
- `How to help someone use a computer, by Phil Agre <https://www.librarian.net/stax/4965/how-to-help-someone-use-a-computer-by-phil-agre/>`__
- #NordicHPC threads on CodeRefinery chat, which has provided many ideas

  - `how to ask for help <https://coderefinery.zulipchat.com/#narrow/stream/198213-nordichpc/topic/how.20to.20ask.20for.20help/near/230190210>`__
  - `how to provide help <https://coderefinery.zulipchat.com/#narrow/stream/198213-nordichpc/topic/how.20to.20provide.20help/near/231130622>`__

- `How to write good support requests
  <https://documentation.sigma2.no/getting_help/how_to_write_good_support_requests.html>`__,
  by Sigma2 (Norway)


Credits
-------
- Author/editor: Richard Darst
- Thanks to Radovan Bast, Anne Fouilloux, and others in the
  CodeRefinery NordicHPC channel for good discussions.
