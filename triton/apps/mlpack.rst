======
MLPack
======

:pagelastupdated: 2014
:supportlevel: C


https://www.mlpack.org/

#. module load cmake; module load armadillo/4.3-mkl; module load mkl
#. mkdir build && cd build
#. cmake -D ARMADILLO\_LIBRARY=$ARMADILLO\_LIBRARY -D
   ARMADILLO\_INCLUDE\_DIR=$ARMADILLO\_INCLUDE ../
#. make
#. bin/mlpack\_test
#. make install CMAKE\_INSTALL\_PREFIX=/share/apps/mlpack/1.0.8

For newer boost library also load boost module and tell cmake where to
find boost

::

    module load boost
    ...
    cmake -D BOOST_ROOT=$BOOST_ROOT -D ARMADILLO_LIBRARY=$ARMADILLO_LIBRARY -D ARMADILLO_INCLUDE_DIR=$ARMADILLO_INCLUDE ../
    ..

Notes
^^^^^

-  1.0.10 installation failed when installing doc to /usr/local (install
   prefix defined ad /share/apps/mlpack/1.0.10). The solution was
   manually tune install prefix at cmake\_install.cmake
