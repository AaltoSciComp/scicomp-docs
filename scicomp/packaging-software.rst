Package your software well
==========================

This page gives hints on packaging your research software well, so that
it can be installed by others.

As HPC cluster administrators, a lot of time is spent trying to
install very difficult software.  Many users want to use a tool
released by someone, but it turns out to not be easy to install.
Don't let that happen to your code - keep the following things in
mind, even at the beginning of your work.  Do you want your code to be
reused, so that you can be cited?

This page is specifically about packaging and distribution, and
doesn't repeat standard programming practices for scientists.

`Watch a humorous, somewhat related talk "How to make package managers
cry" <https://www.youtube.com/watch?v=NSemlYagjIU>`__.



Application or library
----------------------

* **Application:** Runs alone, does not need to be combined with other
  software.  Note that if your application is expected to be installed
  in a environment that is shared with other software, it is more like
  a library.  Note that this is how most scientific software is
  installed!

* **Library:** Runs embedded and connected with other software that is
  not under your control.  You can't expect everything else to use the
  exact versions of software that you need.

The dependency related topics below mostly apply to libraries - but as
the note says, in practice they affect many applications, too.



Use the proper tools
--------------------

Each language has some way(s) to distribute its code "properly".
Learn them and use them.  Don't invent your own way of doing things.

* `Python (pip) <https://packaging.python.org/tutorials/packaging-projects/>`__
* `Python (conda via conda-forge) <https://conda-forge.org/docs/>`__
* `R <https://cran.r-project.org/manuals.html#R-exts>`__

Use the simplest, most boring, reliable, and mainstream system there
is (that suits your needs).


Minimize dependencies
---------------------

Build off of what others make, don't re-invent everything yourself.
But at the same time, see if you can avoid random unnecessary
dependencies, *especially* ones that are not packaged well and
well-maintained.  It will make your life and others worse.


Don't pin dependencies
----------------------

Don't pin exact versions of dependencies in a released library.
Imagine if you want to install several different libraries that pin
slightly different versions of their dependencies.  They can't be
installed together, and the dependency solver may take a long time
trying before it gives up.

But you *do* often want to pin dependencies for your *environments*,
for example, the exact collection of software you are using to make
your paper.  This keeps your results reproducible, but is a different
concept that releasing your *software package*.

You *don't* pin dependencies strictly when someone may indirectly use
your software in combination with arbitrary other packages.  You
should have some particular reason for each pin your have, not just
"something may break in the future".  If the chances of something
breaking in the future are really that high, you should wonder if you
should recommend others to use this until that can be taken care of
(for example, build on a more stable base).

You'll notice that a lot of these topics deal with dependencies.
`Dependency hell <https://en.wikipedia.org/wiki/Dependency_hell>`__ is
a real thing, and you should carefully think about them.


Be flexible on dependencies
---------------------------

Following up from above, be as flexible as dependencies as possible.
Don't expect the newest just because it's the newest.

If you have to be strict on dependencies because the other software is
changing behavior all the time, perhaps it's not a good choice to
build on.  Maybe there's no other choice, but that also means that you
need to realize that your package isn't as reusable as you might hope.


Try to be robust in dependencies
--------------------------------

Follow the `robustness principle
<https://en.wikipedia.org/wiki/Robustness_principle>`__ to the extent
possible: "Be conservative in what you do, be liberal in what you
accept from others".  Try not to be as resistant as possible to
dependencies changing, while providing a stable interface for other
things.  Of course, this is hard, and you need a useful balance.  For
"resistance to dependencies changing", I interpret this as being
careful what interfaces I use, and see if I can avoid using things I
consider likely to change in the future.

Of course, robustness applies to other aspects, too.


Have tests
----------

Have at least some basic automated tests to ensure that your code
works in conjunction with all the dependencies.  Perhaps also have a
minimal example in the README file that someone can use to verify that
they installed properly (could be the same as the tests).  The tests
don't have to be fancy, even something that runs the code in a full
expected use case will let you detect major problems early.  This way,
when someone is installing the software for someone else, they can
check if they did it correctly.


Don't expect the latest OS
--------------------------

Don't design only for the latest and greatest operating system: then,
many people who can't upgrade right away won't be able to use it
easily.  Or, they'll have to go through extra effort to install newer
runtimes on their older operating system.

For example, I usually try to make my software compatible with the
latest stable operating systems from one year ago, and latest Python
packages from two years ago.  This has really reduced my stress in
moving my code around, even if it does mean I have to wait to wait to
use some new features.


Test on different dependency versions/OSs/etc
---------------------------------------------

This starts to get a little bit harder, but it's good to test with
diverse operating systems or versions of your key dependencies.  This
probably isn't worth it in the very early phases, but it is easier
once you start using continuous integration / automated testing.  Look
into these once you get advanced enough.

Most clusters have different and older operating systems that you'd
use on your desktop computer.


A container does not replace good packaging
-------------------------------------------

"I only support using the Docker container" does not replace good
packaging as described above.  At the very least, it assumes that
everyone *can* use Docker/singularity/container system of the year on
the systems they need to run on.  Second, what happens if they need to
combine with other software?

A container is a good way to make compute easier and move it around,
but make good packaging first, and use that packaging to install in
the container.


Other
-----

There is plenty more you should do, but it's not specific to the topic
of this page.  For example,

* Have versions and releases
* Use a package repository suitable to your language and tool.
* Have good documentation
* Have a changelog
* etc...


See also
--------

* `Video "How to make package managers cry" <https://www.youtube.com/watch?v=NSemlYagjIU>`__.
* https://softdev4research.github.io/4OSS-lesson/
