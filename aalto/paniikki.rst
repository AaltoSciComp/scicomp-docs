===================================
Paniikki: Computer Lab For Students
===================================

Paniikki is a cutting edge computer lab in the computer science
department. It is located in `T-building C106
<https://usefulaaltomap.fi/#!/select/paniikki>`_ (right under lecture
hall T1). This documentation is a Paniikki cheatsheet.

.. figure:: /images/paniikki_map.png
  :align: center
  :alt: alternate text
  :figclass: align-center

  < The blue box at the entrance is Paniikki >

For more services directed at students, see :doc:`welcomestudents`.

The name
========
Paniikki means "panic" in English which is a fascinating name as people in panic are in panic. I don't know which comes first, the space or the emotion. Anyway, people experience the both simultaneously.

-------------------------------------------

Hardware
========

.. csv-table::
   :header-rows: 1
   :delim: |

   CPU properties| Spec
   Model                  | Intel(R) Xeon(R) CPU E5-1650 v4 @ 3.60GHz
   Architecture            | x86_64
   CPU(s)                  | 12
   Thread(s) per core      | 2
   max MHz                | 4000.0000
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

-------------------------------------------

Software
========
First thing first, you DO NOT have a sudo right in Aalto classroom
machines and you never will. We provide the most used SW and if you need
more you could inquire via servicedesk@aalto.fi.  We try to have a good
base software that covers most people's needs.

.. csv-table::
   :header-rows: 1
   :delim: |

   What?  |  How?

   Python via Anaconda | ``module load anaconda``
   Python (system) | Default available
   Tensorflow | in the Python environments, e.g. anaconda above


Modules
#######
In short, ``module`` is a software environment management tool. With
``module`` you can manage multiple versions of software easily. Here
are some sample commands:

.. include:: /triton/ref/modules.rst

There are some modules set up specifically for different courses: if
you just load the environment with "module load", you will have everything you need.

Read the details in :doc:`Module environment page </triton/tut/modules>`.

Example 1
^^^^^^^^^
Assume we are in Paniikki and wants to do our homework for CS-E4820 Machine Learning: Advanced probabilistic methods. In the course students use Tensorflow and Edward.

.. code-block:: bash

	# Check available modules
	$ module load courses/    # Tab to auto-complete

	# Finally you will complete this
	$ module load courses/CS-E4820-advanced-probabilistic-methods.lua

	# Check the module you loaded
	$ module list

	Currently Loaded Modules:
		1) courses/CS-E4820-advanced-probabilistic-methods

	# Check the packages
	$ conda list    # You will see Tensorflow and etc.

	# Launch Jupyter
	$ jupyter notebook

	# Do your homework

	# You are done and want to un-load all the modules?
	$ module purge


Example 2: General Python software
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Need Python and general software?  The anaconda modules have Python, a
bunch of useful scientific and data packages, and machine learning
libraries.

.. code-block:: bash

   # Latest Python 3
   $ module load anaconda

   # Old Python 2
   $ module load anaconda2


Example 3: List all software
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
You can check all other modules as well

.. code-block:: bash

	$ module avail


.. figure:: /images/module_avail.png
  :align: center
  :alt: alternate text
  :figclass: align-center

  < Available modules in Paniikki as of 2018 March 8th >

You want to use Matlab?

.. code-block:: bash

	$ module load matlab/2017b
	$ matlab

-------------------------------------------

Questions?
==========
If you have any question please contact seyoung.park@aalto.fi.














