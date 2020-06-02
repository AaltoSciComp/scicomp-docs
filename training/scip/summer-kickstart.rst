==================================
Jun 2020 / FGCI Summer Kickstart
==================================

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

* Tampere:


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
    MPI vs shared memory // Ivan Degtyarenko

  * Module #1.3 (1h): **CSC resources overview** // lecture with demos
    // An overview of CSC computing environment and services
    including Puhti supercomputer, Allas data management solution,
    Cloud services, notebooks, containers, etc // Jussi Enkovaara and
    Henrik Nortamo

  * Module #1.4 (1h) **Gallery of computing workflows** // There are
    more options that just Triton by ssh, like we will learn later.
    We'll give an overview of all the ways you can work. // Enrico
    Glerean

    * Aalto: :doc:`/triton/usage/workflows`
    * Helsinki: `Remote access to university resources
      <https://wiki.helsinki.fi/display/it4sci/Remote+access+to+University+resources>`__
    * Tampere:

  * Module #1.5 (.5h): **Connecting to the cluster** // tutorial //
    Get connected in preparation for day 2 // Enrico Glerean

    * Aalto: :doc:`Connecting to Triton tutorial
      </triton/tut/connecting>` – if you can ssh to Triton and run
      ``hostname``, you are ready for tomorrow.
    * Helsinki:
    * Tampere:

* **Day #2 (Tue 9.jun):**

  * Module #2.1 (4h): **Getting started on the cluster** // tutorial
    // SLURM basics, software, and storage.  Workflow, running and
    monitoring serial jobs on Triton. Interactively and in batch
    mode. module and toolchains, special resources like GPU // Richard
    Darst

    * :doc:`/triton/tut/connecting`

      * Aalto: (link above)
      * Helsinki:
      * Tampere:

    * :doc:`/triton/tut/applications`
    * :doc:`/triton/tut/modules`
    * :doc:`/triton/tut/storage`

      * Aalto: (link above)
      * Helsinki:
      * Tampere:

    * :doc:`/triton/tut/interactive`
    * :doc:`/triton/tut/serial`

* **Day #3 (Wed 10.jun):**

  * Module #3.1 (2h): **Advanced SLURM and cluster usage** // tutorial // Running in
    parallel with MPI and OpenMP, array jobs, running on GPU with
    ``--gres``, local drives, constraints // Simo Tuomisto

    * :doc:`/triton/tut/array`
    * :doc:`/triton/tut/gpu`
    * :doc:`/triton/tut/parallel`

  * Module #3.2 (1.5h): **HTCondor** (at Aalto) // lecture with demos
    // Did you know that department workstations can be used for
    distributed computing? HTCondor lets you // Matthew West



Prerequisites
-------------

Participants will be provided with either access to their university's
cluster or Triton for running examples.

* You should have an account on your university's HPC cluster:

  * Aalto: if you do not yet have access to Triton, :doc:`request an
    account </triton/accounts>` in advance.
  * Helsinki: `Account notes at the bottom of this page <https://wiki.helsinki.fi/display/it4sci/HPC+SUMMER+KICKSTART>`__
  * Tampere: your cluster will require ssh keys to connect.
  * Others: Aalto will provide you with a guest Triton account.

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



