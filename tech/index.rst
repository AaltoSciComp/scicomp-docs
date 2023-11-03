FCCI Tech (fka Behind Triton)
=============================

This is a series of talks about scientific computing support and HPC infrastructure administration in
practice.  It started as our internal kickstart to new members of our
staff, but the scope is expanded and now others interested in research
infrastructure is invited, though our orientation is still primarily
on the Triton team and FCCI admins.  Typical attendee are involved in
HPC cluster administration or scientific computing infrastructure.

In the future, this may turn into a more general "research
engineering" seminar series, once we are done with internal
explanations.

We share what our practices are, what we have learned, and informally
discuss.

.. seealso::

   :doc:`user-support`



Practicalities
--------------

**Time:** The next speaker announce the time/date of the seminar the week
before. The speaker sends invitation with the Zoom link.

**Duration:** Rough estimate: ~40 minutes by the main speaker + ~20
minutes questions/discussion, if any.

**Location:** Zoom, ask for an invitation but it is usually the :doc:`garage
link </help/garage>`.

**Recordings:** You can view a playlist of *some* videos `on youtube
<https://www.youtube.com/playlist?list=PLZLVmS9rf3nN1Rj-TAqFEzFM22Y1kJmvn>`__
(and a few more are available to our team internally).

*It is not a right but a privilege to participate. Free.*



Topics 2021
-----------

- Wed 3.3, 10:00, **Triton hardware**, Ivan Degtyarenko

  + Triton hardware wise: machine room, different archs, IPMI, hardware troubleshooting
  + [Material includes sensitive data, can be provided on request]

- Fri 12.3, 10:15-11:15, **Triton networking**, Ivan Degtyarenko

  + Networking: IB and Ethernet setup, IB islands, troubleshooting
  + [Material includes sensitive data, provided on request]

- Mon 22.3 14-15, **Ansible for FCCI**, Mikko Hakala

  + Ansible, provisioning with OpenHPC, standalone servers

- Mon 29.3 14-15, **User support in Aalto Scientific Computing**, Richard Darst

  + User support made easy: different support level by Science IT,
    docs, issue tracker, garage, etc
  + :doc:`Presentation <user-support>`, `Video <https://youtu.be/P1ttGhPGuN0&list=PLZLVmS9rf3nN1Rj-TAqFEzFM22Y1kJmvn>`__

- Fri 9.4 10:15-11:15, **Triton software stack**, Simo Tuomisto

  + Triton / FCCI software stack: Spack, building software, ...

- Fri 30.4 10:15, **Jupyter at Aalto**, Richard Darst

  + Jupyter setup at Aalto `jupyter.triton.aalto.fi <https://jupyter.triton.aalto.fi/hub/login>`_, best practices.

- Fri 7.5 10:15, **Anaconda on Triton**, Simo Tuomisto

  + Anaconda setup on Triton

- Fri 14.5 10:15, **Sphinx documentation**, Richard Darst

  + Open and accessible documentation using Sphinx, RST/MyST, and
    Readthedocs: the story behind scicomp.aalto.fi.
  + :doc:`Presentation <sphinx-docs>`, `Video <https://youtu.be/X6OzCSiS_VU&list=PLZLVmS9rf3nN1Rj-TAqFEzFM22Y1kJmvn>`__

- Tue, 18.5 12:00, **ClusterStor**, Andreas Muller (HPE)

  + Storage systems: ClusterStor hardware and software behind Triton's new /scratch. Maintenance, troubleshooting.

- Fri 28.5 10:15, **RSE service status update**, Jarno Rantaharju, Marijn van Vliet, and Richard Darst

  + RSE program: spring 2021 summary. Impact we have made so far.
  + `Presentation <https://docs.google.com/presentation/d/1Ti4TvjAilnElk9ITBZVsMnR0g7pfgPg8t5HHe2YOQs4>`__, `Video <https://youtu.be/rvuwLSKLaJI&list=PLZLVmS9rf3nN1Rj-TAqFEzFM22Y1kJmvn>`__

- Fri 8.10 10:15, **Introduction to a Kubernetes deployment**, Richard Darst

  + What is kubernetes and when is it useful?
  + Different types of Kubernetes objects and how you learn about them
  + Walk through how you would deploy a service into kubernetes - live demo
  + Q&A
  + `Session notes <https://hackmd.io/@AaltoSciComp/SyAgcmTQF>`__,
    `Video <https://www.youtube.com/watch?v=CXOPwtJ7qDI&list=PLZLVmS9rf3nN1Rj-TAqFEzFM22Y1kJmvn>`__.

- Fri 19.11 10:00, **jupyter.cs**, Richard Darst

- Fri 26.11 10:15, **Triton authentication**, Mikko Hakala

- Fri 3.12 10:15, **NetApp at Aalto: department admins guide**, Pekka Alaruikka / Mika Kontiala

  + NetApp setup at Aalto
  + what department admins may and may not of TeamWork
  + Practicalities: volumes, exports, qtrees, quotas, settings, permissions etc
  + (if time left) about backups on the TeamWork, troubleshooting, getting help, etc

- Fri 10.12 10:15, **High Performance Clusters at NVIDIA**, Janne Blomqvist

  * NVIDIA cluster setup overview
  * Best practices of the HPC cluster maintenance
  * What we are doing wrong at FCCI as comparing to NVIDIA

- Fri 17.12 10:00, **CodeRefinery teaching strategy** Richard Darst

  * The role of teaching in CodeRefinery and Aalto Scientific Computing
  * Tools and strategies we use to successfully teach online: HackMD,
    streaming, helpers, teams, co-teaching, and more.
  * Future outlook and goals
  * `Video <https://youtu.be/S9Jor12Cxdc>`__, `Materials <https://hackmd.io/KRqQirJ_Rn2SHcE-t1iAUg?view>`__
  * `Demo of our online teaching strategies <https://www.youtube.com/watch?v=WjmttAniZX8>`__

- Fri 17.12 12:00, **Open onDemand experience** by Esko Järnfors et all (CSC)

  * NOTE: the second talk on the same Fri 17.12

- Fri 3 Nov 2023 **Simple Kubernetes deployment** by Richard Darst

  * If you have a containerized service, how can you easily deploy it
    using Kubernetes?
  * `Notes
    <https://hackmd.io/@AaltoSciComp/kubernetes-deployment-demo>`__,
    `Video <https://youtu.be/WnkGkCoRGnk>`__

- (fall 2021) SLURM setup, Simppa Äkäslompolo

- (fall 2021) Cluster monitoring, Simo/Mikko

- Online courses and CodeRefinery, Richard Darst

- Online work and support, Richard Darst

  - :doc:`online-work-and-support`

- Respectfully and efficiently handling user support requests, Richard Darst

  - :doc:`user-support-responses`

- Science-IT data management: policies and procedures

- Science-IT data management: storage systems and tech setup

- History and structure of FCCI

- Security

- add more here
