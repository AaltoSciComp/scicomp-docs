===========================
About Science-IT and Triton
===========================

*This is the first tutorial.  The next is* :doc:`connecting`.

Science-IT is an Aalto infrastructure for scientific computing.  Its
roots was a collaboration between the Information and Computer Science
department (now part of CS), Biomedical Engineering and Computational
Science department (now NBE), and Applied Physics department.  Now, it
still serves all Aalto and is organized from the School of Science.

Our basic administrative web page is http://science-it.aalto.fi, but
it has mostly administrative info.  This site,
https://scicomp.aalto.fi, is our practical info for users.

You are now at the first step of the Triton tutorial.


About Triton
============

Triton is a mid-sized heterogeneous computational Linux cluster.  This
means that we are not at a massive scale (though we are, after CSC,
the largest publically known known cluster in Finland).  We are
heterogeneous, so we continually add new hardware and incrementally
upgrade.  We are designed for scientific computing and data analysis.
We use Linux as an operating system (like most supercomputers).  We
are a cluster: many connected nodes with a scheduling system to divide
work between them.  The network and some storage is shared, CPUs,
memory, and other storage is not shared.

On an international scale of universities, the power of Triton is
relatively high and it has a very diverse range of uses, though `CSC
has much more <https://research.csc.fi/computing>`__.  Using
this power requires more effort than using your own computer -
you will need to get/be comfortable in the shell, using shell
scripting, managing software, managing data, and so on.  Triton is a
good system to use for learning.


Getting skills
==============

.. seealso::

   Main article: :doc:`../../training/index`

As time goes on, computers are getting easier and easier to use.
However, research is not a consumer product, and the fact is that you
need more knowledge to use Triton than most people learn in academic
courses.

Science-IT has created a (still under development) :doc:`modular
training plan <../../training/index>`, divided into A (basics, use
basic software), B (Linux usage), C (high performance computing), and
D (advanced HPC).  In order to use Triton well, you need to be somewhat
proficient at Linux usage (B level).  In order to do parallel work,
you need to be good at the B-level and also somewhat proficient at the
HPC level (C-level).  This tutorial and user guide covers the C-level,
but it is up to you to reach the B-level first.

See our :doc:`training program and plan <../../training/index>` for
suggested material for self-study and lessons.  We offer routine
training, see our `Scientific Computing in Practice lecture series
<http://science-it.aalto.fi/scip/>`__ page for info.



Getting help
============

.. seealso::

   Main article: :doc:`../help`

There are many ways to get help.  Most daily questions should go to
our :ref:`issue tracker <issuetracker>` (`direct link <https://version.aalto.fi/gitlab/AaltoScienceIT/triton/issues>`__), which is hosted on
:doc:`Aalto Gitlab <../../aalto/git>` (login with the HAKA button).
This is especially important because many people end up asking the
same questions, and in order to scale everyone needs to work together.

Please, don't send us personal email, because not everyone is here all
the time and you may end up asking someone other than the best
person.  Personal email is also very likely to get lost.  By the same
token, we have a :ref:`service email address
<esupport-triton-address>`, but this should only be used for account
matters.  If it affects others (software, usage problems, etc), use
the issue tracker, otherwise we will point you there and spend lots of
time answering the same questions over and over.

Also, always search this scicomp docs site and old issues in the issue
tracker.

We have weekly :doc:`"SciComp garage" <../../news/garage>` sessions
where we provide help in person.

However, the most important thing is to be able to continually develop
your skills to help yourself and your colleagues.  See the previous
section for our solution for this.


Software
========

Triton, being a shared system, has more complicated software
requirements.  In an upcoming tutorial, you will learn how to use
existing software.  Be aware that installing your own is possible (and
people do it all the time), but does require some attention to
details.  Either way, you will need to know the basics of software on
Linux.


What's next?
============
The next tutorial is :doc:`connecting`.
