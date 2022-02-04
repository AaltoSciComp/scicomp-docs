=================================================
Feb 2022 / Introduction to HPC (Winter Kickstart)
=================================================

.. admonition:: Quick Links

   * To register for the February 2022 sessions please visit https://link.webropol.com/s/introHPCJan2022
   * Day 1 course page: :doc:`getting-started-with-scientific-computing`
   * Lesson materials: :ref:`Triton tutorials <tutorials>`, see below
     for details.
   * Twitch has videos for 14 days: https://www.twitch.tv/coderefinery/videos
   * Youtube playlist (updated each evening): https://youtube.com/playlist?list=PLZLVmS9rf3nOKhGHMw4ZY57rO7tQIxk5V

Winter Kickstart is a two × half day course for researchers to get
started with high-performance computing (HPC) clusters.  We will take
you from being a new user to being competent to run your code at a
larger scale than you could before.  (However, we don't cover
application-specific matters beyond some Python/R/Matlab basics or
focus on the high-performance part: but this is an easy next step
after this course).

This course is good for any researcher who thinks they may need to
scale up to larger resources in the next six months, in any field.
Even if you don't use computing clusters, you will be better prepared
to understand how computing works on other systems.  If you are a
student, this is an investment in your skills.  By the end of the course you
get the hints, ready solutions and
copy/paste examples on how to find, run and monitor your applications,
and manage your data. In addition to how to optimize your workflow in
terms of filesystem traffic, memory usage etc.

If you are at Aalto University: the course is obligatory for all new 
Triton users and recommended to all interested in the field.

This course is part of :doc:`Scientific Computing in Practice <index>` lecture series
at Aalto University.



Other universities
------------------

This course is hosted at Aalto University but put on in cooperation
with many other universities.  Anyone (even not at a partner site)
could get something out of this course.

**If you are not at Aalto University**, you can follow along with the
course and will learn many things anyway.  The course is designed to
be as useful to people outside of Aalto, but many of the examples
won't directly work on your cluster and you will need to adapt (we
will mention these points where we know of them).  Known sites hosting:

* FCCI (Finland): may register via the Aalto form.
* Participants from University of Helsinki can follow how to connect
  to their Kale/Turso cluster by following `their own instructions
  <https://wiki.helsinki.fi/pages/viewpage.action?pageId=408323613>`__.
* Participants from University of Oulu: please follow instructions on
  `how to access the Carpo2 computing cluster <https://ict.oulu.fi/17120/?page&lang=en>`__.
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



Schedule
--------

**All times are EET (Europe/Helsinki time)!**

THU-FRI 3-4.February, 12:00-16:00.

- **Wed, 2 February 2022 (mandatory for new Triton users)**

  We strongly recommend that you join this day as well. This is a bigger-picture introduction.

  - **11:50 -- 15:00**
    - :doc:`getting-started-with-scientific-computing`
  - **15:00 -- 15:45 (especially important)** Help connecting to
    Triton (Aalto), Zoom link by email to registered participants.

- **Thu, 3 February 2022**

  All times approximate, breaks every hour.

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

- **Fri, 4 February 2022**

  All times approximate, breaks every hour.

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


Practical information
---------------------

The course is also streamed via Twitch (the `CodeRefinery channel <https://www.twitch.tv/coderefinery>`__) so that
anyone may follow along without registration.  There are also Zoom
breakout rooms/help sessions for those at partner universities.  There is a HackMD link
(collaborative edited notes) which is used for asking questions during
the course.

**Registration:** `Please register at this link <https://link.webropol.com/s/introHPCJan2022>`__

**Instructors, organizers, contact:** For additional info, email scip@aalto.fi

* Richard Darst
* Enrico Glerean
* Simo Tuomisto
* Jussi Enkovaara
* ... and you?


Preparation / prerequisites
---------------------------

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

* The :doc:`getting-started-with-scientific-computing` course provides
  good background, and is strongly recommended if you have not used
  Triton before.
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
