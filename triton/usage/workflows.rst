=========================
Remote workflows at Aalto
=========================

.. note::

   The more specific remote access instructions for scicomp is at
   :doc:`/aalto/remoteaccess` (recent email had duplicate links to
   this page).  This page explains the options, including other
   systems.


.. note::

   How can you work from home?  For that matter, how can you work on more than your desktop/laptop while at work?  There are many options which trade off between graphical interfaces and more power.  Read more for details.

You have most likely created your own workflow to analyse data at Aalto and most likely you are using a dedicated desktop workstation in Otaniemi. However, with increased mobility of working conditions and recent global events that recommend tele-working, you might be asking yourself: "how do I stop using my workstation at the dept, and get analysis/figures/papers done from home?".

The data analysis workflows from remote might not be familiar to everyone. We list here few possible cases, this page will expand according to the needs and requests of the users.

What's your style?
------------------

If you need the most power or flexibility, use Triton for your data storage and computation.  To get started, you can use Jupyter (4) and VDI (3) which are good for developing and prototyping.  Then to scale up, you can use the Triton options: 6, 7, 8 which have access to the same data.   (`Triton account required <https://scicomp.aalto.fi/triton/accounts.html>`__ for 4-8).

If you need simple applications with a graphical interface, try 3 (VDI).

If you use your own laptop/desktop (1, 2), then it's good for getting started but you have to copy your data and code back and forth once you need to scale up.

Summary table for remote data analysis workflows
------------------------------------------------

   * Good for data security: 3, 4, 5, 6, 7
   * Good for prototyping, working on the go, doing tests, interactive work: 1, 2, 3, 4, 5
   * Shares Triton data (e.g. scratch folders): 3, 4, 5, 6, 7
   * Easy to scale up, shares software, data, etc: 4, 5, 6, 7
   * Largest resources available 7 (medium: 6)


.. list-table::
   :header-rows: 1

   * * Workflow
     * Pros
     * Cons
     * Recommendation
     * Triton data Y/N
   * * 1. Own laptop/desktop computer
     * Can work from anywhere. Does not require internet connection.  You are in control.
     * Not good for personal or confidential data. Computing resources might not be enough. Accessing large data remotely stored at Aalto might be problematic - you will end up having to copy a lot.  You have to manage software yourself.
     * Excellent for prototyping, working on the go, doing tests, interactive work (e.g. making figures). Don’t use it with large data or confidential / personal data.
     * N
   * * 2. Aalto laptop
     * Same as above, plus same tools available as Aalto employer.
     * Same as above.
     * Same as above.
     * N
   * * 3. Remote virtual machine (https://vdi.aalto.fi)
     * Computing happens on remote. Data access happens on remote, so it is more secure.
     * Computing resources are limited.
     * Excellent for prototyping, working on the go, doing tests, interactive work (e.g. making figures). More secure access to data.
     * Y
   * * 4. Aalto Jupyterhub (https://jupyter.triton.aalto.fi)
     * Cloud based - resume work from anywhere.  Includes command line (#6) and batch (#7) easily.  Same data as seen on Triton (/scratch/dept/ and /work/ folders)
     * Jupyter can `become a mess if you aren't careful <https://scicomp.aalto.fi/scicomp/jupyter-pitfalls.html>`__.  You need to plan to scale up with #7 eventually, once your needs increase.
     * Excellent for prototyping, working on the go, doing tests, interactive work (e.g. making figures).  Secure access to data. Use if you know you need to switch to batch jobs eventually (7).
     * Y
   * * 5. Interactive graphical session on Triton HPC (ssh -X)
     * Graphical programs.
     * Lost once your internet connection dies, needs fast internet connection.
     * If you need specific graphical applications   which are only on Triton.
     * Y
   * * 6. Interactive command line session on Triton HPC (ssh + sinteractive)
     * Works from anywhere.  Can get lots of resources for a short time.
     * Limited time limits, must be used manually.
     * A general workhorse once you get comfortable with shell - many people work here + #7.
     * Y
   * * 7. Non-interactive batch HPC computing on Triton (ssh + sbatch)
     * Largest resources, bulk computing
     * Need to script your computation
     * When you have the largest computational needs.
     * Y
   * * 8. Non-interactive batch HPC computing on CSC (ssh + sbatch)
     * Similar to #7 but at CSC
     * Similar to #7
     * Similar to #7
     * N


1. Own laptop/desktop computer
------------------------------

**Description**: Here you are the administrator. You might be working from a cafe with your own laptop, or from home with a desktop. You should be able to install any tool you need. As an Aalto employer you get access to many nice commercial tools for your private computers. Visit: https://download.aalto.fi/index-en.html  and https://aalto.onthehub.com/  for some options. 

**Pros**: Computing freedom! You can work anywhere, you can work when there is no internet connection, you do not share the computing resources with other users so you can fully use the power of your computer.

**Cons**: If you work with personal or confidential data, the chances of a data breach increase significantly, especially if you work from public spaces. Even if you encrypt your hard disks (links:https://www.aalto.fi/en/cyber-security-hub-under-construction/aalto-it-securitys-top-10-tips-for-daily-activities )  and even if you are careful, you might be forgetting to lock your computer or somebody behind you might see which password you type. Furthermore, personal computers have limited resources when it comes to RAM/CPUs/GPUs. When you need to scale up your analysis, you want to move it to an HPC cluster, rather than leaving scripts running for days. Finally, although you can connect your Aalto folders to your laptop (link https://scicomp.aalto.fi/aalto/remoteaccess.html and https://scicomp.aalto.fi/triton/tut/storage.html#accessing-and-transferring-files-remotely), when the data size is too big, it is very inefficient to analyse large datasets over the internet.

**Recommendation**: Own computer is excellent for prototyping data analysis scripts, working on the go, doing tests or new developments. You shouldn’t use this option if you are working with personal data or with other confidential data. You shouldn’t use this option if your computational needs are much bigger.

2. Aalto laptop
---------------

**Description**: As an Aalto employer, you are usually provided with a desktop workstation or with an Aalto laptop. With an Aalto laptop you can apply for administrator rights (`link to the form <https://workflow.aalto.fi/WorkstationAdminRights/Form.aspx?s=22WxVuFVOUS_TfZlBXI-jA>`__)  and basically everything you have read for option 1 above is valid also in this case.  See "Aalto {Linux|Mac|Windows}" on scicomp's Aalto section at https://scicomp.aalto.fi/aalto/.

**Pros/Cons/Recommendation**: see option 1 above.  But, when on Aalto networks, you have easier access to Aalto data storage systems.

3. Remote virtual machine with VDI
----------------------------------

**Description**: You might be working with very large datasets or with confidential/personal data, so that you cannot or do not want to copy the data to your local computer. Sometimes you use many computers, but would like to connect to “the same computer” from remote where a longer analysis script might be crunching numbers. Aalto has a solution called VDI https://vdi.aalto.fi (`description at aalto.fi <https://www.aalto.fi/en/services/vdiaaltofi-how-to-use-aalto-virtual-desktop-infrastructure>`__) where you can get access to a dedicated virtual machine from remote within the web browser. Once logged in, you can pick if you prefer Aalto Linux or Aalto Windows, and then you see the same interface that you would see if you logged in from an Aalto dedicated workstation.  To access Triton data from the Linux one, use the path /m/{dept}/scratch/ (just like Aalto desktops).

**Pros**: The computing processes are not going to run on your local computer, computing happens on remote which means that you can close your internet connection, have a break, and resume the work where you left it. There is no need to copy the data locally as all data stays on remote and is accessed as if it was a desktop computer from the campus.

**Cons**: VDI machines have a limited computing power (2 CPUs, 8GB of RAM). So they are great for small prototyping, but for a large scale computation you might want to consider Aalto Triton HPC cluster. The VDI session is not kept alive forever. If you close the connection you can still resume the same session within 24h, after that you are automatically logged out to free resources for others. If you have a script that needs more than 24h, you might want to consider Aalto Triton HPC.

**Recommendation**: VDI is excellent when you need a graphic interactive session and access to large data or to personal/confidential data without the risks of data breach. Use VDI for small analysis or interactive development, we do not recommend it when the executing time of your scripts starts to be bigger than a 7 hours working day.

4. Aalto Jupyterhub
-------------------

**Description**: Jupyter notebooks are a way of interactive, web-based computing: instead of either scripts or interactive shells, the notebooks allow you to see a whole script + output and experiment interactively and visually. They are good for developing and testing things, but once things work and you need to scale up, it is best to put your code into proper programs. Triton’s JupyterHub is available at https://jupyter.triton.aalto.fi . Read more about it at: https://scicomp.aalto.fi/triton/apps/jupyter.html. `Triton account required <https://scicomp.aalto.fi/triton/accounts.html>`__.

**Pros**: JupyterHub it has similar advantages than #4, although data and code are accessed through the JupyterHub interface.  In addition, things can stay running in the cloud.  Although it can be used with R or Matlab, Python users will most likely find this to be a very familiar and comfortable prototyping environment. Similar to the VDI case, you can resume workflow (there are sessions of different lengths).  You also also access Triton shell and batch (#6, #7) in the Jupyter interface, and it's easy to scale up and use them all together.

**Cons**: You are limited to the Jupyter interface (but you can upload/download data, and integrate with many other things). Jupyter can `become a mess if you aren't careful <https://scicomp.aalto.fi/scicomp/jupyter-pitfalls.html>`__. Computationally, an instance will always have limited CPUs and memory.  Once you need more CPU/RAM, look into options #6 and #7 - they work seamlessly with the same data, software, etc.

**Recommendation**: Good for exploration and prototyping, access to large dataset, access to confidential/personal data. For more computational needs, be ready to switch to batch jobs (#7) once you are done prototyping.


5. Interactive graphical session on Triton HPC
----------------------------------------------

**Description**: Sometimes what you can achieve with your own laptop or with VDI is not enough when it comes to computing resources. However, your workflow does not yet allow you to go fully automatic as you still need to manually interact with the analysis process (e.g. point-click analysis interfaces, doing development work, making figures, etc). An option is to connect to triton.aalto.fi with a graphical interface. This is usually done with ssh -X triton.aalto.fi. For example you can do it from a terminal within a VDI Linux session. Once connected to the triton log-in node, you can then request a dedicated interactive node with command ``sinteractive``, and you can also specify the amount of CPU or RAM you need (link to sinteractive help page). `Triton account required <https://scicomp.aalto.fi/triton/accounts.html>`__.

**Pros**: This is similar to the VDI case above (#3) without the computing limitation imposed by VDI. 

**Cons**: If you connect from triton.aalto.fi from your own desktop/laptop, your internet connection might be limiting the speed of the graphical session making it very difficult to use graphical IDEs or other tools. Move to VDI, which optimises how the images are transferred over the internet. Sinteractive sessions cannot last for more than 24 hours, if you need to run scripts that have high computational requirements AND long time of execution, the solution for you is to go fully non-interactive using Triton HPC with slurm (case #6)

**Recommendation**: This might be one of the best scenarios for working from remote with an interactive graphical session. Although you cannot keep the session open for more than 24 hours, you can still work on your scripts/code/figures interactively without any limitation and without any risks of data breaches.


6. Interactive command line only session on Triton HPC/dept workstation
-----------------------------------------------------------------------

**Description**: sometimes you do not really need a graphical interface because you are running interactively scripts that do not produce or need a graphical output. This is the same case as sinteractive above, but without the limitation of the 24h session. The best workflow is to: 1) connect to triton ``ssh triton.aalto.fi`` 2) start a screen/tmux session that can be detached / reattached in case you lose the internet connection or in case you need to leave the interactive script running for days 3) request a dedicated interactive terminal with command ``srun -p interactive --time=HH:MM:SS --mem=nnG --pty bash`` (see other examples at https://scicomp.aalto.fi/triton/tut/interactive.html or https://scicomp.aalto.fi/triton/usage/gpu.html for interactive GPU) 4) get all your numbers crunched and remember to close it once you are done. Please note that, if you have a dedicated Linux workstation at a department at Aalto, you can also connect to your workstation and use it as a remote computing node fully dedicated to you. The resources are limited to your workstation, but here you won’t have the time constraint or the need to queue for resources if Triton’s queue is overcrowded. `Triton account required <https://scicomp.aalto.fi/triton/accounts.html>`__.

**Pros**: when you do not need a graphical interface and when you need to run something interactively for days, this is the best option: high computing resources, secure access to data, persistent interactive session. 

**Cons**: when you request an interactive command line session you are basically submitting a slurm job. As with all jobs, you might need to wait in the queue according to the amount of resources you have requested. Furthermore, jobs cannot last more than 5 days. In general, if you have an analysis script that needs more than 5 days to operate, you might want to identify if it can be parallelized or split into sub-parts with checkpoints.

**Recommendation**: this is the best option when you need long-lasting computing power and large data/confidential data access with interactive input from the user. This is useful once you have your analysis pipeline/code fully developed so that you can just run the scripts in command line mode. Post processing/figure making can then happen interactively once your analysis is over.

7. Non-interactive batch computing on Triton HPC
------------------------------------------------

**Description**: this is the case when no interactive input is needed to process your data. This is extremely useful when you are going to perform the same analysis code for hundreds of time. Please check more detailed descriptions at https://scicomp.aalto.fi/triton/index.html and if you havent, go through the tutorials https://scicomp.aalto.fi/triton/index.html#tutorials. `Triton account required <https://scicomp.aalto.fi/triton/accounts.html>`__.

**Pros**: when it comes to large scale data analysis, this is the most efficient way to do it. Having a fully non-interactive workflow also makes your analysis reproducible as it does not require any human input which can sometimes be the source of errors or other irreproducible/undocumented steps.

**Cons**: as this is a non-interactive workflow, this is not recommended for generating figures or with graphical tools that does not allow “batch” mode operations.

**Recommendation**: this is the best option when you need long-lasting parallel computing power and large data/confidential data access. This is also recommended from reproducibility/replicability perspective since, by fully removing human input, the workflow can be made fully replicable. 

8. Non-interactive batch HPC computing at CSC
---------------------------------------------

**Description**: this case is similar to #7. You can read/learn more about this option at https://research.csc.fi/guides

**Pro/Cons/Recommendation**: see #7.
