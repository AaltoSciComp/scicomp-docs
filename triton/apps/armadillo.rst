=========
Armadillo
=========

.. admonition:: Warning: page not updated for current Triton
  :class: warning, triton-v2-apps

  This page hasn't been updated since Triton was completely upgraded
  in May 2024.  The software might not be installed and the old
  information below might not work anymore (or  might need adapting).
  If you need this software, :ref:`open an issue <issuetracker>` and
  tell us so we can reinstall/update it.

:supportlevel: C

Armadillo http://arma.sourceforge.net/ is C++ linear algebra library
that is needed to support some other software stacks. To get best
performance using MKL as backend is adviced.

The challenge is that default installer does not find MKL from
non-standard location.

#. module load mkl
#. Edit "./build\_aux/cmake/Modules/ARMA\_FindMKL.cmake" and add MKL
   path to "PATHS"
#. Edit "./build\_aux/cmake/Modules/ARMA\_FindMKL.cmake" and replace
   mkl\_intel\_thread with mkl\_sequential (we do not want threaded libs
   on the cluster)
#. Edit "include/armadillo\_bits/config.hpp" and enable
   ARMA\_64BIT\_WORD
#. cmake . && make
#. make install DESTDIR=/share/apps/armadillo/<version>
