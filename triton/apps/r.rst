=
R
=


R is a language and environment for statistical computing and graphics
with wide userbase. There exists several packages that are easily
imported to R.

Getting started
~~~~~~~~~~~~~~~

Simply load the latest R.

::

    module load R/3.3.1-goolf-triton-2016a-libX11-1.6.3
    R

Simple R serial job
~~~~~~~~~~~~~~~~~~~

.. include:: ../examples/r_serial.rst

Simple R job using OpenMP for parallelization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../examples/r_openmp.rst

Simple R parallel job using 'parallel'-package
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../examples/r_parallel.rst

Adding packages
~~~~~~~~~~~~~~~

There are two ways to install packages.

#. Simple way is to put a request to the triton issue tracker and
   mention which R-version you are using.
#. | You may also install packages as a user. Good instructions can be
     found
     `here <http://statistics.berkeley.edu/computing/R-packages>`__
   | Before installing packages you should determine a package location
     for y
   | This should be done as R libs can easily fill your home directory
     quota and loading them from the home directory is very slow.
   | Example is provided below.

   ::

       module load R
       export R_LIBS=$WRKDIR/R/$EBVERSIONR
       mkdir -p $R_LIBS

   Afterwards setting

   ::

       export R_LIBS=$WRKDIR/R/$EBVERSIONR

   after loading R module will point R to the correct library location.
   More info on R library paths can be
   found \ `here <https://stat.ethz.ch/R-manual/R-devel/library/base/html/libPaths.html>`__.
   Looking at
   R \ `startup <https://stat.ethz.ch/R-manual/R-devel/library/base/html/Startup.html>`__
   can also be informative.

Example
~~~~~~~

Below is an example where

-  R is used to run a batch job on the cluster
-  R read a .csv file and generates image output

**Running the R script**

Please note, that R usually is rather IO-hungry. Using Node local
directory is HIGHLY RECOMMEMDED

::

    #!/bin/bash
    #SBATCH -p short
    #SBATCH -t 00:30:00
    #SBATCH -n 1
    #SBATCH -o R_example.out
    # load the R module environment
    module load R/3.3.1-goolf-triton-2016a-libX11-1.6.3

    STARTDIR=$(pwd)

    # use the node local directory
    cd $TMPDIR

    # run the actual R script as a batch job. Make sure the job is not using any graphical display.
    R CMD BATCH test.R

    cp r-transparent.svg $STARTDIR 

test.R used in the example above

::

    stuff<-read.csv('./GreekDramaLength.csv',header=TRUE)
    # or full path to filename in place of file.choose() function
    attach(stuff)
    stuff$Year <- stuff$Year * rep(-1, 31) # years are BC, so make them negative
    library(car)
    svg("r-transparent.svg",bg="transparent",width=5,height=5)
    scatterplot(Word.Count~Year)
    dev.off() # file will be saved in working directory (no screen display)

::

    GreekDramaLength.csv used for dataset in the example

::

    Genre,Author,Play,Year,Doc ID,Word Count
    Tragedy,Euripides,Cyclops,438,1999.01.0093,4104
    Tragedy,Aeschylus,The Suppliants,463,1999.01.0015,4939
    Tragedy,Aeschylus,The Seven Against Thebes,467,1999.01.0013,5115
    Tragedy,Aeschylus,The Persians,472,1999.01.0011,5189
    Tragedy,Aeschylus,Eumenides,458,1999.01.0005,5297
    Tragedy,Euripides,The Suppliants,421,1999.01.0121,5426
    Tragedy,Aeschylus,Libation Bearers,458,1999.01.0007,5447
    Tragedy,Euripides,Heracleidae,428,1999.01.0103,6240
    Tragedy,Euripides,Alcestis,438,1999.01.0087,6603
    Tragedy,Euripides,Trojan Women,415,1999.01.0123,7077
    Tragedy,Sophocles,Ajax,451,1999.01.0183,7177
    Tragedy,Euripides,Hecuba,425,1999.01.0097,7279
    Tragedy,Sophocles,Electra,409,1999.01.0187,7363
    Tragedy,Euripides,Andromanche,427,1999.01.0089,7398
    Tragedy,Euripides,Bacchae,405,1999.01.0091,7597
    Tragedy,Euripides,Electra,413,1999.01.0095,7672
    Tragedy,Euripides,Heracles,422,1999.01.0101,7902
    Tragedy,Sophocles,Antigone,441,1999.01.0185,7914
    Tragedy,Euripides,Medea,431,1999.01.0113,8032
    Tragedy,Euripides,Hippolytus,428,1999.01.0105,8157
    Tragedy,Aeschylus,Agamemnon,458,1999.01.0003,8187
    Tragedy,Euripides,Iphigenia in Tauris,413,1999.01.0111,8396
    Tragedy,Sophocles,Oedipus at Colonus,401,1999.01.0189,8702
    Tragedy,Sophocles,The Trachiniae,409,1999.01.0195,8830
    Tragedy,Euripides,Ion,417,1999.01.0109,9240
    Tragedy,Sophocles,Philoctetes,409,1999.01.0193,9280
    Tragedy,Euripides,Iphigenia in Aulis,405,1999.01.0107,9430
    Tragedy,Euripides,Phoenician Women,410,1999.01.0117,9879
    Tragedy,Euripides,Helena,412,1999.01.0099,9927
    Tragedy,Euripides,Orestes,408,1999.01.0115,10030
    Tragedy,Sophocles,Oedipus Rex,409,1999.01.0191,10385
