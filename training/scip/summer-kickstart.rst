=====================================================================
June 2021 / Intro to Scientific Computing (FGCI HPC Summer Kickstart)
=====================================================================

.. admonition:: News

   Before the workshop:

   * Registration is open: https://forms.gle/yNFLYt676kKorF3X7

   * The exact schedule is still being developed, please let us know
     any special requests.

   * Other institutions which would like to join our effort are
     welcome to contact us, you can use our livestream and run your
     own breakout rooms.

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

* `University of Helsinki <https://wiki.helsinki.fi/display/it4sci/HPC+SUMMER+KICKSTART>`__

* Tampere: this course is recommended for all new Narvi users and also all
  interested in HPC. Most things should work with simply replacing triton 
  -> narvi. Some differences in configuration are listed in 
  `Narvi differences <https://narvi-docs.readthedocs.io/narvi/kickstart-diffs.html>`__


Practical information
---------------------

**Time, date:**  Mon 7.6, Tue 8.6, Wed 9.6, 11:50-16:00 EEST

**Place:** Online: Zoom link will be sent to registered participants,
anyone may join for free via livestream at https://twitch.tv/coderefinery

**Lecturering by:** Aalto Scientific Computing (Science-IT) and others

**Registration:** https://forms.gle/yNFLYt676kKorF3X7

**Cost:** Free of charge for FGCI consortium members including Aalto
employees and students.

**Additional course info at:** scip@aalto.fi



Schedule
--------

**Schedule**: The daily schedule will be adjusted based on the
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
    minutes early.

  * 12:00: **Welcome, general introduction**

  * 12:15 **Summary and discussion about the videos "Basic linux shell
    scripting" and "Scientific computing workflows"** (see videos in
    preparatory material above)

  * 12:45: Break

  * 13:00: **HPC crash course: what is behind the
    front-end** // lecture // HPC fundamentals: terminology,
    architectures, interconnects, infrastructure behind, as well as
    MPI vs shared memory // Ivan Degtyarenko // `Slides (.pdf) <https://users.aalto.fi/degtyai1/SCiP2020_kick.HPC_crash_course.2020-06-06.pdf>`__

  * 13:45: Break

  * 14:00: **Git intro**: why you need version control for any
    scientific work and how to get started.

  * 14:45: Break

  * 15:00: **Future outlook of scientific computing and this course.**

  * 15:15: **Connecting to the cluster** // tutorial //
    Get connected in preparation for day 2 // Enrico Glerean

    * Aalto: :doc:`Connecting to Triton tutorial
      </triton/tut/connecting>` – if you can ssh to Triton and run
      ``hostname``, you are ready for tomorrow.
    * Helsinki: `general information <https://wiki.helsinki.fi/display/it4sci/HPC+SUMMER+KICKSTART>`__
    * Tampere: `Connecting to Narvi <https://narvi-docs.readthedocs.io/narvi/tut/connecting.html>`__

* **Day #2 (Tue 8.jun):** Basic use of a cluster

    This day will go over all practical aspects of using the cluster

    * 11:50: Joining time/icebreaker

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

* **Day #3 (Wed 9.jun):** Advanced cluster use

    * 11:50: Joining time/icebreaker

    * :doc:`/triton/tut/array`

    * :doc:`/triton/tut/modules`

      * In other sites, you should ``module load fgci-common`` to be
	able to make the Aalto modules available.  Other specifics,
	such as ``matlab``, won't directly work.

    * **Parallel computing theory**

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
  course </scicomp/shell>`, `watch the video
  <https://youtu.be/56p6xX0aToI>`__, or watch the relevant preparatory
  video linked as part of the schedule.

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


Streaming
---------

This workshop will be streamed, so that anyone can follow along at the
`CodeRefinery Twitch stream, https://www.twitch.tv/coderefinery
<https://www.twitch.tv/coderefinery>`__.
