===========================
Aalto version control (git)
===========================

https://version.aalto.fi is a Gitlab installation for the Aalto
community.  Gitlab is a ``git`` server and hosting facility (an open
source Github, basically).

.. note::

   * This page is about https://version.aalto.fi, the Aalto gitlab
     installation.

   * :doc:`scicomp/git <../scicomp/git>` contains our pointers for Git
     usage in general.

   * :doc:`Git migration <../news/git_migration>` contains information
     on switching from subversion or other git repositories to Gitlab.


Git in general
--------------

Git seems to have become the most popular and supported version control
system, even if it does have some rough corners.  See the general
:doc:`git page <../scicomp/git>` on this site for pointers.


Aalto Gitlab service
--------------------

Aalto has a self-hosted Gitlab installation at
https://version.aalto.fi, which has replaced most department-specific
Gitlabs.  With Aalto Gitlab, you can:

* Have unlimited private repositories
* Have whatever groups you need
* Get local support

The `Aalto instructions can be found here <version-inst_>`_.

.. _version-inst: https://version.aalto.fi/docs/aalto_version_quickstart_guide.pdf

All support is provided by Aalto ITS. Since all data is stored within
Aalto and is managed by Aalto, this is suitable for materials up to
the "confidential" level.

Extra instructions for Aalto Gitlab
-----------------------------------

If you need to share with an outside collaborator, this is supported.
These outside partners can access repositories shared with them, but
not make new ones.  They will get a special gitlab username/password,
and should use that with the normal gitlab login boxes.

For public projects where you want to build a community, you can also consider
Github.  There's nothing wrong with having both for your group, just
make sure people know about it.

**NOTE!** If your work contract type changes (e.g. staff -> visitor),
the Aalto Version blocks the access as a security measure. Please
contact Aalto ITS Servicedesk <servicedesk@aalto.fi> to fix the problem
with your account or warn them in advance so that you can continue using
Aalto Version control.


Recommendations
---------------

``version.aalto.fi`` is a great resource for research groups.  Research
groups should create a "Gitlab group" and give all their members access to
it.  This way, code and important data will last longer than single



FAQ
---

-  **What password should I use?** It is best to use HAKA to log in to
   gitlab, in which case you don't need a separate gitlab password. To
   push, it is best to use ssh keys. You could also set up a separate
   gitlab password.
-  **My account is blocked!** That's not a question, but Gitlab blocks users
   when your Aalto unit changes. This is unfortunately part of gitlab
   and hasn't been worked around yet. Mail servicedesk@aalto.fi with
   your username and request "my version.aalto.fi username XXX be
   unblocked (because my aalto unit changed)" and they should do it.
- **What happens when I leave, can I still access my stuff?** Aalto
  can only support it's community, so your projects should be owned by
  a group which you can continue collaborating after you leave (note
  that this is a major reason for group-based access control!).  Email
  servicedesk for information on what to do to become an external
  collaborator.


