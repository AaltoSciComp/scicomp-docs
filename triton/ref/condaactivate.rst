.. admonition:: ``conda init``, ``conda activate``, and ``source activate``
   :class: toggle

   We don't recommend doing ``conda init`` like many sources
   recommend: this will *permanently* affect your ``.bashrc`` file and
   make hard-to-debug problems later.  The main points of ``conda
   init`` are to a) automatically activate an environment (not good on
   a cluster: make it explicit so it can be more easily debugged)
   and b) make ``conda`` a shell function (not command) so that
   ``conda activate`` will work (``source activate`` works as well in
   all cases, no confusion if others don't.)

   - If you activate one environment from another, for example after
     loading an miniconda module, do ``source activate ENV_NAME`` like
     shown above (conda installation in the environment not needed).

   - If you make your own standalone conda environments, install the
     ``conda`` package in them, then...

   - Activate a standalone environment with conda installed in it by
     ``source PATH/TO/ENV_DIRECTORY/bin/activate`` (which incidentally
     activates just that one session for conda).



