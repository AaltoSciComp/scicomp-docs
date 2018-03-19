====================
Linux shell tutorial
====================


Course basics
=============
Linux Shell tutorial by Science IT at Aalto University.

Abstract: BASH practicalities, shell scripting. Learning by doing.  Corresponds to 4 sessions 3h each, session rough schedule 2x1h25m with 10m break in between.

Setting up instructions for the lecturer: Main terminal white&black
with the enlarged font size.  One small terminal at the top that shows
commands to learners.

 - ``export PROMPT_COMMAND='history -a'``   # .bashrc or all the terminals one launches commands
 - ``tail -n 0 -F .bash_history``

Starred exersices (*) are for advanced users who would like further stimulation.

Based on
 - ``man bash`` v4.2 (Triton default version in Feb 2018)
 - Advanced BASH scripting guide [#]_
 - UNIX Power Tools, Shelley Powers etc, 3rd ed, O'Reilly
 - common sense and 20+ years Linux experience
 - see also other references in the text

Getting a shell
---------------

Before the course: set yourself up with a bash shell.  Connect to a
server or open on your own computer.  Ask for help if needed:

- Linux and Mac users: just open a terminal window.
- Windows users: install PuTTY [#]_ then SSH to any interactive server
  at Aalto or your department.

-----------------------------------------------------------------------------

1. session: interactive shell
=============================
Interactive usage of BASH

- Shell -- is what you get when your terminal window is open. It is a
  command-line (CLI), an interface that interpreters and executes the
  commands.
- The name comes from being a "shell" (layer) around the operating
  system.  It connects and binds all programs together.
- This is the basic, raw method of using UNIX-like systems.  It may
  not be used everyday, but it's really good (necessary) for any type
  of automation and scripting - as is often need in Science or when
  using Triton.
- There are multiple shells.  This talk is about `bash
  <https://en.wikipedia.org/wiki/Bash_(Unix_shell)>`__, which is the
  most common one.  `zsh <https://en.wikipedia.org/wiki/Z_shell>`__ is
  another common shell which is somewhat similar but has some more
  powerful features.  `tcsh <https://en.wikipedia.org/wiki/Tcsh>`__ is
  another shell from a completely different family (the csh family),
  which has quite different syntax.
- ``bash`` is a "Bourne shell": the "bourne-again shell".  Open source
  version of original Bourne shell.


What's a UNIX process?
----------------------
- To understand a shell, let's first understand what processes are.
- All programs are a process
- Processes have:

  - Process ID (integer)
  - Name
  - Command line arguments
  - input and output: ``stdin`` (input, like from keyboard),
    ``stdout`` (output, like to screen), ``stderr`` (like stdout)
  - Return code (integer) when complete
  - Working directory
  - environment variables: key-values which get inherited.

- These concepts bind together *all* UNIX programs.

Built-in and external commands
------------------------------

There are two types of commands:

- shell built-in: ``cd``, ``pwd``, ``echo``, ``test``, etc.
- external: ``ls``, ``date``, ``less``, ``lpr``, ``test``, etc.
- some can be both: e.g. ``test``.  Options not always the same!
- For the most part, these behave similarly, which is a good thing!
  You don't have to tell which is which.

**Hint** ``type -a`` to find what is behind the name

- **echo**: prints out ``echo something to type`` # types whatever you put after

Who am I: ``id``, ``echo $HOME``, ``echo $SHELL``
(Your default shell is not a /bin/bash? Login to kosh/taltta and run ``chsh -s /bin/bash``)

Where am I: ``pwd`` (this shows the first piece of process
information: current directory)

Your best friend ever -- ``man`` -- collection of manuals. Type
*/search_word* for searching through the man page.  But... if it's a
builtin, you need to use ``help``


Files and directories
---------------------
Files contain data.  They have a name, permissions, owner
(user+group), contents, and some other metadata.


``ls`` is the standard way of getting information about files.

::

 ls, ls -l, ls -la, ./, ../, *, ?, [], [!], {}, \

There are a variety of commands to manipulate directories:

::

 cd, mkdir, cp, rm, rm -r, mv, ln, touch

Note that ``cd`` is a shell builtin which change's the shell's own
working directory.  This is the base from which all other commands
work: ``ls`` by default tells you the current directory.  ``.`` is the
current directory, ``..`` is the parent directory, etc.  This is
inherited to other commands you run.

**Hint** ``ls -lX``, ``ls -ltr``, ``file <filename>``

**Hint** Quotation matters

:Exercise: mkdir in your ``$HOME`` (or ``$WRKDIR`` if on Triton), cd
           there and 'touch' a file. Rename it. Make a copy and then
           remove the original
:Exercise*:
 - ``ls`` dot files only
 - create a dozen empty files with one command with names like
   ``file1.txt``, ..., ``file12.txt``
:Exercise*: Compare the data you get from ``ls -l`` and ``stat``.
	    What metadata do you find?

Permissions
-----------
- Permissions are one of the types of file metadata.
- They tell you if you can *read* a file, *write* a file, and
  *execute a file/list directory*
- Each of these for both *user*, *group*, and *others*
- Here is a typical permission bits for a file: ``-rw-r--r--``
- In general, it is ``rwxrwxrwx`` -- read, write, execute/search for
  user, group, others respectively
- ``ls -l`` gives you details on files.

Modifying permissions::

 chmod u+rwx,g-rwx,o-rwx <files>  # u=user, g=group, o=others, a=all
  -or-
 chmod 700 <files>   # r=4, w=2, x=1
 chmod -R <perm> <directory>  # recursive, changing all the subdirectories and files at once

 chgrp group_name <file or directory>  # changing group ownership (you must be a member)

There are some advanced permission bits:

- s-bit:  setuid/setgid bit, preserves user and/or group IDs.
- t-bit: sticky bit, for directories it prevents from removing file by
  another user (example */tmp*)

**Hint** File Manager like Midnight Commander -- ``mc``

:Exercise:
 - on Triton make a directory at ``$WRKDIR``, allow user and group members
   full access and no access for others
 - change group ownership to '[FIXME: must be a group member]', set s-bit for the group (one can
   open another 'scip' session to check that *scip user* has access)
 - Note: make sure your upper directory has *o+x* bit set
:Exercise*: create a directory and a subdirectory in it and set their
            permissions to 700 with one command
:Exercise*: ``ls -ld`` tells you that directory has permissions
            ``rwxr-Sr--``, does group members get access there?

Hotkeys
-------
- Is it annoying to have to type everything in the shell?  No, because
  we have hotkeys.  In fact, it can become much more efficient and
  powerful to use the shell.
- Most important key: **TAB**: autocomplete.  You should never be
  typing full filenames or command names.  TAB can complete almost anything

Common hotkeys:

- TAB -- autocomlpetion
- Home `or` Ctrl-a -- start of the command line
- End `or` Ctrl-e -- end
- Ctrl-left/right arrows `or` Alt-b/Alt-f  - moving by one word there and back
- up/down arrows -- command history
- Ctrl-l -- clear the screen
- Ctrl-Shift-c -- copy
- Ctrl-Shift-v -- paste
- Ctrl-Shift--  -- undo the last changes on cli
- Alt-r -- undo all changes made to this line
- Ctrl-r -- command history search: backward (hit Ctrl-r, then start typing the search word, hit Ctrl-r again to go through commands that have the search word in it)
- Ctrl-s  -- search command history furtherword (for this to work one needs to disable default suspend keys ``stty -ixon``)
- Ctrl-u  -- remove beginning of the line, from cursor
- Ctrl-k -- remove end of the line, from cursor
- Ctrl-w -- remove previous word

**Hint** ``history | grep KEYWORD``  to list all matching commands

**Hint** Check */etc/inpurc* for some default key bindings, more can be defined *~/.inputrc* (left as an exercise)


Initialization files and configuration
--------------------------------------
- When the shell first starts (when you login), it reads some files.
  These are normal shell files, and it evaluates normal shell commands
  to set configuration.
- You can always test things in your own shell and see if it works
  before putting it in the config files.  Highly recommended!
- You customize your environment means setting or expanding aliases,
  variables, functions.
- The config files are:

  - ``.bashrc`` (when SSH) and
  - ``.bash_profile`` (interactive login to a workstation).
  - they are often a symlink from one to another.

One of the things to play with: command line prompt defined in PS1 [#]_

::

 PS1="[\d \t \u@\h:\w ] $ "

For special characters see PROMPTING at ``man bash``. To make it
permanent, should be added to *.bashrc* like ``export PS1``.

:Home exercise:
  - customize a prompt ``$PS1``, make sure is has a current
    directory name and the hostname in it in the format
    *hostname:/path/to/current/dir*. Hint: save the original
    PS1 like ``oldPS1=$PS1`` to be able to recover it any time.
  - make it colorful
  - take a look at https://www.tldp.org/LDP/abs/html/sample-bashrc.html 
    Do you get any good ideas?

Createing/editing/viewing file
------------------------------
* A **text editor* edits files as ASCII.  These are your best friend.
  In fact, text files are your best friend: rawest, most efficient,
  longest-lasting way of storing data.
* "pager" is a generic term for things that view files or data.

Editors like:

- *nano* - simplest
- *vim* - minimal.  To save&quit, ``ESC :wq``
- *emacs* - or the simplest one *nano*.  To save&quit: ``Ctrl-x
  Ctrl-c``

To view contents of a file in a scrollable fashion: ``less``

Quick look at the text file ``cat filename.txt`` (dumps everything to
screen- beware of non-text binary files or large files!)

Other quick ways to add something to a file (no need for an editor)

``echo 'Some sentence, or whatever else 1234567!-+>$#' > filename.txt``

``cat > filename2.txt`` to finish typing and write written to the file, press enter, then Ctrl-d.

**Hint** best text viewer ever -- ``less -S``  (to open a file in your EDITOR, hit *v*, to search through type */search_word*)

Try: add above mentioned ``export PS1`` to *.bashrc*. Remember ``source .bashrc`` to enable changes

:Exercise*: Set some default options for the ``less`` program in your
	    bashrc.  Examples: case-insensitive searching, long
	    prompt, wrapping lines.


Input and output: redirect and pipes
------------------------------------
* Programs can display something: ``echo this is some output`` or ``cat``
* Programs can take some input: e.g. ``less`` by default displays
  input if no filename given.

- ``cat /etc/bashrc`` dumps that file to *stardard output* (stdout)
- ``cat /etc/bashrc | less`` gives it to ``less`` on *standard input*
  (stdin)

Pipe: output of the first command as an input for the second one ``command_a | command_b``

::

 # sort, tr, cut, /dev/null, see also grep below
 man -t ls | lpr  # send man page to a default printer
 du -hs * | sort -h  # see what directories use the most space
 w -h | wc -l  # count a number of logged in users
 ls -1 | tr '\n' ' '   # replace new line with a comma

Redirects:
- Like pipes, but send data to files instead of other processes.
- Replace a file: ``command > file.txt``
- Append to a file: ``command >> file.txt`` (be careful you don't mix
  them up!)

::

 echo Hello World > hello.txt
 ls -lH >> current_dir_ls.txt
 getent passwd | cut -d: -f1,5 > users  # extract user names and store them to a file

**This is the unix philosophy** and the true power of the shell.  The
**unix philosophy** is a lot of small, specialized, good programs
which can be easily connected together.

To dump output of all commands at once: group them

::

 { command1; command2; } > filename  # commands run in the current shell  as a group
 ( command1; command2; ) > filename  # commands run in external shell as a group


Pipelines: ;, &&, and ||
------------------------
- You can put several commands on the same line using different
  separators.
- The shell term for this is *pipelines*.

Chaining: ``command_a ; command_b``: always runs both commands.

Remember exit codes?  In shell, 0=success and anything 1-255=failure.
Note that this is opposite of normal Boolean logic!

The ``&&`` and ``||`` are `short-circuit
<https://en.wikipedia.org/wiki/Short-circuit_evaluation>`__ (lazy)
boolean operators.  They can be used for quick conditionsals.

* ``command_a && command_b``

  * If ``command_a`` is successful, also run ``command_b``
  * final exit code is last evaluated one, which has the role of Boolean *and*.

* ``command_a || command_b``

  * If ``command_a`` is *not* successful, also run ``command_b``
  * final exit code is that of the last evaluated command, which has
    the role of Boolean *or*.

**Hint** command_a && command_b || command_c

Try: ``cd /nonexistent_dir && ls /nonexistent_dir`` compare with ``cd /nonexistent_dir; ls /nonexistent_dir``

Try: ``ping -c 1 8.8.8.8 > /dev/null && echo online || echo offline``


grep
----
Later on you'll find out that ``grep`` is one of the most useful
commands you ever discover on Linux (except for all the *other* most
useful commands ever)

::

 grep <pattern> <filename>  # grep lines that match <pattern>
 command | grep <pattern>  # grep lines from stdin
 grep -R -i <pattern> <directory>  # grep all the files in the <directory>, case insensitive
 grep -v ...  # grep everything except
 grep -C 2 ... # displaying 2 extra lines before and after the match (-A just after, -B just before)
 grep -c ... # counts the number of matches
 grep -o <pattern> ... # shows only the matched part of the string (by default grep shows whole line)
 grep -E <extended_regexpr> ... # accepts way more advanced regular expressions as a search pattern

For details on what <pattern> could be, look for REGULAR EXPRESSIONS
at ``man grep``.  Some examples:

::

 grep -Eio "\b[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,6}\b" file.txt  # grep emails to a list
 ps auxw | grep firefox  # grep currently running firefox processes

:Exercise: make a pipe that counts number of files/directories (including dot files) in your directory
:Exercise: 
 - grep directories out of ``ls -l``
 - grep all but blank lines in the file (Hint: 'man grep' for regular expression)
 - expand the previous one to filter out commented lines (start with #)
:Exercise*: expand ``du`` to list dot files/directories also
:Exercise*: ``uptime; w > wuptime`` how to add output of both commands
	    to the same file with only one redirect?
:Exercise*: Count unique logged in users on kosh/taltta/triton or anywhere else


Aliases
-------
Define a new or re-define an old command ``alias space='du -hs .[!.]* * | sort -h'``, ``alias rm='rm -i'``

Aliases go to *.bashrc* and available later by default.

Try: Define this on command line, then add to *.bashrc* once you
verify it works:

::

 alias chknet='ping -c 1 8.8.8.8 > /dev/null && echo online || echo offline'

and then

::

 source .bashrc
 chknet


find
----
* ``find`` is a very unixy program: it finds files, but in the most
  flexible way possible.
* It is a amazingly complicated program
* It is a number one in searching files in shell

With no options, just recursively lists all files::

  find
  find | grep some_filename

::

 find ~ -name file.txt   # -or-  'find ~ $WRKDIR -name file.txt' one can search more than one dir at once
 find . -maxdepth 1 -name '*.jpg' -type f  # look for jpeg files in the current dir only
 find . -type -f -size +10M -size -100M  # find all files of size more than 10M and less than 100M
 find ~ ! -user $USER | xargs ls -ld # find everything that does not belong to you
 find . -type d -exec chmod g+rwx {} \;   # open all directories to group members

More options: by modification/accessing time, by ownership, by access type, joint conditions, case-insensitive, that do not match, etc [#]_ [#]_

**Hint**  On Triton ``lfs find``.  This uses a raw lustre connection
to make it more efficient than accessing every file.

**Hint**  Another utility that you may find useful ``locate``, but on
workstations only.  This creates a cached database of all files, and
just searches that so it is much faster.

**Hint** 'Too many arguments' error solved with ``find ... | xargs``

:Exercise: Find all files with 'lock' in the name in your home directory
:Exercise*: Find all the files in your $HOME or $WRKDIR that are readable or writable by everyone. What would the ways to "fix them"?
:Exercise*: Find all the dirs/files that do no belong to your UID/GID (user id and effective group id).


Substitute a command output
---------------------------
* Command substitutions execute a command, take its stdout, and  place
  it on the command line in that place.

``$(command)`` or alternatively ```command```. Could be a command or a list of commands with pipes, redirections, variables inside. Can be nested as well.

::

 touch file.$(date +%Y-%m-%d)
 tar czf $(basename $(pwd)).$(date +%Y-%m-%d).tar.gz ...
 now=$(date +%Y-%m-%d)


Transferring files (archiving on the fly)
-----------------------------------------
For Triton users the ability to transfer files to/from Triton is essential.

Assume a use case: you have logged in to kosh/taltta/lyta/etc. To get some files from Triton's WRKDIR to one of the directories available around:

::

 scp -r triton.aalto.fi:/scratch/work/LOGIN_NAME/some/files path/to/copy/to

Another use case, copying to Triton, or making a directory backup

::

 rsync -urlptDxv --chmod=Dg+s somefile triton.aalto.fi:/scratch/work/LOGIN_NAME  # copy a file to $WRKDIR
 rsync -urlptDxv --chmod=Dg+s dir1/ triton.aalto.fi:/scratch/work/LOGINNAME/dir1/  # sync two directories

Another use case, you want to archive your Triton data to some other place

::

 # login to Triton
 cd $WRKDIR
 tar czf - path/to/dir | ssh kosh.aalto.fi 'cat > path/to/archive/dir/archive_file.tar.gz'

*tar* is the de-facto standard for archiving on UNIX systems. *z*
 stands for compressing with GZIP, otherwise directory is packed, but
 not compressed

 - ``tar czvf path/to/archive.tar.gz directory/to/archive/  another/file/to/archive.txt``  # to archive
 - ``tar xzf path/to/archive.tar.gz -C path/to/directory``  # to extract
 - ``tar tzf archive.tar.gz``

:Try: whatever use case you have, try transferring files.

:Exercise: make an alias so *rsyncing* a copy of your local directory (or kosh:somedir) to Triton


Exit the shell
--------------
``logout`` or Ctrl-d (export IGNOREEOF=1 to *.bashrc*)

In order to keep your sessions running while you logged out, you
should discover the ``screen`` program.

 - ``screen`` to start a session
 - Ctrl-a-d to detach the session while you are connected
 - ``screen -ls`` to list currently running sessions
 - ``screen -rx <session_id>`` to attach the session, one can use TAB for the autocompletion or skip the <session_id> if there is only one session running

Example: irssi on kosh / lyta


SSH keys and proxy (*bonus section)
-----------------------------------
* SSH is the standard for connecting to remote computers: it is
  both powerful and secure.
* It is highly configurable, and doing some configuration will make
  your life much easier.

SSH keys and proxy jumping makes life way easier. For example, logging
on to Triton from your Linux workstation or from kosh/lyta.

For PuTTY (Windows) SSH keys generation, please consult section "Using public keys for SSH authentication" at [#]_

On Linux/Mac: generate a key on the client machine

::

 ssh-keygen -t rsa -b 4096  # you will be prompted for a location to save the keys, and a passphrase for the keys. Make sure passphrase is strong (!)
 ssh-copy-id aalto_login@triton.aalto.fi   # transfer file to a Triton, or/and any other host you want to login to

From now on you should be able to login with the SSH key instead of password. When SSH key added to the ssh-agent (once during the login to workstation), one can login automatically, passwordless.

Note that same key can be used on multiple different computers.

SSH proxy is yet another trick to make life easier: allows to jump
through a node (in OpenSSH version 7.2 and earlier ``-J`` option is
not supported yet, here is an old recipe that works on Ubuntu
16.04). By using this, you can directly connect to a system (Triton)
through a jump host (kosh):

On the client side, add to ``~/.ssh/config`` file (create it if does
not exists and make it readable by you only)::

 Host triton triton.aalto.fi
     Hostname triton.aalto.fi
     ProxyCommand ssh YOUR_AALTO_LOGIN@kosh.aalto.fi -W %h:%p

Now try::

 ssh triton


2. session
==========
Command line advances and introduction to BASH scripting

Files and dirs advances
----
Advanced access permissions

Access list aka ACL: ``getfacl`` and ``setfacl``

 - Allow read access for a user ``setfacl -m u:<user>:r <file_or_dir>``
 - Allow read/write access for a group ``setfacl -m g:<group>:rw <file_or_dir>``
 - Revoke granted access ``setfacl -x u:<user> <file_or_dir>``
 - See current stage ``getfacl <file_or_dir>``

**Hint** to get file meta info ``stat <file_or_dir>``

**Hint** even though file has a read access the top directory must be searchable before external user or group will be able to access it. Best practice on Triton ``chmod -R o-rwx $WRKDIR; chmod o+x $WRKDIR``

Setting default access permissions: add to *.bashrc* ``umask 027`` [#]_

:Exercise: practice with chmod/setfacl: set a directory permissions so that only you and some user/group of your choice would have access to a file


Functions as part of your environment
----
Can be defined from the cli, or better in file (for instance *function.sh*)

::

 name() {
   command $1
   command $2
   ...
 }

Invoking a function from command line (source the file first)

::

 $ name arg1 arg2 

As an example ``lcd``

::

 lcd() {
   cd $1
   ls -1 | wc -l
 }

::

 $ source function.sh
 $ lcd

Functions in BASH is just a piece of code that once declared can be invoked at any place later with args or withour. ``return`` returns the exit code only. By default vars are in global space, once chaged in the function is seen everywhere else. ``local`` can be used to localize the vars.

:Exercise: expand ``lcd`` so that it would print number of files and directories separately
:Exercise*: write a function that makes files/subdirectories readable by all on a given directory (note r for files, xr for dirs)


Variables
----
In shell, variables define your environment. Common practice is that environmental vars are written IN CAPITAL: $HOME, $SHELL, $PATH, $PS1, $RANDOM. To list all defined variables ``printenv``. All variables can be used or even redefined. No error if you call an undefined var, it is just considered to be empty.

Assign a variable ``var1=100``, ``var2='some string'``

Invoke a variable ``$var1``

Append a var: ``var+=<string>/<integer>``

Vars can be declared, like if you want it readonly ``declare -r var=xyz``, or to be treated as integer always ``declare -i var``.

BASH is smart enough to distiguish a var inline ``dir=$HOME/dir1; fname=file; fext=xyz; echo "$dir/$fname.$fext"``, though if var followed by a number or a letter ``echo ${dir}2/${file}abc.$fext``

Built-in vars:

 - $?  exit status of the last command
 - $$  current shell pid
 - $#  number of input parameters
 - $0  running script name
 - $1, $2 ... input parameter one by one (function/script)
 - "$@" all input parameters as is in one line

:Exercise: write a function that outputs number of arguments it has got and then all the arguments as a single word
:Exercise*: make a function that takes IP as an argument, ping that IP and returns ok/failed only


More on variables
----
BASH provides wide abilities to work with the vars "on-the-fly" with ${var...} like constructions.

 - Subtitute a var with default *value* if empty: ``${var:=value}``
 - Print an *error_message* if var empty: ``${var:?error_message}``
 - Extract a substring: ``${var:offset:length}``, example ``var=abcde; echo ${var:1:3}`` returns 'bcd'
 - Variable's length: ``${#var}``
 - Replace beginning part: ``${var#prefix}``
 - Replace trailing part: ``${var%suffix}``
 - Replace *pattern* with the *string*: ``${var/pattern/string}``

:Exercise: 
 - shorten *filename.ext* down to *filename* and then down to *ext*. Filename can be of any length, while *.ext* is the same.
 - expand lcd() so that it would go to some specific directory taken as an input parameter, if *$1* is empty (on Triton it could be $WRKDIR)
:Exercise*: extract filename with no extension from */work/archive/OLD/Michel's_stuff.tar.gz*


PATH
----
``chmod +x``, what is next? binaries at /bin, /usr/bin, /usr/local/bin etc. Setting up ~/bin or running as ./binary.

Add to *.bashrc* ``export PATH="$PATH:$HOME/bin"``

**Hint** name your scripts  *\*.sh* and collect them in ~/bin directory


[[ ]]
----
``[[ expression ]]`` returns 0 or 1 depending on the evaluation of the conditional *expression*

``==, <, >, !=, =~, &&, ||, !, ()``

When working with the strings the right-hand side is a pattern (a regular expression). Matched strings in brackets assigned to *${BASH_REMATCH[]}* array elements.

::

 x=5; y=6; z=7; [[ $x < $y && ! $y == $z ]] && echo ok || echo nope
 
 
About regular expressions
----
Regular expression is a pattern, it describes what we are looking for within a string. Selected operators:
 
 - ``.`` 	matches any single character
 - ``?`` the preceding item is optional and will be matched, at most, once
 - ``*`` 	the preceding item will be matched zero or more times
 - ``+``  the preceding item will be matched one or more times
 - ``{N}`` the preceding item is matched exactly N times
 - ``{N,}`` the preceding item is matched N or more times
 - ``{N,M}`` the preceding item is matched at least N times, but not more than M times
 - ``-``  represents the range if it's not first or last in a list or the ending point of a range in a list
 - ``^``  beginning of a line
 - ``$`` 	 the end of a line
 
::

 email='jussi.meikalainen@aalto.fi'; regex='(.*)@(.*)'; [[ "$email" =~ $regex ]]; echo ${BASH_REMATCH[*]}
 txt='Some text with #1278 in it'; regex='#([0-9]+ )'; [[ "$txt" =~ $regex ]] && echo ${BASH_REMATCH[1]} || echo do not match

**Hint** For case insesitive, set ``shopt -s nocasematch``  (to disable it back ``shopt -u nocasematch``)


if/elif/else
----

Though scripting style is more logical with if/else construction

::

 if [[ expression ]]; then
   command1
 elif [[ expression ]]; then
   command2
 else
   command3
 fi

[[ ]] can be a command/function or an arithmetic expression (( )), or a command substitution, that is what ever returns an exit code is fine.

An example: script (or function) that accepts two strings and returns result of comparison

::

 if [[ "$1" == "$2" ]]
 then
   echo The strings are the same
 else
   echo The strings are different
 fi
 
 ::
 
  if ping -c 1 8.8.8.8 &> /dev/null; then echo online; else echo offline; fi
 

:Exercise: Play with the strings/patterns. Make a script/function that picks up a pattern and a string as an input and reports whether pattern matches any part of string or not. Kind of *my_grep pattern string*.
:Exercise*: Expand the *my_grep* script to make search case insesitive and report also a count how many times pattern appears in the string

More conditional expressions
----

 - ``-f`` true if is a file
 - ``-r`` true if file exists and readable
 - ``-d`` true if is a directory
 - ``-z`` true if the length of string is zero (always used to check that var is not empty)
 - ``-n`` true if the length of string is non-zero
 - ``file1 -nt file2`` true if *file1* is newer (modification time)
 - many more others

::

 [[ -f $file ]] && echo $file exists || { echo error; exit 1; }
 [[ -d $dir ]] || mkdir $dir


case
----
For the more complex conditionals, instead of nested *ifs*, BASH has ``case``.

::
 
 read -p "Are you ready (y/n)? " yesno   # expects user input
 case $yesno in
   y|yes) do_something_if_yes ;;
   n|no) do_something_if_no ;;
   *) do_something_else ;;
 esac
 # $yesno can be replaced with ${yesno,,} to convert to a lower case on the fly


It tries to match the variable against each pattern in turn. Understands patterns rules like ``*, ?, [], |``.

::

 read -p "Enter your age? " age
 case $age in
   [1-9]|1[0-2]) echo Child ;;
   1[3-9]|[2-5][0-9]) echo Adult ;;
   [6-9][0-9]) echo Senior ;;
   *) echo Should be dead by now or wrong input ;;
 esac
 
``;;`` is important, if replaced with ``;&``, execution will continue with the command associated with the next pattern, without testing it. ``;;&`` causes the shell to test next pattern. The default behaviour with ``;;`` is to stop matches after first pattern has been found.

Try:

::

 # create a file 'cx'
 case "$0" in
  *cx) chmod +x "$@" ;;
  *cw) chmod +w "$@" ;;
  *c-w) chmod -w "$@" ;;
  *) echo "$0: seems that file name is somewhat different"; exit 1 ;;
 esac
 
 # chmod +x cx
 # ln cx cw
 # ln cx c-w
 # to make a file executable 'cx filename'


More about redirection, pipe and multiple commands execution 
----
STDOUT and STDERR: reserved file descriptors *1* and *2*, always there when you run a command

`` ... >/dev/null`` redirects STDOUT only, to redirect all the output including errors `` ... &>/dev/null``, or redirect outputs in different ways ``1>file.out`` and ``2>file.err``

In order to pipe both STDERR and STDOUT ``|&``.

If ``!``  preceds the command, the exit status is the logical negation.

The third file descriptor is 0, STDIN, valid syntax ``command < input_file &> output_file``. ping exercise explained.

List of the commands can be part of pipe constructions ``{ command1; command2 }`` and ``( command1; command2 )``

::

 [[ -f $file ]] && echo $file exists || { echo error; exit 1; }
 
Here Documents code block
----

::
 
 command <<SomeLimitString
 Here comes text with $var and even $() substitutions
 and more just text
 which finally ends on a new line with the:
 SomeLimitString

Often used for messaging, be it an email or dumping bunch of text to file.

::

 NAME=Jussi
 SURNAME=Meikalainen
 $DAYS=14

 mail -s 'Account expiration' $NAME.$SURNAME@aalto.fi<<END-OF-EMAIL
 Dear $NAME $SURNAME,
 
 your account is about to expire in $DAYS days.
 
 $(date)
 
 Best Regards,
 Aalto ITS
 END-OF-EMAIL

Or just outputting to a file (same can be done with echo commands)

::

 cat <<EOF >filename
 ... text
 EOF
 
One trick that is particularly useful, making a long comment out of it

::
 
 : <<\COMMENTS
 here come text that is seen nowhere
 and no need for #
 COMMENTS
 

**Hint** ``<<\LimtiString`` to turn off substitutions and place text as is with $ marks etc

3. session
====
Managing foreground/background processes
----
Adding *&* right after the command send the process to background. Example: ``firefox --no-remote &`` same can be done with any terminal command/function, like ``tar ... &``.

If you have already running process, then Ctrl-z and then ``bg``. Drawback: there is no easy way to redirect the running task output.

List the jobs ruuning in the background ``jobs``, get a job back online: ``fg`` or ``fg <job_number>``. There can be multiple background jobs (remeber forkbombs).

Kill the foreground job: Ctrl-c


Arithmetics
----
BASH supports wide range of arithmetic operators for integers that can be evaluated within ``(( .. ))``

 - ``n++``, ``n--``, ``++n``, ``--n`` increments/decrements
 - ``+``, ``-`` plus minus
 - ``**`` exponent
 - ``*``, ``/``, ``%`` multiplication, division, remainder
 - ``&&``, ``||`` logical AND, OR
 - ``expr?expr:expr`` conditional operator (trinity)
 - ``==``, ``!=``, ``<``, ``>``, ``>=``, ``<=`` comparison
 - ``=``, ``+=``, ``-=``, ``*=``, ``/=``, ``%=`` assignment
 
For full list incl. bitwise operators, see man page.
 
:Exercise: Gauss 1..100 sum example. Write a function that count a sum of any *1+2+3+4+..+n* sequence of numbers. Where *n* is any positive integer.

Loops
----
::

 for name in list; do
   commands
 done

 for school in "SCI ELEC CHEM"; do
  echo "$school is the best!"
 done

 # example below will convert all the jpg files in the current directory to png. ``*.jpg`` similar to ``ls *.jpg``
 for f in *.jpg; do
  convert $f ${f/.jpg/.png}
 done

Same can be done (and often being done) in one line. Can be used Brace expressions like *{1..10}*, command substitution and all kind of extenssions supported by BASH.

If *in list* is omitted, loops uses script/function input arguments $@.

::

 func() { for i; do echo $i; done }; func a b c
 

C-style, expressions evaluated according to the arithmetic evaluation rules

::

 for (( expr1; expr2; expr3 )); do
   commands
 done
 
 LIMIT=10
 for ((a=1; a <= LIMIT ; a++))  # LIMIT with no $
 do
   echo -n "$a "
 done

Loops can be nested.

Other useful loop statement are ``while`` and ``until``. Both execute continously as long as the condition returns exit status zero/non-zero correspondignly.
::
 while condition; do
   ...
 done
 
 LIMIT=10
 var=0
 until ((var == LIMIT)); do
  echo $var
  ((var++))
 done

Condition can be any command, expression, function or a combination of them.

Loop controling: ``break`` -- terminates the loop, ``continue`` -- jump to a new iteration. ``break n`` will terminate *n* levels of loops if they are nested, otherwise terminated only loop in which it is embedded. Same kind of behaviour for ``continue n``.

::

 for i in {1..10}; do
   if (( i%2 == 0 )); then
    continue
   fi
   echo $i  # output odd numbers only
 done

:Exercise: Write a function that count a sum of any *1+2+3+4+..+n* sequence of numbers directly, thus just by summing all the numbers. Let us benchmark to solutions with *time*.
:Exercise: Using for loop rename all the files in the directories *dir1/* and *dir2/* which file names are like *filename.txt* to *filename.edited.txt*. Where *filename* can be any, while extensions is always the same.
:Exercise*: Implement a Bubble sort using bash loops (not *sort* utility).


Arrays
----
BASH supports both indexed and associative one-dimensional arrays. Indexed array can be declared explicilty or with ``declare -a array_name``, other ways:

::
 
 array=(my very first array)
 array=('my second' array [6]=sure)
 array[5]=234
 
To access array elements

::

  echo ${array[0]} ${array[1]}  # elements one by one
  ${array[@]}  # array values at once
  ${!array[@]}  # indexes at once
  ${#array[@]}  # number of elements in the array
  ${#array[2]}  # length of the element number 2

To append elements to the end of array

::

  $array+=(value)

Loops through the indexed array

:: 

 for i in ${!array[@]}; do
   echo \$array[$i] is ${array[$i]}
 done

Negative index counts back from the end of the array, *[-1]* referencing to the last element.

BASH associative arrays needs to be declared first ``declare -A asarr``

::

 asarr=([university]='Aalto University' [city]=Espoo ['street address']='Otakaari 1')
 asarr[post_index]=02150

Addressing is similar to indexed arrays

::

 for i in "${!asarr[*]}"; do
   echo \$asarr["$i"] is ${asarr["$i"]}
 done

:Exercise: make a script/function that produces an array of random numbers (Tip: $RANDOM)

4. session
====
read
----

Catching kill signals
----
Making scripts booletproofed with ``trap``. It is when you want to control the script even when it is being aborted.

::

 trap command list_of_signals   # thus trap catches listed signals only, others it ignores

 trap "echo We are killed" INT TERM
 while :; do
  sleep 30
 done

While instead of *echo*, one can come up with something more clever: function that removes temp files, put something to the log file or a valuable error message to a screen.

**Hint** About signals see *Standard signals* section at ``man 7 signal``. Like Ctrl-c is INT (aka SIGINT).


printf
----
If you have been ever wondering that whether ``echo`` is the only way to output something to a screen, then nope, BASH has ``printf``. Familiar to programmers, it allows make output formatted.

::

 printf format [arguments]
 # printing a text at the end of the line
 printf "%*s\n" $(tput cols) "Hello world!"
 
See more examples at [#]_


parallel
----
It is not a parallelzation in the HPC way (threads, MPI), but the utility to make a number of similar processes to run in parallel, while they differ in input parameters only.

It is not a built-in feature of BASH but an extra utility. 

::

 parallel -i command {} -- arguments_list   # normally the command is passed the argument at the end of its command line. With -i               option, any instances of "{}" in the command are replaced with the argument.
 
 parallel sh -c "echo hi; sleep 2; echo bye" -- 1 2 3   # will run three subshells that each print a message
 parallel -j 3 -- ls df "echo hi"   # will run three independent processes in parallel

On Triton we have installed Tollef Fog Heen's version of parallel from moreutils-parallel CentOS' RPM. GNU project has its own though, of exactly the same name.

Debugging
----
Check for syntax errors without actual running it ``bash -n script.sh``

Or echos each command and its results with ``bash -xv script.sh``. or even adding options directly to the script

::

 #!/bin/bash -xv

To enable debugging for some parts of the code only

::

  set +x
  ... some code
  set -x

One can always use ``echo``, though more elegant would be a function that only prints output if DEBUG is set to 'yes'.

::
 
 #!/bin/bash

 debug() {
   [[ "$DEBUG" == 'yes' ]] && echo " Line $LINENO: $1"
 }
 
 command1
 debug "after command 1, variables list... $var1, $var2"
 command2
 
 # call this script like 'DEBUG=yes ./script.sh' otherwise *debug* function produces no result and script can be used as is.


Another debugging technique is with trap: tracing the variables.

::

 declare -t VARIABLE=value
 trap "echo VARIABLE is being used here." DEBUG

Or simply output variable values on exit

::

 trap 'echo Variable Listing --- a = $a  b = $b' EXIT  # will output variables value on exit
 
 

References
====
.. [#] http://tldp.org/LDP/abs/html/index.html
.. [#] https://www.putty.org/
.. [#] https://www.ibm.com/developerworks/linux/library/l-tip-prompt/
.. [#] https://alvinalexander.com/unix/edu/examples/find.shtml
.. [#] http://www.softpanorama.org/Tools/Find/index.shtml
.. [#] https://the.earth.li/~sgtatham/putty/0.70/htmldoc/
.. [#] https://www.computerhope.com/unix/uumask.htm
.. [#] http://wiki.bash-hackers.org/commands/builtin/printf
