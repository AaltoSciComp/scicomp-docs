About clusters and your work
============================

.. admonition:: Video

   Watch this in our courses: `2022 February
   <https://www.youtube.com/watch?v=XAbE3OyfYNE&list=PLZLVmS9rf3nOKhGHMw4ZY57rO7tQIxk5V&index=9>`__,
   `2021 January <https://www.youtube.com/watch?v=OYgSBI-5bUo&list=PLZLVmS9rf3nN_tMPgqoUQac9bTjZw8JYc&index=6>`__

*This is the first tutorial.  The next is* :doc:`connecting`.

Science-IT is an Aalto infrastructure for scientific computing.  Its
roots was a collaboration between the Information and Computer Science
department (now part of CS), Biomedical Engineering and Computational
Science department (now NBE), and Applied Physics department.  Now, it
still serves all Aalto and is organized from the School of Science.

You are now at the first step of the Triton tutorial.


About Triton
------------

Triton is a mid-sized heterogeneous computational Linux cluster.  This
means that we are not at a massive scale (though we are, after CSC,
the largest publically known known cluster in Finland).  We are
heterogeneous, so we continually add new hardware and incrementally
upgrade.  We are designed for scientific computing and data analysis.
We use Linux as an operating system (like most supercomputers).  We
are a cluster: many connected nodes with a scheduling system to divide
work between them.  The network and some storage is shared, CPUs,
memory, and other storage is not shared.

.. admonition:: A real Ship of Theseus

   In the `Ship of Theseus
   <https://en.wikipedia.org/wiki/Ship_of_Theseus>`__ thought
   experiment, every piece of a ship is
   incrementally replaced.  Is it the same ship or not?

   Triton is a literal Ship of Theseus.  Over the ~10 years it has
   existed, every part has been upgraded and replaced, except possibly
   some random cables and other small parts.  Yet, it is still Triton.
   Most clusters are recycled after a certain lifetime and replaced
   with a new one.

On an international scale of universities, the power of Triton is
relatively high and it has a very diverse range of uses, though `CSC
has much more <https://research.csc.fi/computing>`__.  Using
this power requires more effort than using your own computer -
you will need to get/be comfortable in the shell, using shell
scripting, managing software, managing data, and so on.  Triton is a
good system to use for learning.


Building your skills
--------------------

.. seealso::

   Main article: :doc:`../../training/index`

As time goes on, computers are getting easier and easier to use.
However, research is not a consumer product, and the fact is that you
need more knowledge to use Triton than most people learn in academic
courses.

We have created a `modular
training plan <https://hands-on.coderefinery.org>`__, which
divides useful knowledge into levels.  In order to use Triton well, you need to be somewhat
proficient at Linux usage (C level).  In order to do parallel work,
you need to be good at the D-level and also somewhat proficient at the
HPC level (E-level).  This tutorial and user guide covers the D-level,
but it is up to you to reach the C-level first.

See our `training program and plan <https://hands-on.coderefinery.org>`__ for
suggested material for self-study and lessons.  We offer routine
training, see our :doc:`Scientific Computing in Practice lecture series
</training/scip/index>` page for info.

**You can't learn everything you need all at once.  Instead,
continually learn and know when to ask for help.**



Getting help
------------

.. seealso::

   Main article: :doc:`../help`

First off, realize **it is hard to do everything alone** - with the
diversity of types of computational research and researchers, it's not
even true that everyone *should* know everything.  If you would like
to focus on your science and have someone else focus on the
computational part, see our :doc:`Research Software Engineer
</rse/index>` service.  It's also available for expert consultations.

There are many ways to get help.  Most daily questions should go to
our :ref:`issue tracker <issuetracker>` (`direct link <https://version.aalto.fi/gitlab/AaltoScienceIT/triton/issues>`__), which is hosted on
:doc:`Aalto Gitlab <../../aalto/git>` (login with the HAKA button).
This is especially important because many people end up asking the
same questions, and in order to scale everyone needs to work together.

We have daily :doc:`"SciComp garage" </help/garage>` sessions
where we provide help in person. Similarly, we have :ref:`chat
<chat>` that can be used to ask quick questions.

Also, always search this scicomp docs site and old issues in the issue
tracker.

Please, don't send us personal email, because it won't be tracked and
might go to the wrong person or someone without time right now.
Personal email is also very likely to get lost.  For email contact, we
have a :ref:`service email address
<scicomp-address>`, but this should only be used for account
matters.  If it affects others (software, usage problems, etc), use
the issue tracker, otherwise we will point you there.



What's next?
------------
The next tutorial is :doc:`connecting to the cluster <connecting>`.
