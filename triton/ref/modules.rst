.. csv-table::
   :delim: |
   :header-rows: 1

   Command                      | Description
   ``module load`` *NAME*       | load module
   ``module avail``             | list all modules
   ``module spider`` *PATTERN*  | search modules
   ``module spider`` *NAME/ver* | show prerequisite modules to this one
   ``module list``              | list currently loaded modules
   ``module show`` *NAME*       | details on a module
   ``module help`` *NAME*       | details on a module
   ``module unload`` *NAME*     | unload a module
   ``module save`` *ALIAS*      | save module collection to this alias (saved in ``~/.lmod.d/``)
   ``module savelist``          | list all saved collections
   ``module describe`` *ALIAS*  | details on a collection
   ``module restore`` *ALIAS*   | load saved module collection (faster than loading individually)
   ``module purge``             | unload all loaded modules (faster than unloading individually)
