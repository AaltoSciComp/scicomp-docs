========
Zulip
========

Introduction
------------

CS-IT can host `Zulip <https://zulipchat.com/>`_ chat instances e.g. for your courses. These chat instances are hosted at ``<chat-name>.zulip.cs.aalto.fi``. Login to the chats uses Aalto credentials (with possible support for extenal users later on).

In order to request a chat instance, please contact `CS-IT <https://wiki.aalto.fi/display/CSdept/IT/>`_.

.. note::

    This service is still in beta. If you encounter issues, report them to `CS-IT <https://wiki.aalto.fi/display/CSdept/IT/>`_ or on #zulip-support at `scicomp.zulip.cs.aalto.fi <https://scicomp.zulip.cs.aalto.fi/>`_

.. note::

    There are also `Rocket.Chat <https://rocket.chat/>`_ instances available, provided by ITS. Rocket.Chat instances can be requested from `Aalto IT <https://it.aalto.fi/>`_

Configuring your organization
------------------------------------

Below are listed the most important settings found under *Manage organization* in Zulip. There is no easy way for us to enforce these, so it is your responsibility as organization owner or admin to make sure they are set correctly. Make sure any owners/admins you appoint are aware of these as well.

.. note::

    Settings that are not mentioned here, you can configure to your liking. However you should still exercise care.


**Organization settings / Video chat provider**

  * Set to ``None``
  * The default provider (Jitsi) has not been evaluated or approved by Aalto
  * Integration with Aalto Zoom may come later on


**Organization permisisons / Invitation settings**

We cannot allow people to register freely using random emails, therefore:

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


**Users**

* You can manage users here. 
* Please be careful with who you assign admins/owners. These roles should be only given to course staff 

