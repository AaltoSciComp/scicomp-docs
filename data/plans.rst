=====================
Data management plans
=====================

Data management plans are a catchphrase these days, mainly because
funders are requiring them now.  This is for a good reason -
researchers often focus on their papers, and making good use of the
data gets forgotten.  Funders pay a lot for research, and they want
*all* the possible value for society.

However, it *is* worth doing a bit of planning about data, even aside
from the required bureaucratic exercise.  It is true that researches
focus on the next paper.  Data has long-term value even inside Aalto,
and if you don't try hard it will get lost.

Actual plan
===========

In this section, we outline recommend ways to use Aalto resources for
different use cases.

No matter what your project, you want to start by thinking how you
will handle your data (this can be "real data", notes, code, papers,
etc).  This will make sure that your team works together well and
doesn't end up with a big mess in a few months - or that you can't
work together because you can't share information.  For this, see the
`A4 DMP template <dmpA4_>`_.  This site is focused on practical DMPs.

.. _dmpA4: https://drive.google.com/drive/u/0/folders/0BzlGN0F6ew2hc0hGVXVTaGZwQjQ

* Suggested DMP for large experimental data (TODO)
* Suggested DMP for simulations or computer-generated data (TODO)
* Suggested DMP for data from humans (surveys, interviews, etc)
  (TODO)



Funder plan
===========

There are plenty of other good resources about making funder DMPs.

* At Aalto, the RIS grantwriters have taken responsibility for helping
  to make good funder DMPs.

* The Aalto RDM pages have a subsection dedicated to `data management
  plans <aaltordm_>`_.

* The `DMPTuuli <https://www.dmptuuli.fi/>`_ is a combination
  template, instructions, and web form which makes it easy to do the
  mechanical assembly of DMPs.  They also have `public docx/pdf
  templates <dmptuuli_templates_>`_ which can be used even without the
  web form.  Aalto recommends this service, though be aware it helps
  you fill out a form, not plan your work.

.. _aaltordm: https://www.aalto.fi/en/services/data-management-plan-dmp

As some concrete suggestions:

* Funders are especially concerned about sharing, preservation,
  reproducibility, and
  dissemination but probably can't evaluate too much about the
  practical side of things.

* You can mention that you will follow the `Aalto RDM policy
  <aaltordm_>`_, which covers mainly opening and licensing.  The policy
  still allows you to make your own choices, but it sounds quite good
  if you refer to it and say you will follow it.

* For data storage considerations, you can say that your
  department/Science-IT provides data storage services (for Science-IT
  departments) and has a data storage policy which you will follow:
  :doc:`citation <outline>` and/or :doc:`full text <datapolicy>`.


.. _dmp-emergency:


Help!  I need a DMP right now!
==============================

If you are reading this, you probably have a grant deadline and you
need to do something *right now*.  Use the resources above, but here
is some more advice:

* Read the :doc:`data management outline <../aalto/aaltodata>` on this
  site.  You should be able to pull many of the practical pieces
  (storage, confidentiality, archiving, etc) from here.  **Read this
  first!**.

* Read the `Aalto-level guidelines <aalto_rdm_plans_>`_.  These are
  quite abstract and high level, and might tell you what people think
  is important but not tell you how to do stuff.

* To internally organize things, you could start with the `A4 DMP template
  <dmpA4_>`_.  This can't be used for something you submit, but lets
  you know the big picture.  If you fill this out first and give it to
  someone, they can guide you in making the next version.

* Use the `DMP Tuuli <https://www.dmptuuli.fi/>`_ tool to prepare the
  DMP.  It just makes a final document you can download (you could do
  the same using a word processor), but breaks everything down into a
  nice form.

  * If you don't like the idea of a web form, the `templates seem to be
    available publically <dmptuuli_templates_>`_, too.  These seem to
    have roughly the info as the DMPTuuli web forms.

.. _aalto_rdm_plans: https://www.aalto.fi/en/services/data-management-plan-dmp
.. _dmptuuli_templates: https://dmptuuli.fi/public_templates/

Why do they want DMPs?  What should it include?  Answering these will
help you to know what to write, since there is not near enough room to
make a plan that contains everything *you* need to know personally.:

* The main purpose is to make sure that other researchers can use your
  data as easily as they can use your published papers.  Can other
  researchers access your data?  Can your results be reproduced?

* Most likely, whoever is reading doesn't care *that* much about the
  actual day to day data storage and so on, but more of the big
  picture: licensing, opening, archiving, sharing, preserving,
  expanding, securing.

* If you produce your own data, how can others use it?  Funders want
  open, but by giving good justification you can do whatever you need.
  If the data comes from others, then can you re-distribute (even for
  validation) or would others need to request it from the source?

* How software you make related to data processing (and really all
  software) will be handled.  Even if data can't be released, software
  can be open sourced which allows reproduction of results and some
  sort of validation.

* How you preserve data for future use: both for you, and for others.
  This is especially important.  Also, how will data be
  *understandable* in 50 years?  Is the program that will read it
  gone?  Do you have a README?  Is your data in a field-specific
  standard structured format?  Is it opened and does it go into an
  archive which will be around in 50-100 years (anything managed by
  you or Aalto specific isn't a credible option for this)?

* You should mention how you will follow the "Aalto Research Data
  Management Policy and related guidance".  The policy just says "you
  will make strategic decisions", so sounds good to the funder while
  not binding you to anything.

* For storage, organization, confidentiality, etc, you can say you
  will follow the Science-IT data management policy.  This isn't
  requirements for you, but the default services we offer for data
  storage (designed to keep data safe and secure, and uuushareable).  It
  also sounds good to say.  (see the :doc:`outline <../aalto/aaltodata>`)


Model Academy of Finland DMP
============================

You can see the Academy's detailed info `in their supplement
<oafg_>`_.  This guide isn't to replace their guidelines (there is a
lot there that isn't duplicated here), but make it clear what the
Aalto correspondences are.  You can also see the `Aalto guidelines
<ardm_plan_>`_, but this is also a bit abstract to be immediately
usable.

.. _oafg: https://www.aka.fi/en/funding/apply-for-funding/az-index-of-application-guidelines/data-management-plan/data-management-plan/

.. _ardm_plan: https://www.aalto.fi/en/services/data-management-plan-dmp

With all the time spent on writing your plan, don't forget to do
something useful, too.

1. General description of the data

   - No specific extra advice here - see academy guidelines.

2. Ethical and legal compliance

   - For identifiable human data, say that you will follow the `Aalto
     personal data policy <apdp_>`_.  In particular, data will only be
     stored only on systems meeting the Aalto guidelines for personal
     data storage.  Preferable, store this on the department network
     drives only - not on personal computers.  You can request ethical
     evaluation from the `Aalto Research Ethics Committee <arec_>`_.
     Is Finland, this is required in quite few cases, but publishers
     are requiring this more and more often.  Thus, you may want to
     check your journal requirements and request ethical evaluation
     anyway.

   - Data always will be made available under the `Aalto data
     management policy <aodp_>`_.  (You can commit to this, because
     the policy only says you should make decisions "strategically" so
     there are actually no obligations.)


   - Software will be made open source if it matches the criteria under the :doc:`Aalto open source
     policy <../aalto/opensource>`.  If software exceeds that
     criteria, there will be discussions with Aalto innovation
     services for commercialization or licensing.

   - There are plenty of other intellectual property concerns which I
     can't go into here, and you need to study yourself.  Aalto
     Research and Innovation Services has lawyers which can help with
     this - you can consult in advance or say you will use them.

3. Documentation and metadata

   - It is harder to comment on this because it is so field-specific.
     Make sure you have READMEs and documents.

   - Everyone talks about "metadata" but this is such a broad term
     that it is essentially meaningless.  I personally put this into
     three types:

     - Cataloging: You can say that the metadata required by your
       repository will be used.

     - Necessary to understand: you will use README files, use formats
       that are self-describing such as CSV files with useful headers
       and comments, include code, and whatever is needed to make
       someone understand the data later (including yourself).

     - Necessary to automatically process: data should be
       automatically usable with the least amount of manual effort.
       This is highly domain-specific, and depends on if your domain
       already has standards to make this possible.  Use the best
       possible practices here, taking into account cost vs benefit.


4. Storage and backup during the research project.

   - Aalto really excels here.  Basically, just use the :doc:`Aalto
     network drives <../aalto/aaltodata>`.  This storage is large,
     free, shareable, snapshotted, backed up to an offsite
     datacenter.  Access is controlled via Aalto accounts plus unix
     groups.  If people need to make other copies (and it's allowed
     for security reasons), they can.  Big data is stored on
     :doc:`/triton/index` from which it has direct access to any
     computational power you may need.

5. Opening, publishing, and archiving the data after the research
   project.

   - This gets more abstract, and really depends on what you want.
     There are many options, and maybe it is best to consult the
     `Aalto page on this <ardm_pub_>`_, though it's again rather
     abstract.

   - You can check the :doc:`services page <services>` to see what
     common services are available.  If you don't have any more
     specialized repository to use, Zenodo is a good choice.  Always
     prefer a specialized, domain-specific repository if you can.
     Don't say it is archived on Aalto resources, since you or Aalto
     can't commit to hosting things or the long term.

   - You can say that organization of data is a part of research,
     though the extra requirements needed to open are small.  Give
     some estimate of the total/extra amount of work needed.

.. _apdp: https://www.aalto.fi/en/services/aalto-university-data-protection-policy

.. _arec: https://www.aalto.fi/en/services/research-ethics-committee

.. _aodp: https://inside.aalto.fi/download/attachments/50234575/2016_02_10_datapolicy.pdf?version=1&modificationDate=1455967763618&api=v2

.. _ardm_pub: https://www.aalto.fi/en/services/publishing-and-reusing-open-data
