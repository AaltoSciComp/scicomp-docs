.. csv-table::
   :delim: |
   :header-rows: 1

   Command / concept            | Description
   "module"                     | A software that can be made available.
   "software stack"             | Includes the compliers (etc) needed for other modules.  Must be loaded before other modules.
   ``module load`` *NAME*       | Load module, can combine multiple names.
   ``module load`` triton/*NAME* | Load software stack module.  Makes other compiled software available.  Generally, run ``module spider`` to first to see what you need.
   ``module avail``             | List all modules available with current software stack.
   ``module spider`` *PATTERN*  | Search modules
   ``module spider`` *NAME/ver* | Show prerequisite modules (the softare stack) to this one
   ``module list``              | List currently loaded modules
   ``module show`` *NAME*       | Details on a module
   ``module help`` *NAME*       | Details on a module
   ``module unload`` *NAME*     | Unload a module
   ``module save`` *ALIAS*      | Save module collection to this alias (saved in ``~/.lmod.d/``)
   ``module savelist``          | List all saved collections
   ``module describe`` *ALIAS*  | Details on a collection
   ``module restore`` *ALIAS*   | Load saved module collection (faster than loading individually)
   ``module purge``             | Unload all loaded modules (faster than unloading individually)
