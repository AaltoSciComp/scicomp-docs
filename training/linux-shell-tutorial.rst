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

Before the course: set yourself up with a BASH shell.  Connect to a
server or open on your own computer. Examples and demos given during the lecture
are done on Triton, though should work on all other Linux installations.
Ask for help if needed:

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

Process stat commands::

   pstree
   pstree -u $USER
   pstree -pu $USER
   ps auxw

You can find info about your user::

  id
  echo $SHELL
  echo $HOME

Where you are::

  pwd

Who am I: ``id``, ``echo $HOME``, ``echo $SHELL``
(Your default shell is not a /bin/bash? Login to kosh/taltta and run ``chsh -s /bin/bash``)

Where am I: ``pwd`` (this shows the first piece of process
information: current directory)


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

Your best friend ever -- ``man`` -- collection of manuals. Type
*/search_word* for searching through the man page.  But... if it's a
builtin, you need to use ``help``

**Disable built-in command** ``enable -n echo``, after this */usr/bin/echo*
becomes a default instead of built-in *echo*


Files and directories
---------------------
Files contain data.  They have a name, permissions, owner
(user+group), contents, and some other metadata.


``ls`` is the standard way of getting information about files.

::

 ls, ls -l, ls -lA, ./, ../, *, ?, [], [!], {abc,xyz}, {1..10}, \

There are a variety of commands to manipulate files/directories:

::

 cd, mkdir, cp, rm, rm -r, mv, ln, touch

Note that ``cd`` is a shell builtin which change's the shell's own
working directory.  This is the base from which all other commands
work: ``ls`` by default tells you the current directory.  ``.`` is the
current directory, ``..`` is the parent directory, etc.  This is
inherited to other commands you run.

**Discover other ls features** ``ls -lX``, ``ls -ltr``, ``ls -Q``

**Type of file in one line** ``file <filename>``

**Quotation matters** ``echo "$USER"`` vs ``echo '$USER'``


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

Modifying permissions

::

 chmod u+rwx,g-rwx,o-rwx <files>   # u=user, g=group, o=others, a=all
 # -or-
 chmod 700 <files>   # r=4, w=2, x=1
 
 # recursive, changing all the subdirectories and files at once
 chmod -R <perm> <directory>

 # changing group ownership (you must be a group member)
 chgrp group_name <file or directory>

Some advanced permission bits:

- s-bit:  setuid/setgid bit, preserves user and/or group IDs.
- t-bit: sticky bit, for directories it prevents from removing file by
  another user (example */tmp*)

**File managers** on Triton we have installed Midnight Commander -- ``mc``

**Advanced file status** to get file meta info ``stat <file_or_dir>``

[Lecture notes: that should be a first half, then joint hands-on/break ~30 mins]


:Exercise 1.1:
 - mkdir in your ``$HOME`` (or ``$WRKDIR`` if on Triton), cd there and 'touch' a file.
   Rename it. Make a copy and then remove the original
 - list all files in /usr/bin and /usr/sbin that start with non-letter characters with
   one ``ls`` command
 - (*) ``ls`` lists all files/directories but dotted, but how to ``ls`` dot files/directories only?
 - Run ``file *`` to see what kind of files you have, how to list dot files also while avoiding . and .. directories on the list?
 - (*) Discover ``stat file`` output. What metadata do you find?

:Exercise 1.2:
 - on Triton use the recently created directory at ``$WRKDIR``, allow user and group members
   full access and no access for others
 - change group ownership to (any group that you belong to is fine), set s-bit for the group and
   apply t-bit to a directory, check that the upper directory has *o+x* bit set: now you should
   have a private working space for your group
 - create a directory and a subdirectory in it and set their permissions to 700 with one command
 - ``ls -ld`` tells you that directory has permissions ``rwxr-Sr--``, do group members have
   access there?

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

**inputrc** Check */etc/inpurc* for some default key bindings, more can be defined *~/.inputrc* (left as an exercise)

**CDPATH** helps changing directories faster. When you type ``cd dirname``, the shell tries to go
to one of the local subdirectories and if it is not found shell will try the same command from every
directory listed in the *$CDPATH*.

::

 export CDPATH=$HOME:$WRKDIR:$WRKDIR/project


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
  - ``.bash_profile`` (interactive login to a workstation)
  - they are often a symlink from one to another

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

Creating/editing/viewing file
------------------------------
* A *text editor* edits files as ASCII.  These are your best friend.
  In fact, text files are your best friend: rawest, most efficient,
  longest-lasting way of storing data.
* "pager" is a generic term for things that view files or data.

Linux command line *text editors* like:

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

**The best text viewer ever** ``less -S``  (to open a file in your EDITOR, hit *v*, to search through type */search_word*)

**Watching files while they grow** ``tail -n 0 -f <file>``

Try: add above mentioned ``export PS1`` to *.bashrc*. Remember ``source .bashrc`` to enable changes

:Home exercise: Set some default options for the ``less`` program in your
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

Pipe: output of the first command as an input for the second one ``command_a | command_b``::

 # cat, sort, tr, cut, head, wc, grep examples
 
 # send man page to a default printer
 man -t ls | lpr
 
 # see what directories use the most space
 du -hs * | sort -h
 
 # count a number of logged in users
 w -h | wc -l
 
 # to remove all carriage returns and Ctrl-z characters from a Windows file
 cat win.txt | tr -d '\15\32' > unix.txt
 
 # to list all matching commands
 history | grep -w 'command name'
 
 # print all non-printable characters as well
 ls -lA | cat -A
 
 # print the name of the newest file in the directory (non-dot)
 ls -1tF | grep -v -E '*/|@' | head -1

Redirects:
 - Like pipes, but send data to/from files instead of other processes.
 - Replace a file: ``command > file.txt``
 - Append to a file: ``command >> file.txt`` (be careful you do not mix them up!)
 - Redirect file as STDIN: ``command < file``  (in case program accepts STDIN only)

::

 echo Hello World > hello.txt
 
 ls -lH >> current_dir_ls.txt
 
 # join two files into one
 cat file1 file2 > file3
 
 # extract user names and store them to a file
 getent passwd | cut -d: -f1,5 > users
 
 # join file1 and 2 lines one by one using : as a delimiter
 paste -s -d : file1 file2 > file3

**This is the unix philosophy** and the true power of the shell.  The
**unix philosophy** is a lot of small, specialized, good programs
which can be easily connected together.

To dump output of all commands at once: group them

::

 { command1; command2; } > filename  # commands run in the current shell  as a group
 ( command1; command2; ) > filename  # commands run in external shell as a group
 
**Coreutils by GNU** You may find many other useful commands at
https://www.gnu.org/software/coreutils/manual/coreutils.html


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

**Hint** ``command_a && command_b || command_c``

Try: ``cd /nonexistent_dir && ls /nonexistent_dir`` compare with ``cd /nonexistent_dir; ls /nonexistent_dir``

Try: ``ping -c 1 8.8.8.8 > /dev/null && echo online || echo offline``


grep
----
Later on you'll find out that ``grep`` is one of the most useful
commands you ever discover on Linux (except for all the *other* most
useful commands ever)

::

 grep <pattern> <filename>  # grep lines that match <pattern>
  -or- 
 command | grep <pattern>  # grep lines from stdin

::

 # search all the files in the dir/ and its subdirs, to match the word 'is', case insensitive
 grep -R -iw 'is' dir/
 
 # grep all lines from *command* output, except those that have 'comment' in it
 *command* | grep -v comment
 
 # displaying 2 extra lines before and after the match (-A just after, -B just before)
 grep -C 2 'search word' file
 
 # counts the number of matches
 grep -c <pattern> file(s)
 
 # shows only the matched part of the string (by default grep shows whole line)
 grep -o <pattern> file(s)
 
 # accepts way more advanced regular expressions as a search pattern
 grep -E <extended_regexpr> file(s)

For details on what <pattern> could be, look for REGULAR EXPRESSIONS
at ``man grep``.  Some examples:

::

 # grep emails to a list
 grep -Eio "\b[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,6}\b" file.txt
 
 # grep currently running firefox processes
 ps auxw | grep firefox
 
 # grep H1 and H2 header lines out of HTML file
 grep "<[Hh][12]>" file.html

[Lecturer's notes: ~20 minutes at the end of the session to proceed with the hands-on excersises.
Leftovers can be said as a homework, one can go through them next session or give hints by email.]

:Exercise 1.3:
 - make a pipe that counts number of files/directories (including dot files) in your directory
 - grep directories out of ``ls -l``
 - grep all but blank lines in triton:/etc/bashrc
 - (*) expand the previous one to filter out commented lines also (line starts with #)
 - expand ``du -hs * | sort -h`` to list dot files/directories also
 - (*) count unique logged in users on triton

:Homework:
 - Finish up the exercises mentioned during the session if you have anything left
 - Get familiar with any of the text editor of your choice, nano, vim or
   emacs. We will use it heavily during remaining sessions.
 - Play with the commands grep, cut: find at least two ways to
   extract IP addresses only out of /etc/hosts. Are there other ways?
 - (*) Using pipes and commands echo/tr/uniq, find doubled words out of 'My
  Do Do list: Find a a Doubled Word'. Any easier way to do it?


Session 2
=========
Last time, we focused on interactive things from the command line.
Now, we build on that some and end up with making our own scripts.

Command line processing and quoting
-----------------------------------
So, shell is responsible for interpreting the commands you type. Executing commands
might seem simple enough, but a lot happens between the time you press RETURN and
time your computer actually does something.

* When you enter a command line, it is one string.
* When a program runs, it always takes an array of strings (the
  ``argv`` in C, ``sys.argv`` in Python, for example).  How do you get
  from one string to an array of strings?  Bash does a lot of
  processing.
* The simplest way of looking at it is everything separated by spaces,
  but actually there is more: variable substitution, command
  substitution, arithmetic evaluation, history evaluation, etc.

The partial order of operations is (don't worry about exact order:
just realize that the shell does a lot of different things in same
particular order):

* history expansion
* brace expansion (``{1..9}``)
* parameter and variable expansion (``$VAR``, ``${VAR}``)
* command substitution (``$()``)
* arithmetic expansion (``$((1+1))``)
* word splitting
* pathname expansion (``*``, ``?``, ``[a,b]``)
* redirects and pipes

One thing we will start to see is shell quoting.  There are several types
of quoting (we will learn details of variables later)::

  # Double quotes: disable all other characters except $, ', \  
  echo "$SHELL"
  
  # Single quotes: disable all special characters
  echo '$SHELL'
  
  # backslash disables the special meaning of the next character
  ls name\ with\ space

By special characters we mean::

 # & * ? [ ] ( ) { } = | ^ ; < > ` $ " ' \

There are different rules for embedding quoting in other quoting.
Sometimes a command passes through multiple layers and you need to
really be careful with multiple layers of quoting!  This is advanced,
but just remember it.

::

 echo 'What's up? how much did you get $$?'      # wrong, ' can not be in between ''
 echo "What's up? how much did you get $$?"      # wrong, $$ is a variable in this case
 echo "What's up? how much did you get \$\$?"    # correct
 echo "What's up? how much did you get "'$$'"?"  # correct

At the end of the line ``\`` removes the new line character, thus the command can continue to a next line::

 ping -c 1 8.8.8.8 > /dev/null && \
 echo online || \
 echo offline


Substitute a command output
---------------------------
* Command substitutions execute a command, take its stdout, and  place
  it on the command line in that place.

``$(command)`` or alternatively ```command```. Could be a command or a
list of commands with pipes, redirections, grouping, variables
inside. The ``$()`` is a modern way, supports nesting, works inside double
quotes.  To understand what is going on in these, run the inner
command first.

::

 # get the latest modified file to a variable
 newest=$(ls -F1t | grep -v */ | head -1)
 
 # save current date to a variable
 today=$(date +%Y-%m-%d)
 
 # create a new file with current timestamp in the name (almost unique filename)
 touch file.$(date +%Y-%m-%d-%H-%M-%S)
 
 # archive current directory content, where new archive name is based on current path and date
 tar czf $(basename $(pwd)).$(date +%Y-%m-%d).tar.gz .
 
 # counting directories and files on the fly
 echo Number of directories $(ls -lA | grep ^d | wc -l) files $(ls -lA | grep ^- | wc -l)
  
This is what makes BASH powerful!


More about redirection and pipe
-------------------------------
*STDIN*, *STDOUT* and *STDERR*: reserved file descriptors *0*, *1* and *2*. They always there
whatever process you run.

*/dev/null*  file (actually special operating system device) that
discards all data written to it.

::

 # discards STDOUT only
 command > /dev/null
 
 # discards both STDOUT and STDERR
 command &> /dev/null
 command > /dev/null 2>&1    # same as above, old style notation
 
 # redirects outputs to different files
 command 1>file.out 2>file.err
 
 # takes STDIN as an input and outputs STDOUT/STDERR to a file
 command < input_file &> output_file
 
::

 # what happens if 8.8.8.8 is down? How to make the command more robust?
 ping -c 1 8.8.8.8 > /dev/null && echo online || echo down
 
 # takes a snapshot of the directory list and send it to email, then renames the file
 ls -l > listing && { mail -s "ls -l $(pwd)" jussi.meikalainen@aalto.fi < listing; mv listing listing.$(date +"%Y-%m-%d-%H-%M") }
 
 # a few ways to empty a file
 > filename
 cat /dev/null > filename
 
 # extreme case, if you can't get the program to stop writing to the file...
 ln -s /dev/null filename
 
Pipes are following the same rules with respect to standard output/error. In order to pipe both STDERR and STDOUT ``|&``.

If ``!``  preceeds the command, the exit status is the logical negation.

**tee** in case you still want output to a terminal and to a file ``command | tee filename``


find
----
* ``find`` is a very unixy program: it finds files, but in the most
  flexible way possible.
* It is a amazingly complicated program
* It is a number one in searching files in shell

With no options, just recursively lists all files starting in current directory::

  find
  find | grep some_filename

The first option gives a starting directory::

  find /etc/

More options: by modification/accessing time, by ownership, by access
type, joint conditions, case-insensitive, that do not match, etc [#]_
[#]_::

 # -or-  'find ~ $WRKDIR -name file.txt' one can search more than one dir at once
 find ~ -name file.txt
 
 # look for jpeg files in the current dir only
 find . -maxdepth 1 -name '*.jpg' -type f
 
 # find all files of size more than 10M and less than 100M
 find . -type -f -size +10M -size -100M
 
 # find everything that does not belong to you
 find ~ ! -user $USER | xargs ls -ld
 
 # open all directories to group members
 find . -type d -exec chmod g+rwx {} \;
 
 # find all s-bitted binaries
 find /usr/{bin,sbin} -perm /u=s
 
 # find and remove all files older than 7 days
 find path/dir -type f -mtime +7 -exec rm -f {} \;

Find syntax is actually an entire boolean logic language given on the
command line: it is a single expression evaluated left to right with
certain precedence.  Thus, you can get amazingly complex if you want to.

**find on Triton**  On Triton's WRKDIR it is ``lfs find``.  This uses a raw lustre connection
to make it more efficient than accessing every file. Has somewhat limited abilities as comparing
to GNU find. For details ``man lfs`` on Triton.

**Fast find -- locate**  Another utility that you may find useful ``locate <pattern>``, but on
workstations only.  This uses a cached database of all files, and
just searches that database so it is much faster.

**Too many arguments**  error solved with the ``find ... | xargs``


Aliases
-------
* Alias is nothing more than a shortcut to a long command sequence
* With alias one can redefine an existing command or name a new one
* Alias will be evaluated only when executed, thus it may have all the expansions and
  substitutions one normally has on the cli
* They are less flexible than functions which we will discuss next

::

 # your own listing command
 alias l='ls -lAF'
 
 # shortcut for checking space usage
 alias space='du -hs .[!.]* * | sort -h'
 
 # prints in the compact way login/group
 alias me="echo \"'$(id -un)' '$(id -gn)'\""
 
 # redefine rm
 alias rm='rm -i'
 alias rm='rm -rf'

Aliases go to *.bashrc* and available later by default (really,
anywhere they can be read by the shell).

[Lecturer's notes: about 30 mins joint hands-on session + break]

:Exercise 2.1:
 - Define above mentioned ``ping ...`` command as an alias (you name it, literally) in *.bashrc*
   once you verify it works. Then ``source .bashrc`` and try the new alias.
 - Pick up */scratch/scip/BASH/windows.txt* file and convert it to UNIX format using ``tr`` and
   redirects only. Tip: remind first session examples.
 - Find all the files in your $HOME that are readable or writable by everyone
 - (*) Using find, duplicate current directory tree (to some other dir, only tree, no content)
 - (*) Join *find* and *grep* power and find all the files in /{usr/,}{bin,sbin} that have '#!/bin/bash' in it

:Exercise 2.2:
 - On Triton find (lfs find ... ) all the dirs/files at $WRKDIR that do not belong to your group.
   Tip: on Triton at WRKDIR your username $USER and group name are the same. On any other filesystem,
   ``$(id -gn)`` returns your group name.
 - Extend above command to fix the group ownership  (... | xargs)
 - On Triton go through all $WRKDIR subdirectories with 'lfs find ...' and set s-bit for the group 


Your ~/bin and PATH
-------------------
The PATH is an environment variable. It is a colon delimited list of directories that your
shell searches through when you enter a command. Binaries are at */bin*, */usr/bin*,
*/usr/local/bin* etc. The best place for your own is *~/bin*.::

 # add to .bashrc
 export PATH="$PATH:$HOME/bin"
 # after you have your script written, set +x bit and run it
 chmod +x ~/bin/script_name.sh
 script_name.sh

You can find where a program is using ``which``::

  which ls
  which cd      # nothing - not a program, it's a builtin!

Other options::

 # +x bit and ./
 chmod +x script.sh
 ./script.sh   # that works if script.sh has #!/bin/bash as a first line
 # with no x bit
 bash script.sh  # this will work even without #!/bin/bash

**Extension is optional** note that *.sh* extension is optional, script may have any name


Functions as part of your environment
-------------------------------------
Alias is a shortcut to a long command, while function is a piece of programming
that has logic and can accept input parameters. Functions can be defined on-the-fly
from the cli, or can go to a file. Let us set *~/bin/functions* and collect
everything useful there.::

 # cd to the directory and lists it at once
 # can be run as: lcd <path/to/directory>
 lcd() {
   cd $1
   ls -FlA
 }
 
 # in one line, note spaces and ; delimiters
 lcd() { cd $1; ls -FlA; }
 # -or- in a full format
 function lcd { cd $1; ls -FlA; }
 
By now function has been defined, to run it, one has to invoke it.::

 source ~/bin/functions
 lcd dir1

The function refers to passed arguments by their position (not by name),
that is $1, $2, and so forth::

 func_name arg1 arg2 arg3  # will become $1 $2 $3

Functions in BASH have ``return`` but it only returns the exit code. By
default variables are in the global space, once chaged in the function is
seen everywhere else. ``local`` can be used to localize the vars. Compare::

 var=2; f() { var=3; }; f; echo $var
 var=2; f() { local var=3; }; f; echo $var

If you happened to build a function in an alias way, redefining a command name while
using that original command inside the function, you need to type *command* before
the name of the command, like::

 rm() { command rm -i "$@"; } 

here you avoid internal loops (forkbombs).


Variables
---------
In shell, variables define your environment. Common practice is that environmental vars are written IN CAPITAL: $HOME, $SHELL, $PATH, $PS1, $RANDOM. To list all defined variables ``printenv``. All variables can be used or even redefined. No error if you call an undefined var, it is just considered to be empty::

 var1=100 var2='some string'  # assign a variable, note, no need for ;
 $var1  # call a variable
 var3=$var1  # assign to another var
 var+=<string>/<integer>  # append a var
   var1+=50  # var1=150
   var2+=' more' # var2 is 'some string more'
 echo "var1 is $var1"  # use is the commands

There is no need to declare things in advance: there is flexible
typing.  In fact, you can access any variable, defined or not.
However, you can still declare things to be of a certain type if you
need to::

 declare -r var=xyz   # read-only
 declare -i var  # must be treated as an integer, 'man bash' for other declare options

BASH is smart enough to distinguish a variable inline without special quoting::

 dir=$HOME/dir1 fname=file fext=xyz echo "$dir/$fname.$fext"

though if variable followed by a number or a letter, you have to
explicitly separate it with the braces syntax::

 echo ${dir}2/${file}abc.$fext

Built-in vars:

 - $?  exit status of the last command
 - $$  current shell pid
 - $#  number of input parameters
 - $0  running script name
 - $FUNCTION  function name being executed, [ note: actually an array ${FUNCTION[*]} ]
 - $1, $2 ... input parameter one by one (function/script)
 - "$@" all input parameters as is in one line

::

 example() { echo -e " number of input params: $#\n input params: $@\n shell process id: $$\n script name: $0\n function name: $FUNCNAME"; return 1; }; f arg1 arg2; echo "exit code: $?"

What if you assing a variable to a variable like::

 var2='something'
 var1=\$var2
 echo $var1     # will return '$var2' literally
 
 # BASH provides built-in 'eval' command that reads the string then re-evaluate it
 # if variables etc found, they are given another chance to show themselves
 
 eval echo $var1  # returns 'something'

In more realistic examples it is often used to compose a command string based on input
parameters or some conditionals and then evaluate it at very end.


Magic of BASH variables
-----------------------
BASH provides wide abilities to work with the vars "on-the-fly" with
``${var...}`` like constructions.  This lets you do simple text
processing easily.  These are nice, but are easy to forget so you will
need to look them up when you need them.

 - Substitute a var with default *value* if empty: ``${var:=value}``
 - Print an *error_message* if var empty: ``${var:?error_message}``
 - Extract a substring: ``${var:offset:length}``, example ``var=abcde; echo ${var:1:3}`` returns 'bcd'
 - Variable's length: ``${#var}``
 - Replace beginning part: ``${var#prefix}``
 - Replace trailing part: ``${var%suffix}``
 - Replace *pattern* with the *string*: ``${var/pattern/string}``

::

 # will print default_value, which can be a variable
 var=''; echo ${var:=default_value}
 var1=another_value; var='';  echo ${var:=$var1}
 
 # will print 'not defined' in both cases
 var='';  echo ${var:?not defined}
 var=''; err='not defined'; echo ${var:?$err}
 
 # will return 'love you'
 var='I love you'; echo ${var:2:8}
 
 # will return 15, that is a number of characters
 var='I love you too!'; echo ${#var}
 
 # returns file.ext
 var=26_file.ext; echo ${var#[0-9][0-9]_}
 
 # in both cases returns 26_file
 var=26_file.ext; echo ${var%.ext}
 var=26_file.ext; echo ${var%.[a-z][a-z][a-z]}
 
 # returns 'I hate you'
 var='I love you'; echo ${var/love/hate}

Except for the *:=* the variable remains unchanged. If you want to
redefine a variable::

  var='I love you'; var=${var/love/hate}; echo $var  # returns 'I hate you'


[Lecturer's note: ~20 minutes for the hands-on exercises. Solution examples can be given at very end.]

:Exercise 2.3:
 - Expand *lcd()* function to have WRKDIR as a default directory in case function is invoked
   without any input parameter.
 - Implement a 'fast find' function ``ff word``. The function should return a long listing
   (ls -ldA) of any file or directory names that contain the <word>. Make search case insensitive.
   Note: your newly ceated functions should go to *~/bin/functions*
 - Write two functions ``get_filename()`` and ``get_extension()``. Both should accept a full filename
   like *path/to/filename.ext* of any length and return *filename* or *ext* correspondingly.
   Extenssion can be of any length. Function should handle missing argument case correctly.
 - Expand *get_filename()* so that it would accept extenssion pattern as a second argument (if given) and
   return *filename* out of *path/to/filename.tar.gz* or alike. I.e. ``get_filename path/to/filename.tar.gz tar.gz``
 - (*) By now one should be able to explain: ``:() { :|:&; };:``. *&* in this case sends process
   to background. [WARNING: it is a forkbomb]
 


Session 3: programming logic
=========

``[[ ]]``
------------------------------
* ``[[ expression ]]`` returns 0=true/success or 1=false/failure depending on the
  evaluation of the conditional *expression*.
* ``[[ expression ]]`` is a new upgraded variation on ``test`` (also known as ``[ ... ]``),
  all the earlier examples with single brackets that one can find on the net, will also work
  with double
* Inside the double brackets it performs tilde expansion, parameter and variable expansion,
  arithmetic expansion, command substitution, process substitution, and quote removal
* Conditional expressions can be used to test file attributes and perform string and arithmetic
  comparisons

Selected examples file attributes and variables testing:
 - ``-f`` true if is a file
 - ``-r`` true if file exists and readable
 - ``-d`` true if is a directory
 - ``-z`` true if the length of string is zero (always used to check that var is not empty)
 - ``-n`` true if the length of string is non-zero
 - ``file1 -nt file2`` true if *file1* is newer (modification time)
 - many more others

::

 # checks that file exists
 [[ -f $file ]] && echo $file exists || { echo error; exit 1; }
 
 # check that directory does not exist before creating one
 [[ -d $dir ]] || mkdir $dir

Note that integers have their own construction ``(( expression ))`` (we come back to this),
though ``[[ ]]`` will work for them too

 - ``==`` strings or integers are equal  (``=`` also works)
 - ``!=`` strings or integers are not equal
 - ``string1 < string2`` true if *string1* sorts before *string2* lexicographically
 - ``>`` vice versa, for integers greater/less than
 - ``string =~ pattern`` matches the pattern against the string
 - ``&&``  logical AND, conditions can be combined
 - ``||`` logical OR
 - ``!`` negate the result of the evaluation
 - ``()`` group conditional expressions

In addition, double brackets inherit several operands to work with integers mainly:

 - ``-eq``, ``-ne``, ``-lt``, ``-le``, ``-gt``, ``-ge``  equal to, not equal  to,
   less  than, less than or equal to, greater than, or greater than or equal


::

 # the way to check input arguments, if no input, exit (in functions 'return 1')
 [[ $# -eq 0 ]] && { echo Usage: $0 arguments; exit 1; }

 # the result will be true, since Aalto sorts before HY
 [[ Aalto < HY ]]; echo $?
 
 # though with a small modification, the way around is going to be true also
 [[ ! Aalto > HY ]]; echo $?

 # this will return also true, here we compare lengths, Aaaaalto has longer... name
 s1=Aalto; s2=HY; [[ ${#s1} -gt ${#s2} ]]; echo $?

 # true, since Aalto in both cases sorted before HY and UTU
 [[ Aalto < HY && Aalto < UTU ]]; echo $?
 
 # false, since both fail
 [[ ( Aalto < HY && Aalto > UTU ) || HY > UTU ]]; echo $?
 
 # syntax allows write in a compact way, though [[ ]] always require spaces
 [[ (Aalto<HY&&Aalto>UTU)||HY<UTU ]]

Matching operator brings more oportunities, here where regular expressions come in place.
Even more: matched strings in parentheses assigned to *${BASH_REMATCH[]}* array elements!

* Regular expressions (regexs) are basically a mini-language for
  searching within, matching, and replacing text in strings.
* They are extremely powerful and basically required knowledge in any
  type of text processing
* Yet there is a famous quote by Jamie Zawinski: "Some people, when
  confronted with a problem, think 'I know, I'll use regular
  expressions.' Now they have two problems."  This doesn't mean
  regular expressions shouldn't be used, but used carefully.

Selected operators:

 - ``.`` 	matches any single character
 - ``?`` the preceding item is optional and will be matched, at most, once
 - ``*`` 	the preceding item will be matched zero or more times
 - ``+``  the preceding item will be matched one or more times
 - ``{N}`` the preceding item is matched exactly N times
 - ``{N,}`` the preceding item is matched N or more times
 - ``{N,M}`` the preceding item is matched at least N times, but not more than M times
 - ``[abd]``, ``[a-z]``  a character or a range of characters/integers
 - ``^``  beginning of a line
 - ``$``  the end of a line
 - ``()`` grouping items, this what comes to ${BASH_REMATCH[@]}

::

 # match an email
 email='jussi.meikalainen@aalto.fi'; regex='(.*)@(.*)'; [[ "$email" =~ $regex ]]; echo ${BASH_REMATCH[*]}

 # a number out of the text
 txt='Some text with #1278 in it'; regex='#([0-9]+ )'; [[ "$txt" =~ $regex ]] && echo ${BASH_REMATCH[1]} || echo do not match

**For case insesitive matching**, set ``shopt -s nocasematch``  (to disable it back ``shopt -u nocasematch``)


if/elif/else
------------
Yes, we have ``[[ ]] && ... || ...`` but scripting style is more logical with if/else construction::

 if condition; then
   command1
 elif condition; then
   command2
 else
   command3
 fi

At the *condition* place can be anything what returns an exit code, i.e. ``[[ ]]``, command/function,
an arithmetic expression ``$(( ))``, or a command substitution.

::

 # to compare two input strings/integers
 if [[ "$1" == "$2" ]]
 then
   echo The strings are the same
 else
   echo The strings are different
 fi

 # checking command output
 if ping -c 1 8.8.8.8 &> /dev/null; then
   echo Online
 elif ping -c 1 127.0.0.1 &> /dev/null; then
   echo Local interface is down
 else
   echo No external connection
 fi

 # check input parameters
 if [[ $# == 0 ]]; then
   echo Usage: $0 input_arg
   exit 1
 fi
 ... the rest of the code 


case
----
Another option to handle flow, instead of nested *ifs*, ``case``.

::
 
 read -p "Are you ready (y/n)? " yesno   # expects user input
 case $yesno in
   y|yes) do_something_if_yes ;;
   n|no) do_something_if_no ;;
   *) do_something_else ;;
 esac
 # $yesno can be replaced with ${yesno,,} to convert to a lower case on the fly

**Here is introduced** ``read`` built-in command that reads one line from the standard
input or file descriptor.

``case`` tries to match the variable against each pattern in turn. Understands patterns rules like ``*, ?, [], |``.

::

 read -p "Enter your age? " age
 case $age in
   [1-9]|1[0-2]) echo Child ;;
   1[3-9]|[2-5][0-9]) echo Adult ;;
   [6-9][0-9]) echo Senior ;;
   *) echo Should be dead by now or wrong input ;;
 esac
 
``;;`` is important, if replaced with ``;&``, execution will continue with the command
associated with the next pattern, without testing it. ``;;&`` causes the shell to test
next pattern. The default behaviour with ``;;`` is to stop matches after first pattern
has been found.

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

:Exercise 3.1:
 - Using BASH builtin functionality implement ``my_grep pattern string`` script that picks
   up a pattern ($1) and a string ($2) as an input and reports whether pattern matches any
   part of the string or not.
   
   - The script must check that number of input parameters is correct.
   - Expand *my_grep* script to make search case insesitive
 
 - Implement a ``my_mkdir`` script that either accepts a directory name as an input parameter or requests it
   with ``read`` if no input parameter is given. Script should create a directory if does not exist with
   the access permissions 700.
   
   - Add a sanity check so that directory name should allow alphanumeric characters only.
  

Arithmetics
-----------
BASH works with the integers only but supports wide range of arithmetic operators using
arithmetic expanssion ``$(( expression ))``.

 * All tokens in the expression undergo parameter and variable expansion, command  substitution,
   and  quote  removal. The result is treated as the arithmetic expression to be evaluated.
 * Arithmetic  expansions  may  be nested.
 * Variables inside double parentheses can be without $ sign.
 * BASH has other options to work with the integers, like ``let``, ``expr``, ``$[]``, and in
   the older scripts/examples you may meet them

 - ``n++``, ``n--``, ``++n``, ``--n`` increments/decrements
 - ``+``, ``-`` plus minus
 - ``**`` exponent
 - ``*``, ``/``, ``%`` multiplication, division, remainder
 - ``&&``, ``||`` logical AND, OR
 - ``expr?expr:expr`` conditional operator (ternary)
 - ``==``, ``!=``, ``<``, ``>``, ``>=``, ``<=`` comparison
 - ``=``, ``+=``, ``-=``, ``*=``, ``/=``, ``%=`` assignment
 - ``()``  sub-expressions in parentheses  are  evaluated first
 
Full list includes bitwise operators, see ``man bash``.

::

 # without dollar sing value is not returned, though 'n' has been incremented
 n=10; ((n++))
 
 # but if we need a value
 n=10; m=3; q=$((n**m))
 
 # here we need exit code only
 if ((q%2)); then echo odd; fi
 if ((n>=m)); then ...; fi
 
 # condition ? integer_value_if_true : integer_value_if_false
 n=2; m=3; echo $((n<m?10:100))
 
::

 #!/bin/bash
 
 # sum all numbers from 1..n, where n is a positive integer
 # Gauss way, summing pairs 
 
 if (($#==1)); then
   n=$1
 else
   read -p 'Give me a positive integer ' n
 fi

 if ((n%2)); then
   s=$(((n-1)/2*n+n))
 else
   s=$((n/2*(n+1)))
 fi

 echo Sum from 1..$n is $s

Left for the exercise: make a summation directly 1+2+3+...+n and compare performance with the above one.

 
Loops
----
BASH offers several options for iterating over the lists of elements. The options include

 * Basic construction ``for arg in [list]``
 * C-style *for loop* ``for ((i=1; i <= LIMIT ; i++))``
 * while and until constructs

::

 # simple loop over a list of items, note that if you put 'list' in quotes it will be
 # considered as one item
 for school in SCI ELEC CHEM; do
   echo "$school is the best!"
 done

 # if path expanssions used (*, ? etc), loop automatically lists current dir
 # example below will convert all jpg files in the current directory to png.
 # ``*.jpg`` similar to ``ls *.jpg``
 for f in *.jpg; do
  convert $f ${f/.jpg/.png}
 done
 
 # do ... done in certain contexts, can be omitted by framing the command block within curly brackets
 # and certainly for loop can be written in one line as well
 for i in {1..10}; { echo i is $i; }

 # if 'in list' omitted, for loop goes through script/function input parameters $@
 # here is a loop to rename files which names are given as input parameters
 # touch file{1..3}; ./newname file1 file2 file3
 for old; do
   read -p "old name $old, new name: " new
   mv -i "$old" "$new"
 done

 # loop output can be piped or redirected as output of any other command
 for u in Aalto HY UTU; do
   case "$u" in
     Aalto|aalto|AALTO) echo My univesity is Aalto Univesity ;;
     HY|hy) echo My univesity is University of Helsinki ;;
     UTU|utu) echo My univesity is University of Turku ;;
     *) echo "Sorry, no university"; exit 1 ;;
   esac
 done | sort > filename

The *list* can be anything what produces a list, like Brace expanssion *{1..10}*, command substitution etc.

::
 
 # on Triton, do something to all pending jobs based on squeue output
 for jobid in $(squeue -h -u $USER -t PD -o %A); do
   scontrol update JobId=$jobid StartTime=now+5days
 done
   
 

C-style, expressions evaluated according to the arithmetic evaluation rules

::

 N=10
 for ((i=1; i <= N ; i++))  # LIMIT with no $
 do
   echo -n "$i "
 done

Loops can be nested.

Other useful loop statement are ``while`` and ``until``. Both execute continously as long as the
condition returns exit status zero/non-zero correspondignly.

::

 while condition; do
   ...
 done
 
 # sum of all numbers 1..n
 read -p 'Give a positive integer: ' n
 i=1
 until ((i > n)); do
   ((s+=i))
   ((i++))
 done
 echo Sum of 1..$n is $s

 # endless loop, note : is noop command in BASH, does nothing
 # can be run as sort of "deamon", process should be stopped with Ctrl-c or killed
 while true; do : ; done
 
 # drop an email every 10 minutes about running jobs on Triton
 # can be used in combination with 'screen', and run in background
 while true; do
   squeue -t R -u $USER | mail -s 'running jobs' mister.x@aalto.fi
   sleep 600
 done

 #  reads a file passed line by line, 
 # IFS= variable before read command to prevent leading/trailing whitespace from being trimmed
 input=/path/to/txt/file
 while IFS= read -r line; do
  echo $line
 done < "$input"
 
 # reading file fieldwise
 file="/etc/passwd"
 while IFS=: read -r f1 f2 f3 f4 f5 f6 f7; do
   printf 'Username: %s, Shell: %s, Home Dir: %s\n' "$f1" "$f7" "$f6"
 done <"$file"
 
All the things mentioned above for *for* loop applicable to ``while`` / ``until`` loops.

*printf* should be familiar to prorgammers, allows formatted output

Loop controling:

 - ``break`` terminates the loop
 - ``continue`` jump to a new iteration
 - ``break n`` will terminate *n* levels of loops if they are nested, otherwise terminated only
     loop in which it is embedded. Same kind of behaviour for ``continue n``.

::

 for i in {1..10}; do
   if (( i%2 == 0 )); then
    continue
   fi
   echo $i  # output odd numbers only
 done

 # this goes through all given directories to process found files
 # if directory is not accessible, it fails, if file is empty it tries next one
 dir_list='dir1 dir2 dir3'
 for dir in $dir_list; do
   cd "$dir" || { echo $dir fails; break; }
   for file in *; do
     [[ -s $file ]] || { echo $dir/$file is empty; continue; }
     echo processing $dir/$file
   done
 done
     

:Exercise 3.2:
 - Write to files both scripts that count a sum of any *1+2+3+4+..+n* sequence. The Gauss version
   and direct summation. Benchmark them with *time* for n=10000 or more.
   
   - For the direct summation one can avoid loops, how? Tip: discover ``eval $(echo {1..$n})``
 
 - On kosh/lyta run ``net ads search samaccountname=$USER accountExpires 2>/dev/null``
   to get your account expiration date. It is a 18-digit timestamp, the number of 100-nanoseconds
   intervals since Jan 1, 1601 UTC. Implement a function that accept a user name, and if not given
   uses current user by default, and then converts it to the human readable time format.
   Tip: http://meinit.nl/convert-active-directory-lastlogon-time-to-unix-readable-time
   
   - Expand it to handle "Got 0 replies" reponse, i.e. account name not found.
   
 - Using for loop rename all the files in the directories *dir1/* and *dir2/* which file names
   are like *filename.txt* to *filename.edited.txt*. Where *filename* can be any.
 


Session 4
=========

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


Here Documents code block
-------------------------

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


Catching kill signals: trap
---------------------------
Making scripts booletproofed with ``trap``. It is when you want to control the script even when it is being aborted.

::

 trap command list_of_signals   # thus trap catches listed signals only, others it ignores

 trap "echo We are killed" INT TERM
 while :; do
  sleep 30
 done

While instead of *echo*, one can come up with something more clever: function that removes temp files, put something to the log file or a valuable error message to a screen.

**Hint** About signals see *Standard signals* section at ``man 7 signal``. Like Ctrl-c is INT (aka SIGINT).


:Exercise:
 - make a script/function that produces an array of random numbers (Tip: $RANDOM)
 - Implement a Bubble sort using arrays and loops and other built-in BASH functionality (no *sort* etc).
 - (*) Implement a script that sorts text file lines by lines length


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


parallel
----
It is not a parallelzation in the HPC way (threads, MPI), but the utility to make a number of similar processes to run in parallel, while they differ in input parameters only.

It is not a built-in feature of BASH but an extra utility. 

::

 parallel -i command {} -- arguments_list   # normally the command is passed the argument at the end of its command line. With -i               option, any instances of "{}" in the command are replaced with the argument.
 
 parallel sh -c "echo hi; sleep 2; echo bye" -- 1 2 3   # will run three subshells that each print a message
 parallel -j 3 -- ls df "echo hi"   # will run three independent processes in parallel

On Triton we have installed Tollef Fog Heen's version of parallel from moreutils-parallel CentOS' RPM. GNU project has its own though, of exactly the same name.


Managing foreground/background processes
----
Adding *&* right after the command send the process to background. Example: ``firefox --no-remote &`` same can be done with any terminal command/function, like ``tar ... &``.

If you have already running process, then Ctrl-z and then ``bg``. Drawback: there is no easy way to redirect the running task output.

List the jobs ruuning in the background ``jobs``, get a job back online: ``fg`` or ``fg <job_number>``. There can be multiple background jobs (remeber forkbombs).

Kill the foreground job: Ctrl-c


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


About homeworks
---------------
Comming soonish...


References
==========
.. [#] http://tldp.org/LDP/abs/html/index.html
.. [#] https://www.putty.org/
.. [#] https://www.ibm.com/developerworks/linux/library/l-tip-prompt/
.. [#] https://alvinalexander.com/unix/edu/examples/find.shtml
.. [#] http://www.softpanorama.org/Tools/Find/index.shtml
.. [#] https://the.earth.li/~sgtatham/putty/0.70/htmldoc/
.. [#] https://www.computerhope.com/unix/uumask.htm
.. [#] http://wiki.bash-hackers.org/commands/builtin/printf


Bonus material
==============
Parts that did not fit.



Files and dirs advances
----
Advanced access permissions

Access list aka ACL: ``getfacl`` and ``setfacl``

 - Allow read access for a user ``setfacl -m u:<user>:r <file_or_dir>``
 - Allow read/write access for a group ``setfacl -m g:<group>:rw <file_or_dir>``
 - Revoke granted access ``setfacl -x u:<user> <file_or_dir>``
 - See current stage ``getfacl <file_or_dir>``

**Hint** even though file has a read access the top directory must be searchable before external user or group will be able to access it. Best practice on Triton ``chmod -R o-rwx $WRKDIR; chmod o+x $WRKDIR``

Setting default access permissions: add to *.bashrc* ``umask 027`` [#]_

:Home exercise: practice with setfacl: set a directory permissions so that only you and some
user/group of your choice would have access to a file 



[FIXME: should be moved to another tutorial *SSH: beyond login*]

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

