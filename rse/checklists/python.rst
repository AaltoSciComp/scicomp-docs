Python project checklist
========================

This checklist covers major considerations when creating a
high-quality, maintainable, reusable Python codebase.  It is designed
to be used along with a RSE to guide you through it (it is in a draft
stage, and doesn't have link to what these mean).  Not everything is
expected for every project, but a sufficiently advanced complicated
project will have most of these things.


* Citeability and credit, authorship discussion

* License

* Version control

  * In use locally
  * In use on some platform (Github/Gitlab/etc)
  * Regular commits
  * Discuss issue tracker
  * Make one example pull request

* Modular design

  * Standard project layout
  * Importable modules
  * Command line or other standard interface
  * (relates to packaging below)

* `Tests <https://coderefinery.github.io/testing/>`__

  * Recommendation: pytest
  * Simple system tests on basic examples
  * More fine-grained integration or unit tests
  * CI setup
  * Test coverage

* `Documentation <https://coderefinery.github.io/documentation/>`__

  * Forms / levels

    * README file: good enough?
    * Project webpage
    * Sphinx project
    * Read The Docs

  * To include

    * About
    * Installation
    * Tutorials
    * How to / simple examples to copy
    * Reference

* Release

  * Module structure
  * pyproject.toml or setup.py
  * requirements.txt or environment.yml
  * PyPI release
  * conda-forge
  * Zenodo
