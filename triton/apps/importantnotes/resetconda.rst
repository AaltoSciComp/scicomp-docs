.. admonition:: Resetting conda
   :class: toggle

   Sometimes it is necessary to reset your Conda configuration. So here are instructions on how to wipe all
   of your conda settings and existing environments. To be able to do so first load the miniconda environment 

   .. code-block:: bash
   
      module load miniconda

   First, check where conda stores your environments:

   .. code-block:: bash
   
     conda config --show env_dirs     
     conda config --show pkgs_dirs
     
   Delete the directories that are listed and start with ``/home/<username>`` (this could e.g. be ``/home/<username>/.conda/envs``)
   and ``/scratch/`` ( e.g. ``/scratch/work/<userame>/conda_envs``). 
   This will clean up all packages and environments you have installed. 
   
   Next, clean up your ``.bashrc``, ``.zshrc``, ``.kshrc`` and ``.cshrc`` (or all of those that exist).
   Open these files in an editor (e.g. ``nano bashrc``) and search for the line ``# >>> conda initialize >>>``
   delete everything between this line and the line ``# <<< conda initialize <<<``. These lines automatically
   initilize conda upon login which can cause a lot of trouble on a cluster.

   Finally delete the file ``.condarc`` from your home folder ( ``~/.condarc``) to reset your conda configuration.
   After this close the current connection to triton and reconnect in a new session. 

   Now you should have a system that doesn't have any remains off conda, so you can now follow the initial steps as detailed 
   `here <conda-first-time-setup>`.

