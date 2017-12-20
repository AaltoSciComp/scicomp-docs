==============
Aalto loves AI
==============

TL;DR
=====
We will make it super easy for you to use Paniikki machines remotely from your home computers. Paniikki machines are powerful workhorses loaded with powerful 8-core CPUs and $1845 GPUs. Take advantange of these for your next amazing AI projects.

Intro
=====
Do you want to do some Machine Learning? Do you want to run a convolutional neural network with 100 layers of 100 units? Go ahead and rock 'n roll but if you are dancing on your Macbook or Thinkpad your algorithm will just never end. That is because AI(machine learning, deep learning, data mining and etc.) is computationally heavy. You need lots of strong CPU cores and especially powerful GPUs. However, GPUs are expensive! A decent GPU can cost as much as your laptop.

Fortunately Aalto has you covered! In Paniikki(panic in Finnish), a computer room in the CS building, there are 31 monster machines waiting to rock 'n roll with you. Here is the spec:

.. csv-table::
   :header-rows: 1
   :delim: |

   CPU properties| Spec
   Model                  | Intel(R) Xeon(R) CPU E5-1650 v4 @ 3.60GHz
   Architecture            | x86_64
   Byte Order              | Little Endian
   CPU(s)                  | 12
   Thread(s) per core      | 2
   MHz                    | 1200.796
   max MHz                | 4000.0000
   min MHz                | 1200.0000
   Virtualization         | VT-x
   L1d cache              | 32K
   L1i cache              | 32K
   L2 cache               | 256K
   L3 cache               | 15360K
   

.. csv-table::
   :header-rows: 1
   :delim: |

   Model | NVIDIA Quadro P5000
   GPU properties| Spec
   Core | GP104GL (Pascal-based)
   Core clock | 1607 MHz
   Memory clock | 1251 MHz
   Memory size | 16384 MiB
   Memory type | 256-bit GDDR5X 
   Memory bandwidth | 320
   CUDA cores | 2560
   CUDA compute capability | 6.1
   OpenGL | 4.5
   OpenCL | 1.2
   Near GeForce Model| GeForce GTX 1080  

.. csv-table::
   :header-rows: 1
   :delim: |

   Memory properties| Spec
   RAM                        | 32GiB
 

Our goal
========
We will build a simple front-end application which you can install on your home computers. Here's how the app will work:

1. App starts. Enter your Aalto credentials
2. You will be given a list of available Python environments, e.g. Tensorflow-py35 or PyTorch-py34.
3. You select the environment you need.
4. A jupyter notebook server is launched on a Paniikki machine which is the most idle. You will be an URL where you can access the Jupyter notebook.
5. You enter the given URL in your browser. You start coding. The code is saved on the Aalto network drive so you can access them from any Aalto nodes.




The Aalto Scicomp Garage is a help session for scientific computing at
Aalto organized by the Science-IT team (Triton admins).  It's the best
time to talk to the people behind scientific computing at Aalto.  This
is a place to get stuff done, so bring your laptop and coffee/food,
and come hang out.

There are two things that can happen: During the whole time, free-form
help from Triton admins.  Second, there may be a *short*,
*introductory* presentation on some topic that can get a discussion
started.  Both usually happen in parallel, and we decide the best
organization each week.

Come if you want to:

-  Solve problems
-  Discuss bigger problems
-  Network with others who are doing similar work
-  Learn something new
-  Give feedback

Schedule
========

-  Days: Triton garage is every week from 14:00-15:00 on Tuesdays. Every
   other week, there is a short talk. Otherwise, we are only there for
   questions and support.
-  Time: We promise to be there only the first 30 minutes. After this,
   we leave once we are done helping attendees. So if you are coming,
   come in the first 30 minutes.
-  Location: See below.  U121a_ and U121b_  (in main building),
   T4_ (CS building).

.. _U121a: http://usefulaaltomap.fi/#!/select/main-U121a
.. _U121b: http://usefulaaltomap.fi/#!/select/main-U121b
.. _T4:    http://usefulaaltomap.fi/#!/select/cs-A238

.. csv-table::
   :header-rows: 1
   :delim: |

   Date (default Tue)   | Time (default 14:00-15:00)  | Loc   | Topic
   26.9     |       | T4    |
   3.10     |       | U115b |
   10.10    |       | T4    | First-time users
   17.10    |       | U121b | GPU computing
   24.10    |       | T4    |
   31.10    |       | U121b | Aalto and department environments
   7.11     |       | T4    |
   14.11    |       | U121b |
   21.11    |       | T4    |
   28.11    |       | U121a |
    5.12    |       | T4    |
   12.12    |       | U121a |
   19.12    |       | T4    |


Topics
======
* `Triton intro: interactive jobs <../triton/tut/interactive>`_
* `Git <http://rkd.zgib.net/scicomp/scip2015/git.html>`_


Possible special topics
=======================

-  Profiling and performance monitoring
-  debugging
-  open source: making software and running a project, licenses
-  shell scripting and automation
-  unix intro
-  software testing
-  building good programs
-  porting python2 to python3
-  R
-  matlab
-  GPU / deep learning computing
-  molecular dynamics software

Past events
===========

-  2017-01-18 (W), 12:00-14:00, T4, CS building.

   -  Theme: Triton user group meeting. Presentation about the latest
      events and hearing user feedback.

-  2017-02-01 (W) 12:00-14:00, U121a (main building)

   -  Proposed topics: Quick introduction version control (git).
      (`materials <http://rkd.zgib.net/scicomp/scip2015/git.html>`__)

-  2017-02-15 (W) 12:00-14:00, T4 (CS building)
-  2017-03-01 (W) 12:00-14:00, U121a (main building)
-  2017-03-15 (W) 12:00-14:00, T4 (CS building)

10     
