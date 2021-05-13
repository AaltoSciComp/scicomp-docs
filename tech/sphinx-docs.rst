Technical documentation with Sphinx
===================================

This talk explains how one can use `Sphinx
<https://www.sphinx-project.org>`__ for technical documentation, in
particular this very site scicomp.aalto.fi.  The focus is to make an
overview for contributing to this site (or similar ones), but it will
also provide a strong basis for creating such a site yourself.


Basics
-------

scicomp.aalto.fi
~~~~~~~~~~~~~~~~

- Home of Aalto Scientific Computing's documentation
- Before 2017, was Triton's documentation using Confluence
- Now has information on many different topics about scientific
  computing.
- Rather highly ranked in search engines.



Properties of good documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Organized
- Easy to use
- Versioned
- Anyone can contribute
- Shareable
- Reuseable
- Open-source
- git?



The basic documentation stack
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Git repository
- Hosted on Github
- Documentation written in ReStructured Text or Markdownn
- Built with Sphinx

  - With various extensions

- Hosted on ReadTheDocs



Demo: making a change
---------------------

I want to add the Journal of Open Sourec Software (JOSS) review
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

* Python projects, including ``requirements.txt``

  * Until recently, was buildable with stock Debian/Ubuntu packages.
    Now it may require some.

* ``conf.py`` contains all configuration

* ``index.rst`` is the root of all docs.

* ``Makefile`` builds it

  * ``make html`` to make it
  * ``make clean html`` to rebuild
  * ``make clean check`` to build and check for any errors
  * ``sphinx-autobuild . _build/html/`` may be useful

* View results in ``_build``



Sphinx toctree (table of contents tree)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* The ``toctree`` directive is the fundamental building block of the
  site.
* It organizes documents into a tree, and that three is used to make
  the sidebar.
* Example::

    .. toctree::
       :maxdepth: 2

       aalto/*
       data/index
       README



Arrangement of the site
-----------------------

* Top-level sections for Aalto, Triton, Data, RSE, Training.
* We need to give a big rethinking.



Other details
-------------

Sphinx
~~~~~~

* Sphinx is a full-fledged extendable documentation generator
* We use many extensions such as ``sphinx_gitstamp``,
  ``sphinx-{copybutton,tabs,togglebutton}``, ``sphinx_rtd_theme``.
* Custom Javascript and CSS in ``_static``



ReStructured Text syntax
~~~~~~~~~~~~~~~~~~~~~~~~

* Why ReST?  Not a thin mapping on HTML like Markdownn
* Markdown is syntantic substitution, ReST is semantic meaning.
* `MyST <https://myst-parser.readthedocs.io/>` is now a reasonable
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



Github Action checks
~~~~~~~~~~~~~~~~~~~~

* `make clean check` will warn on errors
* Github provides error tracking for pushes and pull requests (demo?).



Open questions
--------------

Pull requests or not?
~~~~~~~~~~~~~~~~~~~~~

- When should we use pull requests?  When should we push directly?
- In practice both are fine, up to you to decide what you want



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



Testable docs
~~~~~~~~~~~~~

- Our dream would be to make examples in a testable form, where
- For example, this `python-openmp example
  <https://github.com/AaltoSciComp/scicomp-docs/tree/master/triton/examples/python/python_openmp>`__
  includes everything needed to submit and run the file.
- Can this be automatically tested?  A bit too complex for the typical doctest.



How can we keep things up to date?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Requires continuous work
* The `sphinx-dust extension
  <https://pypi.org/project/sphinx-dust/>`__ to remind us to look at
  pages?



Building a community
~~~~~~~~~~~~~~~~~~~~

- How can we get more people to contribute?
