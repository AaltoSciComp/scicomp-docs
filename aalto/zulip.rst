Zulip
=====

.. seealso::

   Instructors, see the relocated instructor page at
   :doc:`zulip/instructors`.

Zulip is a open-source chat platform, which CS hosts at Aalto as a pilot.
It is used as a chat platform for some courses, and allows better
student and chat privacy.

The primary distinguishing feature of Zulip is **topics**, which
allows one to make order out of a huge number of messages.  By using
topics, you can narrow to a certain thread of conversation (while not
hiding all the older conversations from the main view).



Basics
------

.. sidebar:: Main views

   .. figure:: zulip/img/zulip-sidebar.png
      :align: center

      Sidebar of Zulip, with highlights of the ways to follow
      conversations.  See text for explanations.


Once we have the topics, there are various ways to follow:

* **Recent topics**, to see which topics have new information.

* **All messages**, to see everything that is being posted
  efficiently.

* **Per topic (or stream)**, when you click on a topic or stream
  name or select it from the sidebar.  Then you narrow down to a
  particular thread and see only those messages in order.

* The first is better to manage a flood of information (see what's
  new, click on relevant stuff, ignore all the rest).  The second is
  better when you are caught up and want to make sure you don't miss
  anything.  The third is good for catching up on something you
  don't remember.

* What many of us do is to first look at "Recent topics" after we come
  back after a break, see anything important, then scroll to the
  bottom of "All topics" to monitor new things.  If we see something
  we missed, we click on the topic to narrow to it and catch up.

Topics are grouped into **streams** (called this because it is
completely reasonable to follow everything at once via "All messages").
You can select the streams you are part of with the gear icon, above
the channel list.  It is good to occasionally look at this.

.. figure:: zulip/img/zulip-topics.png
   :align: center

   Basic view of messages and how to interact with it.  You can click
   on various places to narrow your view to one conversation or reply.

.. figure:: zulip/img/zulip-recenttopics.png
   :align: center

   Recent topics, another view of recent activity that shows activity
   per-topic.



How to ask a question
---------------------

Seems obvious, doesn't it?  You can get the best and fastest answers
by helping to keep things organized.  These recommendations are mainly
for Q&A-forum type chats.

- First, search history to see if it has already been asked.

  - If so, click on the topic name.  You will narrow your view to see
    that entire conversation.

- If your question isn't answered yet, but is a follow up to an
  existing topic, click on a message in that topic.  Then, when you
  ask, it will go to that same topic as a follow-up, and anyone else
  can narrow to see the whole history.

  .. figure:: zulip/img/zulip-reply.png
     :width: 300px
     :align: right

     Replying to an existing topic.

  - Unlike other chats, your message will *not* get lost, and people
    will both see that it is new *and* can see the history of that
    thread.

  - Your course can say what the threshold for "new topic" is.  Maybe
    they would have one topic per question pre-created or something
    clever like that.

- If you don't find anything relevant to follow up on, make a new topic.

  .. figure:: zulip/img/zulip-new.png
     :width: 300px
     :align: right

     Making a new topic.

  - Select the stream you want to post to (whatever fits best).

  - Click "New topic".

  - Enter the topic name down below: a few words, like an email
    subject.  For example, ``week 1 question 3``, ``integrals of
    complex functions``, ``exam preparation``.

  - Enter your message and send.

Others (or you...) can split or join topics if they want by going to
"edit message", so there is no risk of doing something wrong.  Don't
worry, just ask!

By being organized, you can get both the benefits of quick chat with
the organization of not missing anything.



Other hints
-----------

- You can format your messages using `Zulip markdown
  <https://zulip.com/help/format-your-message-using-markdown>`__.

- "Mute a stream" (or topic) is useful when you want to stay
  subscribed but not be notified of messages by default.  You can
  still find it if you click through the sidebar.

- The desktop and mobile apps can support `multiple organizations
  <https://api.zulip.com/help/switching-between-organizations>`__.  At
  least on mobile apps, switching is kind of annoying.



Apps
----

There are reasonable applications for most desktop and mobile
operating systems.  These don't send your data to any other services.



Open issues
-----------

We are aware of the following open issues:

- It is annoying to have one chat instance per course (but it seems to
  be).

- There are no mobile Push notifications (since Aalto Security won't
  let us turn them on).

- Likewise with built-in video calls (via https://meet.jit.si or Zoom).

- Various user interface things.  But Zulip is open-source, so feel
  free to contribute to the project...
