Project portfolio
=================

This page lists examples of projects which we have done.  As of early
2024, our internal project numbers are in the 200s.


Summary table
-------------

.. figure:: https://raw.githubusercontent.com/AaltoSciComp/aaltoscicomp-graphics/master/figures/rse-alignment.png
   :alt: 3x3 table with "programming", "workflows integration", "data"
	 across the top and "help you do it", "do it with you", and
	 "do it for you" along the side.

   Example range of projects we do.  We sometimes do things outside of
   this table, too.


Software publishing (M)
-----------------------

A CS doctoral researcher's paper had code released along with it -
with seven PDF pages of installation instructions, five pages of
pre-processing instructions, and fifteen pages on how to run it.  This
code was effectively un-reusable, meaning that the potential for
impact was much lower than otherwise.

Aalto RSE helped to transform this analysis into a standard R package
that could be installed using standard tools and run using a
Snakemake, a workflow automation tool.  Other researchers - including
future researchers in the same group - could reuse the tool for their
science.  Time spent: 3 weeks.  Benefit: One paper's results become
reusable (both internally and externally).



cor:ona data collection platform (L)
------------------------------------

Cor:ona (Comparison of rhythms: old vs. new activity) was research
study studying personal habits during the transition between remote
work and post-remote-work.  For this study to be successful, a platform
to integrate survey and smart device data had to be created within a
one-month time frame.

Aalto RSE worked with the researcher to do a complete and quick
ethical review and build the platform.  Unlike a hired software
developer, our staff already knows the research methods and can work
much faster - and stays around providing years of support with the
post-processing whenever it is needed. [Source code on 
`Github <https://github.com/digitraceslab/corona_study>`__].  Time spent:
~1 month.  Benefits: one study and multiple papers that could not
otherwise exist.



Periodic table of quantum force fields (S)
------------------------------------------

A researcher wanted to create a website that could find quantum
mechanical force fields (≈models).  The researcher dropped by our
:doc:`daily scientific computing garage </help/garage>` for advice,
and we discussed options - by working with us, the path could be
greatly simplified to a static site.  We found a suitable open-source
starting point, adjusted it to work for the needed purpose, and
provided it to them for future work by the next day.  The researcher
has been able to carry on with the project independently.  Time spent:
0.5 day, time saved: 4 days + simpler implementation.



Finnish Center for Artificial Intelligence (dedicated)
------------------------------------------------------

The Finnish Center for AI (FCAI) aims for its research to have an
impact in the world, and to do that, its software must be reusable.
They have identified that as a bottleneck, and thus provides 5 years
of funding for Aalto RSE to hire a research software engineer
dedicated to FCAI projects.  This person works along with all other
RSEs in the team, so that FCAI has far more resources than a single
hire could do themselves.



Business Finland project (M)
----------------------------

A research group had gotten Business Finland funds to develop an idea
into a product, but were still working within Aalto.  They needed
software development expertise to start off quickly.  They were large
enough that they needed a dedicated developer, but our initial work could
allow them to start sooner and lay a good groundwork for the developer
they hired later.



Debugging and Parallelisation (S)
---------------------------------
A researcher had a huge dataset to run an analysis on. Sequential
analysis would have been infeasible and they wanted to run it in
parallel. They tried to implement it themselves but got stuck, so
they came to garage, where an RSE was able to help them to modify
their code allowing them to parallelize a lot of the work and perform
the analysis. The resulting work got published in `Fuel <https://www.sciencedirect.com/science/article/pii/S0016236122038133>`__.



Introduction to Julia course (M)
--------------------------------

Julia is a relatively new programming language that has found many
users in certain fields.  A professor taught an undergraduate course
using Julia, but there were not sufficient introductory resources to
prepare students for the course, nor any other resources to prepare
them.  Aalto RSE found an open-source course prepared by CSC (Finland's
national scientific computing center), improved it to handle the
things needed by the undergraduate course, and successfully taught it
on demand.  All course material is open source, so that others may
also use it.  Time spent: ~1 month.  Benefit: Course given twice,
undergraduate course made better, open material produced, internal
Julia expertise



Releasing an open-source Github-based book (S)
----------------------------------------------

A researcher had prepared the start of an open-source book and needed
help and advice in releasing it as an open project.  Aalto RSE helped
with the technical setup to host the book on Github, the basics of Git
usage, and creating a continuous integration system that would rebuild
the book on every change.  This allowed the book to both be fully
open-source and to accept contributions from others.  Aalto RSE also
used its connections to Research Services to discuss the intellectual
property aspects and how it might affect the possibility for future
publication. Time spent: <1 day. Benefit: Open book and community
project.



Releasing a microscope control code (S)
---------------------------------------

A researcher had created a code in Python to control a physical
measurement device.  This code could be useful to others, but had to
be packaged and released.  Aalto RSE helped to clean and release the
code.  Time spent: 1 day.  Time saved: 1 month.



"Programming parallel supercomputers" course (M)
------------------------------------------------

The "Programming parallel supercomputers" course, as the name says,
gives students a first experience with HPC work.  It can be difficult
to find teaching assistants capable of giving the exercises a
deep-enough check - in addition to confirming they follow best
practices on the cluster.  There is also a secondary effect of
making sure students see best practices in research software
(development, documentation, etc.), which can often be left behind in
academic courses.  Aalto RSE plays an important role in
this course by bridging the technology with the teaching.



Aalto Gitlab improvements (M)
-----------------------------

Aalto University's Gitlab needed some scripting for management tasks.
While not exactly in our scope, we were the logical team to take a
look (as opposed to hiring outside consultants, especially since we
could better fit in with an incremental development schedule and
longer-term support).  We talked with the system owners, refined the
tasks, understood GitLab documentation, created the necessary scripts
and improvements, handed them off to the sysadmins for production, and
helped to understand tasks which should be done at another level.
Time spent: 1 week.  Benefit: improved service for Aalto University,
significant cost savings.  This type of project would be available for
other internal service teams, assuming availability.
