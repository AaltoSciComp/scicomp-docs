=====================================================================
June 2023 / Intro to Scientific Computing /  HPC Summer Kickstart
=====================================================================

.. admonition:: Quick links
   :class: important

   * Videos are on YouTube in `this playlist
     <https://www.youtube.com/playlist?list=PLZLVmS9rf3nMKR2jMglaN4su3ojWtWMVw>`__.

   * Final notes

     * Thanks to all who attended, we hope you enjoyed the course as
       much as we enjoyed giving it.
     * We know that this course was a lot.  Learning scientific
       computing is a lot.  If you felt overwhelmed, it's OK: do what
       you can for your work, and keep referring back to our material
       as you work.  Consider coming back next year for the course
       again - you'll learn much more then.

   * You can still `register
     <https://link.webropol.com/ep/scicomphpc2023>`__ to get HackMD
     access for Q&A.  **Sharing**: You may definitely share the
     livestream with others!
   * Quick links

     * **When**: 6,7,8/June/2023 11:50-16:00 EEST, **Where**: https://www.twitch.tv/coderefinery
     * **Preparation**: Check the :ref:`prerequisites below
       <kickstart-2023-prep>` and the schedule.
     * Videos will appear in `this youtube playlist
       <https://www.youtube.com/playlist?list=PLZLVmS9rf3nMKR2jMglaN4su3ojWtWMVw>`__
       the same evening and `on twitch
       <https://www.twitch.tv/coderefinery/videos>`__ for 7 days.
     * `Archived Q&A <https://hackmd.io/@AaltoSciComp/scicomphpc2023archive>`__


Kickstart is a three × half day course for researchers to get
started with high-performance computing (HPC) clusters.
**The first day serves as a guide to skills you need in your career:** a map to the types of
resources that are available and skills you may need in your career,
so that you can be prepared when you
need more in the future.  This part is especially suitable to new researchers or students trying to
understand computational/data analysis options available to them.  It
won't go into anything too deep, but will provide you with a good
background for your next steps: you will know what resources are
available and know the next steps to use them.

**The second and third days take
you from being a new user to being competent to run your code at a
larger scale than you could before using a computer cluster.**
This part is good for any researcher who thinks they may need to
scale up to larger resources in the next six months, in any field -
this is many new researchers in our departments.
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



Practical information
---------------------

This is a **livestream course with distributed in-person exercise and
support**. Everyone may attend
the **livestream** at https://twitch.tv/coderefinery, no registration
needed, and this is the primary way to watch all sessions.  Aalto has
an **in-person exercise and support session** (location TBA), as do
some other partners, and a **collaborative document** is
used for a continuous Q&A session.

**Time, date:**  6 -- 8 June (Tue--Thu). 11:50-16:00 EEST

**Place:** Online via public livestream, Zoom exercise sessions for
partners, and probably in-person discussion/practice rooms at some
campus.

**Registration:** Please register at this link:
https://link.webropol.com/ep/scicomphpc2023 . It's OK to attend
only individual sessions is fine.

**Cost:** Livestream is free to everyone.  Aalto in-person is free of 
charge for FGCI consortium members including Aalto employees and
students.

**Additional course info at:** scip@aalto.fi

.. admonition:: If you can't attend day 1 (Aalto CS Summer day)
   :class: dropdown

   Most of day 1 is good background information, but not strictly
   required.  You *will* need the Triton connection set up before
   day 1.  We recommend you look at the :doc:`connecting tutorial
   </triton/tut/connecting>` and get this set up in advance (either by
   talking to a colleague or our :doc:`daily garage </help/garage>`).
   Then, try to watch the relevant videos Wednesday morning or Tuesday
   evening.



Other universities
------------------

**If you are not at Aalto University**, you can follow along with the
course and will learn many things anyway.  The course is designed to
be useful to people outside of Aalto, but some of the examples
won't directly work on your cluster (most will, anyway we will give
hints about adapting).  How to register if you are not at Aalto:

* Regardless of where you are from, you may use the primary registration
  form to get emails about the course.  You don't get anything else.
* Participants from **University of Helsinki** can follow how to connect
  to their Kale/Turso cluster by following `their own instructions
  <https://wiki.helsinki.fi/pages/viewpage.action?pageId=408323613>`__.
* Participants from **University of Oulu**: please follow instructions on
  `how to access the Carpo2 computing cluster <https://ict.oulu.fi/17120/?page&lang=en>`__.
* **Tampere**: this course is recommended for all new Narvi users and also all
  interested in HPC. Most things should work with simply replacing triton
  -> narvi. Some differences in configuration are listed in
  `Narvi differences
  <https://narvi-docs.readthedocs.io/narvi/kickstart-diffs.html>`__
* [no active support] `CSC <https://csc.fi>`__ (Finland): Participants with `CSC user
  account <https://docs.csc.fi/accounts/>`__ can try examples also in
  CSC supercomputers, see the `overview of CSC supercomputers
  <https://docs.csc.fi/computing/overview/>`__ for details on
  connecting, etc.

If you want to get your site listed here and/or help out, contact us
via the `CodeRefinery chat
<https://coderefinery.github.io/manuals/chat/>`__ (#kickstart-aalto stream).
We have :doc:`docs for other sites' staff
</triton/tut/required-cluster-setup>` to know what might be different
between our course and your cluster.



Schedule
--------

**All times are EEST (Europe/Helsinki time)!**

The daily schedule will be adjusted based on the audience's questions.
There will be frequent breaks and continuous questions time going on,
this is the mass equivalent of an informal help session to get you
started with the computing resources.


.. admonition:: Subject to change

   Schedule may still have minor updates, please check back for
   the latest.

* **Day #1 (Tue 6.jun):** Basics and background

  * 11:50--12:00: Joining time/icebreaker

  * **12:00--12:10 Introduction, about the course** *Richard Darst and
    other staff* Materials: :doc:`../../training/kickstart/intro`

  * **12:10--12:25: From data storage to your science** *Enrico
    Glerean and Simo Tuomisto*

    - Data is how most computational work starts, whether it is
      externally collected, simulation code, or generated.  And these
      days, you can work on data even remotely, and these workflows
      aren't obvious.  We discuss how data storage choices lead to
      computational workflows. Materials: `SciComp Intro
      <https://hackmd.io/@AaltoSciComp/SciCompIntro>`__

  * **12:25--12:50: What is parallel computing?  An analogy with
    cooking** *Enrico Glerean and Thomas Pfau*

    - In workshops such as this, you will hear lots about parallel
      computing and how you need it, but rarely get a understandable
      introduction to how they relate and which are right for you.
      Here, we give a understandable metaphor with preparing large
      meals.  `Slides <https://docs.google.com/presentation/d/e/2PACX-1vQLTzWkRy7Du3jjPJ6Y9BqKczU_JcSTEL6XsndrNJ7ylzi4RWeEy8lhfWZQu_lpwbAKroh51qqLoPFG/pub>`__

  * **13:00--13:25: How big is my calculation?  Measuring your
    needs.** *Simo Tuomisto and Thomas Pfau*

    - People often wonder how many resources their job needs, either on
      their own computer or on the cluster.  When should you move to a
      cluster?  How many resources to request?  We'll go over how we
      think about these problems. Materials:
      :doc:`How big is my program? </triton/usage/program-size>`

  * **13:25--13:50: Behind the scenes: the humans of scientific
    computing** *Richard Darst and Teemu Ruokolainen*

    - Who are we that teach this course and provide SciComp support?
      What makes it such a fascinating career?  Learn about what goes on
      behind the scenes and how you could join us.

  * **14:00--14:45: Connecting to a HPC cluster** *Thomas Pfau and
    Jarno Rantaharju*

    - Required if you are attending the Triton/HPC tutorials the
      following days, otherwise the day is done.
    - 14:00--14:20?: Livestream introduction to connecting
    - 14:??--15:00: Individual help time in Zoom (links sent to
      registered participants)
    - Break until 15:00 once you get connected.
    - Material: :doc:`/triton/tut/connecting`


  * **15:00--15:25: Using the cluster from the shell (files
    and directories)** *Richard Darst and Teemu Ruokolainen*

    - Once we connect, what can we do?  We'll get a tour of the shell,
      files diretories, and how we copy basic data to the cluster.
      Material: :doc:`/triton/tut/cluster-shell`.

  - **15:25--15:50: What can you do with a computational cluster?**
    *(Jarno Rantaharju and Richard Darst)*

    - See several real examples of how people use the cluster (what you can
      do at the end of the course): 1) Large-scale computing with array
      jobs, 2) Large-scale parallel computing.  Demo.

  * Preparation for day 2:

    - Remember to read/watch the "shell crash course" (see "Preparation"
      below) if you are not yet confident with the command line.  This
      will be useful for tomorrow.

* **Day #2 (Wed 7.jun):** Basic use of a cluster *(Richard Darst, Simo
  Tuomisto)*

  - 11:50--12:00: Joining time/icebreaker

  - **12:00--12:05: Introduction to days 2-3**

    - :doc:`/triton/tut/intro`

  - **12:05--12:30 Structure of a cluster: The Slurm queueing system**

    - :doc:`/triton/tut/slurm`

  - **12:30--15:00: Running your first jobs in the queue**

    - :doc:`/triton/tut/interactive`
    - :doc:`/triton/tut/serial`
    - :doc:`/triton/tut/monitoring`

  - **15:00--15:30: Other things you should know about the HPC environment**

    - :doc:`/triton/tut/applications`
    - :doc:`/triton/tut/modules`
    - :doc:`/triton/tut/storage`
    - :doc:`/triton/tut/remotedata`

  - **15:30--16:00: Q&A**

* **Day #3 (Thu 8.jun):** Advanced cluster use *(Simo Tuomisto, Richard
  Darst)*

  - 11:50--12:00: Joining time/icebreaker

  - **12:00--12:30: What does "parallel" mean?**:

    - :doc:`/triton/tut/parallel`

  - **12:30--14:00: Forms of parallelization**

    - :doc:`/triton/tut/array`
    - :doc:`/triton/tut/parallel-shared`
    - :doc:`/triton/tut/parallel-mpi`

  - **14:00--14:30: Laptops to Lumi**

    - You now know of basics of using a computing cluster.  What if you
      need more than what a university can provide?  CSC (and other
      national computing centers) have even more resources, and this is
      a tour of them. `Slides from 2022 here <https://github.com/AaltoSciComp/scicomp-docs/raw/master/training/scip/CSC-services_062022.pdf>`__.

  - **14:40--15:30: Running jobs that can utilize GPU hardware:**

    - :doc:`/triton/tut/gpu`

  - **15:30--16:00: Ask us anything**



.. _kickstart-2023-prep:

Preparation
-----------

We strongly recommend you are familiar with the Linux command line.
Browsing the following material is sufficient:

* `Basic Linux shell and scripting
  <https://www.youtube.com/watch?v=ESXLbtaxpdI&list=PLZLVmS9rf3nN_tMPgqoUQac9bTjZw8JYc&index=3>`__
  (important) (or read/watch the shorter :doc:`crash course
  </scicomp/shell>` / `video <https://youtu.be/56p6xX0aToI>`__)

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



Next steps / follow-up courses
------------------------------

Keep the :doc:`Triton quick reference </triton/ref/index>` close (or
equivalent for your cluster), or print `this cheatsheet
<https://aaltoscicomp.github.io/cheatsheets/triton-cheatsheet.pdf>`__
if that's your thing.

Each year the first day has varying topics presented.  We don't repeat
these every year, but we strongly recommend that you watch some of
these videos yourself as preparation.

Very strongly recommended:

* `When and how to ask for help
  <https://www.youtube.com/watch?v=5fgXXz3fzdM>`__ (very useful)
* `Git intro
  <https://www.youtube.com/watch?v=r9AT7MqmLrU&list=PLZLVmS9rf3nOaNzGrzPwLtkvFLu35kVF4&index=5>`__ (useful)

Other useful material in previous versions of this course:

* Scientific Computing workflows at Aalto - concepts apply to other
  sites, too (optional): `lecture notes
  <https://hackmd.io/@AaltoSciComp/SciCompIntro>`__ and `video
  <https://www.youtube.com/watch?v=Oz37XAzWFhk>`__, :doc:`reference
  material </triton/usage/workflows>`.
* Tools of scientific computing (optional): `lecture notes
  <https://hackmd.io/@AaltoSciComp/ToolsOfScientificComputing>`__ and
  `video <https://www.youtube.com/watch?v=kXYfxXEb0Go>`__

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
