=======
RStudio
=======

:supportlevel: C
:pagelastupdated: 2014


https://www.rstudio.com/ is an IDE for R

::

    module load R/3.1.1-openblas boost/1.56 cmake/2.8.12.2 gcc/4.9.1 PrgEnv-gnu/0.1 qt/4.8.6

    mkdir build && cd build
    cmake .. -DRSTUDIO_TARGET=Desktop -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/share/apps/rstudio/0.98/ -DBOOST_ROOT=$BOOST_ROOT

..
  mkdir build
  cd build

  ml load cmake
  ml load boost
  yum install pam-devel
  ml load R
  ml load r-uuid
