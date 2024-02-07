VSCode on Triton
================

VSCode is a text editor and IDE (Integrated Development Environment).  It is
very popular these days, partly due to it's good usability.

Installation
------------

If you are using on Triton, it's available as a web app through
:doc:`Open OnDemand <../usage/ood>`, see below.

It can also be installed on your own computer, which might be good to
do anyway.  If you do this, make sure you turn off telemetry if you
don't want Microsoft to get reports of your activity.  Search
"telemetry" in settings to check and disable (note that `this doesn't
fully turn it off
<https://www.roboleary.net/tools/2022/04/20/vscode-telemetry.html>`__).

`VSCodium <https://vscodium.com/>`__ is an open-source build of VScode
(like "chromium" is an open-source build of Google Chrome) that
disables all telemetry by default and removes non-open source bits.
It is essentially the same thing, but due to Microsoft licenses it
can't use the same extension registry as VSCode.  It does have a
`stand-alone extension registry
<https://github.com/VSCodium/vscodium/blob/master/DOCS.md#extensions-marketplace>`__,
though.



Security and extensions
-----------------------

As always when using user-contributed extensions, be cautious of what
extensions you install.  A malicious extension can access and/or
delete all of the data available via your account.



VSCode through Open OnDemand
----------------------------

.. seealso:: :doc:`../usage/ood`

VSCode is available through :doc:`../usage/ood`, and with this you can
select whatever resources you want (memory, CPU, etc) and run directly
in the Slurm queue.  This means you can directly perform calculations
in that VSCode session and it runs properly (not on the login node).

This is useful for getting things done quickly or do simple debugging,
but running in a web browser can be limited in some cases (interface, lifetime, etc.).
Another limitation is OOD VSCode does not support GPU computing.



VSCode remote SSH
-----------------

**"Remote SSH"** is a nice way to work on a remote computer and
provides both editing and shell access, but everything will run
directly on the login node on Triton.  This is OK for wiring code 
and editing, but not for main computations (see the section above or below).
**To repeat: don't use this for running any big computations.**

.. figure:: vscode--connected.png
   :alt: Screenshot saying "SSH: triton".

   If you see this in the lower left corner (or whatever the name of
   your cluster SSH config is), you are connected to the login node
   (and again, should not do big calculations).  It's possible the
   exact look may be different for others.

You can see `connection instructions (including screenshots) at the
Sigma2 instructions
<https://documentation.sigma2.no/code_development/guides/vs_code/connect_to_server.html>`__.

VSCode can use a regular OpenSSH configuration file, so you may as
well set that up once and it can be used for everything - see
:doc:`/scicomp/ssh` for the full story.  The basics of SSH to Triton
are in :ref:`triton-connecting-ssh`.  A SSH key can allow you to
connect without entering a password every time.



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
**may only work on Linux/Mac right now (but Windows might work too
since it uses OpenSSH)**.

In your ``~/.ssh/config``, add this block to define a server
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

* If you ``srun`` from within the job, then it gets messed up because
  the environment variable ``SLURM_JOB_ID`` is set from the
  interactive job that got started.  It's hard for us to unset this,
  so if you are using the terminal to ``srun`` or ``sbatch``, you
  should ``unset SLURM_JOB_ID`` first.  (Note there are many other
  variables set by Slurm.  Make sure that they don't interfere with
  jobs you may run from this vscode session).

Sometimes you want to debug your code using GPU(s). To connect to a
GPU node, you can follow the above guide, and request a `gpudev` partition.
Note that `gpudev` partition has a strict time limitation: Every session
is maximum 30 minutes long. For more information, see :doc:`partitions 
<../ref/partitions.rst>`.

  Host triton-gpu-debug
      ProxyCommand ssh triton /share/apps/ssh-node-proxycommand --partition=gpudev --time=0:30:00
      StrictHostKeyChecking no
      UserKnownHostsFile /dev/null
      User USERNAME

  # You also need a triton alias here:

  Host triton
      HostName triton.aalto.fi
      # ... any other thing you need for connecting to triton.
      User USERNAME



VSCode debugging
--------------------------------------------------

Following this guide, you can attach a debugger to a running job.

