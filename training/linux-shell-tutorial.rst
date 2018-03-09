Course preview
====
Linux Shell tutorial by Science IT at Aalto University.

BASH practicalities, shell scripting. Learning by doing.

Corresponds to 4 sessions 3h each, session rough schedule 2x1h25m with 10m break in between.

Setting up instructions for the lecturer: one slim terminal at the top that keeps a track of the commands

 - export PROMPT_COMMAND='history -a'   # .bashrc or all the terminals one launches commands
 - tail -n 0 -F .bash_history

Main terminal white&black with the enlarged font size.
 
Starred exersices (*) for the advanced user, to keep them busy.

Based on 
 - ``man bash`` v4.2 (Triton default version in Feb 2018)
 - Advanced BASH scripting guide [#]_
 - UNIX Power Tools, Shelley Powers etc, 3rd ed, O'Reilly
 - common sence and 20+ years Linux experience
 - see also other references in the text

-----------------------------------------------------------------------------

1. session
====
Interactive usage of BASH

Linux and Mac users: just open a terminal window.

Windows users: install PuTTY [#]_ then SSH to any interactive server at Aalto or your department.

Shell -- is what you get when your teminal window is open. It is a command-line (CLI), an interface that intepreters and executes the commands.

Built-in and external commands
----
cd, pwd, echo, ls vs. date, less, lpr etc. 

**Hint** ``type -a`` to find what is behind the name

Who am I: ``id``, ``echo $HOME``, ``echo $SHELL`` 
(Your default shell is not a /bin/bash? Login to kosh/taltta and run ``chsh -s /bin/bash``)

Where am I: ``pwd``

Your best friend ever -- ``man`` -- collection of manuals.


**Hint** ``man -t ls | lpr`` to print it to a default printer

Files and dirs
----
ls, ls -l, ls -la, ./, ../, *, ?

cd, mkdir, cp, rm, rm -r, mv, touch

**Hint** ``ls -lX``, ``ls -ltr``, ``file <filename>``

:Exercise: mkdir in your $HOME, cd there and 'touch' a file. Rename it. Make a copy and then remove the original.
:Exercise*: ``ls`` dot files only. Create a dozen of files with one command with names like file1.txt, file2.txt, ... file12.txt

Permissions
----
rwxrwxrwx -- read, write, execute/search
Could be a link -- ln -s. s- and t-bits.

chmod u+rwx,g-rwx,o-rwx <files> -or- chmod 700 <files>

chmod -R ...

**Hint** File Manager like Midnight Commander -- ``mc``

:Exercise: allow group members to open the file, while others should have no acceess to the directory at all.
:Exercise*: make a few more subdirectories and set +x bit for group for the current dir and all subdirectories only (not files) with one command

Hotkeys
----
- TAB -- autocomlpetion
- Home `or` Ctrl-a -- start of the command line
- End `or` Ctrl-e -- end
- Ctrl-left/right arrows `or` Alt-b/Alt-f  - moving by one word there and back
- up/down arrows -- command history
- Ctrl-l -- clear the screen
- Ctrl-Shift-c -- copy
- Ctrl-Shift-v -- paste
- Ctrl-Shift--  -- undo the last changes on cli
- Ctrl-R -- command history search
- Ctrl-u  -- remove beginning of the line, from cursor
- Ctrl-k -- remove end of the line, from cursor
- Ctrl-w -- remove previous word

**Hint** ``history | grep KEYWORD``

Initialization files
----
.bashrc and .bash_profile

Linux terminal editors: VIM, Emacs, Nano. Can be set with the ``export EDITOR=``.

``PS1="[\d \t \u@\h:\w ] $ "``  for permanent changes, add to .bashrc wtih ``export PS1``. For special characters see PROMPTING at ``man bash``

:Exercise: customize a prompt ``$PS1``
:Exercise*: make it colorful

After editing: ``source .bashrc``. source vs execution.

Redirect, pipe
----
Append to a file or replace a file ``command > file.txt`` *or* ``command >> file.txt``

``echo Hello World > hello.txt`` *or* ``ls -lH >> current_dir_ls.txt``

Output of the first command as an input for the second one ``command_a | command_b``

sort, grep, tr, cut, /dev/null

``du -hs * | sort -h``

``w -h | wc -l``

``ls -1 | tr '\n' ' '``

``getent passwd | cut -d: -f1,5 > users``

:Exersice: make a pipe that counts number of files (inluding dot files) in your directory
:Exercise*: expand ``du`` to list dot files/directories also
:Exercise*: Count unique logged in users on kosh/taltta/triton or anywhere else

&& and ||
----
If succesful ``command_a && command_b``

If failed  ``command_a || command_b``

**Hint** command_a && command_b || command_c

Aliases
----
Define a new or re-define an old command ``alias space='du -hs .[!.]* * | sort -h'``, ``alias rm='rm -i'``

Example: ``alias chknet='ping -c 1 8.8.8.8 > /dev/null && echo online || echo offline'``

Create/edit a file
-----
Editors like: *vim*, *emacs* or the simplest one *nano*.

Quick look at the text file ``cat filename.txt``

Other quick ways to add something to file (no need for an editor)

``echo 'Some sentense, or whatever else 1234567!-+>$#' > filename.txt``

``cat > filename2.txt`` to finish typing and write written to the file, press enter, then Ctrl-d.

:Exercise: collect above mentioned (or your own) aliases to a file

find
----
It is a number one in searching files from shell.

``find ~ -name file.txt`` *or* ``find $HOME $WRKDIR -name file.txt``

``find . -name 'file*' -type f``

``find . -type d -exec chmod g+x {} \;``

More options: by modification/accessing time, by ownership, by access type, joint conditions, case-insensitive, that do not match, etc [#]_

**Hint**  On Triton ``lfs find``

:Exercise: Find all files with 'lock' in the name in your home directory
:Exercise*: Find all the files in your $HOME or $WRKDIR that are readable or writable by everyone and make them

Archiving files
----
To archive ``tar czvf path/to/archive.tar.gz directory/to/archive``

To open ``cd directory/to/open/archive; tar xzf path/to/archive.tar.gz``

To watch what is there ``tar tzf ...``

By now you should know that much to get started with the interactive BASH usage.

Managing foreground/background processes
----
Adding *&* right after the command send the process to background. Example: ``firefox --no-remote &`` same can be done with any terminal command/function, like ``tar ... &``.

If you have already running process, then Ctrl-z and then ``bg``. Drawback: there is no easy way to redirect the running task output.

List the jobs ruuning in the background ``jobs``, get a job back online: ``fg`` or ``fg <job_number>``. There can be multiple background jobs (remeber forkbombs).

Kill the foreground job: Ctrl-c

Exit the shell
----
``logout`` or Ctrl-d (export IGNOREEOF=1 to *.bashrc*)

In order to keep your sessions running while you logged out discover ``screen``

 - ``screen`` to start a session
 - Ctrl-a-d to detach the session while you are in
 - ``screen -ls`` to list currently running sessions
 - ``screen -rx <session_id>`` to attach the session, one can use TAB for the autocompletion or skip the <session_id> if there is only one session running 

Example: irssi on kosh / lyta


2. session
====
Command line advances and introduction to BASH scripting

Files and dirs advances
----
Wildcards, on top of * and ?, that can be used with ls, touch, rm, mkdir, cp or anywhere else

[abc], [a-bxy] {abc,xyz}, {3..15}, {c-h}, [!.], \(

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

As an example ``lcd``, could be defined in *.bashrc*

::

 lcd() {
   cd $1
   ls -1 | wc -l
 }

::

 $ source .bashrc
 $ lcd

Functions in BASH is just a piece of code that once declared can be invoked at any place later with args or withour. ``return`` returns the exit code only. By default vars are in global space, once chaged in the function is seen everywhere else. ``local`` can be used to localize the vars.

:Exercise: expand ``lcd`` so that it would print number of files and directories separately
:Exercise*: write a function that makes files/subdirectories readable by all on a given directory (note r for files, xr for dirs)

Variables
----
In shell, variables define your environment. Common practice is that environmental vars are written IN CAPITAL: $HOME, $SHELL, $PATH, $PS1. To list all defined variables ``printenv``. All variables can be used or even redefined. No error if you call an undefined var, it is just considered to be empty.

Assign a variable ``var1=100``, ``var2='some string'``

Invoke a variable ``$var1``

BASH is smart enough to distiguish a var inline ``dir=$HOME/dir1; fname=file; fext=xyz; echo "$dir/$fname.$fext"``, though if var followed by a number or a letter ``echo ${dir}2/${file}abc.$fext``

Built-in vars: $?, $$, $#, $1 ..., "$*", "$@",  

**Hint** Quoting matters: '' vs ""

:Exercise: write a function that outputs number of arguments it has got and then all the arguments as a single word
:Exercise*: make a function that takes IP as an argument, ping that IP and returns ok/failed only

More on variables
----
BASH provides wide abilities to work with the vars "on-the-fly" with ${var...} like constructions.

Subtitute a var with default *value* if empty: ``${var:=value}``

Print an *error_message* if var empty: ``${var:?error_message}``

Extract a substring: ``${var:offset:length}``, example ``var=abcde; echo ${var:1:3}`` returns 'bcd'

Variable length: ``${#var}

Replace beginning part: ``${var#prefix}``

Replace trailing part: ``${var%suffix}``

Replace *pattern* with the *string*: ``${var/pattern/string}``


:Exercise: 
 - shorten *filename.ext* down to *filename* and then down to *ext*. Filename can be of any length, while *.ext* is the same.
 - expand lcd() so that it would go to some specific directory if $1 is empty (if on Triton then $WRKDIR)
:Exercise*: extract filename with no extension from */work/archive/OLD/Michel's_stuff.tar.gz*

[[ ]] and if/elif/else
----
``[[ expression ]]`` returns 0 or 1 depending on the evaluation of the conditional *expression*

==, <, >, !=, =~, &&, ||, !, ()

When working with the strings the right-hand side is a pattern (a regular expression). Matched strings assigned to *${BASH_REMATCH[]}* array elements.

Integer example: ``x=5; y=6; z=7; [[ $x < $y && ! $y == $z ]] && echo ok || echo nope``
String example: ``x='abcefgh kjhkjh #1278?'; regexpr='#([0-9][0-9][0-9][0-9])'; [[ "$x" =~ $regexpr ]] && echo ${BASH_REMATCH[1]} || echo nope``

**Hint** For case insesitive, set ``shopt -s nocasematch``  (to disable it back ``shopt -u nocasematch``)

Though scripting style is more logical if/else

::

 if [[ expression ]]; then
   command1
 elif [[ expression ]]; then
   command2
 else
   command3
 fi

An example: script (or function) that accepts two strings and return result

::

 if [[ "$1" == "$2" ]]
 then
   echo The strings are the same
 else
   echo The strings are different
 fi

:Exercise: Play with the strings/patterns. Make a script/function that picks up a pattern and a string as an input and reports whether pattern matches any part of string or not. Kind of *my_grep pattern string*.
:Exercise*: Expand the script to make search case insesitive and report also a count how many times pattern appears in the string

Loops
----


More about redirection and pipe
----------
STDOUT and STDERR: reserved file descriptors *1* and *2*, always there when you run a command

`` ... >/dev/null`` redirects STDOUT only, to redirect all the output including errors `` ... &>/dev/null``, or redirect outputs in different ways ``1>file.out`` and ``2>file.err``

In order to pipe both STDERR and STDOUT ``|&``.

If ``!``  preceds the command, the exit status is the logical negation.

The third file descriptor is 0, STDIN, valid syntax ``command < input_file &> output_file``. ping exercise explained.


Substitute a command output
----
$(...)

PATH
----
``chmod +x``, what is next? binaries at /bin, /usr/bin, /usr/local/bin etc. Setting up ~/bin or running as ./binary.

Add to *.bashrc* ``export PATH="$PATH:$HOME/bin"``

**Hint** name your scripts  *\*.sh* and collect them in ~/bin directory

Ping World
----
Use an editor of your choice

::

$ cd ~/bin
$ nano chknet.sh

::

 #!/bin/bash
 ping -c 1 8.8.8.8 > /dev/null && echo online || echo offline

To run ``chmod +x chknet.sh; ./chknet.sh``. Setting an x-bit needs to be done only once. If ~/bin is in the $PATH, one can scip ./ prefix.

**Hint** comments in the scripts #

Input arguments
----
$1, $2, $3, ...

::
 
 host=$1
 ${host:-8.8.8.8}
 ping -c 1 $host > /dev/null && echo online || echo offline
 


Functions in general on example of one real one
----
Alias can not accept an argument, function can. Once declared functions can be used within a script and from command line (cli). Any script may use a function but for mudularity let us collect some generic onse into one file.

::

$ nano ~/bin/functions.sh

It doesn't need #!/bin/bash in the header, it can be even just readable, not executable

::

 onlinechk() {
   ping $1 > /dev/null && 
 }


3. session
====
SSH tricks
----


4. session
====

References
====
.. [#] http://tldp.org/LDP/abs/html/index.html
.. [#] https://www.putty.org/
.. [#] https://alvinalexander.com/unix/edu/examples/find.shtml
.. [#] https://www.computerhope.com/unix/uumask.htm
