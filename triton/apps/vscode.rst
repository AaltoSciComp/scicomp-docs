VSCode on Triton
================

VSCode is available through :doc:`../usage/ood`, and with this you can
select whatever resources you want and run directly in the Slurm queue
(and perform your actual calculations).  If you want to
connect through your own computer, it can provide a nice interface but
read below.

As always when using user-contributed extensions, be cautious of what
extensions you install.  A malicious extension can access and/or
delete all of the data available via your account.



VSCode through OOD
------------------

.. seealso:: :doc:`../usage/ood`

This is useful for getting things done quickly, but running in a web
browser can be limited in some cases.



VSCode remote SSH
-----------------

**"Remote SSH"** is a nice way to work on a remote computer and
provides both editing and shell access, but everything will run
directly on the login node on Triton.  This is OK for editing, but not
for main computations (see the section above or below).  **To repeat:
don't use this for running big computations.**

.. figure:: vscode--connected.png
   :alt: Screenshot saying "SSH: triton".

   If you see this in the lower left corner (or whatever the name of
   your cluster SSH config is), you are connected to the login node
   (and should not do big calculations).  It's possible it may be
   different for others.

You can see `connection instructions (including screenshots) at the
Sigma2 instructions
<https://documentation.sigma2.no/code_development/guides/vs_code/connect_to_server.html>`__.

VSCode can use a regular OpenSSH configuration file, so you may as
well set that up once and it can be used for everything.  The basics
of SSH is in :ref:`triton-connecting-ssh` and the real SSH config file
info you really need is in :doc:`/scicomp/ssh`.  A SSH key can allow
you to connect without entering a password every time.



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
  You will lose your state and not be able to save.

* If the job dies due to time or memory exceeded, the same as above
  will happen: your job will die and there is no time to save.

* If you request a GPU node or other high resources, this is reserved
  the whole time even if you aren't using them.  Consider this before
  reserving large resources (unless you close the jobs soon), or you
  might get an email from us asking about resource usage.
