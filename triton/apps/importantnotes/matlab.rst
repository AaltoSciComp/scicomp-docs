.. admonition:: Important notes
   
   Matlab writes session data, compiled code and additional toolboxes to
   ``~/.matlab``. This can quicky fill up your ``$HOME`` quota. To fix this
   we recommend that you replace the folder with a symlink that points to
   a directory in your working directory.

   ::

     rsync -lrt ~/.matlab/ $WRKDIR/matlab-config/ && rm -r ~/.matlab
     ln -sT $WRKDIR/matlab-config ~/.matlab
     quotafix -gs --fix $WRKDIR/matlab-config
          
   If you run parallel code in matlab, keep in mind, that matlab uses your home folder as storage 
   for the worker files, so if you run multiple jobs you have to keep the worker folders seperate    
   To address this, you need to specify the worker location ( the ``JobStorageLocation`` field of the parallel cluster) to a location unique to the job
   
   .. code-block:: matlab
     
     % Initialize the parallel pool
     c=parcluster();
    
     % Create a temporary folder for the workers working on this job, 
     % in order not to conflict with other jobs.
     t=tempname();        
     mkdir(t); 
     
     % set the worker storage location of the cluster               
     c.JobStorageLocation=t;
     
   To address the latter, the number of parallel workers needs to explicitly be provided 
   when initializing the parallel pool::
   
     % get the number of workers based on the available CPUS from SLURM
     num_workers = str2double(getenv('SLURM_CPUS_PER_TASK'));
   
     % start the parallel pool
     parpool(c,num_workers); 
   
   :download:`Here</triton/examples/multilang/matlab/initParPool.m>` we provide a small script, that does all those steps for you.
