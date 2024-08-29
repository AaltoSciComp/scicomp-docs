============
Applications
============

.. include:: /triton/ref/videos.rst

In this tutorial, we talk about the overall process of finding,
building, and compiling software.  These days, installing and managing
scientific software is taking more and more time, thus we need to
specifically talk about it.

Clusters, being shared systems, have more complicated software
requirements.  In this tutorial, you will learn how to use
existing software.  Be aware that installing your own is possible (and
people do it all the time), but does require some attention to
details.  Either way, you will need to know the basics of software on
Linux.

.. admonition:: Abstract

   * There are many ways to get software on Triton:

     * Usually, you can't install software the normal operating system way.
     * The cluster admins install many things for you, and they are
       loadable with :doc:`Modules <modules>`.
     * Sometimes, you need to install some stuff on top of that (your
       own libraries or environments)
     * You can actually install your own applications, but you need to
       modify instructions to work in your own directories.

   * :doc:`Singularity containers <../usage/singularity>` allow you to
     run other hard-to-install software.
   * Ask us to install software if you need it.  Ask for help if you
     try it yourself and it seems to be taking too long.

.. seealso::

   Main article: :doc:`../apps/index`

.. admonition:: Local differences

   Almost every site will use modules.  The exact module names, and
   anything beyond that, will be different.  Containers are becoming
   more common, but they are less standardized.


There are four main ways of getting software:

* It's installed through the operating system some relatively "normal"
  way.
* Someone (a cluster admin) has already installed it for you.  Or you
  ask someone to install what you need.
* Someone has installed the base of what you need.  You do some extra.
* Install it yourself in a storage place you have access to.  (Maybe
  you share it with others?)



Installed through operating system
----------------------------------

People sometimes expect the cluster to work just like your laptop:
install something through a package manager or app store.  This
doesn't really work when you have hundreds of users on the same
system: if you upgrade X, how many other people's work suddenly
breaks?

Thus, this isn't really done, except for very basic, standalone
applications.  If it is done, this stuff isn't upgraded and often old:
instead, we install through modules (the next point) so that people
can choose the version they want.

One unfortunate side-effect is that almost all software installation
instructions you find online don't work on the cluster.  Often times,
it can be installed, but people don't think to mention it in the
documentation.  This often requires some thought to figure out: if you
can't figure it out, ask for help!



Cluster admin has installed it for you
--------------------------------------

The good thing about the cluster is that a few people can install
software and make it usable by a lot of people.  This can save you a
lot of time.  Your friendly admins can install things through the
:doc:`modules` (an upcoming lesson), so  that you can ``module load``
it with very little work.  You can even choose your exact version, so
that it keeps working the same even if someone else needs a newer
version.

Some clusters are very active in this, some expect the users to do more.
Some things are so obscure, or so dependent on local needs, that it
only makes sense to help people install it themselves.  To look for
what is available:

* Check out the page :doc:`../apps/index` and its sub-pages.
* Search the `issue tracker
  <https://version.aalto.fi/gitlab/AaltoScienceIT/triton>`__ to see if
  someone has already requested it and documented there.
* Ask us: Our `issue tracker
  <https://version.aalto.fi/gitlab/AaltoScienceIT/triton>`__,
  :ref:`Zulip chat <chat>` or :ref:`our support garage <garage>`.
* Modules (:doc:`modules` - next lesson) are the usual way of making
  this available.  The command ``module spider NAME`` will search for
  anything of that name.

**If you need something installed, contact us.**  The `issue tracker
<https://version.aalto.fi/gitlab/AaltoScienceIT/triton>`__ is
usually the best way to do this.

Some of the most common stuff that is available:

.. include:: ../ref/software.rst

.. important::

   This is Aalto-specific.  Some of these will work if you ``module
   load fgci-common`` at other Finnish sites (but not CSC).  This is
   introduced in the next lesson.



Already installed, you add extra modules you need
-------------------------------------------------

Even if a cluster admin installs some software, often you might need
to improve it some.  One classic example is Python: we provide Python
installations, but you need your own modules there.  So, you can use
our base Python installation to create your own **environments** -
self-contained systems where you can install whatever you need.
Different languages have different ways of doing this:

* **Python**: Conda environments, virtual environments.  See :doc:`../apps/python-conda`.

Environments have an advantage that you can do multiple projects at
once, and move between computers more easily.



Install it yourself
-------------------

Sometimes, you need to install software yourself - which you *can* do
if you can tell it to install just into your home directory.
Usually, the software's instructions don't talk about how to do this
(and might not even mention things like the environments in the
previous point).

One common way of doing this is **containers** (for example, **Docker**
or **Apptainer**/**Singularity**).  These basically allow you to put an
*entire operating system in one file*, so that your software works
everywhere.  Very nice when software is difficult to install or needs to
be moved from computer to computer, but can take some work to set up.
See :doc:`../usage/singularity` or the longer lesson on `containers on
HPC <https://coderefinery.github.io/hpc-containers/>`__ for more
information.

We can't go into this more right now - ask us for help if needed.  If
you make a "we need X installed" request, we'll tell you how to do it
if self-installation is the easiest way.



What you should do
------------------

* **Check if you can find what you need already**: `issue tracker
  <https://version.aalto.fi/gitlab/AaltoScienceIT/triton>`__ and
  searching this site.
* Ask for :doc:`help </help/index>` if you can't find it.
* Once you get there, make your software nice and reusable, so that
  others won't have the same problems you did: :doc:`make it easy to
  install and reusable </scicomp/packaging-software>`.  Contact the
  :doc:`Research Software Engineers </rse/index>` for help!



Exercises
---------

These are more for thinking than anything.

.. exercise:: Applications-1: Check your needs

   Find the Applications page link above, the issue tracker, etc., and
   if we already have your software installed.  See if we have what
   you need, using any of the strategies on that list.

.. exercise:: (optional) Applications-2: Your group's needs

   Discuss among your group what software you need, if it's available,
   and how you might get it.  Can they tell you how to get started?



What's next?
------------

The next tutorial covers :doc:`software modules <modules>` in more detail.
