=====================================================================
June 2025 / Intro to Scientific Computing /  HPC Summer Kickstart
=====================================================================

.. admonition:: Quick links
   :class: important


   * **Registrations are open**: https://link.webropol.com/ep/scicompsummer2025

   * News:

     - 21.5.2025: Course structure updated!

   * Watching links

     * Livestream: https://twitch.tv/coderefinery
     * Notes doc: for registered participants, you can register and
       get it automatically
     * Zoom: live zoom support for students from partner organisations



**Kickstart: Introduction to HPC and Scientific Computing**

*Kickstart* is a three half-day course for researchers and students who want to get started with high-performance computing (HPC) and scientific computing workflows.

* **Day 1**: focuses on the basics of HPC through practical examples. You will learn how to connect to a supercomputer, how storage choices affect your workflow, how to transfer data, and run your first jobs with slurm.
* **Day 2** introduces tools and practices for efficient and responsible data science. Topics include Conda environments, batch and array jobs, job monitoring, software modules, parallel computing
* **Day 3** covers more advanced topics: GPU usage, working with real examples: local open-weights LLMs (large language models).

By the end of the course, you will be ready to use HPC clusters effectively with hands-on skills and ready-made examples.


If you are at Aalto University: the course is obligatory for all new Triton users and recommended to all interested in the field.

This course is part of :doc:`Scientific Computing in Practice <index>` lecture series
at Aalto University, supported by many others outside Aalto, and offered to others as part of `CodeRefinery <https://coderefinery.org>`__.


Schedule
--------

.. admonition:: Subject to change

   Schedule may still have updates before the course, and also during
   as we adapt to audience questions and interests.

**Times automatically converted to:** :localtime2:`3 Jun 2025 (zzz)`

* **Day 1 (Tue 3 June)**

  * :localtime:`3 June 9:50 +03:00 (hh:mm [(on ]YYYY-MM-DD[)])`: Joining time/icebreaker

  * :localtime:`3 June 10:00 +03:00` **Introduction, about the course** Materials:
    :doc:`../../training/kickstart/intro` (EG, )

    * Intro to SciComp and HPC: (`Material <https://hackmd.io/@AaltoSciComp/SciCompIntro>`__, `Video link from 2024 <https://www.youtube.com/watch?v=8qQ9riStB0Y&list=PLZLVmS9rf3nOeuqXNa8tS-tDtdQrES2We&index=3>`__)

  * :localtime:`3 June 10:10 +03:00` **The HPC Kitchen** (RD, TP)

    - `Video playlist <https://www.youtube.com/watch?v=yqGtnA7CUtU&list=PLZLVmS9rf3nNDHRo1Baz_JVQWDI0mTYyB>`__, `Slides (separate from the videos) <https://docs.google.com/presentation/d/16BTILZlUvEzCt6FfMsB9sSZm0PZHHXLBthE5QfoSrjo/edit>`__

  * :localtime:`3 June 10:20 +03:00` **Connecting to the cluster** (TP, SM)

  * :localtime:`3 June 10:50 +03:00`  Break

  * :localtime:`3 June 11:00 +03:00`  **CSC resources for scientific computing** (JL)

    - A special guest from `CSC <https://csc.fi>`__ will talk about our national supercomputers Mahti/Puhti/LUMI and how to use them in practice.

  * :localtime:`3 June 12:00 +03:00` Lunch break

  * :localtime:`3 June 13:00 +03:00` **Setting up for a new project** (RD, ST)

    - :doc:`/triton/tut/intro`
    - `Cluster workflow <example_project>`
    - Cluster shell, section :ref:`triton-tut-example-repo`
    - Big example: Cloning our Gutenberg analysis code to the cluster.
    - :doc:`/triton/tut/storage`
    - :doc:`/triton/tut/remotedata`
    - Big example: Copying the Project Gutenburg data to your work directory

  * :localtime:`3 June 13:40 +03:00` **What is Slurm?** (ST, RD)

    - :doc:`/triton/tut/slurm`

  * :localtime:`3 June 13:50 +03:00` Break

  * :localtime:`3 June 14:00 +03:00` **Interactive jobs** (RD, ST)

    - :doc:`/triton/tut/interactive`
    - Big example: Project Gutenburg n-gram analysis

  * :localtime:`3 June 14:20 +03:00` **First serial jobs** (RD, ST)

    - :doc:`/triton/tut/serial`
    - Big example: Project Gutenburg n-gram analysis

  * :localtime:`3 June 15:00 +03:00` End of day

* **Day 2 (4 June)**

  * :localtime:`4 June 09:50 +03:00 (hh:mm [(on ]YYYY-MM-DD[)])` Connecting, icebreakers, Q&A

  * :localtime:`4 June 10:00 +03:00` **Behind the scenes: the humans of scientific computing** (RD, SM)

    - Who are we that teach this course and provide SciComp support?
      What makes it such a fascinating career?  Learn about what goes on
      behind the scenes and how you could join us.

  * :localtime:`4 June 10:20 +03:00` **Conda** (JR, YT)

    - :doc:`/triton/apps/python-conda`
    - Big example: Make a conda environment for LLMs

  * :localtime:`4 June 11:00 +03:00` Break

  * :localtime:`4 June 11:10 +03:00` **Array jobs** (ST, RD)

    - :doc:`/triton/tut/parallel`
    - :doc:`/triton/tut/array`
    - Big Example: Project Gutenberg book analysis in parallel

  * :localtime:`4 June 12:00 +03:00`: Lunch break

  * :localtime:`4 June 13:00 +03:00` **Monitoring** (ST, RD)

    - :doc:`/triton/tut/monitoring`

  * :localtime:`4 June 13:20 +03:00` **Applications** (RD, ST)

    - :doc:`/triton/tut/applications`
    - :doc:`/triton/tut/modules`

  * :localtime:`4 June 13:40 +03:00` **Research integrity, security, compliance, and reproducibility** (EG, TP)

  * :localtime:`4 June 14:00 +03:00` Break

  * :localtime:`4 June 14:10 +03:00` **Parallel** (ST, RD)

    - :doc:`/triton/tut/parallel-shared`
    - :doc:`/triton/tut/parallel-mpi`
    - Big example: Calculating pi in parallel

  * :localtime:`4 June 15:00 +03:00` End of day

* **Day 3 (5 June)**

  * :localtime:`5 June 9:50 +03:00 (hh:mm [(on ]YYYY-MM-DD[)])` Connecting, icebreaker, Q&A
  * :localtime:`5 June 10:00 +03:00` **How to ask for help with (super)computers** (RD, )

    - It’s dangerous to go alone, take us! Don’t waste time struggling, there are plenty of people here for you.
      Materials: `Slides <https://cicero.xyz/v3/remark/0.14.0/github.com/bast/help-with-supercomputers/main/talk.md/>`__.

  * :localtime:`5 June 10:20 +03:00` **GPUs** (ST, HF)

    - :doc:`/triton/tut/gpu`

  * :localtime:`5 June 10:50 +03:00` Break
  * :localtime:`5 June 11:00 +03:00` **LLM example** (YT, HF)
  * :localtime:`5 June 11:40 +03:00` **Wrap up and summary, ask us anything**
  * :localtime:`5 June 12:00 +03:00` End of day





Practical information
---------------------

This is a **livestream course with distributed in-person exercise and
support**. Everyone may attend the **livestream** at
https://twitch.tv/coderefinery, no registration needed, and this is
the primary way to watch all sessions.  There is constant Q&A via **shared notes**.

**Time, date:**  3 -- 5 June 2025 (Tue--Thu). 10:00-12:00 EEST  (days 1-3) and 13:00-15:00 EEST (days 1-2).

**Place:** Online via public livestream, Zoom exercise sessions for
partners, and probably in-person discussion/practice rooms at some
campuses.

**Registration:** Please register at this link:
https://link.webropol.com/ep/scicompsummer2025 .
It's OK to register and attend only individual sessions.

**Cost:** Livestream is free to everyone.  Aalto in-person is free of
charge for FCCI consortium members including Aalto employees and
students.

**Additional course info at:** scip@aalto.fi



Other universities
------------------

**If you are not at Aalto University**, you can follow along and
probably learn a lot.  We design the course to be useful even to
others outside of Aalto University, but some of the examples won't
directly work on your cluster (most will, anyway we will give hints
about adapting).  How to register if you are not at Aalto:

* Regardless of where you are from, you may use the `primary registration
  form <https://link.webropol.com/ep/scicompsummer2025>`__ to get emails about the course.  You don't get anything else.
* Participants from **University of Helsinki** can follow how to connect
  to their Kale/Turso cluster by following `their own instructions
  <https://wiki.helsinki.fi/pages/viewpage.action?pageId=408323613>`__.
* Participants from **University of Oulu**: please follow instructions on
  `how to access the Carpo2 computing cluster <https://ict.oulu.fi/17120/?page&lang=en>`__.
* **Tampere**: this course is recommended for all new Narvi users and also all
  interested in HPC. Most things should work with simply replacing triton
  -> narvi. Some differences in configuration are listed in
  `Narvi differences
  <https://narvi-docs.readthedocs.io/kickstart-diffs.html>`__
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










.. _kickstart-2025-prep:

Preparation
-----------

We strongly recommend you are familiar with the Linux command line.
Browsing the following material is sufficient:

* :doc:`/triton/tut/cluster-shell` (`video
  <https://youtu.be/bJMmz5-svJo?t=7&list=PLZLVmS9rf3nMKR2jMglaN4su3ojWtWMVw&index=8>`__, `shorter video <https://www.youtube.com/watch?v=xbTTDLA3txI>`__)
  - important background knowledge for command line work.



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
    </triton/accounts>` in advance.  Others: Access to your computing cluster.

  * Attempt to :doc:`Connect to your cluster </triton/tut/connecting>`
    (don't worry, we will also go over this on day 1 anyway).




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

* `Installing Python packages with Conda
  <https://youtu.be/dmTlNh3MWx8>`__ (Note that conda on new-Triton has changed.  See :doc:`/triton/apps/python-conda` for details)
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
