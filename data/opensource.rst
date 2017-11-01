====================
Open Source at Aalto
====================

.. note::

   This policy was developed at the Department of Computer Science, in
   conjunction with experts from Research and Innovation services
   (both the legal and commercialization sides).  Then, we have heard
   that supposedly the `Aalto Research Data Management Policy
   <aaltordm_>`_ was supposed to have this same effect, however
   reading it it requires a lot of mental stretching to get to this
   point.  In fact, the RDM policy, if interpreted this way, would
   allow you to do essentially anything, including things which are
   not to the benefit of Aalto.

   Thus, while I (Richard Darst) can't promise anything, rumor has it
   this can be directly applied in all Aalto.  Unlike the Aalto
   policies, this provides the necessary guidance to make sure that
   you and Aalto's interests are protected.  If you are doing
   something that is beyond what is in this document, you probably
   want to talk to someone at Aalto anyway.

.. _aaltordm: http://www.aalto.fi/en/research/research_data_management/


This document describes the procedure for Aalto employees releasing the
output of their work openly (open source software, data, and
publications). Aalto University and CS encourage openness. This policy
covers only cases where work can clearly be released openly with no
bureaucracy needed. It does not cover complex cases, such as commercial
software, work related to inventions, complex partnership agreements,
etc. The policy is voluntary, and provides a right to release openly,
but does not require it or preclude any other university process. It
only is relevant when the creator has an employment relationship with
Aalto. If they don't (e.g. students), they own their own work unless
there is some other agreement in place (e.g. their own funding contract,
grant, etc).

Researchers make at least three primary outputs: publications, software,
and data. This policy aims to make openly releasing all types of work as
straightforward the traditional academic publishing process.

We realize that this policy does not cover all cases. We aim to cover
the 99% case, and existing processes are used for complicated cases.
Aalto Innovation Services provides advice on both commercialization and
open source release.

Why release?
~~~~~~~~~~~~

The more people who see and build on our work, the more impact we can
have. If this isn't enough, you get more citations and attention. While
we can't require anything, we strongly encourage that all work is either
made open source or taken through the commercialization process. If you
don't know what to do, don't worry: they are not mutually exclusive.
Proper open-source licensing can protect your ability to commercialize
later. Talk to Innovation services. They like open source, too, they
will help you find the right balance. Anyway, if work matches the
criteria in this policy, it probably has limited commercial potential
anyway: what is more important is your own knowledge and skills.

You want to add a proper open source license to your work, rather than
just putting code on some webpage. Without a license, others can not
build on your code, making your impact limited. No one will build on
you, and eventually your work rots.

You shouldn't release as open source (yet) if your work is intentionally
commercial or contains patentable inventions. In these cases, contact
innovation services. In the second case (patentable inventions),
according to Finnish legislation you are actually required to report the
invention to Innovation services.

Checklist for release under this policy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Check if the work is covered under the "conditions for limited
   commercial potential" in the policy.

#. Choose a proper license to match your needs. See below for
   information. It must be open source, and you can *not* transfer any
   type of exclusive license away - Aalto keeps full right to future
   use.

#. Get the consent of all authors and their supervisors. There are no
   particular requirements for this, the only need is proving it later
   in case a question ever arises. You should also make sure that your
   particular funding source/collaboration agreements don't have any
   further requirements on you. (For example, some grant agreements may
   say no GPL-type licenses without consent of all partners.) Your
   advisor (and Research and Innovation Services) can help you with
   this.

#. You are responsible for making sure that you have the right to
   release your code. For example, that any other included software has
   compatible licenses.

#. Put a copyright license in the source repository. In the best case,
   each individual source file should list copyright and authors, but in
   practice if you don't do this it's not *too* much of a problem.
   Almost all licenses will do this, but make sure that the license
   disclaims any warranty!

#. This policy is seen as Aalto transferring the rights to you to
   release, not Aalto releasing itself (just the same as with
   publications). Release in your own name, but you can(+should) list
   your affiliations.
#. Make your code public. No particular requirements here, but see below
   for best practices. (TODO)

Any borderline or questionable cases should be handled by the existing
innovation disclosure process.

In addition to the above requirements, the following are best practices:

#. You can't require that people cite you, but you can ask nicely. Make
   it easy to do this! Include the best citations directly in the
   README. Make your code itself also citeable by publishing it
   somewhere (github, zenodo, ...)

#. Put on a good hosting location and encourage contributions. For
   example, github is the most popular these days, but there are plenty
   of others. Welcome contributions and bug reports, and build on them.
   Make yourself the hub of expertise of your knowledge and methods.

Choosing a license
~~~~~~~~~~~~~~~~~~

(Under this policy, any `Creative
Commons <https://creativecommons.org/licenses/>`__, `Open Source
Initiative <https://opensource.org/licenses>`__, and `Free Software
Foundation <https://www.gnu.org/licenses/license-list.html>`__ approved
open source licenses are usable. However, you should *not* try to be
creative, and use the most common thing that serves your needs.)

Top-level recommendations:

#. Use this nice site: https://choosealicense.com/. It contains
   everything you need to know, including what is here.
#. **MIT** for software which should be basically public domain,
   **Apache 2.0** for larger almost-public domain things. Anyone can
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

-  Most public domain --> MIT / Apache 2 > CC-BY > LGPL > GPL > AGPL -->
   Most protection against proprietary use
-  If you think you might want to commercialize in the future: **ask
   innovation services** and they'll help you release as open source now
   and preserve commercialization possibilities for the future.

The policy
~~~~~~~~~~

TODO: proper link

This is a copy from the policy attached above, for convenience. See the
attachment for the official copy.

Covered work
^^^^^^^^^^^^

#. Software

#. Publications and other writing (Note that this policy simply
   formalizes the existing process where researchers have the right to
   publish their work, as an exception researchers are allowed to grant
   exclusive licenses to publishers. Open-access publishing is still
   preferred.)

#. Data

Conditions for limited commercial potential
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This policy supports the release of work with limited commercial
potential. Work with commercial potential should be assessed via Aalto’s
innovation process.

#. If work’s entire novelty is equally contained in academic
   publications, there is usually little commercial value. Examples:
   code implementing algorithms, data handling scripts.

#. Similarly, work which only is a byproduct of academic publications
   probably has limited commercial value, unless some other factor
   overrides. For example: analysis codes, blog posts, datasets, other
   communications.

#. Small products with limited independent value. If the time required
   to reproduce the work is small (one week or less), there is likely
   not commercial value. For example: sysadmin scripts, analysis codes,
   etc. Think about the time for someone else to reproduce the work
   given what you are publishing, not the time it took for you to create
   it.

#. Should a work be contributing to an existing open project, there is
   probably little commercial value. For example: contribution to
   existing open-source software, Wikipedia edits, etc.

#. NOT INCLUDED: Should work contain patentable elements or have
   commercial potential, this policy does not apply and it should be
   evaluated according to the Aalto innovation process. Patentable
   discoveries are anything which is a truly new, non-obvious, useful
   inventions. In case of doubt, always contact Innovation Services!
   Indicators for this category: actually novel, non-obvious, useful,
   and actually an invention. Algorithms and math usually do not count,
   but expressions of these can.

#. NOT INCLUDED: Software designed for mass-market consumption or
   business-to-business use should be evaluated according to the Aalto
   innovation process. Indicators for this category: large amount of
   effort, software being a primary output.

Ownership of intellectual property rights at Aalto
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. This policy covers work of employees whose contracts assign copyright
   and other intellectual property rights of their work to Aalto.
   However, determining this can be difficult. This policy is designed
   to be applicable to all work, regardless of the ownership.

#. Your rights are assigned to Aalto if you are funded by external
   funding, or if there are other Aalto agreements regarding your work.

#. If neither of the points in (2) apply to you AND your work is
   independent (self-decided and directed), then according to Finnish
   law you own all rights to your own work. You may release it how you
   please, and the rest of this policy does NOT apply (but we recommend
   reading it anyway for valuable advice). Aalto Innovation Services can
   serve you anyway.

#. Rather than figure out the the ownership of work, this policy can
   also be applied to all work.

Release criteria and process
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. This policy applies to copyright only, not other forms of
   intellectual property. Should a work contain other intellectual
   property (which would not be published academically), this policy
   does not apply. In particular, this policy does not cover any work
   which contains patentable inventions.

#. The employee and supervisor must consider commercial potential. The
   guidelines in the “conditions for limited commercial potential” may
   guide you. Should there be commercial potential, go through the
   existing innovation disclosure processes. In particular, any work
   which may cover patentable inventions must be reported first.

#. If all conditions are satisfied, you, in consultation with your
   supervisor or project leader, may choose to release the work. Should
   the supervisor or PI have a conflict of interest or possible conflict
   of interest, their supervisor should also be consulted.

#. Depending on funding sources, you may have more restrictions on
   licensing and releasing as open source. Project proposals and grant
   agreements may contain provisions relevant to releasing work openly.
   When making project proposals, consider these topics already. When in
   doubt, contact the relevant staff.

#. To be covered under this policy, work must be licensed under a
   open/open source/free software license. In case of doubt, Creative
   Commons, Open Source Initiative, and Free Software Foundation
   approved open source licenses are considered acceptable. See below
   for some license recommendations.

#. All warranty must be disclaimed. The easiest way of doing this is by
   choosing an appropriate license. Practically all of them disclaim
   warranty.

#. All authors must consent to the release terms.

#. The employee should not transfer an exclusive license or ownership to
   a third party. Aalto maintains the right to relicense and use
   internally, commercially, or re-license should circumstances change.

#. Employees should acknowledge their Aalto affiliation, if this
   possible and within the community norms.

#. This right should not be considered Aalto officially releasing any
   work, but allowing the creators to release it in their own name.
   Thus, Aalto does not assume liability or responsibility for work
   released in this way. Copyright owner/releaser should be listed as
   the actual authors.

#. Employees are responsible for ensuring that they have the right to
   license their work as open source, for example ensuring that all
   included software and data is compatible with this license and that
   they have permission of all authors. Also the release must be allowed
   by any relevant project agreements. Should you have any doubts or
   concern, contact Innovation Services.

| To apply this to your work, first receive any necessary permissions.
  In writing, by email, is sufficient. Apply the license in your name,
  but list Aalto University as an affiliation somewhere that makes
  sense. Do not claim any special Aalto approval for your work.

How to run a good software project
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

TODO

References
~~~~~~~~~~

-  Practical guidelines for Open Source: forthcoming, 2017

-  Choosing an open source license:
   \ `http://choosealicense.com/ <http://choosealicense.com/>`__

-  Aalto Innovation Services:
   \ `http://innovation.aalto.fi/ <http://innovation.aalto.fi/>`__

-  Aalto Research Data Management Policy:
   \ `https://inside.aalto.fi/download/attachments/43223812/2016\_02\_10\_datapolicy.pdf?version=1&modificationDate=1455967763618&api=v2 <https://inside.aalto.fi/download/attachments/43223812/2016_02_10_datapolicy.pdf?version=1&modificationDate=1455967763618&api=v2>`__

-  Aalto copyright advice:
   `http://copyright.aalto.fi/ <http://copyright.aalto.fi/>`__

-  Aalto IP guide: forthcoming, 2017

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
