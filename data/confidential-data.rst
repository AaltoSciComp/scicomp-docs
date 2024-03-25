Confidential data handling
==========================

Confidential data is data which has some legal reason to be
protected.



Confidential or sensitive data
------------------------------

.. note::

   The following description is written for the CS department, but
   applies almost equally to NBE and PHYS.  This is being expanded and
   generalized to other department as well.  Regardless of your
   department, these are good steps to follow for any confidential
   data at Aalto.

.. note::

   This meets the requirements for "Confidential" data, which covers
   most use cases.  If you have extreme requirements, you will need
   something more (but be careful about making custom solutions).

Aalto has some `guidelines for classification of confidential
information <https://www.aalto.fi/en/information-processing/classification-of-information>`__,
but they tend to deal with documents as opposed to practical guidelines
for research data. If you have data which needs special attention, you
should put it in a separate group and tell us when creating the
group.

The following paragraph is a "summary for proposals", which can be
used when the CS data security needs to be documented.  This is for
the CS department, but similar thing can be created for other
departments.  A longer description is also available.

    Aalto CS provides secure data storage for confidential data. This data
    is stored centrally in protected datacenters and is managed by dedicated
    staff. All access is through individual Aalto accounts, and all data is
    stored in group-specific directories with per-person access control.
    Access rights via groups is managed by IT, but data access is only
    provided upon request of the data owner. All data is made available only
    through secure, encrypted, and password-protected systems: it is
    impossible for any person to get data access without a currently active
    user account, password, and group access rights. Backups are made and
    also kept confidential. All data is securely deleted at the end of life.
    CS-IT provides training and consulting for confidential data management.

If you have confidential data at CS, follow these steps. CS-IT takes
responsibility that data managed this way is secure, and it is your
responsibility to follow CS-IT's rules. Otherwise you are on your own:

-  Request a new data folder in the project from CS-IT. Notify them that
   it will hold confidential data and any special considerations or
   requirements. Consider how fine-grained you would like the group: you
   can use an existing group, but consider how many people will have
   access.
-  Store data only in this directory on the network drive. It can be
   accessed from CS computers, see :doc:`data
   storage <aalto-details>`.
-  To access data from laptops (Aalto or your own), use :doc:`network drive
   mounting <remote-access>`, not copying. Also consider if
   temporary files: don't store intermediate work or let your programs
   save temporary files to your own computer.
-  Don't transfer the data to external media (USB drives, external hard
   drives, etc) or your own laptops or computers. Access over the
   network.
-  All data access should go through Aalto accounts. Don't send data to
   others and or create other access methods. Aalto accounts provide
   central auditing and access control.
-  Realize that you are responsible for the day to day management of
   data and using best practices. You are also responsible for ensuring
   that people who have access to the data follow this policy.
-  In principle, one can store data on laptops or external devices with
   full disk encryption. However, in this case we does not take
   responsibility unless you ask us first.you must ask us about this. In
   general it's best to try to adapt to the network drive workflow.
   (Laptop full disk encryption is a good idea anyway).

We can assist in creating more secure data systems, as can Aalto IT
security. It's probably more efficient to contact us first.



Personal data (research data about others, not about you)
---------------------------------------------------------

"Personal data" is any data concerning an identifiable person. Personal
data is very highly regulated (mainly by the Personal Data Act, soon by
the General Data Protection Regulation). Aalto has a `document that
describes what is needed to process personal data for
research <https://www.aalto.fi/en/services/how-to-handle-personal-data-in-research>`__,
which is basically a research-oriented summary of the Personal Data Act.
Depending on the type of project, approval from the `Research Ethics
Committee <https://inside.aalto.fi/display/AboutAalto/Research+Ethics+Committee>`__
may be needed (either for publication, or for human interaction. The
second one would not usually cover pure data analysis of existing data).
Personal data handling procedures are currently not very well defined at
Aalto, so you will need to use your judgment.

However, most research does not need data to be personally identifiable,
and thus research is made much simpler. Thus, you want to try to always
make sure that data is not identifiable, even to yourself using any
technique (anonymization). The legal requirement is "reasonable
likelihood of identification", which can include technical and
confidentiality measures, but in the end is still rather subjective.
Always anonymize before data arrives at Aalto, if possible. Let us know
when you have personal data, so we can make a note of it in the data
project.

However, should you need to use personal data, the process is not
excessively involved beyond what you might expect (informed consent,
ethics, but then a notification of personal data file). Contact us for
initial help in navigating the issues and RIS for full advice.



Boilerplate descriptions of security
------------------------------------

For grants, etc. you can find a description under :doc:`/about/for-proposals`
