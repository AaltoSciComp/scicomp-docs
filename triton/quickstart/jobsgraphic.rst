===============================================
Applications with graphical interface on Triton
===============================================

One has two options: the recommended one is use ondemand.triton.alto.fi, though
alternatively, one can run a job.

OOD
---

Using Open OnDemand (OOD) is essential and easy, login to https://ondemand.triton.aalto.fi.
There on you will have several options, if the application you want to run is part
of the Interactve Apps menu, then proceed from there. For instance Matlab, Paraview,
R studio are there. In other case, launch a Triton
Desktop and you recieve a normal Linux GUI environment of your choice (GNOME or alike).

It will be like you run a Linux Desktop on one of the Triton's compute node with native
access to ``/scratch`` and ``module ...``. Start a terminal within the session and proceed.

OOD is the recommended way.

Running a job
-------------

Not recommended, but still an option.

.. admonition:: Prerequisites

    Before submitting a job:
    Optimally, through tests, have a rough idea, how long your job takes, how much memory it needs and how much CPU(s)/GPU(s) it needs.

    Required Reading:

    - :doc:`Submitting jobs on triton <jobs>`

    Required Setup:

    - Setting up your system to connect to Triton according to the :doc:`connection guide <connecting>`
    - Your script and any data need to be on triton (follow e.g. the :doc:`data transfer quick-start guide <data>`)
    - Specific to Windows: Install an XServer

First off, in general, using graphical user interfaces to programming languages (e.g. graphical Matlab, or RStudio)
is not recommended, since there is no real advantage to submitting a job to the cluster.

However, there are instances where you might need large amount of resources e.g. to visualize data which is indeed intended use.
There are two things you need to do to run a graphical program on the cluster:

- Start X-forwarding (when login to Triton, use ``ssh -XY ...``)
- request an interactive job on the cluster (``sinteractive``)

Once you are on a node, you can load and run your program.
