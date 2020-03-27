============
Aalto Gitlab
============

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

The `Aalto instructions can be found here <version-inst_>`_, and
general `gitlab help here <gitlabhelp_>`_.

.. _version-inst: https://version.aalto.fi/docs/aalto_version_quickstart_guide.pdf
.. _gitlabhelp: https://version.aalto.fi/gitlab/help

All support is provided by Aalto ITS. Since all data is stored within
Aalto and is managed by Aalto, this is suitable for materials up to
the "confidential" level.

Extra instructions for Aalto Gitlab
-----------------------------------

Always login with HAKA wherever you see the button.  To use your Aalto
account otherwise, use ``username@aalto.fi`` and your Aalto password
(for example, use this with ``https`` pushing and pulling).  But, you
really should try to configure ssh keys for pushing and pulling.

For outside/public sharing read-only, you can make repositories public.

If you need to share with an **outside collaborator**, this is supported.
These outside partners can access repositories shared with them, but
not make new ones.  They will get a special gitlab username/password,
and should use that with the normal gitlab login boxes.  To request an
collaborator account, their Aalto sponsor should `go here to the
request form <workflow_ext_>`_ (employees only).  (You can always set
a repository as public, so anyone can clone.  Another hackish
method is to add ssh deploy keys (read-only or read-write) for outside
collaborators, but this wouldn't be recommended for serious cases.)

.. _workflow_ext: https://workflow.aalto.fi/version_ext/

For **public projects** where you want to build a community, you can also consider
Github.  There's nothing wrong with having both sites for your group, just
make sure people know about both.  Gitlab can have public projects,
and Github can also have group organizations.

**NOTE!** If your work contract type changes (e.g. staff -> visitor,
student->employee, different department),
the Aalto Version blocks the access as a "security" measure. Please
contact Aalto ITS Servicedesk <servicedesk@aalto.fi> to unblock you.
This is annoying, but can't be fixed yet.

The service doesn't have quotas right now, but has limited resources
and we expect everyone to use disk space responsibly.  If you use too
much space, you will be contacted.  Just do your best to use the
service well, and the admins will work with you to get your work done.



CodeRefinery Gitlab and Gitlab CI service
-----------------------------------------

CodeRefinery is a publically funded project (by Nordforsk / Nordic
e-Infrastructure Collaboration) which provides teaching and a `GitLab
platform for Nordic researchers <coderefinery_repo_>`_.  This is
functionally the same as the Aalto Gitlab and may be more useful if
you have cross-university collaboration, but requires more activation
to set up.

They also have a Gitlab CI (continuous integration) service which can
be used for automated building and testing.  This is also free for
Nordic researchers, and *can be used even with Aalto Gitlab*.  Check
their `repository site info <coderefinery_repo_>`_, if info isn't
there yet, then mail their support asking about it.



Recommendations
---------------

``version.aalto.fi`` is a great resource for research groups.  Research
groups should create a "Gitlab group" and give all their members access to
it.  This way, code and important data will last longer than single
person's time at Aalto.  Add everyone as a member to this group so
that everyone can easily find code.

Think about the long term.  Will you need access to this code in 5
years, and if so what will you do?

- If you are a research group, put your code in a Gitlab group.  The
  users can constantly switch, but the code will stay with the group.

- If you are an individual, plan on needing a different location once
  you leave Aalto.  If your code can become group code, include it in
  the group repository so at least someone will keep it at Aalto.

- `Zenodo <https://zenodo.org>`_ is a long-term data archive.  When
  you publish projects, consider archiving your code there.  (It has
  integration with Github, which you might prefer to use if you are
  actually making your code open.)  Your code is then citeable
  with a DOI.

- In all cases, if multiple people are working on something, think
  about licenses at the beginning.  If you don't, you may be blocked
  from using your own work.



FAQ
---

-  **What password should I use?** It is best to use HAKA to log in to
   gitlab, in which case you don't need a separate gitlab password. To
   push, it is best to use ssh keys.
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
- **When are accounts/data deleted?** The deletion policy is findable
  in the `privacy policy <versionprivacy_>`_.  In 2017, it's 6 months
  after Aalto account closed, 24 months after last login, or 12 months
  after last login of an external collaborator.
- **Are there continuous integration (CI) services available?**  Not
  from Aalto, but the CodeRefinery project has free CI services to
  Nordics, see `their site <coderefinery_repo_>`__
  and the description above.

.. _versionprivacy: https://version.aalto.fi/policies/version_aalto_policy_eng.pdf
.. _coderefinery_repo: https://coderefinery.org/repository/

