=====================
Zulip for instructors
=====================

Introduction
------------
Zulip is an online discussion tool with latex support. It has been used by some
Aalto teachers as an external service on individual courses. For spring and summer 2021,
Zulip was provided by Aalto CS as a pilot solution for all School of Science
departments' course needs. For the autumn 2021 and spring 2022, the pilot at SCI continues and is widened in small scale also for other schools. 
The pilot refers to a) a fixed-term project
with clear lifecycle needs, like in courses which start and end at certain
times and after which the Zulip instance can be deleted; b) a
transitional period between current state and possible production use or change
to other solutions; and c) a basic solution with without all the fancy features
or user interface. During the pilot users are expected to provide feedback,
which will effect on the decision-making for future solutions, and the
development of usability.

CS-IT hosts `Zulip <https://zulipchat.com/>`_ the chat instances for you. These
chat instances are hosted at ``<chat-name>.zulip.aalto.fi`` (or older instances at ``<chat-name>.zulip.cs.aalto.fi``). Login to the
chats is available with Aalto accounts. Email registration for external users
is also possible via invitations. After logging in for the first time with an
Aalto account, if no matching Zulip account was found, you are prompted to
"Register" and create one. Once the Zulip account has been created, it should
be linked to your Aalto credentials.

Internal or confidential matters should not be discussed on the platform.

Get started / request Zulip
---------------------------

.. note::

   Chat realms can be requested using the form at `https://zulip.aalto.fi/requests/ <https://zulip.aalto.fi/requests/>`_.

.. note::

    If you encounter issues, report them to
    `CS-IT <https://wiki.aalto.fi/display/CSdept/IT/>`_ or on #zulip-support
    at `scicomp.zulip.cs.aalto.fi <https://scicomp.zulip.cs.aalto.fi/>`_

    You can also give/discuss feedback, complaints or suggestions on
    #zulip-feedback at `scicomp.zulip.cs.aalto.fi <https://scicomp.zulip.cs.aalto.fi/>`_

.. note::

    You can test out Zulip at
    `testrealm.zulip.cs.aalto.fi <https://testrealm.zulip.cs.aalto.fi/>`_.
    Use the Aalto login. This chat is for testing only.

.. _first-steps:

After you have received the chat instance
-----------------------------------------

Within few days of requesting an instance, you should have gotten details for your chat instance in email. After this you

- Can login to the chat instance *<chat-instance>.zulip.cs.aalto.fi* with your Aalto account
- Should already have the **owner** role assigned.
- Can configure the chat instance from **(cog wheel in the top-right corner) -> Manage organization**

  - Please carefully read the `Configuration<configuration>` section before making changes

- Can appoint more admins/owners (e.g. TAs)

  #. Ask them to login first
  #. Change their role from **Manage organization -> Users**


.. _configuration:

Configuring your organization
-----------------------------

Below are listed the most important settings found under *Manage organization*
in Zulip. There is no easy way for us to enforce these, so it is your
responsibility as organization owner or admin to make sure they are set
correctly. Make sure any owners/admins you appoint are aware of these as well.

.. note::

    Settings that are not mentioned here, you can configure to your liking.
    However you should still exercise care, since you are responsible for the
    service and safety of your user's data.  If you would like advice, please
    ask us.


**Organization settings / Video chat provider**

  * Set to ``None``
  * The default provider (Jitsi) has not been evaluated or approved by Aalto
  * Integration with Aalto Zoom may come later on


**Organization permissions / Invitation settings**

Do not set both "Organizational Premissions→Invitations = not
required" and "Authentication methods→Email = enabled" at the same
time.

You can allow signup by Aalto account or *any* email.  You can allow
anyone to signup or make it invitation only.  But you *can not* set
"Anyone with Aalto account may signup without invitation, but by email
you must be invited" (Zulip limitation).  So, we have to work around
this, otherwise bots and random people might join in your chat. If the
chat needs to include external users, make it invite only.

The exact questions and answers:

* Are invitations required for joining in the organization?

  * If you are only allowing Aalto Login (see ‘Authentication
    methods’): Can be set to ``No,…`` (But still, anyone with Aalto
    account can join)

  * If you are allowing external users/email registration (see
    ‘Authentication methods’ below): Set to ``Yes, only admins can
    send invitations``.  (You can invite people via their Aalto email
    address for Aalto login)

**Organization permissions / Who can access user email addresses**

* Set this to ``Admins only`` or ``Nobody``


**Organization permissions / Who can add bots**

* Set to ``Admins`` only
* Consult `CS-IT <https://wiki.aalto.fi/display/CSdept/IT/>`_ before deploying
  any bots


**Authentication methods**

* AzureAD

  * This is Aalto Login and should be enabled

* Email

  * This allows users to register using an email address
  * We cannot allow random people or bots to register freely
  * If you enable this, make the chat ``invitation only`` as described in
    'Invitation settings' above, for the reason described there.


**Users**

* You can manage users here.
* Please be careful with who you assign admins/owners. These roles should be
  only given to course staff.
* The "moderator" role can has extra permissions assigned, such as
  managing streams and renaming topics.  This could be good for course
  staff/TAs.


**Other settings, up to you**

* You allow messages to be edited longer using Settings → Organization
  Settings.  It is often useful to set this to a longer period.



Practical hints
---------------

There is a fine line between a discussion platform and chat, normal
chat and topic-based chat, and chaos and order.  Here, we give
suggestions for you, based on what other teachers have learned.

* **Topics** (basically, like subject for a message thread) is the key
  feature of Zulip.  It is explained more below, but basically keeps
  things organized.  If you don't want to do that or it doesn't match
  your flow, you won't like the model.

* Read the :doc:`guidelines for students <../zulip>` to see the
  importance of topics and the three ways to use Zulip, and how we
  typically manage the flood of information in practice.

* Give these guidelines to your students (copy and paste from the
  student page).

* Consider *why* you want a course chat.

  * Do you want a way to chat and ask questions/discuss in a
    lower-threshold platform than forum posts?  Then this could be
    good.

  * Do you want a Q&A forum or support center?  Then this may work,
    but would MyCourses be a better forum?

  * Do you want a place for students groups to be able to chat among
    small groups?

  * Do you mainly want announcements?  Then maybe simply use
    MyCourses?

* Create your channels ("streams") before your students join, and make
  the important ones default streams (this is done under "Manage
  organization"), so that everyone will be subscribed (since peolpe
  will always forget to join streams).

  * If you do create a new default stream later, use the "clone
    subscribers" option to clone from another default stream, so that
    everyone will be subscribed.

  * Some common streams you might want are ``#general``,
    ``#announcements``, ``#questions``.  Some people have one stream
    per homework, exam, theme, and/or task.

  * The main point of streams is to be able to independently filter,
    mute, and subscribe to notifications.  For example, it might be
    useful to view all questions about one homework in order, or
    request email notifications from the ``#announcements`` stream.

* You can create user groups (teams) with a certain name.  The group
  can be ``@``-mentioned together, or added to a stream.

* Moderators (and others) can organize other people's messages by
  topic.  Edit the message to do this, including other people's.
  Hotkey is ``e``.

* If you want a Q&A forum, make a stream called ``#questions``, or
  smaller streams for specific topics, and direct students there.

  * You can click the check mark by a topic to mark it as resolved.

  * Remind students to make a *new topic* for each new question.  This
    enables good follow-up via "Recent topics"

  * If students don't make a new topic (or a topic goes off-track),
    edit the message and change the topic (change topic for "this
    message and all later messages").  Then, you keep questions
    organized, findable, and trackable.

  * If you don't want to be answering questions in private message
    (who does?... it leads to duplicate work), make a clear policy on
    either reposting the questions publicly yourself (without
    identification), or directing the students to repost in the public
    steam themselves.

* If you want to limit students to not be able to do anything, you can
  consider disabling:

  * Adding streams, adding others to streams (if you want people to
    only ask and not make their own groups).

  * Disable private messages (if you really don't want personal
    requests for help).

  * Adding bots, adding custom emojis.

  * Seeing email addresses.  Changing their name.

* On the other hand, you might want to "allow message editing" to a
  much longer period and allow message deleting.  For Q&A these are
  quite useful to have.

* You can use the ``/poll [TITLE]`` command to make lightweight
  non-anonymous polls.  For anonymous polls, someone has used a bot
  called Errbot, but we don't currently know much about that.



FAQ
---

* Is there an easier way than subscribing students manually when
  streams are created?  Yes, you should never be doing that manually.
  See above for cloning membership of a stream from another.

* Isn't it too much work to have to give a topic to every message?
  Well, you don't have to when replying.  And this is sort of a
  natural trade-off needed to keep things organized and searchable:
  you have to think before you send.  Most people consider this a
  worthy trade-off.  Note that you can change the topic of messages
  after the fact, just talk and organize later as needed.



Extra requested features
------------------------

(see also the student page)

* Anonymous polls (a pull request exists with this feature)

* Anonymous discussion

* More fine-grained permissions for TAs.  DONE: moderator role now exists.

* Support for bots and other advanced features (more like permission
  to recommend them, bot support works very well already).

* Pinned topics (pull request exists, high-priority issue, #19483).

* Long-term invitations (upcoming, high-priority issue, #20337)
