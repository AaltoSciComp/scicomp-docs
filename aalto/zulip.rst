========
Zulip
========

Introduction
------------
Zulip is an online discussion tool with latex support. It has been used by some Aalto teachers as an external service on individual courses. For Spring 2021, Zulip is provided by Aalto as a pilot solution for all School of Science departments' course needs. The pilot period covers teaching periods 3-5, so summer courses are not included. The pilot refers to a) a fixed-term project with clear lifecycle needs, like in courses which start and end at certain times. After the course has ended, the Zulip instance can be deleted. b) a transitional period between current state and possible production use or change to other solutions, and c) a basic solution with without all the fancy features or user interface. During the pilot users are expected to provide feedback, which will effect on the decision-making for future solutions, and the development of usability.

CS-IT hosts `Zulip <https://zulipchat.com/>`_ the chat instances for you. These chat instances are hosted at ``<chat-name>.zulip.cs.aalto.fi``. Login to the chats is available with Aalto accounts. Email registration for external users is also possible via invitations.

Internal or confidential matters should not be discussed on the platform.

.. note::

    Request a chat instance at https://webropol.com/s/zuliprequest

    We are taking in chat instance requests for the 2021 spring teaching periods 3-5 only. In general, the chat instances will be removed after the academic year has ended.

.. note::

    This service is still in beta. You might encounter some issues. If you encounter issues, report them to `CS-IT <https://wiki.aalto.fi/display/CSdept/IT/>`_ or on #zulip-support at `scicomp.zulip.cs.aalto.fi <https://scicomp.zulip.cs.aalto.fi/>`_

    You can also give/discuss feedback, complaints or suggestions on #zulip-feedback at `scicomp.zulip.cs.aalto.fi <https://scicomp.zulip.cs.aalto.fi/>`_

.. note::

    You can test out Zulip at `testrealm.zulip.cs.aalto.fi <https://testrealm.zulip.cs.aalto.fi/>`_. Use the Aalto login. This chat is for testing only.

Configuring your organization
------------------------------------

Below are listed the most important settings found under *Manage organization* in Zulip. There is no easy way for us to enforce these, so it is your responsibility as organization owner or admin to make sure they are set correctly. Make sure any owners/admins you appoint are aware of these as well.

.. note::

    Settings that are not mentioned here, you can configure to your liking. However you should still exercise care, since you are responsible for the service and safety of your user's data.  If you would like advice, please ask us.


**Organization settings / Video chat provider**

  * Set to ``None``
  * The default provider (Jitsi) has not been evaluated or approved by Aalto
  * Integration with Aalto Zoom may come later on


**Organization permisisons / Invitation settings**

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

**Organization permisisons / Who can access user email addresses**

* Set this to ``Admins only`` or ``Nobody``


**Organization permisisons / Who can add bots**

* Set to ``Admins`` only
* Consult `CS-IT <https://wiki.aalto.fi/display/CSdept/IT/>`_ before deploying any bots


**Authentication methods**

* AzureAD

  * This is Aalto Login and should be enabled

* Email

  * This allows users to register using an email address
  * We cannot allow random people or bots to register freely
  * If you enable this, make the chat ``invitation only`` as described in 'Invitation settings' above, for the reason described there.


**Users**

* You can manage users here.
* Please be careful with who you assign admins/owners. These roles should be only given to course staff
