Maintenance downtime
====================

.. note::

   This was written in 2026 May in response to the increasing
   frequency of urgent security updates.  We hope that there is less
   downtime in the future.

We turn off Triton access when it needs urgent security updates for
things which can affect data integrity - in short, anything that can
allow a Triton user to access data/accounts they aren't allowed to,
corrupt other data, or corrupt the system.  Like it or not, it seems
there are many more of these being found these days (thanks to AI
tools), and they are happening faster and with less advance warning to
be fixed before public release.


Policy for downtime for updates
-------------------------------

* Anytime one of these vulnerabilities is known but not fixed in
  Triton, or we know of one that is probably affecting Triton, we will
  close Triton access immediately (or whatever component is affected).
* This is because data security is more important than
  high-availability.  Without data security, most Triton work can't
  take place.
* We will work on fixing the vulnerability as soon as possible, but we
  aren't on call 24/7 and there isn't a Triton availability guarantee.
  In the worst case, plan on waiting for the next working day, or a
  few days for public fixes to be released if we have to wait for
  someone else to fix and release.

We know that losing access to compute, especially right before
deadlines, can be quite bad.  We will do what we can, to minimize
this, and if it's any compensation, realize that the same thing is
happening to other big computers.  Some of these can be fixed
completely transparently, without reboot or users noticing (if we can
figure out how to do this faster than we can turn off access).  Some
require downtime and rebooting.

Basically, what this means is that you should plan your workflows to
be more resilient to HPC outages.  Plan for possible short downtimes
(few minutes or hours) while we immediately mitigate something.  Plan
for the possibility of several days of downtime in the extreme worst
case that a vulnerability needs an upstream fix that we have to wait
for.


Effects of downtime
-------------------

What will downtimes look like?  Everything is different but some
patterns are:

* Login nodes (all SSH) and Open OnDemand are turned off.  We can't
  allow users to run arbitrary code anymore.
* We expect that a lot of the time jobs can continue to run, so the
  compute time isn't wasted.  Sometimes we may need to cancel running
  jobs and/or reboot all nodes (even before logins are allowed again,
  meaning some wasted compute time.)
* We hope that in most cases, Scratch access will be possible via
  :ref:`SMB mounting <triton-remotedata-servers>` and :ref:`mounts on
  other servers <triton-remotedata-mounting>` (assuming those other
  servers haven't been turned off for the same reasons...).  This allows
  you to see your data and not be totally blocked. (in cases of high
  risk it's theoretically possible we need to block scratch access,
  too.)

Recommendations
---------------

Our recommendation is to build resilience (this is probably good for
modern cybersecurity anyway): Don't assume that things are reliable as
before.  Make sure you keep your code in version control and pushed
off the cluster, so you can do something during the downtime.  Try not
to run to the last minute of deadlines.  Practice accessing data via
SMB mounting so that you can access it more flexibly.  Think about
backups of your own personal data.

Communication about these things will happen via:

* In all but the shortest cases, chat on #triton on
  scicomp.zulip.cs.aalto.fi and the Triton issue tracker.
* Longer downtimes will get an email + link to an issue tracker for
  updates between emails.
* If you want to talk to us, The #triton channel is a public forum
  (recommend for most things) or scicomp at aalto.fi to report any
  unmitigated vulnerabilities you learn about.

Despite all this, we think that Triton is still a good long-term place
for work, especially since it will get continual security updates.
