===============================================
Oct 2019 / Practical R and Python data analysis
===============================================

Part of `Scientific Computing in Practice <https://scicomp.aalto.fi/training/scip/index.html>`__ lecture series at Aalto University.

**Audience:** Researchers who are or will soon be using R and Python
for data analysis, who know a bit about these languages but haven’t
studied best practices for data analysis in them. We do not assume
familiarity with R (but some sort of knowledge of programming), but do
assume a small amount of Python.

**About the course:** We provide a practical introduction and advice
for data analysis in R and Python. The primary lessons will be in
libraries and visualization in these languages (the data frame in R
and pandas in Python) and optimizing data storage and access. Side
lessons will include data storage formats, Jupyter notebooks, Triton
and HPC for data processing, optimization of time and memory usage,
profiling, workflow automation, and overall good practices. The course
is suited both for beginners and those already using these tools but
feel they should be better. Material will be divided approx. into two
equal parts, 3 sessions of R and 3 sessions of Python.  The two haves
will cover similar information and concepts, so you may choose to only
come to one part (see below). With lots of demos and hands-on
exercises to try on your own.

**Lecturer:** Janne Blomqvist, D. Sc., Science IT / Department of
Applied Physics, Richard Darst, Ph. D., Science IT / Department of
Computer Science, Simo Tuomisto, Science IT / Department of Computer
Science

**Time, date:**

- Mon 30.9, 12:00-15:00 (Python)
- Thu 3.10, 12:00-15:00 (Python)
- Mon 7.10, 12:00-15:00 (Python)
- Thu 10.10, 12:00-15:00 (R)
- Mon 14.10, 12:00-15:00 (R)
- Thu 17.10, 12:00-15:00 (R)

**Place:** Otakaari 1, U135a (the auditorium next to Cafe Elissa in
the main building)

**Cost:** Free of charge for FGCI consortium members including Aalto
employees and students.

**Registration:** `registration is open <https://www.webropolsurveys.com/S/427A39987ED882BA.par>`__

**Credits:** Credits available for the Aalto students and course
certificate can be provided on request for the outsiders. Full course
hours correspond roughly to 1 ECTS. Students who wish to get a
certificate should hand in the homework assignments and participate to
at least 4 of 6 lectures.

**Other comments:** During the tutorials we’ll use jupyter.cs.aalto.fi
and jupyter.triton.aalto.fi.  It's also good to have an SSH client
installed.  *Participants are expected to bring their own laptops.*

**Additional course info at:** janne.blomqvist -at aalto.fi, richard.darst -at- aalto.fi, simo.tuomisto -at- aalto.fi

**Course preparation**

This course will use https://jupyter.cs.aalto.fi and
https://jupyter.triton.aalto.fi .  You will need an Aalto account.

..
  Make sure that you can connect via at least one of these ways (you
  have to be on the Aalto networks):

   * from the Aalto eduroam wireless network (recommended for personal
     and standalone computers)
   * from the aalto wireless network on an Aalto managed computer
     (recommend when possible)
   * from any network, via the Aalto VPN (or proxy as described in the
     scicomp instructions).  This is the worst-case possibility
   * You need a Triton account.  If you do not have one, read the
     scicomp instructions and request one.
   * If you can access https://jupyter.triton.aalto.fi and log in, you
     are ready to go.
   * It is best if you can SSH to Triton.  Install a ssh client in
     advance, we can help with the rest of the connection process during
     the course.

**Course material**

You can find our git repository at
https://github.com/AaltoScienceIT/python-r-data-analysis-course.  Note
that it is a work in progress and until (and even after) something has
been presented, it may still change.  The links below go to the “raw”
notebooks, and you can find the work and “solutions” we have done in
class in the `classwork-2019 branch`_.  By day, we have covered:

.. _classwork-2019 branch: https://github.com/AaltoScienceIT/python-r-data-analysis-course/tree/classwork-2019

* Day 1: Python

  * 01_Course_intro_and_Jupyter.ipynb
  * 02_Jupyter_demo_pi.ipynb
  * python/01_Python_intro.ipynb
  * python/02_Python_data_types_and_structures.ipynb
  * python/03_Numpy.ipynb

* Day 2: Python

  * python/03_Numpy.ipynb
  * python/10_Tidy_data.ipynb
  * python/04_Pandas.ipynb (or moved to the next day)
  * Time handling

* Day 3: Python, plotting

  * python/04_Pandas.ipynb (continuing from previous lecture)
  * python/05_Python_IO.ipynb
  * python/06_Pandas_split_apply_combine.ipynb
  * python/08_Profiling_and_debugging.ipynb (if time allows)
  * python/09_Matplotlib.ipynb
  * Presentation of homework exercises (if time allows)

* Day 4: R

* Day 5: R

* Day 6: R

To get the repository::

  git clone https://github.com/AaltoScienceIT/python-r-data-analysis-course/

To set up the git merge and diff hooks (Triton magic), copy and paste these inside the repository::


  /share/apps/jupyterhub/live/miniconda/bin/nbdime config-git --enable
  sed --in-place -r 's@(= )[ a-z/-]*(git-nb)@\1/share/apps/jupyterhub/live/miniconda/bin/\2@' .git/config

**Homework**

The homework is in the git repository in the ``/homework``
directory. A README file in that directory explains the instructions:
just take each notebook as a starting point and try to solve the
exercise inside of it.  The deadline to return is 15.11 (middle of
November) at 12:00.  To return, create a repository at
``version.aalto.fi`` and send Janne a link to a commit in the repo
(make sure to share it with Janne first!). If you don't have an Aalto
account, you can send a ``.tar.gz`` or ``.zip`` archive to Janne as
attachment via email, or create a repo e.g. on ``gitlab.com`` (make
sure to make it private, and share it with Janne only!).

**Update: For exercise 4, the ntsb.gov site is down, so we have
mirrored the data needed at:**
https://users.aalto.fi/~tuomiss1/rcourse/elfaro.kmz
