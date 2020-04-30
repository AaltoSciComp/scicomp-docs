==================================
Jun 2020 / Triton Summer Kickstart
==================================

Part of `Scientific Computing in Practice <https://scicomp.aalto.fi/training/scip/index.html>`__ lecture series at Aalto University.

**Audience:** All FGCI consortium members looking for the HPC crash course.

**About the course:**

Three days kickstart for the researchers to get started with the available
computational resources at Aalto (=FGCI resources in general) and CSC.
The course is modular, we cover one by one several aspects. First day
dedicated to the computational resources in general: one will get whole
picture what computational resources are available in particular what is
HTCondor, what CSC has to offer and how to access a Triton cluster at
Aalto. The days two and three are focused on Triton usage practicalities, given in
the hands-on style tutorial, there will be lot of practical things on
how to get started on Triton. We will go through all the basics and advances like running in parallel, running on GPU, troubleshooting.
During the course there will be particular use cases like examples in
Matlab, Python, machine learning.

Overall we give you hints, ready solutions and copy/paste examples on how
to find, run and monitor your applications and manage your data. In addition to how to optimize
your workflow in terms of filesystem traffic, memory usage etc.

The course is obligatory for all new Triton users and recommended to all
interested in the field.

**Time, date:** Mon 8.6, Tue 9.6, Wed 10.6, 12:00-16:00

**Place:** Online: Zoom link is TBA

**Lecturering by:** Aalto Science IT and CSC people

**Registration:** `registration link <https://link.webropolsurveys.com/S/B1752A5EBD3BF08F>`__

Days’ time schedule is flexible, here is the tentative plan. 
Short 10 minutes breaks in between. You will be given time
to try and ask, it’s more like an informal help session to get you started
with the computing resources.

BTW, HPC stands for High Performance Computing

**Day #1:**

  Module #1.1 (15m): Welcoming, course details

  Module #1.2 (1h): HPC crash course: what is behind the front-end // lecture

  *HPC fundamentals: terminology, architectures, interconnects, infrastructure behind, as well as MPI vs shared memory // Ivan Degtyarenko

  Module #1.3 (1h): CSC resources overview // lecture with demos

  *An overview of CSC computing environment and services including Puhti supercomputer, Allas data management solution, Cloud services, notebooks, containers, etc // Jussi Enkovaar and Henrik Nortamo

  Module #1.4 (1h): HTCondor setup at Aalto // lecture with demos

  *Did you know that department workstations around could be accessible for computing? It is were HTCondor comes in game // Matthew West

  Module #Extra (.5h): Connecting to Triton // tutorial

  *Get connected to Triton in preparation for day 2 // Enrico Glerean

  See the `Connecting to Triton tutorial </triton/tut/connecting.html>`__ – if you can ssh to Triton and run “hostname”, you are ready for tomorrow.

**Day #2:**

  Module #2.1 (4h): Getting started on Triton, SLURM basics, module // tutorial

  *Triton’s workflow, running and monitoring serial jobs on Triton. Interactively and in batch mode. module and toolchains, special resources like GPU // Richard Darst

  See the Triton tutorials (“connecting” to “running in the queue”)

**Day #3**

  Module #3.1 (4h): SLURM advances // tutorial

  *Running in parallel with MPI and OpenMP, array jobs, running on GPU with –gres, local drives, constrains // Simo Tuomisto

  See the same Triton tutorials (“array jobs” to “GPU computing”)


**Cost:** Free of charge for FGCI consortium members including Aalto employees and students.


**Course prerequisite requirements and other details:**

Participants will be provided with access to Triton for running examples.
Participants are expected to have SSH client installed.

* Aalto people, if you do not yet have access to Triton, :doc:`request an account
  </triton/accounts>` in advance.
* Then, try to :doc:`connect to Triton </triton/tut/connecting>` to be
  ready.
* If you aren't familiar with the Linux shell, :doc:`read the crash
  course </scicomp/shell>`

**Additional course info at:** Ivan Degtyarenko, ivan.degtyarenko -at- aalto.fi
