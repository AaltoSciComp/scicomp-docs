=====================================================================
June 2021 / Intro to Scientific Computing (FGCI HPC Summer Kickstart)
=====================================================================

.. admonition:: News

   Before the workshop:

   * See the :ref:`prerequisites <kickstart-2021-prereq>` below.

   * Request a HPC account (see university-specific instructions in
     prerequisites).

   * Verify you can connect to your cluster (but if you can't, we will
     also do this together on the first day).

   **Check back here for other updates that don't get their own
   email**. 

   This workshop will be streamed at https://twitch.tv/coderefinery.



Part of the :doc:`Scientific Computing in Practice
</training/scip/index>` lecture series at Aalto University.

**Audience:** All FGCI consortium members looking for the HPC crash
course. This is specifically designed for our summer workers who are just 
starting their internship.

**About the course:**

Summer Kickstart is a three day courses for researchers to get started
with the available computational resources at FGCI (Finnish Grid and
Cloud Infrastructure, basically HPC, high-performance computing, at
universities) and CSC (the Finnish national computing center).  On the
day one we start with the basic HPC intro, and some basic intro to 
Linux command line and Git version control, for those who are not yet familiar
with these tools.

On days two and three we cover one by one steps on how to get started on
the local computational clusters: learning by doing with lots of
examples and hands-on exercises.  

By the end of the course you get the hints, ready solutions and
copy/paste examples on how to find, run and monitor your applications,
and manage your data. In addition to how to optimize your workflow in
terms of filesystem traffic, memory usage etc.

While the material is based on previous years Aalto
courses, most of material will be common for all the participants and 
in addition we organize break-out rooms for different sites (= sort of parallel
sessions) when needed.  

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

**Time, date:**  Mon 7.6, Tue 8.6, Wed 9.6, 11:50-16:00 EEST

**Place:** Online: Zoom link will be sent to registered participants.

**Lecturering by:** Aalto Science IT and CSC

**Registration:** https://forms.gle/yNFLYt676kKorF3X7

**Cost:** Free of charge for FGCI consortium members including Aalto
employees and students.

**Additional course info at:** scip@aalto.fi



Schedule
--------

**Schedule**: The daily schedule will be adjusted based on the
audience; below is the tentative plan.  There will be frequent
breaks. You will be given time to try and ask, it’s more like an
informal help session to get you started with the computing resources.


* **Day #1 (Mon 7.jun):**

  * 11:50-12:00: **Joining time and pre-discussion**, please join 10
    minutes early.

  * Module #1.1 (12:00-12:15): **Welcome, course details**

  * Module #1.2 (12:15-13:00): **HPC crash course: what is behind the
    front-end** // lecture // HPC fundamentals: terminology,
    architectures, interconnects, infrastructure behind, as well as
    MPI vs shared memory // Ivan Degtyarenko // `Slides (.pdf) <https://users.aalto.fi/degtyai1/SCiP2020_kick.HPC_crash_course.2020-06-06.pdf>`__

  * Break (13:00-13:15)

  * Module #1.3 (13:15-14:00): **CSC resources overview** // lecture with demos
    // An overview of CSC computing environment and services
    including Puhti supercomputer, Allas data management solution,
    Cloud services, notebooks, containers, etc // Jussi Enkovaara and
    Henrik Nortamo // `Slides (.pdf) <https://kannu.csc.fi/s/3K8q93XSwtSgHEa>`__

  * Break (14:00-14:15)

  * Module #1.4 (14:15-14:40) **Gallery of computing workflows** // There are
    more options that just Triton by ssh, like we will learn later.
    We'll give an overview of all the ways you can work. // Enrico
    Glerean

    * Aalto: :doc:`/triton/usage/workflows`
    * Helsinki: `Remote access to university resources
      <https://wiki.helsinki.fi/display/it4sci/Remote+access+to+University+resources>`__
    * Tampere: `Tampere workflows <https://narvi-docs.readthedocs.io/narvi/usage/workflows.html>`__

  * Module #1.5 (14:40-15:00): **Connecting to the cluster** // tutorial //
    Get connected in preparation for day 2 // Enrico Glerean

    * Aalto: :doc:`Connecting to Triton tutorial
      </triton/tut/connecting>` – if you can ssh to Triton and run
      ``hostname``, you are ready for tomorrow.
    * Helsinki: `general information <https://wiki.helsinki.fi/display/it4sci/HPC+SUMMER+KICKSTART>`__
    * Tampere: `Connecting to Narvi <https://narvi-docs.readthedocs.io/narvi/tut/connecting.html>`__

  * Break (15:00-15:15)
  * Crash course intro to Linux command line shell (15:15-15:30)
  * Crash course intro to git version control (15:30-16:00)

* **Day #2 (Tue 8.jun):**

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

* **Day #3 (Wed 9.jun):**

  * Module #3.1 (4h): **Advanced SLURM and cluster usage** // tutorial // Running in
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


.. _kickstart-2021-prereq:

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

This workshop will be streamed, so that anyone can follow along at the
`CodeRefinery Twitch stream, https://www.twitch.tv/coderefinery
<https://www.twitch.tv/coderefinery>`__.
