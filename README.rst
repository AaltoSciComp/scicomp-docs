================
About these docs
================

These docs originally came from the Triton User Guide, but now serves
as a general Aalto scientific computing guide.  The intention is a
good central resources for researchers, kept up to date by the whole
community.

Contributing
~~~~~~~~~~~~

This documentation is Open Source (CC-BY 4.0), and we welcome
contributions from the Aalto community.  The project is run on Github
in the repository `AaltoSciComp/scicomp-docs <https://github.com/AaltoSciComp/scicomp-docs>`__.

To contribute, you can always use the normal Github contribution
mechanisms: make a `pull request`__, issues__, or comments.  If you are at Aalto, you
can also get direct write access.  Make a github issue, then contact
us in person/by email for us to confirm.

__ https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/proposing-changes-to-your-work-with-pull-requests
__ https://docs.github.com/en/github/managing-your-work-on-github/managing-your-work-with-issues

**The worst contribution is one that isn't made.** Don't worry about
making things perfect: since this is in version control, we track all
changes and will just fix anything that's not perfect.  This is also
true for formatting errors - if you can't do ReStructudedText
perfectly, just do your best (and pretend it's markdown because all
the basics are similar).

When you submit a change, there is continuous testing that will notify
you of errors, so that you can make changes with confidence.

Contributing gives agreement to use content under the licenses (CC-BY
4.0 or CC0 for examples).


Requirements and building
~~~~~~~~~~~~~~~~~~~~~~~~~

To build the docs, run ``make html``.  You can run ``make clean
check`` to build it and report only the errors that would cause a
failure.

There is a ``requirements.txt`` file, but the only real Python
dependencies to do basic tests is ``sphinx`` and ``sphinx_rtd_theme``
(debian packages: ``python-sphinx`` and ``python-sphinx-rtd-theme``).

HTML output is in ``_build/html/index.html``, and other output formats
are available as well.


Editing
~~~~~~~

Look at examples and copy.  To add sections, add a new page in a
subfolder.  Link it from the main Table of Contents (``toctree``) in
``index.rst`` to have the document appear and be cross-referenced.

You can see a complete example from UiT: `source
<https://github.com/uit-no/hpc-doc>`_ and `compiled HTML
<http://hpc.uit.no/en/latest/>`_.



ReStructured text
~~~~~~~~~~~~~~~~~

ReStructured Text is similar to markdown for basics, but has a more
strictly defined syntax and more higher level structure.  This
allows more semantic markup, more power to compile into different
formats (since there isn't embedded HTML), and advanced things like
indexing, permanent references, etc.

Restructured text `home <https://docutils.sourceforge.io/rst.html>`_
and `quick reference
<https://docutils.sourceforge.io/docs/user/rst/quickref.html>`_.

Note: Literal inline text uses `````` instead of a single ````` (second
works but gives warning).

A very quick guide is below.

----

``Inline code/monospace``, *emphasis*, **strong emphasis**

::

   ``Inline code/monospace``, *emphasis*, **strong emphasis**

----

::

   Block quote
   Block quote


::

   ::

     Block quote
     Block quote

----

Block quotes can also start with paragraph ending in double colon,
like this::

  Block quote

::

   Block quotes can also start with paragraph ending in double colon,
   like this::

       Block quote

----

Inline `link <https://www.python.org>`_, or
anonymous__, or
separate_, or
`different text <separate_>`_ links.
Trailing underscores indicate links.

__ https://www.python.org

.. _separate: https://www.python.org

::

    Inline `link <https://www.python.org>`_, or
    anonymous__, or
    separate_, or
    `different text <separate_>`_ links.
    Trailing underscores indicate links.

    __ https://www.python.org

    .. _separate: https://www.python.org

----

Linking to the web.  If possible use a permanent reference (next
section), but you can also refer to specific files by name.  Note,
that for internal links there are no trailing underscores::

  :doc:`../tut/interactive.rst`  (recommended)
  `../tut/interactive.rst`       (short, no warning if link breaks)

  With different text:
  :doc:`Text <../tut/interactive.rst>`  (recommended)
  `Text <../tut/interactive.rst>`       (short, no warning if link breaks)


----

Internal links.  `Permanent references across files <https://www.sphinx-doc.org/en/stable/usage/restructuredtext/roles.html#role-ref>`_

Label things this way (note only one colon)::

  .. _label-name:

Reference them this way::

  :ref:`label-name`     (recommended)
  `label-name`          (short, no warning if link breaks)
  `Text <label-name>`   (short, no warning if link breaks)

----

Notes, warnings, etc.

.. note::

   This is a note

.. warning::

   This is a warning

::

  .. note::

    This is a note

  .. warning::

    This is a warning
