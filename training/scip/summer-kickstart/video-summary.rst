Summary of videos
=================

Why do we have these video summaries?
-------------------------------------

- There are some important topics that you need to know.
- But we can't teach them every time (and don't need to).
- Modern tech to the rescue!  We teach them occasionally and you can
  watch at your own pace.
- Still, we want to summarize them now.




Scientific computing workflows
------------------------------

.. admonition:: Link

   https://www.youtube.com/watch?v=ExFbc5EikU0

Why workflows?

There are many ways to do your work, from

- Your own laptop
- Remote desktop system
- Remote server
- Cluster computing

All of these have their own role.

- Days 2-3 of this course are about the cluster computing.
- But many people don't need to go so far
- Or start off and it becomes difficult to go further.



Plan for the future
~~~~~~~~~~~~~~~~~~~

- It is good to start simple when developing.

- Eventually you need:

  - More computing power for a single task
  - To do it automatically, over and over again.

- Then, you need to be able to move up this "computing ladder"

- It pays to learn how to design your code/analysis workflow to grow:

  - Design for reusable with different parameters and data
  - Command line interfaces
  - Split the calculation from the analysis
  - ...



Where to go next?
~~~~~~~~~~~~~~~~~

- Each university hopefully has some guide to the different services
- Don't get locked into the lower levels
- Slowly move up as you need
- Ask for help when needed.



Basic Linux shell and scripting
-------------------------------

.. admonition:: Link

   https://www.youtube.com/watch?v=ESXLbtaxpdI

- Like we said above, sometimes you need to do things over and over
  again.
- Clicking buttons is *not* scaleable.
- The command line is the standard way of automating programs.
- It is also the standard way of interacting with servers or clusters.


What's the command line?
~~~~~~~~~~~~~~~~~~~~~~~~

- Current interface developed as part of UNIX in 1960-70s, now used by
  almost everything.
- Interface includes program name and arguments

.. highlight:: bash

For example, you can run to copy a file::

  cp source.txt destination.txt

Or you can run a program with arguments::

  ./your_code --argument1 input1 input2 -o output2

These can equally be done interactively (in the **shell**) or via a
**shell script**.


Typical uses
~~~~~~~~~~~~

- Making a reusable program
- Separating parameters from code
- Connecting different programs together
- Automating things for yourself
- Automating things for the cluster


Where to go next?
~~~~~~~~~~~~~~~~~

- You really need to know some basics
- Watching these crash course videos and attending this course is
  *plenty* for now.
- Don't be scared, ask for help about what you need to do
- You don't need to go very deep at the start
