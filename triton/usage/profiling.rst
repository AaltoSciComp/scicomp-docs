=========
Profiling
=========

.. note::

   Also see :doc:`debugging`.

You have code, you want it to run fast. This is what Triton is for. But
how do you know if your code is running as fast as it can? We are
scientists, and if things aren't quantified we can't do science on them.
Programming can often seem like a black box: modern computers are
extremely complicated, and people can't predict what is actually making
code fast or slow anymore. Thus, you need to *profile* your code: get
detailed performance measurements. These measurements let you know how
to make it run faster.

There are many tools for profiling, and it really is one of the
fundamental principles for any programming language. You really should
learn how to do quick profile just to make sure things are OK, even if
you aren't trying to optimize things: you might find a quick win even if
you didn't write the code yourself (for example, 90% of your time is
spent on input/output).

This page is under development, but so far serves as an introduction. We
hope to expand it with specific Triton examples.


Summary: profiling on Linux
---------------------------

First off, look at your language-specific profiling tools.

-  Generic Linux profiling tools (big and comprehensive list, also some
   presentations):\ http://www.brendangregg.com/linuxperf.html
-  Profiling in C and Python (introduction + examples):
   http://rkd.zgib.net/scicomp/profiling/profiling.html

CPU profiling
-------------

This can give you a list of where all your processor time is going,
either per-function or per-line. Generally, most of your time is in a
very small region of your code, and you need to know what this is in
order to improve *just* that part.

See the C and Python profiling example above.


GNU gprof
^^^^^^^^^

`gprof <http://sourceware.org/binutils/docs/gprof/>`__ is a profiler
based on instrumenting your code (build with -pg). It has relatively
high overhead, but gives exact information e.g. for the number of times
a function is called.

Perf
^^^^

`perf <https://perf.wiki.kernel.org/index.php/Tutorial>`__ is a
*sampling profiler*, which periodically samples *events* originating
e.g. from the CPU performance monitoring unit (PMU). This generates a
statistical profile, but the advantage is that the overhead is very low
(single digit %), and one can get timings at the level of individual asm
instructions. For a simple example, consider a (naive) matrix
multiplication program:

Compile the program (-g provides debug symbols which will be useful
later on, at no performance cost)::

  $ gfortran -Wall -g -O3 mymatmul.f90

Run the program via the profiler to generate profile data::

  $ perf record ./a.out

Now we can look at the profile::

 $ perf report
 # Samples: 1251
 #
 # Overhead Command Shared Object Symbol
 # ........ .............. ............................. ......
 #
 85.45% a.out ./a.out [.] MAIN\_\_
 4.24% a.out /usr/lib/libgfortran.so.3.0.0 [.] \_gfortran\_arandom\_r4
 3.12% a.out /usr/lib/libgfortran.so.3.0.0 [.] kiss\_random\_kernel

So 85% of the runtime is spent in the main program (symbol MAIN\_\_),
and most of the rest is in the random number generator, which the
program calls in order to generate the input matrices.

Now, lets take a closer look at the main program::

  $ perf annotate MAIN__
  ------------------------------------------------
  Percent \| Source code & Disassembly of a.out
  ------------------------------------------------
  :
  :
  :
  : Disassembly of section .text:
  :
  : 00000000004008b0 <MAIN__>:

... ::

  : c = 0.
  :
  : do j = 1, n
  : do k = 1, n
  : do i = 1, n
  : c(i,j) = c(i,j) + a(i,k) \* b(k,j)
  30.12 : 400a40: 0f 28 04 01 movaps (%rcx,%rax,1),%xmm0
  4.92 : 400a44: 0f 59 c1 mulps %xmm1,%xmm0
  12.36 : 400a47: 0f 58 04 02 addps (%rdx,%rax,1),%xmm0
  40.73 : 400a4b: 0f 29 04 02 movaps %xmm0,(%rdx,%rax,1)
  9.65 : 400a4f: 48 83 c0 10 add $0x10,%rax

Unsurprisingly, the inner loop kernel takes up practically all the time.

For more information on using perf, see the perf tutorial at

https://perf.wiki.kernel.org/index.php/Tutorial


Input/output profiling
----------------------

This will tell you how much time is spent reading and writing data,
where, and what type of patterns it has (big reads, random access, etc).
Note that you can see the time information when CPU profiling: if
input/output functions take a lot of time, you need to improve IO.

``/usr/bin/time -v`` prints some useful info about IO operations and
statistics.

Lowest level: use strace to print the time taken in every system call
that accesses files. This is not that great.::

    #  Use strace to print the total bytes
    strace -e trace=desc $command |& egrep 'write' | awk --field-separator='='  '{ x+=$NF } END { print x }'
    strace -e trace=desc $command |& egrep 'read' | awk --field-separator='='  '{ x+=$NF } END { print x }'

    # Number of calls only
    strace -e trace=file -c  $command


Memory profiling
----------------

Less common, but it can tell you something about what memory is being
used.

If you are making your own algorithms, memory profiling becomes more
important because you need to be sure that you are using the memory
hierarchy efficiently. There are tools for this.


MPI and parallel profiling
--------------------------

mpiP
^^^^

mpiP: Lightweight, Scalable MPI Profiling http://mpip.sourceforge.net/.
Collects statistical information about MPI functions. mpiP is a
link-time library, that means that it can be linked to the object file,
though it is recommended that you have recompiled the code with -g.
Debugging information is used to decode the program counters to a source
code filename and line number automatically. mpiP will work without -g,
but mileage may vary.


Usage example::

    # assume you have you MPI flavor module loaded
    module load mpip/3.4.1

    # link or compile your code from scratch with -g
    mpif90 ­-g ­-o my_app my_app.f90 ­-lmpiP ­-lm ­-lbfd ­-liberty ­-lunwind
    # or
    mpif90 ­-o my_app my_app.o ­-lmpiP ­-lm ­-lbfd ­-liberty ­-lunwind

    # run the code normally (either interactively with salloc or as usual with sbatch) 
    salloc -p play --ntasks=4 srun mpi_app

If everything works, you will see the mpiP header preceding your program
stdout, and there will be generated a text report file in your work
directory. File is small, no worries about quota. Please, consult the
link above for the file content explanation. During runtime, one can set
MPIP environment variables to change the profiler behavior. Example::

    export MPIP="-t 10.0 -k 2"


Scalasca
^^^^^^^^

Available through ``module load scalasca``

.. _gpu-profiling:

GPU profiling
-----------------
There are several tools available on triton for GPU profiling.

PyTorch Profiler
^^^^^^^^^^^^^^^^^

PyTorch Profiler is a tool that helps monitor and optimize the performance of PyTorch models. It provides insights into resource usage such as CPU, GPU, and memory, helping developers identify bottlenecks in model training. For detailed information on how to use PyTorch Profiler, refer to the `official documentation <https://pytorch.org/tutorials/recipes/recipes/profiler.html>`__.

On Triton, there are at least two approaches to visualizing profiler results:

.. tabs::

   .. tab:: OpenOnDemand/Desktop

      To visualize the report on Triton, you can launch a desktop from :doc:`Open Ondemand <../usage/ood>`. In the desktop's terminal, run:

      .. code-block:: console

        $ module load mamba
        $ source activate yourenv
        $ tensorboard --logdir ./log

      to launch the tensorboard and point it to the log directory where the profiling results were saved. Now you can view results in TensorBoard: open a browser and go to http://localhost:6006. Navigate to the PyTorch Profiler tab to view detailed profiling information, such as:

        - CPU and GPU utilization
        - Memory usage
        - Kernel execution times
        - Operation breakdowns
        
      **NOTE:** you need to have PyTorch Profiler TensorBoard Plugin installed in your environment via:

        .. code-block:: bash

           pip install torch-tb-profiler


   .. tab::  VS Code integration

      If you connect to Triton through VS Code by setting up an SSH connection.
      You can install the TensorBoard VS Code Extension to view TensorBoard outputs directly on the VS Code interface. 

      Typically, once you have added this line of code ``import torch.profiler`` to your python script, you will be prompted to install the extension, you will see something like this:

      .. image:: https://raw.githubusercontent.com/AaltoSciComp/aaltoscicomp-graphics/master/figures/tensorboard-vscode.png
         :alt: TensorBoard VS Code Extension
         :width: 300px  
         :align: center

      Once the extension is installed, you can view the profiling results directly in the VS Code interface by launching a TensorBoard session.  


NVIDIA Profilers
^^^^^^^^^^^^^^^^^^

NVIDIA provides a suite of profiling tools designed to help users optimize and analyze the performance of applications running on NVIDIA GPUs. These tools are essential for understanding how applications utilize GPU resources and for identifying bottlenecks in the code.

Overview of NVIDIA Profilers:
"""""""""""""""""""""""""""""""""

Nsight Systems is a system-wide performance analysis tool that provides detailed insights into GPU workloads, CPU workloads, and their interactions. It helps identify issues related to CPU-GPU interaction, GPU utilization, memory bandwidth, and other system-level bottlenecks, such as I/O operations.

Nsight Compute is a GPU kernel profiling tool specifically designed for deep-dive analysis of CUDA kernels. It provides a wide range of performance metrics.

The old profiler nvprof is being deprecated and is no longer recommended for profiling GPU applications. It has been replaced by Nsight Compute and Nsight Systems, which provide a more comprehensive and user-friendly profiling experience. 

Examples
"""""""""""
We have produced some profiling examples.

**To use Nsight Systems**, you need to run:

.. code-block:: console  

   $ module load cuda  
   $ nsys profile -o my_application_report ./my_application  

This will generate a report file called ``my_application_report.qdrep``. To visualize the report on Triton, you can launch a desktop from :doc:`Open Ondemand <../usage/ood>`. In the desktop's terminal, run:

.. code-block:: console

   $ module load cuda qt
   $ nsys-ui

to launch the Nsight Systems GUI. You can then open the report file in the GUI to analyze the performance of your application.

If you want to have a quick overview of the performance of your application, you can add the ``--stats true`` flag to the ``nsys`` command:

.. code-block:: console

   $ nsys profile --stats true -o my_application_report ./my_application

Sample output might look something like this::

   Calculating pi using 1000000000 stochastic trials
   Throws: 785390400/1000000000 Pi: 3.141561508
   Generating '/tmp/nsys-report-dae1.qdstrm'
   [1/8] [========================100%] my_application_report.nsys-rep
   [2/8] [========================100%] my_application_report.sqlite
   [3/8] Executing 'nvtx_sum' stats report
   SKIPPED: /home/username/hpc-examples/slurm/my_application_report.sqlite does not contain NV Tools Extension (NVTX) data.
   [4/8] Executing 'osrt_sum' stats report

 Time (%)  Total Time (ns)  Num Calls   Avg (ns)   Med (ns)   Min (ns)  Max (ns)   StdDev (ns)           Name
 --------  ---------------  ---------  ----------  ---------  --------  ---------  -----------  ----------------------
     67.5        386063524         12  32171960.3  1869947.5      1922  212805298   68194552.0  poll
     31.2        178480955        530    336756.5    15054.0       863   86904639    4568774.8  ioctl
      0.4          2103660         43     48922.3    11494.0      6474     828043     147057.8  mmap64
      0.3          1592392         11    144762.9    38465.0      1054    1057811     310592.0  write
      0.2          1191873          1   1191873.0  1191873.0   1191873    1191873          0.0  pthread_cond_wait
      0.1           668982          2    334491.0   334491.0    153375     515607     256136.7  pthread_create
      0.1           419792         66      6360.5     6045.0      1315      16170       2895.0  open64
      0.1           321168          2    160584.0   160584.0       365     320803     226583.9  pthread_cond_broadcast
      0.0           248340         33      7525.5     4207.0      2493      32380       6793.7  fopen
      0.0           143869         15      9591.3     3959.0      1813      61837      15235.8  mmap
      0.0            62325         27      2308.3     1941.0       961       8547       1660.7  fclose
      0.0            60643         48      1263.4       44.0        42      58482       8434.5  fgets
      0.0            58613         74       792.1      759.5       509       1824        208.7  fcntl
      0.0            35772          6      5962.0     5731.0      2006      12850       3821.8  open
      0.0            26375         14      1883.9     1158.5       655       8367       2022.1  read
      0.0            23330          2     11665.0    11665.0      7532      15798       5844.9  fread
      0.0            22813          3      7604.3     9569.0      3606       9638       3462.8  pipe2
      0.0            21978          5      4395.6     4144.0      2141       6999       1769.5  munmap
      0.0            15134          2      7567.0     7567.0      4708      10426       4043.2  socket
      0.0            10788          1     10788.0    10788.0     10788      10788          0.0  connect
      0.0             4913          7       701.9      720.0       552        973        153.8  dup
      0.0             4911          2      2455.5     2455.5      2180       2731        389.6  fwrite
      0.0             3976         64        62.1       26.0        24        128         40.5  pthread_mutex_trylock
      0.0             2007          1      2007.0     2007.0      2007       2007          0.0  bind
      0.0             1081          1      1081.0     1081.0      1081       1081          0.0  listen

   [5/8] Executing 'cuda_api_sum' stats report

 Time (%)  Total Time (ns)  Num Calls   Avg (ns)   Med (ns)   Min (ns)  Max (ns)   StdDev (ns)           Name
 --------  ---------------  ---------  ----------  ---------  --------  ---------  -----------  ----------------------
     92.4        196623264          3  65541088.0   122225.0      9122  196491917  113406758.7  cudaMalloc
      6.5         13852441          2   6926220.5  6926220.5     68117   13784324    9698823.0  cudaMemcpy
      0.9          1941642          2    970821.0   970821.0     20026    1921616    1344627.2  cudaLaunchKernel
      0.1           300228          3    100076.0   126648.0     13525     160055      76794.0  cudaFree
      0.0             1428          1      1428.0     1428.0      1428       1428          0.0  cuModuleGetLoadingMode

   [6/8] Executing 'cuda_gpu_kern_sum' stats report

 Time (%)  Total Time (ns)  Instances   Avg (ns)    Med (ns)   Min (ns)  Max (ns)  StdDev (ns)                           Name
 --------  ---------------  ---------  ----------  ----------  --------  --------  -----------  -------------------------------------------------------
     85.3         11426785          1  11426785.0  11426785.0  11426785  11426785          0.0  throw_dart(curandStateXORWOW *, int *, unsigned long *)
     14.7          1970581          1   1970581.0   1970581.0   1970581   1970581          0.0  setup_rng(curandStateXORWOW *, unsigned long)

   [7/8] Executing 'cuda_gpu_mem_time_sum' stats report

 Time (%)  Total Time (ns)  Count  Avg (ns)  Med (ns)  Min (ns)  Max (ns)  StdDev (ns)      Operation
 --------  ---------------  -----  --------  --------  --------  --------  -----------  ------------------
     64.3            41055      1   41055.0   41055.0     41055     41055          0.0  [CUDA memcpy DtoH]
     35.7            22784      1   22784.0   22784.0     22784     22784          0.0  [CUDA memcpy HtoD]

   [8/8] Executing 'cuda_gpu_mem_size_sum' stats report

 Total (MB)  Count  Avg (MB)  Med (MB)  Min (MB)  Max (MB)  StdDev (MB)      Operation
 ----------  -----  --------  --------  --------  --------  -----------  ------------------
      0.524      1     0.524     0.524     0.524     0.524        0.000  [CUDA memcpy DtoH]
      0.262      1     0.262     0.262     0.262     0.262        0.000  [CUDA memcpy HtoD]

This output shows that the kernel ``throw_dart`` (part of the Monte Carlo simulation) takes up 88% of the time, while ``setup_rng`` (for setting up random number generators) takes 12%. It is also important to note that in this example memory allocation ``cudaMalloc`` and memory copying ``cudaMemcpy`` used more time than the actual computation. Memory operations are time consuming operations and thus best codes try to minimize the need for doing them.

For more detailed guides on how to use ``nsys``, refer to the    `official NVIDIA documentation <https://docs.nvidia.com/nsight-systems/UserGuide/index.html>`__. 


**To use Nsight Compute**, you need to run:

.. code-block:: console

   $ module load cuda
   $ ncu --target-processes all --set full ./my_application

This command profiles all CUDA kernels in your application, providing a comprehensive set of performance metrics including instruction throughput, memory access efficiency, and occupancy. Nsight Compute generates a report file called ``my_application.ncu-rep``.

Nsight Compute also allows to analyze the performance of specific CUDA kernels.
For example, you can run:

.. code-block:: console

   $ ncu --kernel-name 'myKernel' ./my_cuda_application

to profile a kernel named ``myKernel``,
or 

.. code-block:: console

   $ ncu --kernel-name '^myKernel.*' ./my_cuda_application

to profile all kernels whose names start with ``myKernel``.

Sample output might look something like this:

::

   Calculating pi using 1000000000 stochastic trials
   ==PROF== Connected to process 3944692 (/home/username/hpc-examples/slurm/pi-gpu)
   ==PROF== Profiling "throw_dart": 0%....50%....100% - 19 passes
   Throws: 785390400/1000000000 Pi: 3.141561508
   ==PROF== Disconnected from process 3944692
   [3944692] pi-gpu@127.0.0.1
  throw_dart(curandStateXORWOW *, int *, unsigned long *) (512, 1, 1)x(128, 1, 1), Context 1, Stream 7, Device 0, CC 7.0
    Section: GPU Speed Of Light Throughput
    ----------------------- ------------- ------------
    Metric Name               Metric Unit Metric Value
    ----------------------- ------------- ------------
    DRAM Frequency          cycle/usecond       877.96
    SM Frequency            cycle/nsecond         1.24
    Elapsed Cycles                  cycle     10544719
    Memory Throughput                   %        49.01
    DRAM Throughput                     %         0.04
    Duration                      msecond         8.52
    L1/TEX Cache Throughput             %        73.75
    L2 Cache Throughput                 %        49.01
    SM Active Cycles                cycle   8850096.11
    Compute (SM) Throughput             %        37.09
    ----------------------- ------------- ------------

    OPT   This kernel grid is too small to fill the available resources on this device, resulting in only 0.4 full
          waves across all SMs. Look at Launch Statistics for more details.

    Section: Launch Statistics
    -------------------------------- --------------- ---------------
    Metric Name                          Metric Unit    Metric Value
    -------------------------------- --------------- ---------------
    Block Size                                                   128
    Function Cache Configuration                     CachePreferNone
    Grid Size                                                    512
    Registers Per Thread             register/thread              21
    Shared Memory Configuration Size            byte               0
    Driver Shared Memory Per Block        byte/block               0
    Dynamic Shared Memory Per Block       byte/block               0
    Static Shared Memory Per Block        byte/block               0
    Threads                                   thread           65536
    Waves Per SM                                                0.40
    -------------------------------- --------------- ---------------

    Section: Occupancy
    ------------------------------- ----------- ------------
    Metric Name                     Metric Unit Metric Value
    ------------------------------- ----------- ------------
    Block Limit SM                        block           32
    Block Limit Registers                 block           21
    Block Limit Shared Mem                block           32
    Block Limit Warps                     block           16
    Theoretical Active Warps per SM        warp           64
    Theoretical Occupancy                     %          100
    Achieved Occupancy                        %        39.97
    Achieved Active Warps Per SM           warp        25.58
    ------------------------------- ----------- ------------

    OPT   Estimated Speedup: 60.03%
          This kernel's theoretical occupancy is not impacted by any block limit. The difference between calculated
          theoretical (100.0%) and measured achieved occupancy (40.0%) can be the result of warp scheduling overheads
          or workload imbalances during the kernel execution. Load imbalances can occur between warps within a block
          as well as across blocks of the same kernel. See the CUDA Best Practices Guide
          (https://docs.nvidia.com/cuda/cuda-c-best-practices-guide/index.html#occupancy) for more details on
          optimizing occupancy.

The profiling result suggests that the kernel grid is too small, meaning the workload is not sufficient to fully utilize the GPU's resources. Only 0.4 full waves across all SMs were active, indicating suboptimal GPU utilization. To improve performance, one may need to increase the grid size to better match the GPU's capabilities.

For detailed guides on how to use ``ncu``, refer to the documentation: `NVIDIA Nsight Compute suite <https://docs.nvidia.com/nsight-compute/index.html>`__.

