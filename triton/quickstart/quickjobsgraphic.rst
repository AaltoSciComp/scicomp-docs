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
    - Specific to Windows: Install an X-Server

First off, in general, using graphical user interfaces to programming languages (e.g. graphical Matlab, or RStudio)
is not recommended, since there is no real advantage to submitting a job to the cluster. 

However, there are instances where you might need large amount of ressources e.g. to visualize data which is indeed intended use.
There are two things you need to do to run a graphical program on the cluster:

- Start X-forwarding (``ssh -X host`` or ``ssh -Y host``)
- request an interactive job on the cluster (``sinteractive``)

Once you are on a node, you can load and run your program.


