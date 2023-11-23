Technical documentation with Sphinx
===================================

.. seealso::

   `Video recording of this talk <https://www.youtube.com/watch?v=X6OzCSiS_VU&list=PLZLVmS9rf3nN1Rj-TAqFEzFM22Y1kJmvn>`__

This talk explains how one can use `Sphinx
<https://www.sphinx-project.org>`__ for technical documentation, in
particular this very site scicomp.aalto.fi.  The focus is to make an
overview for contributing to this site (or similar ones), but it will
also provide a strong basis for creating such a site yourself.

.. seealso::

   :doc:`/README` for a quick guide for editing this site.



Basics
-------

scicomp.aalto.fi
~~~~~~~~~~~~~~~~

- Home of Aalto Scientific Computing's documentation
- Before 2017, was Triton's documentation using Confluence (wiki
  software)
- Now has information on many different topics about scientific
  computing.
- Rather highly ranked in search engines.
- Converted from wiki.aalto.fi (Triton) using
  ``_meta/confluence2html.py`` and then pandoc to convert HTML→ReST.
- CC-BY license agreed at that time


Properties of good documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Organized, easy to use
- Versioned
- Anyone can contribute
- Shareable, reuseable, licensed
- No lock-in, can migrate later
- Plain text so 50 years of text processing development (``grep``,
  ``sed``), etc all work.
- Not standalone, can integrate with other materials
  (e.g. ``literalinclude``).
- git? (naturally comes out of the above)



The basic documentation stack
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Git repository
- Hosted on Github
- Documentation written in ReStructured Text or MyST-Markdown
- Built with Sphinx

  - With various extensions

- Hosted on ReadTheDocs
- GitHub actions validate basic syntax



Demo: making a change
---------------------

I want to add the Journal of Open Source Software (JOSS) review
checklist
(https://joss.readthedocs.io/en/latest/review_checklist.html) to the
RSE checklists section (https://scicomp.aalto.fi/rse/#checklists).

Through this, we will see:

- Git repository layout
- ReStructructured Text format
- Sphinx table of contents directives (``toctree``)
- Creating a pull request with git-pr
- Reviewing the pull request
- Merging
- See the rendered version.



Building the site
-----------------

* Git repo: https://github.com/AaltoSciComp/scicomp-docs/
* It has a ``requirements.txt`` like a normal Python project.

  * Until recently, was buildable with stock Debian/Ubuntu packages.
    Now it may require custom extensions.

* ``conf.py`` contains all configuration

* ``index.rst`` is the root of all docs.

* ``Makefile`` builds it

  * ``make html`` to make it
  * ``make clean html`` to rebuild
  * ``make clean check`` to build and check for any errors
  * ``sphinx-autobuild . _build/html/`` may be useful - start a web
    server that automatically reloads on changes.

* View results in ``_build/``


Editing on the web
~~~~~~~~~~~~~~~~~~
* The Github web interface is suitable for making simple changes.
* You can either directly commit or open a PR.
* Can we use this more?


Sphinx toctree (table of contents tree)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* The ``toctree`` directive is the fundamental building block of the
  site.
* It organizes documents into a tree, and that three is used to make
  the sidebar.  This directive can be put into any page.
* Example::

    .. toctree::
       :maxdepth: 2

       aalto/*
       data/index
       README

* Example: Follow it from ``index.rst`` → ``aalto/index.rst`` →
  ``aalto/jupyterhub.rst`` →
  ``aalto/jupyterhub-instructors/index.rst`` → various subpages.

* It makes sense, but for complicated case I often do trial and error.



Arrangement of the site
-----------------------

* scicomp.aalto.fi started from the Triton wiki
* It then grew top-level sections for Aalto, Triton, Data, Training,
  RSE, etc.
* It is about time that we rethink how it is organized.
* rkdarst is currently the one with the overall picture in mind - for
  consultations about big changes.



Other details
-------------

Sphinx
~~~~~~
* Sphinx is a full-fledged extendable documentation generator
* We use many extensions such as ``sphinx_gitstamp``,
  ``sphinx-{copybutton,tabs,togglebutton}``, ``sphinx_rtd_theme``.
* Custom Javascript and CSS in ``_static``.
* Very useful to know for other projects in general
* `CodeRefinery documentation lesson on Sphinx
  <https://coderefinery.github.io/documentation/sphinx/>`__.


ReStructured Text syntax
~~~~~~~~~~~~~~~~~~~~~~~~
* Why ReST?  Because it's not a thin mapping on HTML like Markdown.
* Markdown is syntactic substitution, ReST is semantic meaning.
* `MyST <https://myst-parser.readthedocs.io/>`__ is now a reasonable
  alternative, but it is closer to a different ReST syntax than Markdown.
* See syntax quickstart at https://scicomp.aalto.fi/README/
* https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html

Most surprising ReST points:

* Double quotes for literals::

     Run ``nano`` to begin

  (configurable)

* Links are scoped::

    :doc:`/triton/index`
    :ref:`tutorials`

  (configurable)

* Two underscores under links::

    The main `Aalto website <https://aalto.fi/>`__



Github Action checks
~~~~~~~~~~~~~~~~~~~~
* ``make clean check`` will warn about the same errors that Github
  will fail on.
* Github provides error tracking for pushes and pull requests (demo?).
* Example failure:

  * Code view: https://github.com/AaltoSciComp/scicomp-docs/commit/5f43ae628e3a60b1e5d3c1845f04a2c518520b7f
  * Actions view: https://github.com/AaltoSciComp/scicomp-docs/runs/2579364572

* I purposely have checks as rather strict and disabled some options
  that would allow us to do more flexible ReST: "explicit is better
  than implicit".


ReadTheDocs
~~~~~~~~~~~
* https://readthedocs.org provides a management interface for the docs
* There is a joint aalto-scicomp account to manage it
* Demo if time, but pretty much self-explanatory
* Occasionally a build fails for no reason and rkdarst needs to go
  wipe and rebuild, or fix dependency versions.



Little-known features
---------------------


We could use Markdown or Jupyter
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* Via `MyST-parser <https://myst-parser.readthedocs.io/>`__ or
  `MyST-nb <https://myst-nb.readthedocs.io/>`__ for Jupyter.
* They all work together in the same site.
* ReST is really nicer for this than shoving directives into
  Commonmark.


Compatible with many other projects
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* Standard documentation system for many projects
* Used in recent CodeRefinery lessons, for example


Minipres
~~~~~~~~
* Turn any site into a presentation
* Demo: https://scicomp.aalto.fi/tech/sphinx-docs/?minipres&h=3
* https://github.com/coderefinery/sphinx-minipres
* Can anyone help do this properly?


Redirect to HTTPS
~~~~~~~~~~~~~~~~~
* ReadTheDocs doesn't natively do this for external domains
* Done via Javascript
* Can anyone improve?


Other output formats
~~~~~~~~~~~~~~~~~~~~
* Sphinx can output to PDF, single-page HTML, epub, manual pages, and
  more.
* Can anyone think of a use for this?


Substitution extension
~~~~~~~~~~~~~~~~~~~~~~
* https://github.com/NordicHPC/sphinx_ext_substitution
* Written for Hands-on Scientific Computing


sphinx-gitstamp
~~~~~~~~~~~~~~~
* Bottom of every page lists date that exact page was actually
  modified.
* https://pypi.org/project/sphinx-gitstamp/



Open questions
--------------

Pull requests or not?
~~~~~~~~~~~~~~~~~~~~~
- When should we use pull requests?  When should we push directly?
- In practice both are fine, up to you to decide what you want
- rkdarst believes that, if you aren't sure, push directly and ask for
  review.


Sharing with other sites
~~~~~~~~~~~~~~~~~~~~~~~~
- We had this long-term plan to build scicomp.aalto.fi so that other
  sites could share our HPC tutorials and customize them to their
  sites.
- `sphinx_ext_substitution
  <https://github.com/NordicHPC/sphinx_ext_substitution>`__ (written
  by rkdarst) could make this easier
- This has not yet been done, and by now scicomp-docs is so complex
  I'm not sure if that if it is a reasonable thing to do.


Others at Aalto can use scicomp.aalto.fi
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Should we encourage others to join our project here?


Testable docs
~~~~~~~~~~~~~
- Our dream would be to make examples in a testable form, where one
  can automatically run them all and find errors.
- For example, this `python-openmp example
  <https://github.com/AaltoSciComp/scicomp-docs/tree/master/triton/examples/python/python_openmp>`__
  includes everything needed to submit and run the file.
- Can this be automatically tested?  A bit too complex for the typical doctest.


Integrated HPC-examples
~~~~~~~~~~~~~~~~~~~~~~~
* We have two example locations:

  * https://scicomp.aalto.fi/triton/examples/
  * https://github.com/AaltoSciComp/hpc-examples/

* The second (hpc-examples) could be included as a submodule to reduce
  duplication, and users can also clone it during courses.


Don't use ReadTheDocs anymore?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* Github Actions + GitHub Pages or other hosting sites would work
  instead of ReadTheDocs now.


How can we keep things up to date?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* Requires continuous work, like any docs.
* What should the threshold be for removing old material?
* We now have a last updated time at the top.
* We clearly need to think about this more.


Visitor stats
~~~~~~~~~~~~~
* ReadTheDocs provides limited stats based on web server logs.
* rkdarst is against detailed web tracking.
* Can we find a way to get both?.
* 2022 update: we have Plausible analytics which is sufficiently
  anonymous.


Building a community
~~~~~~~~~~~~~~~~~~~~
- How can we get more people to contribute?
