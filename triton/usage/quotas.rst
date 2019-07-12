======
Quotas
======

Triton has quotas which limit both the space usage and number of files.
The quota for your home directory is 10GB, for $WRKDIR by default is
200GB, and project directories depending on request. These quotas exist
to avoid usage exploding without anyone noticing. If you ever need more
space, just ask. We'll either give you more or find a solution for you.

The file quota is because scratch is not that great for too many small
files. If you have too many small files, see `the page on small files
<smallfiles>`.

Normally, things just work, but there are certain intrinsic problems in
scratch, so if you ever get a "disk quota exceeded" error, then read on.

.. note::

   To try a quick fix, you can:
     ``quotafix -gs --fix /path/to/the/directory``

   If that fixes something, and problem recurs, then:
     ``module load teflon``

How quotas work
---------------

There are both quotas for users and projects (/m/$dept/$project).
However, Lustre (scratch) can currently only do quotas by user or group,
not by file path. If you ``ls -l`` a file or directory, you see both
user and group. Unfortunately, with lustre it only really works for one
of them at a time. So, on Triton, we use **user private groups**:
everyone has a group with the same name as your user, and in $WRKDIR all
files should have your group, and in project directories the group of
that project. We have things set up so that things will Just Work if you
do normal things.

::

    $ ls -l test
    drwxrwsr-x 3 darstr1 darstr1      4096 Jan 25 15:13 test/
          ^      ^^^^^^^ ^^^^^^^
          |      ^-- user  ^-- group
          ^-- SETGID

**Important!** If a file has a group of ``domain users`` or
``triton-users``, which occurs by default, then there is no quota for
the files! To get around this, we have all directories "SETGID"
(``chmod g+s``) and then files automatically are made in the correct
group. That leads to the next point...

``Disk quota exceeded`` error but I have plenty of space!
---------------------------------------------------------

If the ``quota`` command says you have plenty of space AND sufficient
number of files, then you've hit a common problem. Probably, the
directory does not have the SETGID bit set, so when you try to make a
new file, it appears as group 'domain users', and there's no quota
assigned, so it fails!

Quick fixes
~~~~~~~~~~~

Run either quotafix which will try to do things automatically, or this
find command. You can only fix $WRKDIR on Triton, since the
user-private-group does not exist on Aalto Linux workstations.

::

    # AUTOMATIC ON TRITON: Fix everything.
    #  (only for $WRKDIR or group directories, still in testing):
    /share/apps/bin/quotafix -sg --fix /path/to/dir/

    # MANUAL ON TRITON: use find yourself.
    # $GROUP is your username for work, or project-group name for scratch.
    lfs find /path/to/dir -type d -print0 | xargs -0 chmod g+s
    lfs find /path/to/dir  ! -group $GROUP -print0 | xargs -0 chgrp $GROUP

    # AALTO WORKSTATIONS: use "find" instead of "lfs find" above.

Details
~~~~~~~

Check the SETGID bit and group ownership for directories:
``drwxrwsr-x``. Directories must have "**s**" there and the right group,
otherwise when you try to make new files in that directory, they are
group= 'domain users' and it fails.

I can't rsync/sftp/etc
----------------------

It is related to the above mentioned issue, something like rsync -a ...
or cp -p ... are trying to save original group ownership attribute,
which will not work. Try this instead:

.. raw:: html

   <div class="container" title="Hint: double-click to select code">

::

    ## mainly one should avoid -g (as well as -a) since it preserves the old group (with no quota)
    $ rsync -urlptDxv --chmod=Dg+s somefile triton.aalto.fi:/path/to/work/directory

    ## avoid '-p' with cp, or if you want to keep timestapms, mode etc, then use '--preserve='
    $ cp -r --preserve=mode,timestamps  somefile /path/to/mounted/triton/work/directory

.. raw:: html

   </div>

You may need similar things for other different programs.

*Details:* Some programs change the group or don't preserve the SETGID
bit. This especially happens when you try to copy a directory from
somewhere else to Triton while preserving the SETGID bit. You get a
directory in the wrong group, or directory without SETGID bit so new
files are in the wrong group, so no quota.

Other solutions
---------------

teflon
~~~~~~

This is a new hack we are working on and hasn't been extensively tested.
Teflon is "anti-SETGID" which stops any program from changing either the
group or SETGID bit, using LD\_PRELOAD magic. It should work with *any*
program, currently probably only 64-bit though. This is still under
development. Please report problems or success stories.

You have to run quotafix or chmod/chgrp commands above first.

::

    # Use via a module - applies to everything in this session.
    module load teflon

    # OR: Run a single program under teflon
    /share/apps/bin/teflon your_program [args]] ]>newgrpThis changes your default group.  You can do the below commands, and it will change your default group.  This is per-shell (it makes a subshell).  When you are done, use exit to revert back.  Theoretically there's no downside to this, but if you alternate between project directories and group directories, eventually the quotas will get mixed up between the directories.newgrp $USER            # for $WRKDIR
    newgrp $PROJECT_GROUP   # for project directories - find the right group</pre></ac:plain-text-body></ac:structured-macro><p> </p><p> </p><h2>Details</h2><p><em>Why this happens:</em> $WRKDIR directory is owned by the user and user's group that has the same name and GID as UID. Quota is set per group, not per user. That is how it was implemented since 2011 when we got Lustre in use. Since spring 2015 Triton is using Aalto AD for the authentication which sets everyone a default group ID to 'domain users'. If you copy anything to $WRKDIR/subdirectory that has no +s  bit you copy as a 'domain users' member and file system refuses to do so due to no quota available. If g+s bit is set, all your directories/files copied/created will get the directory's group ownership instead of that default group 'domain users'.  There can be very confusing interactions between this and user/shared directories.</p>
