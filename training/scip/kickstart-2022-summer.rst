=====================================================================
June 2022 / Intro to Scientific Computing /  HPC Summer Kickstart
=====================================================================

.. warning::

   This courses schedule is still under development, below you see the
   template from last year.  The dates will be 7, 8-9 June 2022 (T,
   Th-F).  If you have requests for the schedule or would like to
   offer a talk as part of this course, please get in touch with us.

Kickstart is a three × half day course for researchers to get
started with high-performance computing (HPC) clusters.
**The first day serves as a guide to your career:** a map to the types of
resources that are available and skills you may need in your career,
so that you can be prepared when you
need more in the future.  This part is especially suitable to new researchers or students trying to
understand computational/data analysis options available to them.  It
won't go into anything too deep, but will provide you with a good
background for your next steps: you will know what resources are
available and know the next steps to use them.

**The second and third days take
you from being a new user to being competent to run your code at a
larger scale than you could before.**
This part is good for any researcher who thinks they may need to
scale up to larger resources in the next six months, in any field.
Even if you don't use computing clusters, you will be better prepared
to understand how computing works on other systems.  If you are a
student, this is an investment in your skills.  By the end of the course you
get the hints, ready solutions and
copy/paste examples on how to find, run and monitor your applications,
and manage your data.

If you are at Aalto University: the course is obligatory for all new
Triton users and recommended to all interested in the field.

This course is part of :doc:`Scientific Computing in Practice <index>` lecture series
at Aalto University, supported by many others outside Aalto, and offered to others as part of `CodeRefinery <https://coderefinery.org>`__



Other universities
------------------


**If you are not at Aalto University**, you can follow along with the
course and will learn many things anyway.  The course is designed to
be as useful to people outside of Aalto, but many of the examples
won't directly work on your cluster and you will need to adapt (we
give hints about this).  Known sites partnering with this course:

* Others in Finland: may register via the Aalto form.
* Participants from University of Helsinki can follow how to connect
  to their Kale/Turso cluster by following `their own instructions
  <https://wiki.helsinki.fi/pages/viewpage.action?pageId=408323613>`__.
* Participants from University of Oulu: please follow instructions on
  `how to access the Carpo2 computing cluster <https://ict.oulu.fi/17120/?page&lang=en>`__.
* Tampere: this course is recommended for all new Narvi users and also all
  interested in HPC. Most things should work with simply replacing triton
  -> narvi. Some differences in configuration are listed in
  `Narvi differences <https://narvi-docs.readthedocs.io/narvi/kickstart-diffs.html>`__* `CSC <https://csc.fi>`__ (Finland): Participants with `CSC user
  account <https://docs.csc.fi/accounts/>`__ can try examples also in
  CSC supercomputers, see the `overview of CSC supercomputers
  <https://docs.csc.fi/computing/overview/>`__ for details on
  connecting, etc.

If you want to get your site listed here and/or help out, contact us
via the `CodeRefinery chat
<https://coderefinery.github.io/manuals/chat/>`__ (#workshops stream).
Our :doc:`hints for other sites' support staff
</triton/tut/required-cluster-setup>` are available.


Practical information
---------------------

**Time, date:**  Tue, Thu, Fri 7 and 9-10 June. 11:50-16:00 EEST

**Place:** Online, see below

**Lecturering by:** Aalto Scientific Computing and others

**Registration:** Not yet open.  Attending individual sessions is fine.

**Cost:** Free of charge for FGCI consortium members including Aalto
employees and students.  Livestream is free to everyone.

**Additional course info at:** scip@aalto.fi



How to attend
-------------

This is an online hybrid of MOOC and interactive:

* **Livestream**: anyone may watch at https://twitch.tv/coderefinery,
  no registration needed!  This is the primary way to watch all sessions.

* **Zoom**: if you register, you will be able to attend a Zoom meeting
  that includes interactive breakout rooms and hands-on help.  We
  watch the livestream for the main material.

* **HackMD**: instead of chat, this is used for Q&A.  See the
  `CodeRefinery HackMD manual
  <https://coderefinery.github.io/manuals/hackmd-mechanics/>`__ for
  how this works.



Schedule
--------

**All times are EET (Europe/Helsinki time)!**

The daily schedule will be adjusted based on the
audience; below is the tentative plan.  There will be frequent
breaks. You will be given time to try and ask, it’s more like an
informal help session to get you started with the computing
resources.  All times are EEST (Helsinki) time.


.. warning::

   This is last year's schedule.  It will be updated for this year,
   but the overall times and plan are correct.

* **Day #1 (Tue 7.jun):** Basics and background

  * **11:50: Joining time and pre-discussion**, please join 10
    minutes early.  (Richard Darst, Enrico Glerean)

  * **12:00: Welcome, general introduction** (:doc:`Notes <summer-kickstart/intro>`) (Enrico Glerean and all)

  * **12:10: HPC crash course: what is behind the front-end** HPC fundamentals:
    terminology, architectures, interconnects, infrastructure behind, as well as
    MPI vs shared memory. Continued on day 3. (Ivan Degtyarenko, Simppa Äkäslompolo)
    (`Slides (.pdf) <https://users.aalto.fi/degtyai1/SCiP2021_kick.HPC_crash_course.2021-06-04.pdf>`__)

  * **12:40: Summary and discussion about the videos "Basic linux shell
    scripting" and "Scientific computing workflows"** (see videos in
    preparatory material above) (:doc:`Notes <summer-kickstart/video-summary>`) (Richard Darst, Enrico Glerean)

  * 12:50: Break

  * **13:00: Currently available resources at CSC** CSC is the Finnish
    center for scientific computing, and also has many resources for
    research. (`Slides <https://kannu.csc.fi/s/3K8q93XSwtSgHEa>`__)
    (Jussi Enkovaara, CSC).

  * 13:45: Break

  * **14:00: Special topic #1**

  * 14:45: Break

  * **15:00: Your future career in scientific computing (and this
    course).** (:doc:`Notes <summer-kickstart/future>`) (Enrico Glerean, TBA)

  * **15:15: Connecting to the cluster**, hands-on.
    Get connected in preparation for day 2 (Enrico Glerean)

* **Day #2 (Thu 9.jun):** Basic use of a cluster (Richard Darst, Simo
  Tuomisto)

  - **11:50 -- 12:30: What can you do with a computational cluster?**

    - :doc:`/triton/tut/intro`
    - Real example 1: Large-scale computing with array jobs
    - Real example 2: Large-scale parallel computing

  - **12:30 -- 15:00: Running your first jobs in the queue**

    - :doc:`/triton/tut/interactive`
    - :doc:`/triton/tut/serial`
    - :doc:`/triton/tut/monitoring`

  - **15:00 -- 15:30: Other things you should know about the HPC environment**

    - :doc:`/triton/tut/modules`
    - :doc:`/triton/tut/storage`
    - :doc:`/triton/tut/remotedata`

  - **15:30 -- 16:00: Questions to presenters**

* **Day #3 (Fri 10.jun):** Advanced cluster use (Simo Tuomisto, Richard
  Darst)

  - 11:50: Joining time/icebreaker

  - **11:50 -- 13:00: Simple parallelization with array jobs**

    - :doc:`/triton/tut/array`

  - **13:00 -- 14:00: Using more than one CPU at the same time**

    - :doc:`/triton/tut/parallel`

  - **14:00 -- 14:30: Laptops to Lumi**, Jussi Enkovaara, CSC

    You now know of basics of using a computing cluster.  What if you
    need more than what a university can provide?  CSC (and other
    national computing centers) have even more resources, and this is
    a tour of them. `Slides here <https://github.com/AaltoSciComp/scicomp-docs/raw/master/training/scip/CSC-services_022022.pdf>`__.

  - **14:40 -- 15:30: Running jobs that can utilize GPU hardware**

    - :doc:`/triton/tut/gpu`

  - **15:30 -- 16:00:** Questions to presenters


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




Preparation
-----------

Each year the first day has varying
topics presented.  We don't repeat these every year, but we strongly
recommend that you watch these videos yourself as preparation:

  * `Basic Linux shell and scripting
    <https://www.youtube.com/watch?v=ESXLbtaxpdI&list=PLZLVmS9rf3nN_tMPgqoUQac9bTjZw8JYc&index=3>`__
  * `Scientific computing workflows
    <https://www.youtube.com/watch?v=ExFbc5EikU0>`__




.. _kickstart-2021-prereq:

Prerequisites
-------------


**Software installation**

* SSH client to connect to the cluster (+ be able to connect, see next
  point)
* `Zoom <https://coderefinery.github.io/installation/zoom/>`__ (if
  attending breakout rooms)


**Cluster account and connection verification:**

* Access to your computer cluster.

  * Aalto: if you do not yet have access to Triton, :doc:`request an account
    </triton/accounts>` in advance.

* Then, connect and get it working

  * Aalto (and possibly useful to others): try to :doc:`connect to
    Triton </triton/tut/connecting>` to be ready.  Come to the
    Wednesday session for help connecting (required).


**Background knowledge:** "A HPC cluster is easy to use if you know
the Linux command line well".  A lot of this course is actually about
getting comfortable with Linux so that you can use the cluster well.

* The :doc:`Linux shell crash course </scicomp/shell>` (`video
  <https://youtu.be/56p6xX0aToI>`__).


**Mental preparation:** Online workshops can be a productive format, but it
takes some effort to get ready.  Browse these resources:

* `Attending an online workshop
  <https://coderefinery.github.io/manuals/how-to-attend-online/>`__,
  good to read in detail (ignore the CodeRefinery-specific parts).
* `How to use HackMD to take answer questions and hold discussions <https://coderefinery.github.io/manuals/hackmd-mechanics/>`__.
* `The Zoom mechanics we will use
  <https://coderefinery.github.io/manuals/zoom-mechanics/>`__, might
  be useful to browse.



Community standards
-------------------

We hope to make a good learning environment for everyone, and expect
everyone to do their part for this.  If there is anything we can do to
support that, let us know.

If there is anything wrong, *tell us right away* - if you need to
contact us privately, you can message the host on Zoom or
:doc:`contact us outside the course </help/index>`.  This could be as
simple as "speak louder / text on screen is unreadable / go slower" or
as complex as "someone is distracting our group by discussing too
advanced things".



Material
--------

See the schedule
