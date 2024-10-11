How to actually respond to user support requests?
=================================================

I've been asked before, "how do you actually respond to customer
support requests?".  There are some obvious answers (be polite, try to
answer, etc), but are there any specific references for research
computing / scientific computing support staff?  This page collects my
ideas after having done it formally and informally for years.

This page is specifically about making responses respectfully and with
compassion for the requestors.  It's not designed to be a big-picture
how-to of user support - there are plenty of other resources about
that.

Unsorted notes:

- one person takes the lead in communication
- Start by talking with people about the big picture

  - their position
  - past work
  - what they expect to get out of the support

- many questions are actually about:

  - the environment setup


Quick reference
---------------

This is the quick summary about effective synchronous one-on-one
support strategies to avoid common problems.  There are many things on
the list: the more you know the person or the work, the less you need
to ask.  Maybe some are obvious.  It's an art, not a science.

.. admonition:: Summary

1. Starting

   a) Understand who they are, their department, their current job
      (postdoc, professor, PhD, research assistant, etc.  Ask at
      beginning, not end - if you ask at end is only recordkeeping)
   b) Other questions: who do you work for? What's your background?
      (try to understand the kinds of skills they have and what kind
      of level you should answer)
   c) :ref:`Other questions from the help page
      <formulate-your-question>`, if it's not clear yet:

      - Has it ever worked before?
      - What's your end objective?
      - What did you do so far?
      - What do you want now?

   d) Have you excluded the XY problem (need X but are asking for Y, Y
      isn't a very good solution for X).

2. Doing

   a) My general rule of thumb is that if someone has never seen
      something before, they don't do it themselves the first time. At
      least I demo it once.  Often (with their permission) I request
      Zoom remote control in the screenshare and do it for them,
      slowly, explaining the steps.  They can focus on understanding
      and not typing.
   b) Take time to check if you are doing what they want.
   c) Avoid harsh things like "X is wrong" or "you can't have seen
      that". Avoid saying things are easy, simple, obvious, and so on.
      (It never is for someone else).
   d) Avoid direct commands without at least something like "does that
      sound good to you?" or similar.

3. Wrap-up

   a) Check in again: "Did you get what you wanted out of this?" (This
      should also be asked several times along the way).
   b) Give some encouraging words, I often say things like "with your
      experience I think you are well prepared to figure it out now".
   c) A team member who is a former (human) doctor had a really good
      idea insight. Don't ask about their understanding, ask if you
      explained clearly enough.
   d) Say they can come back if they still have problems and this is
      normal. It's normal for us to give some basic info and let them
      explore some, but already be planning for them to come back for
      implementation.  Express desire to hear more or see them again.

4. Internal follow-up

   a) Did you do well?  If others are around You can discuss
      internally if it if was good technical, and social, support.

Remember: the above is things to consider, decide what's appropriate
for each circumstance.




Why care about how you respond?
-------------------------------

An example:

When interviewing people once, we started our interview with
to-the-point factual information and questions.  Our tone of voice was
"bureaucratic", to say the least.  Our interviewees responded in kind:
with little enthusiasm and we could wonder if they even wanted the
job.

We realized something had to change.  Our next interviewees were
greeted with enthusiasm and excitement about the job.  The
interviewees responded likewise, and we could more easily see how
someone could perform.

Why is this important?  Basically, *we* feed our users how they will
respond.  Is computing a chore they hate?  Is it something that's
fascinating, even if not their main goal?  Do they see working with us
as the highlight of their day or a last-resort?  **We need to set the
right tone with our interactions**.  This is true in all of:

- Our answers
- Our requests for follow-up information
- Outreach about our services

See also: `Observer-expectancy effect
<https://en.wikipedia.org/wiki/Observer-expectancy_effect>`__ and
`Clever Hans <https://en.wikipedia.org/wiki/Clever_Hans>`__.



Levels of competence
--------------------

Customers have all levels of existing competences and needs.  The more
you understand of this, the better you can assist - and it is needed
to frame any response.


- Understand the level that the requestor is at and the level they
  need to be at.  (this is usually not apparent at first)
- An answer far below their level is demeaning.
- An answer far above their level is demotivating.
- It can be hard to know the level to answer, so multiple levels of
  answer are useful: one general paragraph, then one more detailed
  paragraph properly connected.  This also helps people advance up
  their level of confidence, but needs more writing.
- Aalto SciComps's `Bloom's taxonomy of scientific computing skills
  <https://docs.google.com/document/d/1WW00hohZG0Lc2Ga1wSoSzE_ijLSLwX8JlE0ryKnSIgU/edit>`__
  may help to guide your thoughts in evaluating this.
- Discuss: Is it better to assume at too low a level or too high?  How
  can we find the right level to answer at?



XY problem
----------

**XY problem: someone asks about their attempted solution (Y) and not
their root problem (X)**.  If a supporter focuses on the Y and not the
X can cause very inefficient answers.

Examples: "How do I turn on the stove?" vs "I am trying to make tea,
how do I turn on the stove" which allows the answer to point out that
the asker is trying to us an electric kettle on the stove.

- Don't assume that what someone asks for is what they really need -
  you need to read between the lines.
- This isn't their fault, maybe they don't know what they need.
- Possible mitigations:

  - When replying, state your assumptions in your response so that they
    can correct you if they notice it wrong (if this is relevant).
  - Also consider stating several other possibilities briefly, and
    when they would be relevant.  For example: "Do XXX to install the
    software.  But do you know that you can also load it via the YYY
    module?"



General guidelines
------------------

* Think about what the underlying need is (X, not the Y)
* Be verbose (or at least not short).

  * If your answer is "no", it feels better to say it with many words,
    rather than few.
  * Verbosity is a sign of engagement, which makes the customer feel
    respected no matter if the verbosity is useful to them or not.
  * Be especially cautious about answers that are just a link to the
    documentation - unless they are specifically asking for that.
    Even then, try putting it in context.

* **Service gesture**: something more than people expect (beyond the
  minimum that they asked).  (example: try harder to find someone who
  *can* answer, point them to that person.)



Know your audience
------------------

- The more you know about the very work of the person, the faster and
  better you can answer questions.
- This is a more direct lesson for the people managing support, but
  can you do anything about it yourself, too?



Consider at what level someone needs support
--------------------------------------------

* Do they need single answers to a question?
* Are they very lost and need to work with someone to implement it?

  * If you answer small questions piece-by-piece this is inefficient
    hill-climbing.
  * Direct to a RSE service for more support?

* Do they need a tutorial, reference, theoretical explanation, or
  how-to (the 4 types of docs).  These are all very different types of
  answers or links.



Accept that you can't do everything
-----------------------------------

- Make this decision explicit, not implicit.
- An implicit decision here means it is made based on internal biases.
- Better to discuss among the team to make sure it is consistent.
- Document what you do know and learn while working, even if you don't
  have the full answer yet.

  - Yes, this can be a rather hard thing to do: we don't want to give
    a partial or possibly wrong answer.
  - On the other hand, being silent for days or weeks until you have
    the proper answer really doesn't help anyone.  With the rate of
    research, they have probably even gone on to something else!
  - Consider if you should keep the requestor in the loop (generally
    yes, probably good, but qualify if something is still in progress
    and may not work).
  - This also helps any future staff who may pick up after you.  So,
    even if you don't document to the requestor, document internally.

- Try to avoid long silences before any replies, for example if you
  don't even know who can answer.  This can be especially hard without
  a front desk or if you think "just a bit more and we'll know
  something".



Giving bad news
---------------

Sometimes you have to say "no"

- Again, be more verbose rather than less
- Acknowledge the X and the Y of the initial request, so that they
  know the request really isn't possible (rather than "you not
  understanding").
- State why it's not possible, in more or less words.
- Can you turn this into an X-Y answer - find what they really need,
  that you (or someone) can do?



If you don't know the answer
----------------------------

Our audience does all kinds of advanced work, so often we don't know
the answer - or don't know it right away.

* Ask to see what they actually do, all error messages, etc.  Ask to
  share screen.  This can help you to see some problems, and makes
  most problems easy.
* Request the basic information to "work on it yourself for a bit to
  save time", this gives you enough time to study solutions.
* Related to the above, take the time to make things reproducible.
  This is needed for you to begin working, but also seeing the basic
  steps will help to understand the background.



Dealing with mis-directed issues
--------------------------------

* It can be frustrating when someone asks the wrong place
* If you need to be nicer than just saying "no", since you have
  presumably already understood what the issue is, you actually can
  give useful pointers to where to ask next.  This itself may be a
  useful answer to them.

* Can you give keywords / a copy-paste text that explain the actual
  problem, that they can send to the other support you are now
  directing them to.  This:

  - Save the other staff time (they don't have to do the X-Y analysis
    themselves)
  - Save the customer time in thinking about what to say
  - Makes the customer feel valued and validated



Communication strategies
------------------------

- Communicate with respect.  Informal is probably OK, but know your
  audience.
- Sarcasm is usually bad (but we should have already know it's bad
  online).  Even if you think the person reading now will get it, what
  about all the people in the future who might read and rely on the
  same answer?



In-person or synchronous support
--------------------------------

- See the `How to help someone use a computer
  <https://www.librarian.net/stax/4965/how-to-help-someone-use-a-computer-by-phil-agre/>`__
  for many ideas that are relevant to in-person support (and more).
- When you learn something, do you want to create an issue about it so
  that the knowledge can be used later?
- Try to avoid simply taking over their computer and doing something.
  On the other hand, dictating something key-by-key can be equally
  frustrating.  Try to let the user do as much as possible and clearly
  explain why you do some things yourself.

  - Does saying "I don't know, so it's hard for me to tell you what to
    do.  But I can try to figure it out while you watch - is that
    good?"

  - Online support allows screen-sharing and remote control, which
    allows you to type but the other person to still feel like they
    are an important part of the process since they can see
    everything.



Ticketing system support
------------------------

- Is your ticket system public (e.g. Gitlab internal to organization,
  but not private to your team) or private (requestors only see their
  own tickets).  You should answer respectfully anyway, but this does
  matter somehow.  The more people who can see it, the more careful
  you should be, but also the more long-term benefit your answers
  have.
- Document your intermediate progress at least as comments in the
  tickets - if it's not appropriate to send to the user, too.  (see
  above about silence)
- You want separate issues in separate tickets.  Often times, users
  will ask multiple things at once.  You'll have to figure out what to
  do about it, but you should probably clearly say "more emails is
  better, don't worry about sending us three emails all at the same
  time if they are different things".

  - Can you separate issues yourself, instead of replying "please send
    this again"



Private email support
---------------------

- Do you forward it to a ticket system?  Information in private email
  always gets lost.
- If you reply with only "please re-send this", that can sound like
  you don't want the issue in the first place.  What do you do?



Plan for problem situations
---------------------------

Exercises:

How do you answer things such as the following?  Write draft responses:

- Not enough information
- Possibly
- Mis-directed
- Something requestor should be able to do themselves?



Examples
--------

(examples to be inserted here)


See also
--------

- `How to help someone use a computer, by Phil Agre
  <https://www.librarian.net/stax/4965/how-to-help-someone-use-a-computer-by-phil-agre/>`__
