About this site
===============

These docs originally came from the Triton User Guide, but now serves
as a general Aalto scientific computing guide.  The intention is a
good central resources for researchers, kept up to date by the whole
community.  Many parts are useful to the broader world, too.  We
encourage the community and world to all contribute when they see a
need.

`Sphinx <https://www.sphinx-doc.org/en/master/>`__ is a static site
generator - you can build the site on your own computer and browse the
HTML.  It's automatically built and hosted by ReadTheDocs, but you
don't need to mess with that part.  Github will validate basic syntax
in pull requests.

.. seealso::

   :doc:`/tech/sphinx-docs` for an overview about how and why it's set
   up like this.



Contributing
------------

We welcome contributions via normal Github open source practices: send
us a pull request.

This documentation is Open Source (CC-BY 4.0), and we welcome
contributions from the community.  The project is run on Github
in the repository `AaltoSciComp/scicomp-docs <https://github.com/AaltoSciComp/scicomp-docs>`__.

To contribute, you can always use the normal Github contribution
mechanisms: make a `pull request`__, issues__, or comments.  If you
are at Aalto, you can also get direct write access.  Make a github
issue, then contact us in person/by email for us to confirm.

__ https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/proposing-changes-to-your-work-with-pull-requests
__ https://docs.github.com/en/github/managing-your-work-on-github/managing-your-work-with-issues

**The worst contribution is one that isn't made.** Don't worry about
making things perfect: send your improvement and someone can improve
the syntax/writing/etc as needed.  This is also true for formatting
errors - if you can't do ReStructudedText perfectly, just do your best
(and pretend it's markdown because all the basics are similar).

When you submit a change, there is continuous testing that will notify
you of errors, so that you can make changes with confidence:
"wiki rules: deploy and iterate" rather than "perfect before merge".

Contributing gives agreement to use content under the licenses (CC-BY
4.0 or CC0 for examples).



Requirements and building
-------------------------

.. highlight:: console

Set up the environment first (example, but do as you'd like).  The
basic requirements are ``sphinx`` and ``sphinx_rtd_theme` which are
also in Ubuntu: (``python-sphinx`` and ``python-sphinx-rtd-theme``)::

  $ python3 -m venv venv
  $ source venv/bin/activate
  $ pip install -r requirements.txt

Then you can build it locally to test::

  $ make html
  $ sphinx-autobuild . _build/html/     # starts web server that automatically updates
  $ make clean check                    # Full rebuild and warn of important errors

HTML output is in ``_build/html/index.html``.



Editing
-------

In short: find an example page and copy.  To add sections, add a new page in a
subfolder.  In order to appear in the sidebar, it has to be linked
from a ``toctree`` directive.  Check nearby ``index.rst``  pages and
add there.

Recommended pages for copying:

* :doc:`/triton/tut/serial` - tutorial
* :doc:`/triton/apps/python-conda` - topical discussion on a certain
  item
* ``/triton/apps/TEMPLATE.rst.template`` is a template for an
  application information page.
* :doc:`/aalto/aaltoharbor`: service page.



Most common missed quirks
-------------------------

* Double backquote for literal text, not single.  (Why?  Single can be
  assigned other purposes, like :doc: links, :ref: links, or in other
  projects :func: and so on.  We be generic so compatible with other
  projects that make a different choice.)::

    Run ``ssh -X triton.aalto.fi`` to ...

* Raw HTML links have two underscores.  (Why?  single underscore is
  some other fancy things.  Most links are internal reference/docs
  links)::

    The `OpenSSH project <https://www.openssh.com/>`__ does...

* Internal links have structures: they can be ``:doc:``, ``:ref:``,
  etc.  If you give a link to something, it knows where it is,
  validates it at build time, and you can give just the link and it
  takes the title from the target.

* You can set default highlighting for literal blocks, so you don't
  have to do ``.. code-block:: LANGUAGE`` all the time::

    .. highlight:: console

  This sets the default for all literal blocks, but you can still make
  a ``..code-block::`` for other cases (or change it partway through).

* For command line, use the ``console`` highlighting language instead
  of ``bash`` or others.  ``console`` will highlight the ``$`` and
  *make it not selectable* so it won't be copied.

* This isn't relevant to scicomp-docs, but `intersphinx
  <https://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html>`__
  lets you link directly to function/etc definitions in other Sphinx
  docs, by function name.  (This is why rigid structure is nice).
  `Python for SciComp
  <https://aaltoscicomp.github.io/python-for-scicomp/>`__ heavily uses
  this for great effect.



ReStructured text
-----------------

ReStructured Text is similar to markdown for basics, but has a more
strictly defined syntax and more higher level structure.  This
allows more semantic markup, more power to compile into different
formats (since there isn't embedded HTML), and advanced things like
indexing, permanent references, etc.

Restructured text `quick reference
<https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`__
and `home <https://docutils.sourceforge.io/rst.html>`__.

Note: Literal inline text uses `````` instead of a single ````` (second
works but gives warning).

A very quick guide is below.


Inline syntax
~~~~~~~~~~~~~

``Inline code/monospace``, *emphasis*, **strong emphasis**

::

   ``Inline code/monospace``, *emphasis*, **strong emphasis**


Literal blocks, code highlighting
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Literal blocks (= code blocks) use ``::`` and are intended:

::

   Literal block
   Literal block


::

   ::

     Literal block
     Literal blocks

Block quotes can also start with paragraph ending in double colon,
like this::

  Block quote

::

   Block quotes can also start with paragraph ending in double colon,
   like this::

       Block quote

If you define a highlight language, it will be used as the default
highlight language for every block::

  .. highlight:: python

Use ``Python`` for python.  Use ``console`` for console commands, and
include the ``$`` before the commands.  The ``$`` won't be selectable
so copy-and-paste works well.


Internal page links
~~~~~~~~~~~~~~~~~~~

Linking internally.  If possible use a permanent reference (next
section), but you can also refer to specific files by name.  Note,
that for internal links there are no trailing underscores.  Internal
links can get their text from the target.  Internal links are the
``:doc:`` domain::

  :doc:`../tut/interactive.rst`

  With different text: :doc:`Text <../tut/interactive.rst>`


Internal reference links
~~~~~~~~~~~~~~~~~~~~~~~~

Internal links: `ReST permanent references across files <https://www.sphinx-doc.org/en/stable/usage/restructuredtext/roles.html#role-ref>`__.

Label things this way (note only one colon)::

  .. _label-name:

Reference them this way::

  :ref:`label-name`     (recommended)
  `label-name`          (short, don't use, no warning if link breaks)
  `Text <label-name>`   (short, don't use, no warning if link breaks)


URL links
~~~~~~~~~

Inline `link <https://www.python.org>`__, or
anonymous__, or
separate_, or
`different text <separate_>`_ links.
Trailing underscores indicate links.  Note there should be two
underscores for the raw links.

__ https://www.python.org

.. _separate: https://www.python.org

::

    Inline `link <https://www.python.org>`__, or
    anonymous__, or
    separate_, or
    `different text <separate_>`_ links.
    Trailing underscores indicate links.

    __ https://www.python.org

    .. _separate: https://www.python.org


Admonitions: notes, warnings, etc.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Notes, warnings, etc.

.. note::

   This is a note.

.. warning::

   This is a warning.

.. admonition:: Admonition directives have titles.

   This has misc text.

.. admonition:: Dropdown can be clicked to expand.
   :class: dropdown

   When it's not important for everyone to see.  ``:class: dropdown``
   sets a CSS class which gets interpreted in the HTML.

::

  .. note::

    This is a note.

  .. warning::

    This is a warning.

  .. admonition:: Admonition directives have titles.

     This has misc text.

  .. admonition:: Dropdown can be clicked to expand.
     :class: dropdown

     When it's not important for everyone to see.  ``:class: dropdown``
     sets a CSS class which gets interpreted in the HTML.


Indexing
~~~~~~~~

Indexing isn't currently used.

::

   .. index:: commit; amend

   .. index::
      commit
      commit; message
      pair: commit; amend

   :index:`commit`

   :index:`loop variables <pair: commit; amend>`
