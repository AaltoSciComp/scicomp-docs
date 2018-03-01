Course preview
====
Linux Shell tutorial by Science IT at Aalto University.
BASH practicalities, shell scripting. Learning by doing.

Corresponds to 4 sessions 3h each, session rough schedule 1h25m + 10m break + 1h25m.

Starred exersices (*) for the advanced user, to keep them busy.

Based on 
 - ``man bash``
 - Advanced BASH scripting guide [#]_
 - common sence and 20+ years experience, see also other references

1. session
====
Practical aspects of BASH, command line usage.

Linux and Mac users: just open a terminal window.

Windows users: install PuTTY [#]_ then SSH to any interactive server at Aalto or your department.

Shell -- is what you get when your teminal window is open. It is a command-line (CLI), an interface that intepreters and executes the commands.

Built-in and external commands
----
cd, pwd, echo, ls vs. date, man, less, lpr etc. 

**Hint** ``type -a`` to find what is behind the name

Who am I: ``id``, ``echo $HOME``, ``echo $SHELL`` 
(Your default shell is not a /bin/bash? Login to kosh/taltta and run ``chsh -s /bin/bash``)

Where am I: ``pwd``

Your best friend ever -- ``man`` -- collection of manuals.


**Hint** ``man -t ls | lpr`` to print it to a default printer

Files and dirs
----
ls, ls -l, ls -la, ./, ../, *, ?, []

cd, mkdir, cp, rm, rm -r, mv, touch

**Hint** ``ls -lX``, ``ls -ltr``, ``file <filename>``

:Exercise: mkdir in your $HOME, cd there and 'touch' a file. Rename it. Make a copy and then remove the original.
:Exercise*: ``ls`` dot files only. Create a dozen of files with one command with names like file1.txt, file2.txt, ... file12.txt

Permissions
----
rwxrwxrwx -- read, write, execute/search
Could be a link -- ln -s. s- and t-bits.

chmod: u+rwx,g-rwx,o-rwx -or- 700

chmod -R ...

[note: ``setfacl`` to be covered later on]

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
- Ctrl-i -- clear the screen
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

:Exersise: customize a prompt ``$PS1``

After editing: ``source .bashrc``. source vs execution.

Redirect, pipe
----
Append to a file or replace a file ``command > file.txt`` *or* ``command >> file.txt``

``echo Hello World > hello.txt`` *or* ``ls -lH >> current_dir_ls.txt``

Output of the first command as an input for the second one ``command_a | command_b``

sort, grep, tr, cut, /dev/null

``du -hs * | sort -h``

``w -h | wc -l``

:Exersice: 
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

Examples: ``alias chknet='ping -c 1 8.8.8.8 > /dev/null && echo online || echo offline'``

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



2. session
====
BASH Scripting

PATH
----
``chmod +x``, what is next? binaries at /bin, /usr/bin, /usr/local/bin etc. Setting up ~/bin or running as ./binary.

Hello World
----




3. session
====

4. session
====

References
====
.. [#] http://tldp.org/LDP/abs/html/index.html
.. [#] https://www.putty.org/
.. [#] https://alvinalexander.com/unix/edu/examples/find.shtml
