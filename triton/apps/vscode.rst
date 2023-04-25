VSCode on Triton
================

VSCode is available through :doc:`../usage/ood`.  If you want to
connect through your own computer, read below.

"Remote SSH" is a nice way to work on a remote computer, but on
Triton, that will run everything on the login node.  For light use
this is OK, but for heavy calculations it should be avoided, since it will affect other
login node usage.


VSCode remote SSH host directly to interactive job
--------------------------------------------------

Sometimes you want more resources than the login node.  This section
presents a way to have VSCode directly connect to a job resource
allocation on Triton - so you can do larger calculations / use more
memory / etc. without interfering with others.  **Note that for real
production calculations,** you should use :doc:`../tut/serial`, and
*not* run stuff through your editor, **since everything gets lost when
your connection dies.**

This section contains original research and may not fully work, and
**may only work on Linux/Mac right now**.

In you ``~/.ssh/config``, add this block to define a server
``triton-vscode``.  For more information ``.ssh/config``, including
what these mean and what else you might need in here, see
:doc:`/scicomp/ssh`::

  Host triton-vscode
      ProxyCommand ssh triton /share/apps/ssh-node-proxycommand --partition=interactive --time=1:00:00
      StrictHostKeyChecking no
      UserKnownHostsFile /dev/null
      User USERNAME

  # You also need a triton alias here:

  Host triton
      HostName triton.aalto.fi
      # ... any other thing you need for connecting to triton.
      User USERNAME


Now, with VSCode's Remote SSH, you can select the ``triton-vscode``
remote.  It will ssh to Triton, request a job, and then directly
connect to the job.  **Configure the job requirements in the
ProxyCommand line** (see :ref:`ref-job-submission` - you can have
multiple ``Host`` sections for different types of requirements).


Possible issues which may affect usage:

* If the ssh connection dies, the background job will be terminated.
  You will lose your state and not be able to save.q

* If the job dies due to time or memory exceeded, the same as above
  will happen: your job will die and there is no time to save.

* If you request a GPU node or other high resources, this is reserved
  the whole time even if you aren't using them.  Consider this before
  reserving large resources (unless you close the jobs soon), or you
  might get an email from us asking about resource usage.


