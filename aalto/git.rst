===========================
Aalto version control (git)
===========================

Version control systems track changes to files. This means that as you
are working on your projects (code, LaTex, notes, etc), you can track
history. This means that you can see former history, and collaborate
better. Using one for at least for code should probably be one of the
minimum standards of computational research.

Git
---

"*Git is a distributed version control system designed to handle
everything from small to very large projects with speed and efficiency.
Git is easy to learn and has a tiny footprint with lightning fast
performance. It outclasses SCM tools like Subversion, CVS, Perforce, and
ClearCase with features like cheap local branching, convenient staging
areas, and multiple workflows.*" `Git <http://git-scm.com/>`__

Git seems to have become the most popular and supported version control
system, even if it does have some rough corners.

Aalto offers access to a git hosting service. Right now we have no
documentation for git, but web is full of guides (good one can be found
from `Git’s official website <http://git-scm.com/documentation/>`__).

You can also find an online book and guides about git: `Pro Git book,
written by Scott Chacon <http://git-scm.com/book/>`__, `A Visual Git
Reference <http://marklodato.github.com/visual-git-guide/index-en.html>`__

Read tips and tricks from `niksula’s git
page <http://www.niksula.hut.fi/git#tips-and-tricks>`__

Aalto gitlab service
--------------------

Aalto has a self-hosted Gitlab installation at
https://version.aalto.fi. This is the recommended place for all
internal repositories, the other department ones will be deprecated
eventually. All support is provided by Aalto ITS. In principle, since
all data is stored within Aalto and is managed by Aalto, this is
suitable for materials up to the "confidential" level.

For public projects where you want a community, you can also consider
Github.

**NOTE!** If your work contract type changes (e.g. staff -> visitor),
the Aalto Version blocks the access as a security measure. Please
contact Aalto ITS Servicedesk <servicedesk@aalto.fi> to fix the problem
with your account or warn them in advance so that you can continue using
Aalto Version control.


SVN to Git migration
--------------------

You may use ``git-svn`` to create a git repository with all the history
from your svn repo, or you can ask us for assistance. Information that
we need to perform a SVN to Git migration:

-  Usernames and emails (author information; this is used to transform
   the usernames in svn commit history to git authors)

   -  Should be a plaintext file (UTF-8, UNIX newlines) with the
      following format:

      -  One username/email data per line
      -  ``username = Firstname Lastname <username@example.com>``

   -  Tip: you can get a list of all committer usernames from svn with
      ``svn log -q | awk '/^r/ { print $3 }' | sort | uniq``

-  Name and short (one-line) description for the new Git repository
-  Name of the old SVN repository and how to access it
-  The location of an empty git repository that you have created in
   gitlab (ie. where we should put the migrated history)

More about Git: `Git - official website <http://git-scm.com/>`__

Students and teaching
---------------------
