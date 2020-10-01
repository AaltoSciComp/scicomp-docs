Python projects
===============

This checklist covers major considerations when creating a
high-quality, maintainable, reusable Python codebase.  It is designed
to be used along with a RSE to guide you through it (it is in a draft
stage).


* License

* Citeability and credit, authorship discussion

* Version control

  * In use locally
  * In use on some platform (Github/Gitlab/etc)
  * Regular commits
  * Discuss issue tracker
  * Make one example pull request

* Modular design

  * Standard project layout
  * Importable modules
  * Command line interface
  * (relates to packaging below)

* Tests

  * Recommendation: pytest
  * Simple integration tests
  * More fine-grained test
  * CI setup

* Documentation

  * README file: good enough?
  * Project webpage
  * Sphinx project
  * readethedocs

* Release

  * Module structure
  * setup.py
  * requirements.txt
  * PiPI release
  * conda-forge
  * Zenodo
