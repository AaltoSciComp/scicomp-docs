.. admonition:: Important notes
          
   There is an issue, when running multiple jobs using MATLAB workers in a parpool. 
   When running multiple parallel jobs, MATLAB worker files can overlap which can, best case, 
   lead to job(s) failing, and worst case cause wrong data to be used in a job.     
   To address this, you need to specify the worker location ( the ``JobStorageLocation`` field of the parallel cluster) to a location unique to the job::
   
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
