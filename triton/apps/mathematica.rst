Using Mathematica on Triton
---------------------------

Login with X support
~~~~~~~~~~~~~~~~~~~~

For a sake of GUI interface, login to triton.aalto.fi with -X, i.e. X11
forwarding enabled.

::

    ssh -X triton.aalto.fi

Load Mathematica through module
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    module load mathematica/10.2

See available versions with 'module avail mathematica'.

Running
~~~~~~~

Run in GUI mode

::

    $ mathematica &

Run in text based mode

::

    $ wolfram

***For the first time runners***, choose 'Other ways to activate'" then
"Connect to a network license server", paste "lic-mathematica.aalto.fi"
(without quotes).
