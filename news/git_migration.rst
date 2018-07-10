============================
Git migration (2017 January)
============================

This guide explains how to move projects from department Gitlab to the
new version.aalto.fi service.

Migrating from svn
==================

There are many guides online, but a minimum guide is included below
(this preserves all history). You
should create the repository on version.aalto.fi yourself, get your
computer set up to use version.aalto.fi, and then do the following:

::

    # If you want to convert svn usernames to email addresses (can be shared among projects):
    svn log -q %s | awk -F '|' '/^r/ {sub("^ ", "", $2); sub(" $", "", $2); print $2" = "$2" <"$2">"}' | sort -u >> authors-orig.txt
      # edit authors-orig.txt
    mv authors-orig.txt authors.txt

    git svn clone --authors-file=authors.txt   svn-url/ tmp_directory/

    cd tmp_directory
    git svn create-ignore
    git commit -a -m 'Add .gitignore from svn ignore'

    # Add Aalto gitlab info
    git remote add origin $VERSION.AALTO.FI_URL
    git push -f origin master

If you have a giant subversion repository with many different
unrelated (or loosely related) projects, it is recommended to split
this into separate git repositories per project.  You can also do this
preserving all history.  If you are in a Science-IT department, we can
help with this, :doc:`contact Science-IT <../triton/help>`.  If you
aren't, contact us anyway and we can try to help anyway.

Preserving the working directory
--------------------------------

Let's say you are switching to git, but have some stuff that isn't
checked in yet, so you don't want to re-get the whole repository.  You
can keep your working directory if you want::

  # project/ is the old subversion directory

  mv project/.svn project/.svn-old
  # Now it won't appear to be a subversion repo anymore.  You may have
  # to move other .svn directories in subdirectories.  This step isn't
  # really needed, but prevents mistakes!

  git clone git@version.aalto.fi:gitlab/new/repo.git new-git-repo/
  cp -r new-git-repo/.git project/.git
  # Now project/ looks like a git repo!  You keep all your old files
  # and resume where you left off.




Migrating from other Gitlab (like departments had)
==================================================

Prerequisites
-------------

-  The department gitlab must be upgraded to the same version as
   version.aalto.fi. Your department administrators will tell you when
   this is done (if they sent you here, it is probably done).
-  Take and push all existing code. You can also commit all code that
   needs committing. This isn't actually required, but
-  For a shared repository, talk to everyone who is using it and agree
   on a time. Nothing will be lost if you don't, but it avoids the
   possibility of confusing or accidentally making conflicts. Make sure
   everyone stops making wiki edits or issues on the old one.

Instructions: manually
----------------------

This is easy if you only have code within the repository.

-  Make a new repository on version.aalto.fi.
-  Push the code to the new repository using the instructions under
   "finalizations" below. They also appear on the new project page, but
   you need to remove the old remote.

Instructions: import a public repository, main files only
---------------------------------------------------------

-  Create a new project on version.aalto.fi
-  Import "repo by url" and give the URL. Do import.

Instructions: full export/import (includes wiki, issues, etc)
-------------------------------------------------------------

On old gitlab
~~~~~~~~~~~~~

-  Navigate to project to be exported. Go to project settings.
-  In the "Export project", click "Export project". Wait a few seconds
   and refresh the page. (In theory wait for an email to come, but in
   practice it is very fast for small repositories)
-  Scroll down to the same section and now select "Download Export" and
   save the project.

On version.aalto.fi
~~~~~~~~~~~~~~~~~~~

-  Log in, go to projects, create new project, select the namespace and
   the project name. Leave everything else blank, it won't be used
   anyway.
-  Under the import project section, click "Gitlab export" and select
   the downloaded .tar.gz. Upload and click "import project".

Instructions (advanced, scripting using API)
--------------------------------------------

There is an `Gitlab API <https://docs.gitlab.com/ce/api/>`__. It can
probably be used to automate some or all of the migration, but we don't
have a custom script for this yet and we haven't identified other
scripts yet. If you develop/find such a thing, let us know and it will
be mentioned here.

Finalizing
----------

-  In your old gitlab, either archive or move the project to a new name.
   This prevents anyone from accidentally using the old one.

-  Update the project metadata on version.aalto.fi. Especially if you
   are are migrating a lot of old stuff, use this opportunity to update
   the project description. Add publication references, etc. Remember:
   data management!

-  Set the project visibility and add back all of the members, if
   needed. (Note: people do not appear on version.aalto.fi until they
   log in once)
-  Set up ssh keys for your own account (once).
-  Update existing cloned copies to point to the new server. This is
   easy, there is no re-downloading, and all versions match up.

   ::

       cd existing_repo
       git remote set-url origin THE_URL
       git push -u origin master   # only pushes master branch

       # To push everything:
       git push -u origin --all
       git push -u origin --tags   # if you want tags mirrored

-  Tell everyone that you are done and to use the new location.

FAQ
---

-  How long does it take? In practice about one minute per project once
   you get started with it.
-  What is migrated? From gitlab itself: Project and wiki repositories,
   Project uploads, Project configuration including web hooks and
   services, Issues with comments, merge requests with diffs and
   comments, labels, milestones, snippets, and other project entities.
-  What is not migrated?: From gitlab itself: Build traces and
   artifacts, LFS objects, Container registry images

   -  We also find this is not exported: project permissions, project
      descriptions, project visibility, project members.

FAQ about version.aalto.fi
==========================

Moved to :doc:`the gitlab page <../aalto/git>`.

