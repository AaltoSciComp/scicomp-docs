Requesting Science-IT department storage space
==============================================

Existing data groups and responsible contacts:

* CS: `Existing groups <https://wiki.aalto.fi/display/CSdept/Data+groups>`__
  and `CS-IT (guru) email here <http://do.cs.aalto.fi>`__
* NBE: `Existing groups <https://wiki.aalto.fi/display/NBE/Data+groups>`__ and
  `NBE IT (it-nbe) email here <https://wiki.aalto.fi/display/NBE/IT+Information>`__
* PHYS:
* Aalto: `Aalto IT servicedesk <https://www.aalto.fi/en/services/it-service-desk-contact-information-and-service-hours>`__



Requesting to be added to a group
---------------------------------

.. note::

   **CS department**: New!  Group owners/managers can add members to
   their groups self-service.  Go to https://domesti.cs.aalto.fi from
   Aalto networks, over VPN, or remote desktop at
   https://vdi.aalto.fi, and it should be obvious.

Send an email to the responsible department/IT services email address (see above) and **CC the
group owner or responsible person**.  An example message is below:

    Hi, I (account=ones1) would like to join the AD/unix group
    ``MY_PROJECT_NAME``.  I am aware that all data stored here is
    managed by the group's owner and have read the data management
    policies.

    I have cc:ed GROUP_MANAGER_NAME, who can reply with confirmation
    of adding me to the group.

Do you need access to Triton project scratch directories? If so, you
need a Triton account and you should :doc:`request it separately </triton/accounts>`.



Requesting a new group
----------------------

Send an email such as the below to the right contact address (mix and
match to make it suit your needs).  Include whichever paragraphs are
relevant to your needs.  The group owners should be long-term
(e.g. professor level) staff, but it can be requested by someone else
who cc:s the owner (please discuss some first):


    I would like to request a new project directory named
    ``coolproject`` on the [Triton scratch / XXX department project
    / Aalto teamwork] drive.

    We would like 200GB of storage space on the [CS department
    project / Triton scratch / etc.] filesystems


    I am the owner, but my postdoc Tiina Tekkari can also approve
    adding new members to the access group. / I am
    requesting this on behalf of my supervisor, who is cc:ed.


    [ Should I become unavailable, my colleague Anna Algorithmi
    (also a professor here) can provide advice on what to do with
    the data / Follow these special instructions: ... ]

    The initial people who have access should be:
    PROJECT_MEMBER_LIST

    This is for our day to day work in algorithms development, we
    don't expect anything surprising about this data.  There isn't
    any personal data here.



Requesting space on Triton if you are not in the School of Science
------------------------------------------------------------------

This is a little bit different since someone in the central IT
Services needs to make the group and then the Triton team needs to
allocate the storage.  Ideally, this is fast, but it's easy for
messages to get lost communicating between the teams (the wording
below is designed to prevent this).  Send to the `IT Servicedesk
address
<https://www.aalto.fi/en/services/it-service-desk-contact-information-and-service-hours>`__:

    Hi, could assign this to right IdM team to make new AD group with
    the name MY_PROJECT_NAME and include PROJECT_MEMBER_LIST in it?
    The owner of the group will be SPERVISOR_EMAIL.  This is needed
    for creating a project-based scratch directory on Triton.

    Then, can you assign this ticket to the Triton team so that they
    can create a scratch directory with AMOUNT_OF_STORAGE_SPACE space.
