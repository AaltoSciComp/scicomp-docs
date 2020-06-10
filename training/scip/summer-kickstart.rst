==================================
Jun 2020 / FGCI Summer Kickstart
==================================

.. admonition:: News

   Before the workshop:

   * See the :ref:`prerequisites <kickstart-2020-prereq>` below.

   * Request a HPC account (see university-specific instructions in
     prerequisites).

   * Verify you can connect to your cluster (but if you can't, the
     last thing on Monday will a help session to get it working).

   **Check back here for other updates that don't get their own
   email**.  Minor announcements and past communication are also
   available at `this issue
   <https://github.com/AaltoSciComp/scicomp-docs/issues/105>`__.  If
   you are from Aalto and have technical issues, please post on `the
   issue tracker
   <https://version.aalto.fi/gitlab/AaltoScienceIT/triton/issues>`__.

   This workshop may be streamed.  This is not decided yet, but if it
   is, it will be at https://twitch.tv/coderefinery.



Part of the :doc:`Scientific Computing in Practice
</training/scip/index>` lecture series at Aalto University.

**Audience:** All FGCI consortium members looking for the HPC crash
course.

**About the course:**

Summer Kickstart is a three day courses for researchers to get started
with the available computational resources at FGCI (Finnish Grid and
Cloud Infrastructure, basically HPC, high-performance computing, at
universities) and CSC (the Finnish national computing center).  On the
day one we start with the basic HPC intro, go through the available
resources at CSC and then switch to the FGCI sites practicalities. The
days two and three we cover one by one steps on how to get started on
the local computational clusters: learning by doing with lots of
examples and hands-on.  In addition, on the last day we will have
HTCondor introduction for all interested.

By the end of the course you get the hints, ready solutions and
copy/paste examples on how to find, run and monitor your applications,
and manage your data. In addition to how to optimize your workflow in
terms of filesystem traffic, memory usage etc.

The first FGCI-wide kickstart for all FGCI consortium members, meaning
we will try to adapt our material to serve all universities.  We'll
have support representatives from several universities. Most of
material will be common for all the participants and in addition we
organize breaking rooms for different sites (= sort of parallel
sessions) when needed.  Material is based on previous years Aalto
courses.

University specific information:

* Aalto: this course is obligatory for all new Triton users and
  recommended to all interested in scientific computing in general.
  :doc:`Basic reference information is at the Triton page </triton/index>`

* `University of Helsinki <https://wiki.helsinki.fi/display/it4sci/HPC+SUMMER+KICKSTART>`__

* Tampere: this course is recommended for all new Narvi users and also all
  interested in HPC. Most things should work with simply replacing triton 
  -> narvi. Some differences in configuration are listed in 
  `Narvi differences <https://narvi-docs.readthedocs.io/narvi/kickstart-diffs.html>`__


Practical information
---------------------

**Time, date:** Mon 8.6, Tue 9.6, Wed 10.6, 12:00-16:00 EEST

**Place:** Online: Zoom link will be sent to registered participants.

**Lecturering by:** Aalto Science IT and CSC people

**Registration:** `registration link
<https://link.webropolsurveys.com/S/B1752A5EBD3BF08F>`__.  Please
register to get the Zoom link and updates in general.

**Cost:** Free of charge for FGCI consortium members including Aalto
employees and students.

**Additional course info at:** Ivan Degtyarenko, ivan.degtyarenko -at-
aalto.fi



Schedule
--------

**Schedule**: The daily schedule will be adjusted based on the
audience; below is the tentative plan.  There will be frequent
breaks. You will be given time to try and ask, it’s more like an
informal help session to get you started with the computing resources.


* **Day #1 (Mon 8.jun):**

  * 11:50-12:00: **Joining time and pre-discussion**, please join 10
    minutes early.

  * Module #1.1 (15m): **Welcome, course details**

  * Module #1.2 (1h): **HPC crash course: what is behind the
    front-end** // lecture // HPC fundamentals: terminology,
    architectures, interconnects, infrastructure behind, as well as
    MPI vs shared memory // Ivan Degtyarenko // `Slides (.pdf) <https://users.aalto.fi/degtyai1/SCiP2020_kick.HPC_crash_course.2020-06-06.pdf>`__

  * Module #1.3 (1h): **CSC resources overview** // lecture with demos
    // An overview of CSC computing environment and services
    including Puhti supercomputer, Allas data management solution,
    Cloud services, notebooks, containers, etc // Jussi Enkovaara and
    Henrik Nortamo // `Slides (.pdf) <https://kannu.csc.fi/s/3K8q93XSwtSgHEa>`__

  * Module #1.4 (1h) **Gallery of computing workflows** // There are
    more options that just Triton by ssh, like we will learn later.
    We'll give an overview of all the ways you can work. // Enrico
    Glerean

    * Aalto: :doc:`/triton/usage/workflows`
    * Helsinki: `Remote access to university resources
      <https://wiki.helsinki.fi/display/it4sci/Remote+access+to+University+resources>`__
    * Tampere: `Tampere workflows <https://narvi-docs.readthedocs.io/narvi/usage/workflows.html>`__

  * Module #1.5 (.5h): **Connecting to the cluster** // tutorial //
    Get connected in preparation for day 2 // Enrico Glerean

    * Aalto: :doc:`Connecting to Triton tutorial
      </triton/tut/connecting>` – if you can ssh to Triton and run
      ``hostname``, you are ready for tomorrow.
    * Helsinki: `general information <https://wiki.helsinki.fi/display/it4sci/HPC+SUMMER+KICKSTART>`__
    * Tampere: `Connecting to Narvi <https://narvi-docs.readthedocs.io/narvi/tut/connecting.html>`__

* **Day #2 (Tue 9.jun):**

  * Module #2.1 (4h): **Getting started on the cluster** // tutorial
    // SLURM basics, software, and storage.  Workflow, running and
    monitoring serial jobs on Triton. Interactively and in batch
    mode. module and toolchains, special resources like GPU // Richard
    Darst

    * :doc:`/triton/tut/connecting`

      * Every site will have its own ways of connecting.  The basic
	lessons of ``ssh`` is the same for everyone, but it will have
	a different hostname and possibly different initial steps
	(jump hosts).
      * Aalto: (same)
      * Helsinki: `general information <https://wiki.helsinki.fi/display/it4sci/HPC+SUMMER+KICKSTART>`__
      * Tampere: `Connecting to Narvi
	<https://narvi-docs.readthedocs.io/narvi/tut/connecting.html>`__.
	Note, that you will need SSH keys.

    * :doc:`/triton/tut/applications`

      * Each site will be quite different here, so don't worry about
	making the exercises work outside of Aalto, but think and
	prepare for what comes next (where we'll explain the differences).

    * :doc:`/triton/tut/modules`

      * In other sites, you should ``module load fgci-common`` to be
	able to make the Aalto modules available.  Other specifics,
	such as ``matlab``, won't directly work.

    * :doc:`/triton/tut/storage`

      * Aalto: (same)
      * Helsinki: `general information <https://wiki.helsinki.fi/display/it4sci/HPC+SUMMER+KICKSTART>`__
      * Tampere: `Narvi storage <https://narvi-docs.readthedocs.io/narvi/tut/storage.html>`__
      * This topic is *very* site-specific.  The general principles
	will apply everywhere, but the exact paths/servers will vary.

    * :doc:`/triton/tut/interactive`

      * The basic Slurm concepts are the same across all clusters (at
	least all those that use Slurm, but that is everyone in
	Finland).  However, partition names may be different.  You can
	list partitions at your site using ``sinfo -O partition`` and
	list nodes at your site with ``sinfo -N``.  How these work
	will vary depending on your site - definitely read up on this.

    * :doc:`/triton/tut/serial`

* **Day #3 (Wed 10.jun):**

  * Module #3.1 (2h): **Advanced SLURM and cluster usage** // tutorial // Running in
    parallel with MPI and OpenMP, array jobs, running on GPU with
    ``--gres``, local drives, constraints // Simo Tuomisto

    * :doc:`/triton/tut/array`
    * :doc:`/triton/tut/gpu`

      * Aalto: (same as above)
      * Helsinki: `general information <https://wiki.helsinki.fi/display/it4sci/HPC+SUMMER+KICKSTART>`__
      * Tampere: `Narvi GPU computing differences
	<https://narvi-docs.readthedocs.io/narvi/tut/gpu.html>`__
      * At other sites, you may need to use ``-p gpu`` in addition to ``--gres=gpu``.

    * :doc:`/triton/tut/parallel`

  * Module #3.2 (1.5h): **HTCondor** (at Aalto) // lecture with demos
    // Did you know that department workstations can be used for
    distributed computing? HTCondor lets you // Matthew West

    * `Users Manual <https://htcondor.readthedocs.io/en/latest/users-manual/index.html>`__
    * Binder: https://mybinder.org/v2/gh/htcondor/htcondor-python-bindings-tutorials/master?urlpath=lab/tree/index.ipynb
    * Python Bindings

      * Quickstart: `Submitting and Managing Jobs <https://htcondor.readthedocs.io/en/latest/apis/python-bindings/users/Submitting-and-Managing-Jobs.html>`__
      * Making a workflow: `Diamond DAG <https://github.com/htcondor/htcondor-dags/tree/master/examples/basic_diamond>`__



.. _kickstart-2020-prereq:

Prerequisites
-------------

Participants will be provided with either access to their university's
cluster or Triton for running examples.

* You should have an account on your university's HPC cluster:

  * Aalto: if you do not yet have access to Triton, :doc:`request an
    account </triton/accounts>` in advance.
  * Helsinki: `Account notes at the bottom of this page <https://wiki.helsinki.fi/display/it4sci/HPC+SUMMER+KICKSTART>`__
  * Tampere: your cluster will require ssh keys to connect.
  * Others: Aalto will provide you with a guest Triton account, check
    back for more information.

* Participants are expected to have a SSH client installed (for
  options, see :doc:`the Triton connecting tutorial for examples
  </triton/tut/connecting>`).

* You should install Zoom.  `Hints on installation
  <https://coderefinery.github.io/installation/zoom/>`__.

* If you aren't familiar with the Linux shell, :doc:`read the crash
  course </scicomp/shell>` or `watch the video
  <https://youtu.be/56p6xX0aToI>`__.

* Try to get connected to your cluster in advance.  We have some time
  scheduled for this, but you *need* to also try in advance, or else
  we can't keep up.

  * Aalto: :doc:`connecting to Triton </triton/tut/connecting>`
  * Helsinki: `general information <https://wiki.helsinki.fi/display/it4sci/HPC+SUMMER+KICKSTART>`__
  * Tampere: `Connecting to Narvi <https://narvi-docs.readthedocs.io/narvi/tut/connecting.html>`__


Other preparation
-----------------

How to attend this course:

* Take this seriously.  There is a lot of material and hands-on
  exercises.  Don't overbook your time, don't skip hands-on parts, and
  come prepared.

* You will be given a Zoom link to join.  Join each session 10 minutes
  early.

* Join with a name of "(University) First Last", e.g. "(Aalto) Richard
  Darst".  This will help us to put people into university-specific
  breakout rooms.

* There will be a <HackMD.io> document sent to all participants.  This
  is for communication an asking questions.

  * Always write new questions or comments at the bottom of the
    document.

  * Moderators will follow the developments, and answer questions and
    comments.  You may get several answers from different
    perspectives, even.  Our focus is the bottom, but we will scan the
    whole document and keep it organized.

  * The final document (excluding personal data and questions about
    individual circumstances) will be published as the notes at the
    end.


Streaming
---------

This workshop may be streamed, so that anyone can follow along.  We
are still deciding if we will do this, but if we do it will be at the
`CodeRefinery Twitch stream, https://www.twitch.tv/coderefinery
<https://www.twitch.tv/coderefinery>`__.
