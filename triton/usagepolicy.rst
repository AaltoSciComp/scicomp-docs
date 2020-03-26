Usage policies and legal
========================

Acceptable Use Policy and Terms of Service
------------------------------------------

By using the Triton cluster resources, you shall be deemed to accept
these conditions of use:

#. You shall only use Triton cluster to perform work, or transmit or
   store data consistent with the stated goals and policies of Aalto
   University and in compliance with these conditions of use.

#. You shall not use Triton cluster for any unlawful purpose and not
   (attempt to) breach or circumvent any administrative or security
   controls. You shall respect copyright and confidentiality
   agreements and protect your credentials (e.g. user login name,
   password, ssh private key), sensitive data and files.

#. You shall immediately report any known or suspected security breach
   or misuse of Triton cluster or credentials to the :doc:`cluster support
   team <help>`.

#. Use of the cluster is at your own risk. There is no guarantee that
   the cluster will be available at any time or that it will suit any
   purpose.

#. Logged information, including information provided by you for
   registration purposes, shall be used for administrative,
   operational, accounting, monitoring and security purposes
   only in accordance with the policy below.
   This information may be disclosed to other organizations
   anywhere in the world for these purposes in the extent allowed by
   local laws. Although efforts are made to maintain confidentiality,
   no guarantees are given.

#. The cluster support team is entitled to regulate and terminate
   access for administrative, operational and security purposes and
   you shall immediately comply with their instructions.

#. You are liable for the consequences of any violation by you of
   these conditions of use.

#. You agree to explicitly mention and acknowledge the use of
   Science-IT resources in your work in any reports, workshops, papers
   or similar that result from such usage. Appropriate reference can
   be found at `Acknowledgement of Triton usage
   <acknowledgingtriton>`.


.. _privacypolicy:

Triton data (privacy) policy
----------------------------

Triton is a part of Aalto University IT systems, thus is fundamentally
governed by the Aalto Privacy Policy for Employees or Privacy Policy
for Students, the `latest versions of which can always be found on
aalto.fi <https://www.aalto.fi/services/privacy-notices>`__.

For clarity, in this section, we describe the special cases of Triton
data:

In summary:

* The **Triton account** is not a separate account, it is part of the
  Aalto account.  We do not control that.
* **Triton usage statistics and logs.**  Triton is used for university
  academic research only, so this information may be used for
  reporting and management in any way.  Identifying information won't
  be public, but note that it will be used for internal operations and
  contacting users as needed.
* **Data stored on Triton.**  We are not the controller of this data.
  Data in your personal directories is controlled by you, and data in
  shared directories is controlled by the manager of that group.  See
  the :ref:`section below <tritondata>` for more information on this data.
* **HAKA login data** (JupyterHub only).  This is used to secure
  access to JupyterHub.  Only your Aalto account name is requested, it
  is compared and immediately discarded (Triton is already linked to
  your Aalto account).
* **The triton-users mailing list** is automatically formed from all
  Aalto accounts in the triton-users group (everyone with an
  account).  This is used to send service announcement and information
  related to scientific computing.  This subscription is intrinsically
  tied to the Triton account and a requirement of the cluster usage.
  (Email information held by Aalto IT services).

We do not consider the Triton management data to consist of a personal
data file (this is covered under Aalto policies), but for full
disclosure we describe our use of data.

*Note about research data*: This section does not cover any data which
users store on the cluster: for that, the user is the controller and
Science-IT is only a processor.  You are responsible for any
administrative privacy matters.  The following subsections relate only
to administrative metadata.


Controller and contact
~~~~~~~~~~~~~~~~~~~~~~
*Controller*: Aalto Science-IT, Aalto University, Espoo, Finland.
:doc:`Contact information <help>`.  Please use the support email alias for
account and personal data queries.

Account information comes from `Aalto ITS registers
<https://www.aalto.fi/en/services/privacy-notices>`__.

The purpose for processing the personal data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Data is processed and stored in accordance with our agreement to
provide a HPC cluster service including accounting and reporting, in
accordance with the usage agreement.  The cluster may only be used to
support Aalto (not personal) activities, and all thus usage metadata
represents Aalto activities and is owned by Aalto University.

Types of data
~~~~~~~~~~~~~
Triton stores the information necessary for provision of its services,
including accounting, funding, and security.  This includes logs of
all operations and metadata of stored data.  Data is only generated
when a users uses the cluster.  For example (including but not limited
to):

* Connection logs
* Job submission and statistics logs
* Filesystem and storage metadata and logs

Uses of data
~~~~~~~~~~~~
Data is used in the provision of the HPC cluster service.  Primarily,
this is through accounting, reporting, and scheduling of tasks.
Historical data will automatically adjust future cluster priority.

Sources of information
~~~~~~~~~~~~~~~~~~~~~~
Data is produced during the use of Triton for research purposes.  This
data is generated directly by users while using the cluster.  Account
information is provide by Aalto University, and in general not stored
or processed here.

Data sharing
~~~~~~~~~~~~
Data may be used for internal Aalto reporting and accounting (usually
but not always aggregated at least at the group level), and used in
non-identifiable forms in public reports and statistics.  It may also
be used as needed to investigate usage matters.

All users of the cluster may inspect the usage information and job
statistics of the entire cluster (including all other users).

Timeframe
~~~~~~~~~
Data related to usage remains as long as the user has an active Triton
account.  Technical logging data allows accounting and reporting, and
may be kept as long as needed for security and reporting purposes
(indefinitely).  Where possible, this may be in anonymous form.

Legal notices
~~~~~~~~~~~~~
Data is stored in Finland in Aalto or CSC approved facilities.  Access
is only via Aalto account.

You may request rectification of your data.  However, most data is
technical logging information which can not be removed or changed.

You may cease using the cluster, remove your research data, and
request your account be closed (this does not close your Aalto account
because we do not control that), but historical usage data will remain
for accounting purposes.  Should technical errors in data be
identified, a bug should be reported.

You may access and extract your own data using the standard interfaces
described in the user guide.

Identifiable administrative metadata and accounting data is not
transferred outside of the EU/EEA except under proper agreement.  (We
have to say that, but in reality identifiable data is never
transferred out of Aalto or maybe the FGCI consortium in Finland).

You may lodge a complaint with the Aalto data protection officer (see
Aalto privacy notices for up to date contact information) or the
Finnish supervision authority `Tietosuoja
<http://www.tietosuoja.fi/>`__.



.. _tritondata:

Research and home data stored on cluster
----------------------------------------

We provide a storage service for for data stored on the cluster
(scratch and home directories):

Our responsibility is limited to keeping this data secure and
providing access to the corresponding Aalto accounts.  The shared
directory manager should be able to make choices about data.  We do
not access this data except with an explicit request, but for
management purpose we do use the file metadata (``stat $filename``).
For full information, see the :doc:`Science-IT data policy
<../aalto/datapolicy>`.

* We do not look into private files without your explicit request (if
  you want help with something, explicitly tell us if we can look at
  them).

* If your files are made cluster-readable (the ``chmod`` "other"
  permissions), you give permission for others to look at contents.
  Note that this is not the default setting.

* Should you report a problem, we may run ``stat`` as superuser on
  relevant files to determine basic metadata without further checks.

* Should you have a problem that requires us to look at the contents
  of files or directories, we must first have your explicit permission
  (either in writing or in person)

Our data storage service is suitable for confidential data.  You must
ensure that permissions are such that technical access is limited.
