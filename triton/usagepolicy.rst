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
   or misuse of Triton cluster or credentials to the `cluster support
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



Triton metadata policies
------------------------

In this section, we describe the use of personal data on Triton.  In
this context, "personal data" refers to administrative metadata about
users and cluster usage.

Triton does not store basic account information. Only username and uid
are stored within Triton, and actual account information is provided
by Aalto ITS.  We do not consider Triton to hold a personal data file,
but for full disclosure we describe the data we do hold.

*Note about research data*: This section does not cover any data which
users store on the cluster: for that, the user is the controller and
Science-IT is only a processor.  Terms are listed under the storage
pages.


Controller and contact
~~~~~~~~~~~~~~~~~~~~~~
*Controller*: Aalto Science-IT, Aalto University, Espoo, Finland.
`Contact information <help>`_.  Please use the support email alias for
account and personal data queries.

Account information comes from `Aalto ITS registers
<https://inside.aalto.fi/display/ITPK/Rekisteriselosteet>`__.

The purpose for processing the personal data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Data is processed and stored in accordance with our agreement to
provide a HPC cluster service, in accordance with the usage agreement.
The cluster may only be used to support Aalto (not personal)
activities, and all usage metadata represents Aalto activities and is
owned by Aalto University.

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
and directory information is provide by Aalto University, and in
general not stored or processed here.

Data sharing
~~~~~~~~~~~~
Data may be used for internal Aalto reporting and accounting (usually
but not always aggregated at the cost center level), and used in
non-identifiable forms in public reports and statistics.  It may also
be shared as needed to investigate usage problems.

All users of the cluster may inspect the usage information and job
statistics of the entire cluster (including all other users).

Timeframe
~~~~~~~~~
Data related to usage remains as long as the user has an active Triton
account.  Technical logging data allows accounting and reporting, and
may be kept indefinitely.  Where possible, this may be in anonymous
form.


Legal notices
~~~~~~~~~~~~~
Data is stored in Finland in Aalto or CSC data centers.  Access is
only via Aalto account.  Data is not transmitted outside of Finland.

You may request rectification of your data.  However, most data is
technical logging information which can not be removed.  You may cease
using the cluster, remove your research data, and request your account
be closed.  Should technical errors in data be identified, a bug
should be reported.

You may access and extract your own data using the standard interfaces
described in the user guide.

You may lodge a complaint with the Aalto data protection officer (link
TODO) or the Finnish supervision authority `Tietosuoja
<http://www.tietosuoja.fi/>`__.



Research and home data stored on cluster
----------------------------------------

We provide a storage service for for data stored on the cluster.  For
full disclosure, the following are our rules for access of this data:

* We do not look into private files without your consent.

* If your files are made cluster-readable (`chmod` "other"
  permissions), we may look at contents.  Note that this is not the
  default setting.

* Should you report a problem, we may run `stat` as superuser on
  relevant files to determine basic metadata without further checks.

* Should you have a problem that requires us to look at the contents
  of files or directories, we must first have your explicit permission
  (either in writing or in person)

Our data storage service is suitable for confidential data.  You must
ensure that permissions are such that technical access is limited.
