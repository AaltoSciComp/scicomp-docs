=====================================================================
June 2021 / Intro to Scientific Computing (FGCI HPC Summer Kickstart)
=====================================================================

.. admonition:: News

   * Watch at https://twitch.tv/coderefinery

   * The livestream is `archived on Twitch for 14 days
     <https://www.twitch.tv/coderefinery/videos>`__.  Videos will be
     posted on `this playlist
     <https://www.youtube.com/playlist?list=PLZLVmS9rf3nPFw29oKUj6w1QdsTCECS1S>`__
     once they are ready.

   Before the workshop:

   * Registration is open: https://forms.gle/yNFLYt676kKorF3X7

   * View the prerequisites below.

   **Check back here for other updates that don't get their own
   email**.




Part of the :doc:`Scientific Computing in Practice
</training/scip/index>` lecture series at Aalto University.

**Audience:** All researchers looking for a start to scientific
computing.  We go over the various options and tools that everyone
needs to know about, and then go in-depth about using a remote
computational cluster (though these skills will be useful to
everyone).  This is specifically designed for our summer workers who are just
starting their internship, but anyone who is doing computing or data-focused
work can get something from this course.  Anyone is welcome to listen along
and learn from some experts.

Most examples use Aalto University resources, but everyone can learn
something and we are careful to explain local vs general practices.

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


University specific information:

* Aalto: this course is obligatory for all new Triton users and
  recommended to all interested in scientific computing in general.
  :doc:`Basic reference information is at the Triton page </triton/index>`

* `University of Helsinki <https://wiki.helsinki.fi/display/it4sci/HPC+SUMMER+KICKSTART+2021>`__

* Tampere: this course is recommended for all new Narvi users and also all
  interested in HPC. Most things should work with simply replacing triton 
  -> narvi. Some differences in configuration are listed in 
  `Narvi differences <https://narvi-docs.readthedocs.io/narvi/kickstart-diffs.html>`__


Practical information
---------------------

**Time, date:**  Mon 7.6, Tue 8.6, Wed 9.6, 11:50-16:00 EEST

**Place:** Online, see below

**Lecturering by:** Aalto Scientific Computing (Science-IT) and others

**Registration:** https://forms.gle/yNFLYt676kKorF3X7

**Cost:** Free of charge for FGCI consortium members including Aalto
employees and students.  Livestream is free to everyone.

**Additional course info at:** scip@aalto.fi



How to attend
-------------

This is an online hybrid of MOOC and interactive:

* **Livestream**: anyone may watch at https://twitch.tv/coderefinery,
  no registration needed!

* **Zoom**: if you register, you will be able to attend a Zoom meeting
  that includes interactive breakout rooms and hands-on help.  We
  watch the livestream for the main material.

* **HackMD**: instead of chat, this is used for Q&A.  See the
  `CodeRefinery HackMD manual
  <https://coderefinery.github.io/manuals/hackmd-mechanics/>`__ for
  how this works.



Schedule
--------

The daily schedule will be adjusted based on the
audience; below is the tentative plan.  There will be frequent
breaks. You will be given time to try and ask, it’s more like an
informal help session to get you started with the computing
resources.  All times are EEST (Helsinki) time.

* **Preparatory material**.  Each year the first day has varying
  topics presented.  We don't repeat these every year, but we strongly
  recommend that you watch these videos yourself as preparation:

  * `Basic Linux shell and scripting
    <https://www.youtube.com/watch?v=ESXLbtaxpdI&list=PLZLVmS9rf3nN_tMPgqoUQac9bTjZw8JYc&index=3>`__
  * `Scientific computing workflows
    <https://www.youtube.com/watch?v=ExFbc5EikU0>`__


* **Day #1 (Mon 7.jun):** Basics and background

  * 11:50: **Joining time and pre-discussion**, please join 10
    minutes early.  (Richard Darst, Enrico Glerean)

  * 12:00: **Welcome, general introduction** (:doc:`Notes <summer-kickstart/intro>`) (Enrico Glerean and all)

  * 12:10: **HPC crash course: what is behind the front-end** HPC fundamentals:
    terminology, architectures, interconnects, infrastructure behind, as well as
    MPI vs shared memory. Continued on day 3. (Ivan Degtyarenko, Simppa Äkäslompolo)
    (`Slides (.pdf) <https://users.aalto.fi/degtyai1/SCiP2021_kick.HPC_crash_course.2021-06-04.pdf>`__)

  * 12:40: **Summary and discussion about the videos "Basic linux shell
    scripting" and "Scientific computing workflows"** (see videos in
    preparatory material above) (:doc:`Notes <summer-kickstart/video-summary>`) (Richard Darst, Enrico Glerean)

  * 12:50: Break

  * 13:00: **Currently available resources at CSC** CSC is the Finnish
    center for scientific computing, and also has many resources for
    research. (`Slides <https://kannu.csc.fi/s/3K8q93XSwtSgHEa>`__)
    (Jussi Enkovaara, CSC).

  * 13:45: Break

  * 14:00: **Git intro**: why you need version control for any
    scientific work and how to get started.  We don't go in depth into
    theory, but talk about the simplest usage by yourself. (Richard
    Darst, Jarno Rantaharju)

  * 14:45: Break

  * 15:00: **Your future career in scientific computing (and this
    course).** (:doc:`Notes <summer-kickstart/future>`) (Enrico Glerean, TBA)

  * 15:15: **Connecting to the cluster**, hands-on.
    Get connected in preparation for day 2 (Enrico Glerean)

    * Aalto: :doc:`Connecting to Triton tutorial
      </triton/tut/connecting>` – if you can ssh to Triton and run
      ``hostname``, you are ready for tomorrow.
    * Helsinki: `general information <https://wiki.helsinki.fi/display/it4sci/HPC+SUMMER+KICKSTART+2021>`__
    * Tampere: `Connecting to Narvi <https://narvi-docs.readthedocs.io/narvi/tut/connecting.html>`__

* **Day #2 (Tue 8.jun):** Basic use of a cluster (Richard Darst, Simo
  Tuomisto)

    This day will go over all practical aspects of using the cluster

    * 11:50: Joining time/icebreaker

    * 12:00: :doc:`/triton/tut/connecting`

      * Every site will have its own ways of connecting.  The basic
	lessons of ``ssh`` is the same for everyone, but it will have
	a different hostname and possibly different initial steps
	(jump hosts).
      * Aalto: (same)
      * Helsinki: `general information <https://wiki.helsinki.fi/display/it4sci/HPC+SUMMER+KICKSTART+2021>`__
      * Tampere: `Connecting to Narvi
	<https://narvi-docs.readthedocs.io/narvi/tut/connecting.html>`__.
	Note, that you will need SSH keys.

    * 12:30: :doc:`/triton/tut/applications`

      * Each site will be quite different here, so don't worry about
	making the exercises work outside of Aalto, but think and
	prepare for what comes next (where we'll explain the differences).

    * 12:50: Break

    * 13:00: :doc:`/triton/tut/modules`

    * 13:20: :doc:`/triton/tut/storage`

      * Aalto: (same)
      * Helsinki: `general information <https://wiki.helsinki.fi/display/it4sci/HPC+SUMMER+KICKSTART+2021>`__
      * Tampere: `Narvi storage <https://narvi-docs.readthedocs.io/narvi/tut/storage.html>`__
      * This topic is *very* site-specific.  The general principles
	will apply everywhere, but the exact paths/servers will vary.

    * 13:50: Break

    * 14:00: Short talk: `Radovan Bast <https://bast.fr/>`__ (UiT The Arctic University of Norway): `Asking for help with supercomputers <https://cicero.xyz/v3/remark/0.14.0/github.com/bast/help-with-supercomputers/main/talk.md/#1>`__ 

      * How should you write support requests so that you get quick 
        (and useful!) answers? Radovan, one of the founders of 
        `CodeRefinery <https://coderefinery.org/>`__, will talk about how we can all improve 
        the dialogue between supercomputer user community and support staff 
        so that we always remain respectful and try to learn and solve problems together.
       

    * 14:35: :doc:`/triton/tut/interactive`

      * The basic Slurm concepts are the same across all clusters (at
	least all those that use Slurm, but that is everyone in
	Finland).  However, partition names may be different.  You can
	list partitions at your site using ``sinfo -O partition`` and
	list nodes at your site with ``sinfo -N``.  How these work
	will vary depending on your site - definitely read up on this.

    * 14:50: Break

    * 15:00 Continuing with interactive slurm jobs and exercises

    * 16:00: End

* **Day #3 (Wed 9.jun):** Advanced cluster use (Simo Tuomisto, Richard
  Darst)

    * 11:50: Joining time/icebreaker

    * 12:00 :doc:`/triton/tut/serial`

    * :doc:`/triton/tut/monitoring`

    * :doc:`/triton/tut/array`

      Array jobs allow you to quickly run many jobs, and are the
      simplest unit of advanced computing.  We will go over them in detail.

    * :doc:`/triton/tut/modules`

      * In other sites, you should ``module load fgci-common`` to be
	able to make the Aalto modules available.  Other specifics,
	such as ``matlab``, won't directly work.

    * :doc:`/triton/tut/gpu` (Simo Tuomisto)

      * Aalto: (same as above)
      * Helsinki: `general information <https://wiki.helsinki.fi/display/it4sci/HPC+SUMMER+KICKSTART+2021>`__
      * Tampere: `Narvi GPU computing differences
	<https://narvi-docs.readthedocs.io/narvi/tut/gpu.html>`__
      * At other sites, you may need to use ``-p gpu`` in addition to ``--gres=gpu``.

    * :doc:`/triton/tut/parallel` (Simo Tuomisto)

    * **Parallel computing programming** (Ivan Degtyarenko, Simo
      Tuomisto)

    * 16:00: End


* **Follow-up suggestions:**  While not an official part of this
  course, we suggest these videos (co-produced by our staff) as a
  follow-up perspective:

  * Attend a `CodeRefinery workshop <https://coderefinery.org>`__,
    which teaches more useful tools for scientific software
    development.

  * Look at `Hands-on Scientific Computing
    <https://hands-on.coderefinery.org>`__ for an online course to
    either browse or take for credits.

  * `Cluster Etiquette (in Research Software Hour)
    <https://www.youtube.com/watch?v=NIW9mqDwnJE&list=PLpLblYHCzJAB6blBBa0O2BEYadVZV3JYf>`__:
    The Summer Kickstart teaches what you *can* do from this course,
    but what *should* you do to be a good user.
  * `How to tame the cluster (in Research Software Hour)
    <https://www.youtube.com/watch?v=5HN9-MW7Tw8&list=PLpLblYHCzJAB6blBBa0O2BEYadVZV3JYf>`__.
    This mostly repeats the contents of this course, with a bit more
    discussion, and working one example from start to parallel.




.. _kickstart-2021-prereq:

Prerequisites
-------------

Participants will be provided with either access to their university's
cluster or Triton for running examples.

* You should have an account on your university's HPC cluster:

  * Aalto: if you do not yet have access to Triton, :doc:`request an
    account </triton/accounts>` in advance.
  * Helsinki: `Account notes at the bottom of this page <https://wiki.helsinki.fi/display/it4sci/HPC+SUMMER+KICKSTART+2021>`__
  * Tampere: your cluster will require ssh keys to connect.
  * Others: Aalto will provide you with a guest Triton account, check
    back for more information.

* Participants are expected to have a SSH client installed (for
  options, see :doc:`the Triton connecting tutorial for examples
  </triton/tut/connecting>`).

* You should install Zoom.  `Hints on installation
  <https://coderefinery.github.io/installation/zoom/>`__.

* If you aren't familiar with the Linux shell, :doc:`read the crash
  course </scicomp/shell>`, `watch the video
  <https://youtu.be/56p6xX0aToI>`__, or watch the relevant preparatory
  video linked as part of the schedule.

* Try to get connected to your cluster in advance.  We have some time
  scheduled for this, but you *need* to also try in advance, or else
  we can't keep up.

  * Aalto: :doc:`connecting to Triton </triton/tut/connecting>`
  * Helsinki: `general information <https://wiki.helsinki.fi/display/it4sci/HPC+SUMMER+KICKSTART+2021>`__
  * Tampere: `Connecting to Narvi <https://narvi-docs.readthedocs.io/narvi/tut/connecting.html>`__


Other preparation
-----------------

How to attend this course:

* Take this seriously.  There is a lot of material and hands-on
  exercises.  Don't overbook your time, don't skip hands-on parts, and
  come prepared.

* Anyone may watch via Livestream, https://twitch.tv/coderefinery .
  Register anyway to get emails.

* You will be given a Zoom link to join.  Join each session 10 minutes
  early.

* Join with a name of "(University) First Last", e.g. "(Aalto) Richard
  Darst".  This will help us to put people into university-specific
  breakout rooms.

* There will be a <HackMD.io> document sent to all participants.  This
  is for communication an asking questions. `Read more about how this
  works here <https://coderefinery.github.io/manuals/hackmd-mechanics/>`__

  * Always write new questions or comments at the bottom of the
    document.

  * Moderators will follow the developments, and answer questions and
    comments.  You may get several answers from different
    perspectives, even.  Our focus is the bottom, but we will scan the
    whole document and keep it organized.

  * The final document (excluding personal data and questions about
    individual circumstances) will be published as the notes at the
    end.
