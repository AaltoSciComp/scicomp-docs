===========================================================
New project: Paniikki GPU machine remote utilisation for AI
===========================================================

TL;DR
=====
Aalto CS-IT is initiating a new project: Paniikki GPU machine remote utilisation for AI. You will be able to use Paniikki machines for your Kaggle_ projects or `Stanford Convolutional Neural Network course`_ from anywhere. If you find this interesting please give us a feedback :)

.. _`Stanford Convolutional Neural Network course`: http://cs231n.github.io
.. _Kaggle: https://www.kaggle.com


Background
==========
AI is the new sexy
------------------
Alphago is the new GO champion. Everyone is hiring data scientists. `Aalto machine learning course`_ is exploding with 600 students and everyone is teaching machine learning and deep learning. Aalto machine learning master's program, MACADAMIA, is packed with international talents.

.. _`Aalto machine learning course`: https://mycourses.aalto.fi/course/view.php?id=16918

While the topic itself is very interesting and there are many resources for studying it, there are some chanllenges that people face: GPU and dependency installations. You could always use a powerful GPU workstation in Paniikki but you may be busy to go there or you may not be familiar with remote SSH.

Can Aalto help you?
-------------------
YES!!! We are always glad to help you and we want you to get advantage of the luxurious workstations in Paniikki(The NVIDIA Quadro P5000 GPUs in Paniikki costed us €2K/module). We will build a desktop app that allows you to use complete scientific containers on Paniikki machines, remotely without any use of Terminal. We will also prepare containers for famous ML courses so you don't have to struggle setting the infrastructures.   

How are we going to deliver this?
=================================
We will distribute a cross-platform app. You install it on your Linux/Windows/Mac. When you start the app, click a container of your choice e.g. Tensorflow_py35. A jupyter notebook server will start on a most idle machine in Paniikki and you will be given an URL & token for the notebook. We are considering of using ElectronJS_ for the front-end and Singularity_ for the containers. We use containers because you can just take them if you want to use it somewhere else.

.. _ElectronJS: https://www.electronjs.org/
.. _Singularity: https://sylabs.io/docs/

Who could use it?
=================
All Aalto students and staffs.

When will it be available?
==========================
2018 spring. Hopefully April.

Last but not least: let's make Aalto great together!
====================================================
Our mission is to serve you the best to enhance the science. We work hard but we want to make sure that we are doing it right. So your feedbacks are tremendously invaluable to us. Tell us how you like our ideas and what you want and need, but please be nice ;) We are humans and we have feelings like you.
If you would like to collaborate with us you are more than welcome! Please pay us a visit at A243 at CS building or send us an e-mail @ guru@cs.hut.fi.

#########################

Appendix
========
In Paniikki(panic in Finnish), a computer room in the CS building, there are 31 monster machines waiting to rock 'n roll with you. Here is the spec:

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
 

     
