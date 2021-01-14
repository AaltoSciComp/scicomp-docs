=============================================
Jan 2020 / Intro to Linux and Aalto Computing
=============================================

.. admonition:: To be confirmed

   Tentative, to be confirmed soon

This course is a general introduction to computing resources at Aalto,
suitable as an introduction to any researcher doing somewhat
computational or data-intensive work now or in the future.

This course is especially suitable to new researchers or students trying to
understand computational/data analysis options available to them.  It
won't go into anything too deep, but will provide you with a good
background for your next steps: you will know what resources are
available and know the next steps to use them.

It consists of two parts:

* **Aalto computing workflows:** There are so many different computing
  resources to use, and this hour will introduce you to the different
  options and what kinds of work each are suited to.  You'll learn how
  they all interrelate and which can be easily used together.  The
  focus is what is at Aalto, but the general principles apply to most
  universities as well.  This is not just advanced computing.

* **Basic Linux shell:** Shell and command line (on Linux or on other
  operating systems) is the basis of large-scale computing, and
  knowing a little bit will go a long way in your career even if you
  don't use it on a daily basis.  This introduction will make you
  confident enough to take any other computing courses you may need in
  the future.  This is not Aalto specific.  This is a good intro to
  the :doc:`Winter HPC Kickstart <winter-kickstart>` that comes next
  (but still useful on its own).

Attending only one part is fine.

Prerequisites:

* No prerequisites
* You should have access to a ``bash`` shell. See instructions below
  for how we can provide this.
* Aalto or university account useful but not needed to try things out
  yourself.

Part of :doc:`Scientific Computing in Practice <index>` lecture series
at Aalto University.


Practical information
---------------------

This is an online course via Zoom (link sent to registered
participants).  The course is also streamed via Twitch (the
`CodeRefinery channel <https://www.twitch.tv/coderefinery>`__) so that
anyone may follow along without registration.  There is a HackMD link
(collaborative edited notes) which is used for asking questions during
the course.

**Instructors and organizers:**

* Richard Darst
* Enrico Glerean

**Time, date, place:** (all times EET):

- Friday, 29 January, online

  - Please connect 10 minutes early for icebreakers and introductions

  - **12:00--12:45:**  Workflows at Aalto (and other universities via
    breakout rooms)

    - Material: :doc:`/triton/usage/workflows`

  - Q&A

  - **13:00--13:45:**  Introduction to Linux shell

  - Q&A

  - [**14:00--14:45:**  Connecting to Triton as part of
    :doc:`winter-kickstart`.]

    - [Not technically a part of this course, but a next step from this
      course and integrated here]

  - Q&A


**Registration:** Not yet open.  We aim to not require registration
if you will be only passively watching.  Lurkers welcome.  Priority
for Finnish academic institutions (FGCI members).

**Credits:** Certificates are not provided for this course.

**Additional course info at:** scip@aalto.fi



Preparation
-----------

**Software installation:**

* You will need the BASH shell.  This is the basic of automating
  almost anything, so is useful to have on your computer.

  * Linux: Open the Terminal application and type: ``bash``
  * MacOS: Open the Terminal application and type: ``bash``
  * Windows:

    * If you have an Aalto account, download `PuTTY <https://www.putty.org/>`__
      and use it to connect to ``kosh.aalto.fi`` (see this `screenshot
      <PuTTY.png>`__). Use your Aalto username and password to login. After
      login, type: ``bash``
    * If you have Windows 10 and admin rights, you can install `Ubuntu
      <https://www.microsoft.com/store/productId/9NBLGGH4MSV6>`__ through the
      Microsoft Store. Then, start the Ubuntu application and type: ``bash``
    * If you don't have an Aalto account, and no Windows 10 with admin rights,
      you can install Git BASH by following `these instructions
      <https://coderefinery.github.io/installation/bash>`__.

  * If all the above fails, the backup plan is to use BASH through your
    webbrowser by `clicking here
    <https://mybinder.org/v2/gh/AaltoSciComp/bash-binder/HEAD?urlpath=terminals%2F1>`__.

* `Zoom <https://coderefinery.github.io/installation/zoom/>`__ (if
  attending via Zoom)

**Mental preparation:** Online workshops can be a productive format, but it
takes some effort to get ready.  Browse these resources:

* `Attending an online workshop
  <https://coderefinery.github.io/manuals/how-to-attend-online/>`__,
  good to read in detail (ignore the CodeRefinery-specific parts).
* `How to use HackMD to take answer questions and hold discussions <https://coderefinery.github.io/manuals/hackmd-mechanics/>`__.
* `The Zoom mechanics we will use
  <https://coderefinery.github.io/manuals/zoom-mechanics/>`__, might
  be useful to browse.
* It is useful to `watch <https://youtu.be/56p6xX0aToI>`__ or `read
  <https://scicomp.aalto.fi/scicomp/shell/>`__ the Linux shell crash
  course, to already become familiar with the content of the course.




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

- Computing strategies

  - Material: :doc:`/triton/usage/workflows`
  - Custom materials for other universities taking part in this
    training.

- Shell

  - Crash course: https://scicomp.aalto.fi/scicomp/shell/ (everything)
  - Shell in-depth tutorial: :doc:`/training/linux-shell-tutorial`
    (minor parts)
  - We will also emphasize how the shell fits in with modern
    science.



News and notes
--------------

None yet
