.. admonition:: Important notes
          
   Matlab tends to use as many cores as it can get, and often ignores limitations imposed by the assigned resources. 
   This causes unnecessary load on the scheduler and slows down computation. Therefore, by default matlab is run in 
   singlethreaded mode on the cluster. To use multiple cores you have to run matlab using the ``matlab_multithread``
   executable. There are two more issues: 
   
   1. When running multiple parallel jobs, MATLAB worker files can overlap and 
   2. MATLAB cannot determine the correct number of allocated cores.
   
   To address the former, you need to specify the worker location ( the ``JobStorageLocation`` field of the parallel cluster)
   to a location unique to the job::
   
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
  

