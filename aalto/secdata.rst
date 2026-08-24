=======
SECDATA
=======

.. seealso::

   * Official service page: `Secure operating environment for sensitive
     data <https://www.aalto.fi/en/services/secure-operating-environment-for-sensitive-data>`__
   * Official user guide: `User guide to secure operating environment
     for health and social data <https://www.aalto.fi/en/services/user-guide-to-secure-operating-environment-for-health-and-social-data>`__
   * Request / admin contact: secdata@aalto.fi
   * Container background: `CodeRefinery: computational
     environments <https://coderefinery.github.io/reproducible-research/environments/>`__
     and :doc:`/triton/usage/singularity`
   * :doc:`Confidential data at Aalto </data/confidential-data>`
   * Aalto `classification of
     information <https://www.aalto.fi/en/cyber-security/classification-of-information-basic-instructions-and-services>`__

**SECDATA** is Aalto's dedicated secure computing environment for
**secret** research data (the highest Aalto classification), including
secondary-use health and social data.  It is a virtual Ubuntu desktop
with a network filesystem that is only available from that system.
GPUs are available.  Most software is brought in as
:doc:`Singularity/Apptainer containers </triton/usage/singularity>`.

Legal requirements mean that **data transfer and software installation
are done only by admins**.  Structure your work so that you transfer
as little as possible.

To request an environment, write to **secdata@aalto.fi**.  Aalto
Scientific Computing (Data Agents and :doc:`AaltoRSE </rse/index>`)
can help you decide whether you need SECDATA, use the environment, and
build containers.  Come to the :doc:`SciComp garage </help/garage>`
with your goal and links to the software instructions you want to
follow — we can build the container with you, or even build it for
you.

.. highlight:: console


When to use SECDATA
-------------------

Use SECDATA when the data is **actually secret**: required by
legislation (for example secondary-use health data with a Findata
permit), a DPIA that calls for strong isolation, or another high-risk
case where tightly controlled transfers are desirable.

It is **not** a good fit when:

* Ordinary **confidential** data is enough (this is most research
  data, including typical personal data).  Confidential systems used
  properly — Teamwork, department project directories, Triton, Aalto
  managed workstations — are the right default.  See
  :doc:`/data/confidential-data` and :doc:`/scicomp/rcr-scicomp`.
* **SECWORK** or encrypted files on Teamwork already cover the need.
* You are **generating a lot of new data** (getting results out is
  slow, because admins must move every transfer).
* You need **Windows**.  SECDATA is Ubuntu only.
* Sensitive content is **not asked for or expected**, but might come
  up (for example qualitative interviews on a non-health topic).
  Clean or code the data at the start; leftover raw material can sit
  in SECWORK, or be encrypted on Teamwork.
* You could **pseudonymise or encrypt a single file** as soon as you
  receive it, and then work on a confidential system.

**Data management plans:** mention SECDATA only in plans that will
really use it (health/secondary-use data, or other data classified
secret).  Do not list it "just in case" for projects where sensitive
topics might appear but are not the focus — SECWORK is more
appropriate, and the transfer process is too heavy for that.

Over-classifying data is common and costly.  Researchers usually have
a hunch about how likely a study is to contain secret data.  If you
are unsure, talk to a Data Agent or come to the garage **before**
requesting SECDATA.


How the environment works
-------------------------

Each project gets a dedicated virtual desktop (Ubuntu Linux), accessed
with VMware Horizon at https://finvdi.aalto.fi (from the
:ref:`Aalto VPN <aalto_vpn>`).  Multi-factor authentication is
required.  Access is restricted to Finland by default.  Collaboration
partners need an Aalto visitor account.

Inside the instance, work happens on a network filesystem that exists
only there.  Typical layout after admins have moved files in:

* **Source data** (read-only): ``/nfs/data`` (sometimes
  ``/nfs/data/source``)
* **Incoming code / containers**: ``/nfs/incoming``
* **Your working area**: ``/nfs/home/username``

There is no public internet from the desktop.  You cannot install
packages with ``apt``, ``pip``, or ``conda`` on the live system in the
usual way.  Put the software in a container **before** it is uploaded.

SECDATA is a Valvira-registered environment for secondary use of
health and social data (see the `Valvira
registry <https://valvira.fi/sosiaali-ja-terveydenhuolto/toisiokayttoymparistojen-rekisteri>`__).
For Aalto researchers it is one of the few such environments with
**GPUs** (Findata Kapseli and CSC SD Desktop do not provide them).
Findata's primary environment is still Kapseli: using SECDATA for
Findata-permit work needs Findata's approval and a justification in
the permit application.


Who does what
-------------

**Aalto ITS** does the technical administration: monitoring, accounts,
hardware, and every data transfer in or out.

**You** plan the analysis, prepare software as containers, work inside
the VDI, and ask ITS when something must be moved.

**Data Agents and AaltoRSE** help with: is SECDATA actually needed;
how to structure the project; building and testing Singularity
containers; Jupyter / Python / R workflows.

Develop and test methods **outside** SECDATA with non-secret test
data.  Only move into SECDATA once the tools and scripts work.


Containers (how software gets in)
---------------------------------

A container is a whole computer in one file, so it can be copied into
SECDATA as a single transfer.  You write a **recipe** (a Singularity /
Apptainer definition file) that describes the operating system and
packages.  Building that recipe produces a ``.sif`` image.  That image
is what admins move in.

This is the practical way to get Python, R, Jupyter, and most research
software into SECDATA.  Some packages may already be on the Ubuntu
desktop, but do not rely on installing more yourself.

Background:

* `CodeRefinery: computational
  environments <https://coderefinery.github.io/reproducible-research/environments/>`__
* :doc:`Singularity/Apptainer on Triton </triton/usage/singularity>`
* Example cases: https://github.com/AaltoSciComp/secure-workflows


Practical workflow
------------------

The steps below follow a typical Python / Jupyter analysis.  Replace
names (instance, project folder, packages) with your own.  Official
limits still apply: only admins move data in or out.

A. Prepare the container outside SECDATA
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Work on a normal Aalto Linux workstation or Triton, with
**non-secret** test data.

Create a Conda environment file ``environment.yml``.  List the
packages you actually need; this is only a sketch:

.. code-block:: yaml

   name: myproject
   channels:
     - conda-forge
   dependencies:
     - python=3.11
     - jupyterlab
     - numpy
     - pandas
     - matplotlib
     - pip
     - pip:
       - pydeface

Create a Singularity definition file ``conda.def``:

.. code-block:: singularity

   Bootstrap: docker
   From: continuumio/miniconda3:4.10.3-alpine

   %files
     environment.yml

   %post
     # https://github.com/ContinuumIO/docker-images/issues/151
     mkdir /opt/conda/pkgs
     touch /opt/conda/pkgs/urls.txt
     ENV_NAME=$(head -1 environment.yml | cut -d' ' -f2)
     conda env create -f environment.yml -p /opt/conda/envs/$ENV_NAME
     conda clean --all

   %environment
     export LC_ALL=C

   %runscript
     exec "$@"

Build the image (root is often required; Apptainer can also build
without root in some setups)::

   $ sudo singularity build conda.sif conda.def

Test the image locally with dummy data until Jupyter and your scripts
run.  Then put the image, code, and **only the files that must go in**
into one folder and upload them to the SECDATA incoming share (ITS
will tell you the instance name, here ``INSTANCE``).  Connect and
upload from the folder that contains your files::

   $ cd FOLDER
   $ smbclient -k //teamwork/secdata
   smb: \> cd INSTANCE
   smb: \> cd incoming

To transfer a **single file** (for example the container image)::

   smb: \> put my_file.sif

To transfer a **whole folder** (all files in ``FOLDER``)::

   smb: \> recurse ON
   smb: \> mput *

B. Admins move files into the instance
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ask ITS (secdata@aalto.fi) to import the upload.  They place data and
code into the instance: data read-only under ``/nfs/data``, code and
the container under ``/nfs/incoming``.

Connect with **VMware Horizon Client** to https://finvdi.aalto.fi
(Aalto VPN), authenticate, and start your instance.

Open a terminal and create a working project folder (adjust user and
instance names)::

   $ cd /nfs/home
   $ mkdir project
   $ chown YOURUSERNAME:INSTANCENAME project
   $ chmod 770 project

C. Work with the data and the container
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Copy incoming material into your project (source data stays read-only
in ``/nfs/data``; this copy is what you write alongside)::

   $ cd /nfs/home/project
   $ mkdir code
   $ cp -r /nfs/incoming/. code/
   $ mkdir data
   $ cp -r /nfs/data/. data/

If the data was zipped, tarred, or password-encrypted, extract it
here.

Start the container and JupyterLab::

   $ cd /nfs/home/project/code
   $ singularity shell -B /nfs --no-home ./conda.sif
   $ conda env list
   $ source activate myproject
   $ jupyter-lab

Jupyter prints a local URL, for example
``https://localhost:8888/lab?token=...``.  Open **Firefox inside the
VDI** and paste that URL.  There is no need (and no way) to open that
port from your own laptop.

You can also run scripts already baked into the image instead of
Jupyter; the Jupyter path is the usual way to prototype.

D. Get results out
~~~~~~~~~~~~~~~~~~

You cannot copy files out yourself.  Ask ITS (secdata@aalto.fi) to
export the specific results you need.  Plan for this delay: keep
exports small and infrequent.


Related: sending secret data on ordinary services
-------------------------------------------------

Secret data that is **not** inside SECDATA must be encrypted on a
system rated for secret before it touches ordinary tools.

* **Send:** on SECWORK, encrypt → send with OneDrive or Funet
  FileSender.
* **Receive:** download the encrypted file from OneDrive or Funet
  FileSender → save to SECWORK → decrypt on SECWORK.

Aalto IT centrally managed workstations are rated **secret**.  SECWORK
is reached from such a system (or equivalent), not from the public
internet.  Decrypting on a personal computer is not enough.


Getting help
------------

* **ITS / the environment itself:** secdata@aalto.fi
* **Need, workflow, containers, analysis:** :doc:`SciComp garage
  </help/garage>` (Data Agents and AaltoRSE).  Bring the goal and the
  install instructions you want to follow.
* Data Agents who hit classification or SECDATA questions can ask
  SciComp the same way; you do not have to solve the "do we really
  need SECDATA?" question alone.
