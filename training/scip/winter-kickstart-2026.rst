==============================================================
January 2026 / Intro to Triton and HPC /  HPC Winter Kickstart
==============================================================

.. admonition:: Quick links
   :class: important

   * News and important links (12/01/2026):

     * Link to register: https://link.webropol.com/ep/kickstartwinter2026
     * See the time-line below
     * Livestream: https://twitch.tv/coderefinery
     * Notes document: *Link sent to registered participants*



For winter 2026, we are running an intensive version (one-day-only) of our **Kickstart course**.
The longer version of the course will be held on the first week of June and will last for 3 half days

Learning goals
--------------

* Learn the basics of High Performance Computing with slurm
* Watch a step-by-step example of the typical data analysis workflow with Aalto Triton HPC cluster
* Engage with hands-on exercises to make sure you are able to run your analysis on Triton

This course is part of :doc:`Scientific Computing in Practice <index>` lecture series
at Aalto University, supported by many others outside Aalto, and offered to others as part of `CodeRefinery <https://coderefinery.org>`__.
For those who need it, it is possible to get 1 ECTS for Aalto University doctoral and master students as part of course SCI-L1010. More info later.


Practical information
---------------------

The course happens on Wed 28 January 2026. The schedule below is being updated.

**Streaming lectures** (11:50 - 15:00 EET): The course is run as a **livestream demo**. Everyone may attend the **livestream** at
https://twitch.tv/coderefinery, no registration needed. This is done so that we get a higher quality recording without any personal data from course participants

**Cost:** Free!

**Language:** English

**Additional course info at:** scip@aalto.fi




Schedule
--------

**All times are EEST (Europe/Helsinki time)!**

The daily schedule will be adjusted based on the audience's questions.
There will be frequent breaks and continuous questions time going on,
this is the mass equivalent of an informal help session to get you
started with the computing resources.


.. admonition:: Subject to change

   Schedule may still have minor updates as it happens.

  * 11:50--12:00: Joining time/icebreaker

  * **12:00--12:15 Introduction: what are HPC systems?** *Enrico Glerean and
    Hossein Firooz*

    - Materials: :doc:`../../training/kickstart/introoneday` and `A short introduction to scientific computing <https://hackmd.io/@AaltoSciComp/SciCompIntro>`__

  * **12:15--13:30: A day in the life of an HPC user** *Simo Tuomisto and Thomas Pfau*

    1. What is a cluster
    2. :doc:`ngrams an example problem </triton/tut/exercises-ngrams>`
    3. Set up our project
         - :doc:`Get the files to triton </triton/tut/storage>`
         - Some initial tests via interactive sessions
    4. Run code on cluster
         - :doc:`The Queue system </triton/tut/slurm>`
         - :doc:`Interactive Sessions </triton/tut/interactive>`
         - :doc:`Batch submission scripts </triton/tut/serial>`
         - :doc:`Check Your Jobs </triton/tut/monitoring>`
    5. Run code parallel
         - :doc:`What are array jobs and how do they work </triton/tut/array>`
         - :doc:`Multiprocessing on the cluster </triton/tut/parallel>`
    6. :doc:`Looking at results and outputs </triton/tut/monitoring>`
    7. Speed considerations
         - :doc:`IO limitations </triton/tut/storage>`
         - :doc:`GPU / CPU interactions </triton/tut/gpu>`

  * **13:30--13:45: Break**

  * **13:45--14:30: Moving your program to an HPC cluster** *Simo Tuomisto and Patricia Hernandez Leon*

    - Materials: `Moving your program to an HPC cluster <https://hackmd.io/@AaltoSciComp/wks2026-moving-programs>`__
    - Covered topics include: storage, environment modules and program installations.

  * **14:30--15:00: What is SciComp and who can you ask for help?** *Enrico Glerean and Susanne Merz*

    - :doc:`How to get help from us </help/index>`
    - :doc:`Skills map, our courses, CodeRefinery, CSC </training/index>`



Preparation
-----------

We strongly recommend you are familiar with the Linux command line.
Browsing the following material is sufficient:

* Command line/shell basics `[ref] <https://scicomp.aalto.fi/triton/tut/cluster-shell>`__ `[video] <https://youtu.be/bJMmz5-svJo?t=7&list=PLZLVmS9rf3nMKR2jMglaN4su3ojWtWMVw&index=8>`__
  - **Important background knowledge which we won't go over again.**

  - A more detailed version of the above, for those who automate a lot of analysis, is `[Basic Linux shell and scripting]<https://www.youtube.com/watch?v=ESXLbtaxpdI&list=PLZLVmS9rf3nN_tMPgqoUQac9bTjZw8JYc&index=3>`__
  - Or read/watch the shorter :doc:`crash course
    </scicomp/shell>` / `video <https://youtu.be/56p6xX0aToI>`__.


* Watch `this background info about why we use computer clusters <https://www.youtube.com/playlist?list=PLZLVmS9rf3nNDHRo1Baz_JVQWDI0mTYyB>`__.  This is important information for *why* we are in this course, which we *won't cover directly*.  The most important videos are the `intro (what is a cluster and why?) <https://www.youtube.com/watch?v=yqGtnA7CUtU&list=PLZLVmS9rf3nNDHRo1Baz_JVQWDI0mTYyB&index=1&pp=gAQBiAQB>`__, `storage hierarchy (how the data looks) <https://www.youtube.com/watch?v=JAR9xyy5rcE&list=PLZLVmS9rf3nNDHRo1Baz_JVQWDI0mTYyB&index=2&pp=gAQBiAQB>`__, and `the Slurm job scheduler (how the cluster runs things) <https://www.youtube.com/watch?v=Y73A7lXISxU&list=PLZLVmS9rf3nNDHRo1Baz_JVQWDI0mTYyB&index=5&pp=gAQBiAQB>`__.



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

* `Installing Python packages with Conda
  <https://youtu.be/dmTlNh3MWx8>`__ (Note that conda on new-Triton has changed.  See :doc:`/triton/apps/conda` for details)
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
  <https://hands-on.coderefinery.org>`__ for an online course.
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
