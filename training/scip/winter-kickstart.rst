==================================
Feb 2022 / Triton Winter Kickstart
==================================

.. admonition:: Quick Links

   * To register for the February 2022 sessions please visit https://link.webropol.com/s/introHPCJan2022
   * Day 1 course page: :doc:`getting-started-with-scientific-computing`
   * Lesson materials: :ref:`Triton tutorials <tutorials>`, see below
     for details.

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

The course is obligatory for all new Triton users and recommended to
all interested in the field.

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
  to their Kale/Ukko2 cluster by following `their own instructions
  <https://wiki.helsinki.fi/display/it4sci/HPC++Winter+KICKSTART+2021>`__.

If you want to get your site listed here and/or help out, contact us
via the `CodeRefinery chat
<https://coderefinery.github.io/manuals/chat/>`__ (#workshops stream).
Our :doc:`hints for other sites' support staff
</triton/tut/required-cluster-setup>` are available.



Schedule
--------

**All times are EET (Europe/Helsinki time)!**

THU-FRI 3-4.February, 12:00-16:00.

- **Wed, 2 February 2022 (mandatory if new Triton user)**

  - **11:50-14:00** We strongly suggest also
    attending the :doc:`getting-started-with-scientific-computing`
    course.  This is a bigger-picture introduction.
  - **15:00 -- 15:45 (especially important)** Help connecting to
    Triton (Aalto), Zoom link by email to registered participants.

- **Thu, 3 February 2022** (roughly connecting to serial jobs in
  the :ref:`tutorials <tutorials>`)

  - **11:50 -- 16:00**, all times approximate, breaks every hour
  - :doc:`/triton/tut/about-tutorials`
  - :doc:`/triton/tut/intro`
  - Real example 1: Large-scale computing with array jobs
  - Real example 2: Large-scale parallel computing
  - :doc:`/triton/tut/interactive`
  - :doc:`/triton/tut/serial`
  - :doc:`/triton/tut/monitoring`
  - :doc:`/triton/tut/storage`
  - :doc:`/triton/tut/remotedata`
  - :doc:`/triton/tut/applications`
  - :doc:`/triton/tut/modules`

- **Fri, 4 February 2022**

  - **11:50 -- 16:00**, all times approximate, breaks every hour
  - :doc:`/triton/tut/array`
  - :doc:`/triton/tut/gpu`
  - :doc:`/triton/tut/parallel`
  - ~ 14:30 **Laptops to Lumi**, by CSC

    You now know of basics of using a computing cluster.  What if you
    need more than what a university can provide?  CSC (and other
    national computing centers) have even more resources, and this is
    a tour of them.

  - ~15:00 Real examples of a few common programming languages/frameworks
  - Likely there is time for additions or special requests



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
