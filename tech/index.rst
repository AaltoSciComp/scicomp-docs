FCCI Tech (aka the SciComp Tech series)
=======================================

.. admonition:: Upcoming talks

   (none right now)

This is a seminar series on scientific computing, research software
engineering, and generally being a good collaborator in scientific
computing research.  The target ranges from aspiring research software
engineers to computing infrastructure specialists.  It is part of the
ASC's new research software engineer training.

It evolved from a series "how ASC does things, taught to people
joining our team" to something similar (with more general topics) but
with a broader audience (everyone is invited).  If you want to network
with and learn from other people in research computing, you are
welcome to attend.



Practicalities
--------------

**Time:** Usually Fridays at 10:00 Europe/Helsinki time.

**Duration:** 60 minute time slot, good to plan for 20-30 minutes
presentation and 20-30 minutes discussion.

**Location:** Zoom, usually the :doc:`garage link </help/garage>`.

**Recordings:** You can view a playlist of *some* videos `on youtube
<https://www.youtube.com/playlist?list=PLZLVmS9rf3nN1Rj-TAqFEzFM22Y1kJmvn>`__.

**How to present:** Talk to rkdarst, get on the schedule.

*It is not a right but a privilege to participate. Free.*


Proposed/requested future topics
--------------------------------

- SLURM setup, Simppa Äkäslompolo

- Cluster monitoring, Simo/Mikko

- Online courses and CodeRefinery, Richard Darst

- Online work and support, Richard Darst

  - :doc:`online-work-and-support`

- Respectfully and efficiently handling user support requests, Richard Darst

  - :doc:`user-support-responses`

- Science-IT data management: policies and procedures

- Science-IT data management: storage systems and tech setup

- History and structure of FCCI

- Security



Past and currently planned
--------------------------

.. toctree::
   :maxdepth: 1
   :hidden:

   user-support
   Diversity vs services (external) <https://docs.google.com/presentation/d/1pVjFnxGzfy0DTPuc1XLQDFg0-44GUWwfSMxe5vVg-Lc/edit>
   sphinx-docs
   The future of teaching <https://hackmd.io/KRqQirJ_Rn2SHcE-t1iAUg?view>
   online-work-and-support
   user-support-responses
   How we did Kickstart 2021 <https://rkdarst.github.io/presentation-kickstart/>
   RSE service status 2021 <https://docs.google.com/presentation/d/1Ti4TvjAilnElk9ITBZVsMnR0g7pfgPg8t5HHe2YOQs4>
   Triton software stack (external) <https://www.youtube.com/watch?v=2lj4JqJWzz8&list=PLZLVmS9rf3nN1Rj-TAqFEzFM22Y1kJmvn>
   Anaconda on Triton (external) <https://www.youtube.com/watch?v=2lj4JqJWzz8&list=PLZLVmS9rf3nN1Rj-TAqFEzFM22Y1kJmvn>
   Introduction to kubernetes deployment <https://hackmd.io/@AaltoSciComp/SyAgcmTQF>
   jupyter.cs <https://hackmd.io/TCPjGdR5Q7WoLbzlvsPHUA>
   Simple kubernetes deployment <https://hackmd.io/@AaltoSciComp/kubernetes-deployment-demo>

Events are listed below in chronological order, but sort of sorted by
usefulness to a broad audience in the left sidebar (including events
which have been drafted but not presented).

- **Triton hardware**, Ivan Degtyarenko, Wed 3.3 2021, 10:00

  + Triton hardware wise: machine room, different archs, IPMI, hardware troubleshooting
  + [Material includes sensitive data, can be provided on request]

- **Triton networking**, Ivan Degtyarenko, Fri 12.3 2021, 10:15-11:15

  + Networking: IB and Ethernet setup, IB islands, troubleshooting
  + Interval video (Material includes sensitive data, provided on
    request)

- **Ansible for FCCI**, Mikko Hakala, Mon 22.3 2021, 14-15

  + Ansible, provisioning with OpenHPC, standalone servers
  + Internal video

- **User support in Aalto Scientific Computing**, Richard Darst, Mon
  29.3 2021, 14-15

  + User support made easy: different support level by Science IT,
    docs, issue tracker, garage, etc
  + :doc:`Presentation <user-support>`
  + `Video <https://youtu.be/P1ttGhPGuN0&list=PLZLVmS9rf3nN1Rj-TAqFEzFM22Y1kJmvn>`__

- **Triton software stack**, Simo Tuomisto, Fri 9.4 2021, 10:15-11:15

  + Triton / FCCI software stack: Spack, building software, ...
  + `Video <https://www.youtube.com/watch?v=2lj4JqJWzz8&list=PLZLVmS9rf3nN1Rj-TAqFEzFM22Y1kJmvn>`__

- **Jupyter at Aalto**, Richard Darst, Fri 30.4 2021, 10:15

  + Jupyter setup at Aalto `jupyter.triton.aalto.fi <https://jupyter.triton.aalto.fi/hub/login>`_, best practices.
  + Internal video (but it should be published)

- **Anaconda on Triton: automatic build system**, Simo Tuomisto, Fri 7.5 2021, 10:15

  + Anaconda setup on Triton
  + `Video <https://www.youtube.com/watch?v=2lj4JqJWzz8&list=PLZLVmS9rf3nN1Rj-TAqFEzFM22Y1kJmvn>`__

- **Diversity in computational sciences vs university services**

  + This wasn't originally given in FCCI Tech but is relevant to the
    people reading this page.
  + `Presentation <https://docs.google.com/presentation/d/1pVjFnxGzfy0DTPuc1XLQDFg0-44GUWwfSMxe5vVg-Lc/edit>`__
  + `Video <https://www.youtube.com/watch?v=z1VS1wleN-o&list=PLZLVmS9rf3nN1Rj-TAqFEzFM22Y1kJmvn>`__

- **Sphinx documentation**, Richard Darst, Fri 14.5 2021, 10:15

  + Open and accessible documentation using Sphinx, RST/MyST, and
    Readthedocs: the story behind scicomp.aalto.fi.
  + :doc:`Presentation <sphinx-docs>`
  + `Video <https://youtu.be/X6OzCSiS_VU&list=PLZLVmS9rf3nN1Rj-TAqFEzFM22Y1kJmvn>`__

- **ClusterStor**, Andreas Muller (HPE), Tue 18.5 2021, 12:00

  + Storage systems: ClusterStor hardware and software behind Triton's
    new /scratch. Maintenance, troubleshooting.

- **RSE service status update**, Jarno Rantaharju, Marijn van Vliet,
  and Richard Darst, Fri 28.5 2021, 10:15

  + RSE program: spring 2021 summary. Impact we have made so far.
  + `Presentation
    <https://docs.google.com/presentation/d/1Ti4TvjAilnElk9ITBZVsMnR0g7pfgPg8t5HHe2YOQs4>`__
  + `Video
    <https://youtu.be/rvuwLSKLaJI&list=PLZLVmS9rf3nN1Rj-TAqFEzFM22Y1kJmvn>`__

- **How we did Summer Kickstart 2021**, Richard darst
  + `Reading <https://rkdarst.github.io/presentation-kickstart/>`__
  + `Video <https://www.youtube.com/watch?v=gi_zHFPgpfw&list=PLZLVmS9rf3nN1Rj-TAqFEzFM22Y1kJmvn>`__

- **Introduction to a Kubernetes deployment**, Richard Darst, Fri 8.10 2021,
  10:15

  + What is kubernetes and when is it useful?
  + Different types of Kubernetes objects and how you learn about them
  + Walk through how you would deploy a service into kubernetes - live demo
  + Q&A
  + `Reading <https://hackmd.io/@AaltoSciComp/SyAgcmTQF>`__
  + `Video <https://www.youtube.com/watch?v=CXOPwtJ7qDI&list=PLZLVmS9rf3nN1Rj-TAqFEzFM22Y1kJmvn>`__.

- **jupyter.cs**, Richard Darst, Fri 19.11 2021, 10:00

  + `Reading <https://hackmd.io/TCPjGdR5Q7WoLbzlvsPHUA>`__
  + `Video <https://www.youtube.com/watch?v=pogWj8COX4o&list=PLZLVmS9rf3nN1Rj-TAqFEzFM22Y1kJmvn>`__

- **Triton authentication**, Mikko Hakala, Fri 26.11 2021, 10:15

  + Internal video

- **NetApp at Aalto: department admins guide**, Pekka Alaruikka / Mika
  Kontiala, Fri 3.12 2021, 10:15

  + NetApp setup at Aalto
  + what department admins may and may not of TeamWork
  + Practicalities: volumes, exports, qtrees, quotas, settings, permissions etc
  + (if time left) about backups on the TeamWork, troubleshooting, getting help, etc

- **High Performance Clusters at NVIDIA**, Janne Blomqvist, Fri 10.12
  2021, 10:15

  * NVIDIA cluster setup overview
  * Best practices of the HPC cluster maintenance
  * What we are doing wrong at FCCI as comparing to NVIDIA

- **The future of teaching: CodeRefinery teaching strategy** Richard
  Darst, Fri 17.12 2021, 10:00

  * The role of teaching in CodeRefinery and Aalto Scientific Computing
  * Tools and strategies we use to successfully teach online: HackMD,
    streaming, helpers, teams, co-teaching, and more.
  * Future outlook and goals
  * `Reading <https://hackmd.io/KRqQirJ_Rn2SHcE-t1iAUg?view>`__
  * `Video <https://youtu.be/S9Jor12Cxdc>`__
  * `Demo of our online teaching strategies <https://www.youtube.com/watch?v=WjmttAniZX8>`__

- **Open onDemand experience** by Esko Järnfors et all (CSC), Fri
  17.12 2021, 12:00

  * NOTE: the second talk on the same Fri 17.12

- **Simple Kubernetes deployment** by Richard Darst, Fri 3 Nov 2023

  * If you have a containerized service, how can you easily deploy it
    using Kubernetes?
  * `Notes
    <https://hackmd.io/@AaltoSciComp/kubernetes-deployment-demo>`__,
    `Video <https://youtu.be/WnkGkCoRGnk>`__

- **Demo: Publishing a Python Package** by Jarno Rantaharju, Fri Jan 26th 2024

 * Demonstration of open source software publishing. I will take a part of an
   existing Python package and spin it of as a small stand-alone package. We
   will discuss what is needed for a software publication and recommended
   practices.
 * `Notes <https://hackmd.io/@AaltoSciComp/python-package-publication-demo>`__
