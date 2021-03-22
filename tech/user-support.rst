User support
============

As infrastructure providers, we are often thrust into a user support
role (as well as a teaching role).  We should look at this as a good
thing: support of top-level science requires an intimate connection to
the tools to do that science.  I see that as part of our plan.

This talk is about Aalto Scientific Computing's user support.  It is
designed as much to explain our philosophy of user support as it is to
talk about specific tools.  It takes a critical view of some existing
common practices, as discussed in CodeRefinery/NordicHPC channels.

Broad contents:

- What does "user support" even mean for
- How we do user support
- Strategic risks and considerations

.. figure:: /about/img/scicomp-3-components.png

   The three roles of Aalto Scientific Computing are all
   interdependent on one another.


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
- We often pick up slack in teaching and other skills
- We are disconnected from the user community


Types of support
~~~~~~~~~~~~~~~~

- How do we even answer questions people may have?  Some issues are
  system bugs to fix, but when it is a user thing to do:

  a) "read the manual: <link>"
  b) tell them what to do
  c) give them a live demo
  d) pair program working example, you lead
  e) do the task for them, you do it.

- Lower letters are faster to answer and traditional support.  Higher
  letters are much more time-consuming, and approach Research Software
  Engineering services.


XY problem
~~~~~~~~~~
- People ask for what they think they need (X)
- They are given X
- X isn't even a good way of doing what they actually want (Y), but we
  spend a huge amount of time doing X, when Z is much simpler.
- **XY problem**: people don't ask for the end goal, but some
  intermediate step.
- **XY solution** (my term): Support personnel wants to answer X
  because it's faster and you can close the ticket and move on, even
  though you get the feeling it's not a good idea.


Support vs usability
~~~~~~~~~~~~~~~~~~~~
- Let's face it: user interfaces are usually *bad*.  Teaching is
  usually *bad*.



Support vs diversity goals
~~~~~~~~~~~~~~~~~~~~~~~~~~


Be motivating
~~~~~~~~~~~~~

- Hanlon's razor: "never attribute to malice that which is adequately
  explained by stupidity"
- In our case, this is "never attribute to malice that which is
  adequately explained by having never been told something obvious"
- Avoid language expressing unhappieness, displeasure, a condescending
  attitude, expectation that they should have known better, "damage",
  etc.




ASC's user support tools
------------------------

Issue tracker
~~~~~~~~~~~~~
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
- Email is a bad medium, issues must be *public* so that users can
  learn from each other
- Low threshold to direct to the issue tracker instead.

  - Most users know this and we get few emails

Daily Garage
~~~~~~~~~~~~
- :doc:`/help/garage`

Chat
~~~~
- :ref:`chat`

Office drop-in
~~~~~~~~~~~~~~
- Not done in pandemic time, obviously
- Mostly replaced by "daily garage" which is better anyway
- Our offices are spread around the departments we serve, and we
  accept drop-ins anytime we are there.
- This keeps us closely connected.

Personal networks
~~~~~~~~~~~~~~~~~
- Most of us came from the departments we serve now
- Our existing networks are a good way of contacting us

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

SysAdmin ↔ RSE
~~~~~~~~~~~~~~

Strategic benefits of good support
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Diversity
- Open science


Strategic risks
~~~~~~~~~~~~~~~
- The middle layer of science always gets cut first: when funding goes
  down, support will get cut and researchers left more alone.
- Our load increases, and our funding doesn't
  - We become unhappy, support level goes down
  - Emphasis increases on speed of closing tickets


Conclusions
-----------



See also
--------

- Richard Darst's talk on `Support services vs diversity
  <https://www.youtube.com/watch?v=z1VS1wleN-o>`__
- #NordicHPC threads on CodeRefinery chat

  - `how to ask for help <https://coderefinery.zulipchat.com/#narrow/stream/198213-nordichpc/topic/how.20to.20ask.20for.20help/near/230190210>`__
  - `how to provide help <https://coderefinery.zulipchat.com/#narrow/stream/198213-nordichpc/topic/how.20to.20provide.20help/near/231130622>`__

Credits
-------
