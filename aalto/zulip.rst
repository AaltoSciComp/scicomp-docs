========
Zulip
========

Introduction
------------

CS-IT can host `Zulip <https://zulipchat.com/>`_ chat instances e.g. for your courses. These chat instances are hosted at ``<chat-name>.zulip.cs.aalto.fi``. Login to the chats works with Aalto account. Email registration for external users is also possible via invitations.

The chat instances are meant for informal discussion. The chat should not be used for grading and it should not be mandatory for students. Internal or confidential matters should not be discussed on the platform. 

.. note::

    We are taking in chat instance requests for the 2021 spring semester. In general, the chat instances will be removed after the semester.

.. note::

    This service is still in beta. You might encounter some issues. If you encounter issues, report them to `CS-IT <https://wiki.aalto.fi/display/CSdept/IT/>`_ or on #zulip-support at `scicomp.zulip.cs.aalto.fi <https://scicomp.zulip.cs.aalto.fi/>`_

.. note::

    You can test out Zulip at `testrealm.zulip.cs.aalto.fi <https://testrealm.zulip.cs.aalto.fi/>`_. Use the Aalto login. This chat is for testing only.

.. note::

    There are also `Rocket.Chat <https://rocket.chat/>`_ instances available, provided by ITS. Rocket.Chat instances can be requested from `Aalto IT <https://it.aalto.fi/>`_

In order to request a chat instance, please contact `CS-IT <https://wiki.aalto.fi/display/CSdept/IT/>`_

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

Do not allow registering with just an email without invitation. Doing so might cause bots and random people to join in your chat. If the chat needs to include external users, make it invite only.

* Are invitations required for joining in the organization 
  
  * If you are allowing external users/email registration (see ‘Authentication methods’) 

    * Set to ‘Yes, only admins can send invitations’ 
  
  * If you are only allowing Aalto Login (see ‘Authentication methods’) 

    * Can be set to ‘No,…’ (Anyone with Aalto account can join) 

**Organization permisisons / Who can access user email addressess**

* Set this to ``Admins only`` or ``Nobody``


**Organization permisisons / Who can add bots**

* Set to ``Admins`` only
* Consult `CS-IT <https://wiki.aalto.fi/display/CSdept/IT/>`_ before deploying any bots  


**Authentication methods**

* AzureAD 

  * This is Aalto Login and should be enabled 

* Email 

  * This allows users to register using an email address 
  * If you enable this, make the chat ``invitation only`` as described in 'Invitation settings'
  * We cannot allow random people or bots to register freely  
  * Unfortunately, there is no option for "Anyone with an Aalto account can register without invitation, but you can invite others with an email address."


**Users**

* You can manage users here. 
* Please be careful with who you assign admins/owners. These roles should be only given to course staff 
