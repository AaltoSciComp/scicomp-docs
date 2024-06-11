======
Spyder
======

.. admonition:: Warning: page not updated for current Triton
  :class: warning, triton-v2-apps

  This page hasn't been updated since Triton was completely upgraded
  in May 2024.  The software might not be installed and the old
  information below might not work anymore (or  might need adapting).
  If you need this software, :ref:`open an issue <issuetracker>` and
  tell us so we can reinstall/update it.

Spyder is the Scientific PYthon Development
EnviRonment:\ https://www.spyder-ide.org/

On triton there are two modules that provide Spyder:
- The basic scicomp environment module:  ``module load scicomp-python-env`` or
- The neuroimaging environment module: ``module load neuroimaging``

By loading either module you will get access to Spyder.

Using Spyder on Triton
~~~~~~~~~~~~~~~~~~~~~~

To use spyder on triton, you will need an xserver on your local machine 
(in order to display the spyder GUI) e.g. `VcXsrv <https://sourceforge.net/projects/vcxsrv/>`_.
You will further need to connect to triton with X-Forwarding:  
``ssh -X triton.aalto.fi``

Finally, load the module you want to use Spyder from (see above) and run ``spyder``

Use a different environment for Spyder
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you want to use python packages which are not part of the module you use spyder from,
it is strongly to suggested to create a virtual environment (e.g. :doc:`e.g. Conda environments <python-conda>`).
Set up the environment with all packages you want to use. After that, the following steps will make spyder use the environment:

1. Activate your environment
2. Run ``python -c "import sys; print(sys.executable)`` to get the path to the python interpreter in your environment
3. Deactivate the environment
4. Start Spyder
5. In spyder Navigate to "Tools -> Preferences" and select "Python interpreter".
   Under "Use the following Python Interpreter" enter the path from step 2

That will make Spyder use the created python environment.





