=====================================================================
June 2022 / Intro to Scientific Computing /  HPC Summer Kickstart
=====================================================================

.. admonition:: Quick Reference

   - Date: 7, 9-10 June 2022, 11:50-16:00 EEST (Helsinki time).
   - A registration form is not yet available.
   - This courses schedule is still under development, and will remain
     so right until the course.  The schedule below is a sample
     inspired by last year (it will be better this year).
   - Get involved!

     - If you have an idea for a talk you offer/request,
       `get in touch <https://coderefinery.org/manuals/chat/>`__
     - If you would like to support others to take this course via a
       `local breakout room
       <https://coderefinery.org/manuals/local-breakout-rooms/>`__,
       read that page and `get in touch
       <https://coderefinery.org/manuals/chat/>`__ if we can help you.
       (you can read about :doc:`what is needed to be able to follow
       our examples on your cluster
       </triton/tut/required-cluster-setup>`.


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
at Aalto University, supported by many others outside Aalto, and offered to others as part of `CodeRefinery <https://coderefinery.org>`__.



Other universities
------------------

**If you are not at Aalto University**, you can follow along with the
course and will learn many things anyway.  The course is designed to
be as useful to people outside of Aalto, but some of the examples
won't directly work on your cluster (most will, anyway we will give
hints about adapting).  Known sites partnering with this course:

* Regardless of where you are from, you may register using the
  registration form below to get emails about the course.
* Participants from University of Helsinki can follow how to connect
  to their Kale/Turso cluster by following `their own instructions
  <https://wiki.helsinki.fi/pages/viewpage.action?pageId=408323613>`__.
* Participants from University of Oulu: please follow instructions on
  `how to access the Carpo2 computing cluster <https://ict.oulu.fi/17120/?page&lang=en>`__.
* Tampere: this course is recommended for all new Narvi users and also all
  interested in HPC. Most things should work with simply replacing triton
  -> narvi. Some differences in configuration are listed in
  `Narvi differences
  <https://narvi-docs.readthedocs.io/narvi/kickstart-diffs.html>`__*
* `CSC <https://csc.fi>`__ (Finland): Participants with `CSC user
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

This is an online hybrid of MOOC and interactive: everyone may attend
the **livestream** at https://twitch.tv/coderefinery, no registration
needed!  This is the primary way to watch all sessions.  **Zoom** is
used for exercise sessions of partner audiences, and **HackMD** is
used for a continuous Q&A session.

**Time, date:**  7 and 9-10 June (Tue, Thu-Fri). 11:50-16:00 EEST

**Place:** Online via public livestream, Zoom exercise sessions for
partners.

**Registration:** Not yet open.  Attending individual sessions is fine.

**Cost:** Free of charge for FGCI consortium members including Aalto
employees and students.  Livestream is free to everyone.

**Additional course info at:** scip@aalto.fi



Schedule
--------

**All times are EEST (Europe/Helsinki time)!**

The daily schedule will be adjusted based on the audience's questions.
There will be frequent breaks and continuous questions time going on,
this is the mass equivalent of an informal help session to get you
started with the computing resources.


.. admonition:: Subject to change

   This is last year's schedule.  It will be updated for this year,
   but the overall times and plan are correct.

* **Day #1 (Tue 7.jun):** Basics and background

  - **12:00--12:25: Me and HPC or: How I learned to stop worrying
    and love the computing.**

    Are you at the start of your scientific computing journey?

    Would you like to hear tips and tricks from someone who knows
    what they are doing, but still remembers what it was like to
    be a newbie?

    In this talk a we will get a personal views of high-performance
    computing from a final year PhD student and one of our staff
    scientists.

  - **12:25--12:50: Scientific Computing workflows at Aalto**

    The types of services available at Aalto and many other
    universities, a summary of what you might actually use in the next
    six months.

    - Material: https://hackmd.io/@AaltoSciComp/SciCompIntro
    - Material: :doc:`/triton/usage/workflows`
    - Breakout rooms for other sites (as available).

  - **13:00--13:25: What is HPC?  An analogy with cooking**

  - **13:25--13:50: A tour of scientific computing skills and
    tools**

    There are so many tools available for computing.  We'll describe
    some of most important things and give you links to your next
    steps.

    - Material: https://hackmd.io/@AaltoSciComp/ToolsOfScientificComputing

  - **14:00--14:50: Special topic #2/#3**

  - **15:00--15:45: Connecting to a HPC cluster as part of**
    :doc:`winter-kickstart`

    - Required if you are attending the Triton/HPC tutorials the
      following days.
    - 15:00--15:20?: Livestream introduction to connecting
    - 15:??--??: Individual help time in Zoom (links sent to
      registered participants)
    - Material: :doc:`/triton/tut/connecting`

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

  - **14:00 -- 14:30: Laptops to Lumi**

    You now know of basics of using a computing cluster.  What if you
    need more than what a university can provide?  CSC (and other
    national computing centers) have even more resources, and this is
    a tour of them. `Slides here <https://github.com/AaltoSciComp/scicomp-docs/raw/master/training/scip/CSC-services_022022.pdf>`__.

  - **14:40 -- 15:30: Running jobs that can utilize GPU hardware**

    - :doc:`/triton/tut/gpu`

  - **15:30 -- 16:00:** Questions to presenters



Preparation
-----------

Each year the first day has varying
topics presented.  We don't repeat these every year, but we strongly
recommend that you watch these videos yourself as preparation:

* `Basic Linux shell and scripting
  <https://www.youtube.com/watch?v=ESXLbtaxpdI&list=PLZLVmS9rf3nN_tMPgqoUQac9bTjZw8JYc&index=3>`__
  (important) (or read/watch the shorter :doc:`crash course
  </scicomp/shell>` / `video <https://youtu.be/56p6xX0aToI>`__)
* `When and how to ask for help
  <https://www.youtube.com/watch?v=5fgXXz3fzdM>`__ (very useful)
* `Git intro
  <https://www.youtube.com/watch?v=r9AT7MqmLrU&list=PLZLVmS9rf3nOaNzGrzPwLtkvFLu35kVF4&index=5>`__ (useful)

**How to attend:** Online workshops can be a productive format, but it
takes some effort to get ready.  Browse these resources:

* `Attending a livestream workshop
  <https://coderefinery.github.io/manuals/how-to-attend-stream/>`__,
  good to read in detail (ignore the CodeRefinery-specific parts).
* `How to use HackMD to take answer questions and hold discussions <https://coderefinery.github.io/manuals/hackmd-mechanics/>`__.




Technical prerequisites
-----------------------

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



Follow-up courses
-----------------

While not an official part of this course, we suggest these videos
(co-produced by our staff) as a follow-up perspective:

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
