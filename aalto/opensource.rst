====================
Open Source at Aalto
====================

.. note::

   This policy was developed at the Department of Computer Science, in
   conjunction with experts from Research and Innovation services
   (both the legal and commercialization sides) with the intention of
   serving the wider community.

   After more research, we have learned that this policy is, in fact,
   de-facto applicable to all of Aalto, it is just extremely
   unclear that open source is actually allowed.  Thus, this policy
   can be seen as best practices for all of Aalto.  However, everyone
   (including CS) has more rights: one does not have to use this
   policy.  You don't have to use an open source license.  IP
   ownership may be in more limited hands, so that you need fewer
   agreements to release.

   However, we strongly encourage you to use this policy anyway.  If
   you use this, you *know* that you are safe and have all permissions
   to make open source, regardless of your particular funding
   situation.  It also ensures that you make proper open source
   software, for maximum benefit and open science impact.

   References at bottom.




Researchers make at least three primary outputs: publications, software,
and data. This policy aims to make openly releasing all types of work as
straightforward the traditional academic publishing process.

This document describes the procedure for Aalto employees releasing the
output of their work openly (open source software, data, and
publications). Aalto University encourages openness. This policy
covers only cases where work can clearly be released openly with no
bureaucracy needed. It does not cover complex cases, such as commercial
software, work related to inventions, complex partnership agreements,
etc. The policy is voluntary, and provides a right to release openly,
but does not require it or preclude any other university process.
(Thus it's more of a guideline than a policy.)  It
only is relevant when the creator has an employment relationship with
Aalto. If they don't (e.g. students), they own their own work unless
there is some other agreement in place (e.g. their own funding contract,
grant, etc).  Still, they can use this same process with no extra
bureaucracy needed.

We realize that this policy does not cover all cases. We aim to cover
the 99% case, and existing processes are used for complicated cases.
Aalto Innovation Services provides advice on both commercialization and
open source release.

This policy is for public licensing only (one to many).  You must go
through Research and Innovation Services for anything involving a
multi-party agreement.

Why release?
~~~~~~~~~~~~

The more people who see and build on our work, the more impact we can
have. If this isn't enough, you get more citations and attention. While
we can't require anything, we strongly encourage that all work is either
made open source or taken through the commercialization process. If you
don't know what to do, don't worry: they are not mutually exclusive.
Proper open-source licensing can protect your ability to commercialize
later. Talk to Innovation Services. They like open source, too, and
will help you find the right balance. Anyway, if work matches the
criteria in this policy, it probably has limited commercial potential
anyway: what is more important is your own knowledge and skills that
went into it.

You want to add a proper open source license to your work, rather than
just putting code on some webpage. Without a license, others can not
build on your code, making your impact limited. No one will build on
you, and eventually your work rots and gets lost.

You *always* want to go through this process as soon as possible at
the beginning of a project: if
you don't, it becomes much harder to track everyone down.

You shouldn't release as open source (yet) if your work is intentionally
commercial or contains patentable inventions. In these cases, contact
`Innovation Services <innosrv_>`_. In the second case (patentable inventions),
according to Finnish legislation you are actually required to report the
invention to Innovation Services.

.. _innosrv: https://innovation.aalto.fi/contact-us/


Traps and acting early
~~~~~~~~~~~~~~~~~~~~~~
Intellectual property rights don't give you the right to do anything -
they give you the right to block others from doing something.  Thus,
it is very important that you don't end up in a situation where others
can block you, and that means *thinking early*.

Decide on a license as soon as possible.  Once it goes into the
repository, future contributors implicitly agree to it.  Otherwise,
you are stuck trying to find all past contributors and get their
agreement.

Another common trap is non-open source friendly grants.  Not many
outright ban it, but some require permission from *all* partners, and
if there are a lot then this becomes close to impossible.  Ask in
advance, but in the worst case it might be you just *can't* write
software at the times you are paid by these projects!


Step-by-step guide for release under this policy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Do these steps at the beginning of your project, not at the end!

#. Check if the work is covered under the "conditions for limited
   commercial potential" in the policy.

#. Choose a proper license to match your needs. See below for
   information. It must be open source, and you can *not* transfer any
   type of exclusive license away - Aalto keeps full right to future
   use.

#. Get the consent of all authors and their supervisors and/or funders. There are no
   particular requirements for this, the only need is proving it later
   in case a question ever arises. You should also make sure that your
   particular funding source/collaboration agreements don't have any
   further requirements on you. (For example, some grant agreements may
   say no GPL-type licenses without consent of all partners.) Your
   advisor (and Research and Innovation Services) can help you with
   this.

   If you are funded by Aalto basic funding, you by default have
   permission.  Same goes for other big public funding agencies
   (Academy, EU... but the grant can always override this).

   If you are in services, follow your source of funding.  At the very
   worst, whoever is responsible for your funding can decide, but it
   may be someone lower too.

#. You are responsible for making sure that you have the right to
   release your code. For example, that there are no other agreements
   other rights (intellectual property and privacy), legal
   restrictions, or anything else restricting a release. Also, any
   other included software must have compatible licenses.

#. Put a copyright license in the source repository. In the best case,
   each individual source file should list copyright and authors, but in
   practice if you don't do this it's not *too* much of a problem.
   Make sure that the license disclaims any warranty (almost all
   licenses will do this). After this, contributors implicitly
   consent to the license.  If you have an important case, ask
   explicitly too.  The important thing is that you have more evidence
   than the amount of scrutiny you might get (low in typical projects,
   will be higher if your project becomes more important).

#. This policy is seen as Aalto transferring the rights to you to
   release, not Aalto releasing itself (just the same as with
   publications). Release in your own name, but you can(+should) list
   your affiliations.

#. Make your code public if/when you want. No particular requirements
   here, but see below for best practices.

Any borderline or questionable cases should be handled by the existing
innovation disclosure process.

In addition to the above requirements, the following are best practices:

#. You can't require that people cite you, but you can ask nicely. Make
   it easy to do this! Include the proper citations directly in the
   README. Make your code itself also citeable by publishing it
   somewhere (Github, Zenodo, ...).

#. Put on a good hosting location and encourage contributions. For
   example, Github is the most popular these days, but there are plenty
   of others. Welcome contributions and bug reports, and build on them.
   Make yourself the hub of expertise of your knowledge and methods.

Choosing a license
~~~~~~~~~~~~~~~~~~

Under this policy, any `Creative
Commons <https://creativecommons.org/licenses/>`__, `Open Source
Initiative <https://opensource.org/licenses>`__, and `Free Software
Foundation <https://www.gnu.org/licenses/license-list.html>`__ approved
open source licenses are usable. However, you should *not* try to be
creative, and use the most common license that serves your needs.

Top-level recommendations:

#. Use this nice site: https://choosealicense.com/. It contains
   everything you need to know, including what is here. If you need
   something more specific you can have a look at http://oss-watch.ac.uk/apps/licdiff/.
#. **MIT** for software which should be basically public domain,
   **Apache 2.0** for larger almost-public domain things (the Apache
   license protects more against patent trolling). Anyone can
   use this for any purpose, including putting it in their own
   proprietary, non-open products.
#. **GNU General Public License (GPL)** ("v2 or any later version") for
   software which you may try to commercialize in the future. This
   license says that others can not make it closed-source without your
   consent. Others can use it for commercial purposes, but all
   derivative work must also be made open source - so you keep an
   advantage.

For special cases:

#. **Lesser GNU General Public License** (LGPL, GPL with classpath
   exception) type licenses. Suitable where the GPL would be appropriate
   but the software is a library. It can be embedded within other
   proprietary products, but the code itself must stay open.
#. The **Affero GPL/LGPL**. These get around the "webservice loophole":
   if your code is available via a webservice, the code running it must
   stay open.
#. **CC-BY** for other non-software output.

Discussion:

-  Most public domain → MIT / Apache 2 > CC-BY > LGPL > GPL > AGPL →
   Most protection against proprietary use
-  If you think you might want to commercialize in the future: **ask
   innovation services** and they'll help you release as open source now
   and preserve commercialization possibilities for the future.



The policy
~~~~~~~~~~
.. toctree::
   :hidden:

   opensource-policy


For clarity, :doc:`raw official text <opensource-policy>` is separate
from the guidance on this page. Current approvals: Department of
Computer Science (2017-03-17).





How to run a good open-source software project
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

One of the largest benefits to open source is having a community of
people contributing back to you.  To do this, you need to have a good
environment.  Open development, good style and a basic contribution
guide, and encouragement is the base of this.  Eventually, this
section may contain some more pointers to how to create this type of
community.  (TODO)

References
~~~~~~~~~~


-  Aalto Research Data Management Policy:
   \ `https://inside.aalto.fi/download/attachments/43223812/2016\_02\_10\_datapolicy.pdf?version=1&modificationDate=1455967763618&api=v2 <https://inside.aalto.fi/download/attachments/43223812/2016_02_10_datapolicy.pdf?version=1&modificationDate=1455967763618&api=v2>`__

-  Aalto IP guide: `FI <ipguidefi_>`_ `EN <ipguideen_>`_: contains
   evidence that this policy is applicable to all Aalto.

-  Aalto Innovation Services:
   \ `https://innovation.aalto.fi/ <https://innovation.aalto.fi/>`__

-  Choosing an open source license:
   \ `https://choosealicense.com/ <https://choosealicense.com/>`__

-  Aalto copyright advice:
   `http://copyright.aalto.fi/ <http://copyright.aalto.fi/>`__

-  Practical guidelines for Open Source Projects: forthcoming, 2017

.. _ipguidefi: https://inside.aalto.fi/display/firis/IPR-opas
.. _ipguideen: https://inside.aalto.fi/display/enris/IP+Guide






..
  Planning stuff below
  - -------------------

  Attachment:

  This is a request for feedback on an open source policy for the
  Department of Computer Science. The policy:

  -  Does not introduce any new obligations,
  -  Provides clear permissions and procedures for releasing work
     (publications, software, data) openly, should the worker and
     supervisor agree,
  -  Is designed to cover most of the simple cases, for complex cases it
     directs you to the proper university procedures.

  The reason for a policy is that even though within university
  administration are not sure who is required to give approval for opening
  works, even though everyone agreed that opening was good. Thus, we start
  from the bottom and work our way up. The following policy so far
  includes feedback from researchers, RIS legal staff, and RIS innovation
  advisors, so documents current best practices at the university.

  **Please provide feedback on this policy**. It is designed to cover all
  of the daily situations which researchers may encounter. Should you
  think of any situations which are not covered by the "limited commercial
  potential" clauses, please comment so that we can try to cover them.
  This policy includes some practical instructions, but will be
  supplemented by longer documents which go through all the practical
  steps that are needed to make good open source
  software/data/publications.

  Comments can go to richard.darst@aalto.fi or on this page. This page is
  temporary and will be deleted/archived after it is finished.

  Comments
  ~ ~~~~~~~

  -  Richard Darst: this is also written to cover publications, including
     to non-open places. Obviously, everyone publishes all the time,
     though so far university rules haven't made it explicit that you can
     sign rights away.
  -  Richard Darst: There is a difference between people with basic
     funding and external funding (the first does not need this policy
     because they have their own rights). Policy explains this.
  -  Richard Darst: Hopefully the policy can also be applicable to other
     departments and all of Aalto eventually. Comments from that
     perspective are welcome too.
  -  Richard Darst: What about recommending Apache license instead,
     instead of MIT? Apache has more protection against patent claims, and
     otherwise is similar.
  -  Contributor: But doesn't Aalto own all rights? (Answer: it heavily
     depends on how your own funding comes in, points 1 and 2 under the
     process try to explain it. It will be made more clear)
  -  Contributor: Make the "innovation process" more clear. In the text
     itself, it is very vague except for the link at the end. Add
     clarification.
