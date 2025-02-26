===============================================================
February 2025 / Intro to Triton and HPC /  HPC Winter Kickstart
===============================================================

.. admonition:: Quick links
   :class: important

   * News and important links (20/02/2025):

     * Link to register: https://link.webropol.com/ep/hpcwinter25
     * See the time-line below
     * Livestream (morning): https://twitch.tv/coderefinery
     * Video playlist: https://www.youtube.com/playlist?list=PLZLVmS9rf3nOeuqXNa8tS-tDtdQrES2We
     * Exercises (afternoon): *Link sent to registered participants*
     * Notes document: *Link sent to registered participants*



For winter 2025, we are running an intensive version (one-day-only) of our **Kickstart course**.
The longer version of the course will be held on the first week of June and will last for 3 half days

Learning goals
--------------

* Learn the basics of High Performance Computing with slurm
* Watch a step-by-step example of the typical data analysis workflow with Aalto Triton HPC cluster
* Engage with hands-on exercises to make sure you are able to run your analysis on Triton

This course is part of :doc:`Scientific Computing in Practice <index>` lecture series
at Aalto University, supported by many others outside Aalto, and offered to others as part of `CodeRefinery <https://coderefinery.org>`__.



Practical information
---------------------

The course happens on Wed 26 February 2025 and is divided in two parts:

**Morning lectures** (9:45 - 12:00 EET): This is the **livestream demo** part of the course. Everyone may attend the **livestream** at
https://twitch.tv/coderefinery, no registration needed. This is done so that we get a higher quality recording without any personal data from course participants

**Lunch** (12:00 - 13:00 EET): Lunch on your own

**Afternoon hands-on session** (13:00 - 16:00): This is the practical part of the course. We will be connected to the same zoom room and do the exercises together.

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

  * 09:45--10:00: Joining time/icebreaker

  * **10:00--10:15 Introduction: what are HPC systems?** *Enrico Glerean and
    other staff* 
    
    - Materials: :doc:`../../training/kickstart/introoneday` and `A short introduction to scientific computing <https://hackmd.io/@AaltoSciComp/SciCompIntro>`__

  * **10:15--11:45: A day in the life of an HPC user** *Richard Darst and Simo Tuomisto*

    - 1. :doc:`Check your connection to the cluster </triton/tut/connecting>`
    - 2. :doc:`Moving data to the cluster </triton/tut/storage>`
    - 3. Datasets/projects that could be used for the demo:

        - `"Ngrams example" <https://github.com/AaltoSciComp/hpc-examples/tree/master/ngrams>`__

    - 4. Loading an application? Not needed but good to remeber (e.g. python env): :doc:`Modules </triton/tut/modules>`
    - 5. :ref:`Analysing data with slurm <tutorials>`

        - 5.1 :doc:`Getting an interactive session </triton/tut/interactive>`
        - 5.2 :doc:`Non-interactive serial job </triton/tut/interactive>`
        - 5.3 :doc:`Parralelisation and array jobs </triton/tut/parallel>`, :doc:`[ref2] </triton/tut/array>`
        - 5.4 More advanced parallelisation - discussion only - (:doc:`multithreading/multiprocessing </triton/tut/parallel-shared>`, :doc:`MPI </triton/tut/parallel-mpi>`, :doc:`GPUs </triton/tut/gpu>`

    - 6. Visualising the results (e.g OOD)
    - 7. Moving the data away from the cluster



  * **11:45--12:00: Where to go from here and how to ask for help (Susanne Merz and Enrico Glerean)**

    - :doc:`How to get help from us </help/index>`
    - :doc:`Skills map, our courses, CodeRefinery, CSC </training/index>`


  * **12:00--13:00: Lunch break (on your own)**

  * **13:00--16:00: Hands-on exercises with Triton HPC cluster**

    - Main room: Lobby and Generic questions (SM)
    - Room 1: Hands-on with exercises from the morning, Slurm and Triton basics (RD, EG)
    - Room 2: Connecting questions? (TP)
    - Room 3: GPUs and parallelization (ST)
    - Room 4: AI / LLMs (YT)
    - Room 5: Speech2Text (TR)

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
