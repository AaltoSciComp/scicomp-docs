==================================
Creating a graphical job on triton
==================================

.. admonition:: Prerequisites

    Before submitting a job:  
    Optimally, through tests, have a rough idea, how long your job takes, how much memory it needs and how much CPU(s)/GPU(s) it needs.
    Required Reading:
    - :doc:`Submitting jobs on triton<quickjobs>`

    Required Setup:
    
    - :doc:`Setting up your System to connect to triton according to the :doc:`connection guide<quickconnecting>`
    - Your script and any data need to be on triton (follow e.g. the :doc:`data transfer quick-start guide<quickdata>`)
    - Specific to Windows: Install Xming, according to these instructions TODO
    
    Required on Windows:
    - Install an X-server 

First off, in general, using graphical user interfaces to programming languages (e.g. graphical Matlab, or RStudio)
is not recommended, since there is no real advantage to submitting a job to the cluster. 

However, there are instances where you might need large amount of ressources e.g. to visualize data which is indeed intended use.
There are two things you need to do to run a graphical program on the cluster:


- Start X-forwarding (on Windows you will need an X-Window manager)


There are multiple different types of jobs available on triton. Here we focus on the most commonly used ones.

- Interactive jobs (commonly to test things or run graphical platforms with cluster ressources)
- Batch jobs (normal jobs submitted to the cluster without direct user input)

to run an interactive job simply run 

::

    sinteractive
    # you will then be transferred to a node, where you can run your scripts

to run graphical applications, 

Parallelization
~~~~~~~~~~~~~~~

Job Parameters

Interactive Jobs
Batch Jobs
Array Jobs

Most important parameters (table: Parameter Effect, Script command, command line parameter)


