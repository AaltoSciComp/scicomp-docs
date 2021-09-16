Hybrid events
=============

This page is our recommendations/ideas for hybrid events (in-person
plus online components).  It may be out of place on scicomp.aalto.fi,
but it's the best place we have to put them right now.  Unlike other
recommendations, this page is not just for teaching but applies to any
type of event.



Why hybrid?
-----------

* Why do you want hybrid, as opposed to online or in-person?  If you
  can't clarify the purpose to yourself, it may be hard to put on a
  successful event.

  * In-person gives better chances to talk in small groups and among
    your friends, both during and after the event.  (Is your in-person
    event disadvantaging introverts or less well connected people?)
  * Online allows anyone to participate with a lower threshold.  If
    you do it right, you could allow anyone in the world to take part.

As a side note, for massive events, participants can get a full
experience by having their own group chat to discuss the topics,
separate from the event chats.


General considerations
----------------------
- Plan and test early, don't assume things work unless you experience
  it yourself.
- The first time (or few times), have a separate "director" who can
  manage the online part and tech, so the hosts focus on hosting.
- Related to the above (possibly the same person), have someone to
  help interface with the audience and relay questions from them to
  you, answer basic questions, etc.  This person should be able to
  interrupt you immediately for pressing questions.
- Audio is the most important part and will most often go wrong.  Make
  sure you use microphones well, don't count on wide-area room mics,
  do an audio check days before and immediately before, ask audience
  if it is good, and make sure they tell you immediately if problems
  develop.early if things get worse.

Feedback and interaction
~~~~~~~~~~~~~~~~~~~~~~~~

One of the biggest advantage of online events is the combination of
multiple communication channels, so that it is not just extroverts
asking questions.

- Have a clear way to get feedback (like presomo).  Make it very
  explicit how this works.  Have some icebreaker polls/questions.
- Require in-person audience to ask questions via the feedback tool,
  not via voice.  Distributing microphones is a lot of work and will
  often be forgotten, and also voice questions bias towards
  extroverts, and you will be able to better order your answers.  Text
  questions also allow other people to answer and give help at the
  same time.  If a question becomes a discussion, you could distribute
  microphones.
- When feedback and questions are done well, they can be published
  along with the talk (make sure you announce this in advance).
  Especially the "document-based" method below is very good for this,
  since it can be fixed up after the course.
- Make sure that the current presenter can always see the questions.
  A good recommendation is a separate computer with it large font next
  to your presentation computer.
- To encourage people to use this, it is best to also
  screenshare/project it, so that the audience can see that it is in
  active use.  This takes some screen space, but can be well worth it
  if it increases interaction.
- If the text communication tool is the same as the rest of what the
  event uses, and has good treading support, then you get even more
  synergies.

There are different types of feedback tools:

* Chat is simple, but linear and thus questions can easily get lost,
  and answers are hard to connect to questions.  The advantage is it
  is usually built-in to meeting software.
* feedback tools like Presemo (https://presemo.aalto.fi) allows basic
  questions, voting, and replies.
* Documents (google docs, HackMD, etc) allow free-form text.  The
  general idea is people write a free-form question or comment at the
  bottom of the document, and bullet points are used to give answers
  or replies.  This requires some getting used to and has risk of
  trolling in extremely large events, but when this works, it works
  well.  See the `CodeRefinery HackMD mechanics
  <https://coderefinery.github.io/manuals/hackmd-mechanics/#asking-questions>`__
  for an example and advice.



Tech: Zoom
----------

Zoom, and other meeting software, have many of the features that can
be used for an easy, self-service hybrid event.  We assume you know
how to use Zoom (or equivalent) by yourself for an online meeting, and
here we describe the changes for hybrid events.

The advantage of using normal meeting software is that you don't need
to learn a new tool and it is perfectly reasonable to do everything
self-service.

- Classrooms set up for hybrid work have camera inputs hooked up to
  the room cameras.  There is a separate control panel for switching
  and rotating the cameras.  Play around with the controls to learn
  how they work.  Select the right input.
- Zoom can equally share the screen like normal.
- If you present from your own computer, you can run zoom on your
  computer to share screen, and use the room computer to share the
  camera view + sound.  You can tell any other presenters to do the
  same.
- Remember the benefits of being online.  Providing slides and
  material in advance allows online (and in-person) people to use
  multiple channels at the same time, if it suits them.

Zoom audio in a classroom
~~~~~~~~~~~~~~~~~~~~~~~~~

As described above, audio is one of the most important considerations.
In principle it is easy, but there are many details to consider.


* The first is your goals: we have three categories, (presenter),
  (in-person audience), (online audience).  Which of them should hear
  each other?
* The main thing is to prevent audio feedback.  To solve this, it is
  important to have one machine as the audio master in the room (it
  has both the microphone and speakers connected to it).  This also
  prevents the presenter from having their audio go back into the room
  via the online meeting.
* **Presenter → online** can be done with microphones connected to a
  computer, for example the classroom computer connected to the
  microphones or a bluetooth microphone.
* **In-person audience → online**, in practice, needs to be done by
  passing around microphones.  An wide-area microphone might work, or
  might not.
* **Online → in-person** is a bit more interesting.  You can connect
  the audio computer to the speakers in the room (or external
  speakers).  You will need to position the speakers to avoid feedback
  into the microphones as much as possible, and adjust all the
  different volumes.
* To adjust for different sound levels of the different groups, you
  might need someone continually monitor and go adjusting the volumes
  of the various microphones separately.

Overall, you could say that voice communications is the main point of
in-person meetings.  But it is also the hardest to scale to a large
audience.  Consider if you can get text feedback and interaction
working well, and then perhaps you could skip audio - and perhaps the
entire effort of a hybrid event?



Tech: dedicated A/V setup
-------------------------

We have put on an event with a dedicated A/V setup, with external
microphones, etc.  In the end, it also used Zoom to broadcast to the
world, so was quite similar to the above.  Perhaps this recommendation
is obsolete and one should just use the above as a starting point?

TODO: more info



Tech: live streaming
--------------------

For a largest events, meeting software doesn't work: you have to manage
all the participants, and any one participant can disrupt the event
for everyone else.  The "live streaming" model is much better in this
case: it is a one-to-many broadcast, not many-to-many meeting.  Live
streaming is popular these days, and thus you can find many
user-friendly but powerful tools.

For now, see `CodeRefinery manuals on the MOOC strategy
<https://coderefinery.github.io/manuals/coderefinery-mooc/>`__ for a
detailed description.


See also
--------

Aalto University links:

- Rooms with lecture capture built-in (or filter by "Lecture capture"
  in booking system):
  https://wiki.aalto.fi/display/OPIT/Lecture+capture+spaces
- Hybrid teaching recommendations (not really focused on technology,
  but how to engage):
  https://wiki.aalto.fi/display/OPIT/Hybrid+teaching+in+Aalto+University
- Another lecture Zoom-capture idea (Uses a smartphone and a bluetooth
  microphone, simple but may miss some communication channels. This could
  be combined with the above.):
  https://wiki.aalto.fi/display/OPIT/Zoom#expand-Case1Onlineandinpersonlecturesimultaneously
