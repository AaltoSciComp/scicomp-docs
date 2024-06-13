=====================================================================
June 2024 / Intro to Scientific Computing /  HPC Summer Kickstart
=====================================================================

.. admonition:: Quick links
   :class: important

   * News (final):

     - We hope that you are inspired by this course.  There is plenty
       more to learn, keep reading and asking.
     - The website will be updated with some more recommended
       follow-up info (extra special topics we haven't covered this
       time).
     - Things we would recommend for follow-ups:

       - `Kickstart best-of list <https://www.youtube.com/playlist?list=PLZLVmS9rf3nPd3HpX5x3Ff2IAyS6kuhMi>`__
         has some videos from this year, but also videos that are
         taught only some years.  Check this list for things you
         *didn't* see this year, and consider watching them.
       - :doc:`Python environments with Conda
	 </triton/apps/python-conda>` - a page on this site.
       - `CodeRefinery workshop <https://coderefinery.org>`__ -
	 software and programming tools for scientists and researchers
	 (also a livestream course)
       - `Python for Scientific Computing
	 <https://aaltoscicomp.github.io/python-for-scicomp>`__ (also
	 livestream, later this year)

   * Watching links

     * Livestream: https://twitch.tv/coderefinery
     * Notes doc: for registered participants, you can register and
       get it automatically
     * `Archive notes doc <https://hackmd.io/@AaltoSciComp/scicomphpc2023archive>`__
     * Videos (2024) will end up on `this youtube playlist
       <https://www.youtube.com/playlist?list=PLZLVmS9rf3nOeuqXNa8tS-tDtdQrES2We>`__
       the same evening, and appear `on Twitch
       <https://twitch.tv/coderefinery/videos>`__ immediately.

   * Registrations are open at
     https://link.webropol.com/ep/scicompsummer2024


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
support**. Everyone may attend the **livestream** at
https://twitch.tv/coderefinery, no registration needed, and this is
the primary way to watch all sessions.  Aalto sometimes an **in-person
exercise and support session**, as do some other
partners, and a **shared notes** is used for a continuous
Q&A session.

**Time, date:**  4 -- 6 June 2024 (Tue--Thu). 11:50-16:00 EEST /
10:50-15:00 CEST

**Place:** Online via public livestream, Zoom exercise sessions for
partners, and probably in-person discussion/practice rooms at some
campus.

**Registration:** Please register at this link:
https://link.webropol.com/ep/scicompsummer2024 .
It's OK to register and attend only individual sessions.

**Cost:** Livestream is free to everyone.  Aalto in-person is free of
charge for FCCI consortium members including Aalto employees and
students.

**Additional course info at:** scip@aalto.fi



Other universities
------------------

**If you are not at Aalto University**, you can follow along with the
course and will learn many things anyway.  The course is designed to
be useful to people outside of Aalto, but some of the examples
won't directly work on your cluster (most will, anyway we will give
hints about adapting).  How to register if you are not at Aalto:

* Regardless of where you are from, you may use the `primary registration
  form <https://link.webropol.com/ep/scicompsummer2024>`__ to get emails about the course.  You don't get anything else.
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



Schedule
--------

**All times are EEST (Europe/Helsinki time)!**

The daily schedule will be adjusted based on the audience's questions.
There will be frequent breaks and continuous questions time going on,
this is the mass equivalent of an informal help session to get you
started with the computing resources.


.. admonition:: Subject to change

   Schedule may still have minor updates as it happens.


* **Day #1 (Tue 4.jun):** Basics and background

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
      
  * **12:25--12:50: (Computational) reproducibility and open science** *Enrico Glerean and Samantha Wittke*
     
    - Transparency in science is one of the core principles in research integrity. Did you know that half of published studies are actually not reproducible? Here we give an overview of CodeRefinery learning materials for those who want to start picking up good enough practices like git version control, clear project folder structure, conda environments, containers. Materials: `Reproducible research (CodeRefinery) <https://coderefinery.github.io/reproducible-research/>`__  

  * **12:50--13:00: Break**
  
  * **13:00--13:25: Behind the scenes: the humans of scientific computing** *Richard Darst and a special guest*

    - Who are we that teach this course and provide SciComp support?
      What makes it such a fascinating career?  Learn about what goes on
      behind the scenes and how you could join us.
  
  * **13:25--13:50: What can you do with a computational cluster?**
    *(Simo Tuomisto and Enrico Glerean)*

    - A couple of real examples of how people use the cluster (what you can
      do at the end of the course): 1) Multi-cpu-node computations with LAMMPS, 2) Suprise demo.  
      
  * **13:50--14:00: break** 
  
  * **14:00--14:50: Connecting to a HPC cluster** *Thomas Pfau and
    Jarno Rantaharju*

    - Required if you are attending the Triton/HPC tutorials the
      following days, otherwise the day is done.
    - 14:00--14:20: Livestream introduction to connecting (ssh, openondemand)
    - 14:20--14:50: Individual help time in Zoom (links sent to
      registered participants for the affiliated HPC clusters)
    - Break until 15:00 once you get connected.
    - Material: :doc:`/triton/tut/connecting`

  * **14:50--15:00: Break**

  * **15:00--15:25: How to ask for help with (super)computers** *Radovan Bast and Richard Darst*

    - It’s dangerous to go alone, take us! Don’t waste time struggling, there are plenty of people here for you.
      Materials: `Slides <https://zenodo.org/records/8392763>`__.
      
  * **15:25--15:50: VS Code on HPC** *Hossein Firooz and Richard Darst*
   
    - One can use clusters also without the shell, but it comes with some extra care. Materials: :doc:`/triton/apps/vscode`
  * **15:50--16:00: Wrapping-up and getting ready for day 2** *Richard Darst*

  * Preparation for day 2:

    - Remember to read/watch the "shell crash course" (see "Preparation"
      below) if you are not yet confident with the command line.  This
      will be useful for tomorrow.


* **Day #2 (Wed 5.jun):** Basic use of a cluster *(Richard Darst, Simo
  Tuomisto)*

  - 11:50--12:00: Joining time/icebreaker

  - **12:00--12:05: Introduction to days 2-3**

    - :doc:`/triton/tut/intro`

  - **12:05--12:30 Structure of a cluster: The Slurm queueing system**

    - :doc:`/triton/tut/slurm`

  - **12:30--15:00: Running your first jobs in the queue**

    - Cluster shell, section :ref:`triton-tut-example-repo`
    - :doc:`/triton/tut/interactive`
    - :doc:`/triton/tut/serial`
    - :doc:`/triton/tut/monitoring`

  - **15:00--15:30: Other things you should know about the HPC environment**

    - :doc:`/triton/tut/applications`
    - :doc:`/triton/tut/modules`
    - :doc:`/triton/tut/storage`
    - :doc:`/triton/tut/remotedata`

  - **15:30--16:00: Q&A**

* **Day #3 (Thu 6.jun):** Advanced cluster use *(Simo Tuomisto, Richard
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
      a tour of them. `Slides here <https://github.com/AaltoSciComp/scicomp-docs/raw/master/training/scip/CSC-services_062024.pdf>`__.

  - **14:40--15:30: Running jobs that can utilize GPU hardware:**

    - :doc:`/triton/tut/gpu`

  - **15:30--16:00: Ask us anything**



.. _kickstart-2024-prep:

Preparation
-----------

We strongly recommend you are familiar with the Linux command line.
Browsing the following material is sufficient:

* :doc:`/triton/tut/cluster-shell` (`video
  <https://youtu.be/bJMmz5-svJo?t=7&list=PLZLVmS9rf3nMKR2jMglaN4su3ojWtWMVw&index=8>`__)
  - important background knowledge for days 2-3.

* A more detailed version of the above is `Basic Linux shell and scripting
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
