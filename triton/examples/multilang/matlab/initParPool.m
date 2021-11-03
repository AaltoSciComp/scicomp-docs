function initParPool()
% initializes a parallel pool on a slurm cluster using the correct number
% of workers based on the SLURM_CPU_PER_TASK environment variable.

% Check, whether there is already an open parallel pool, in order to avoid
% creating a new one.
parpoolOn = ~isempty(gcp('nocreate'));
% Try-catch expression that quits the Matlab session if your code crashes
if  ~parpoolOn
    % get the number of workers based on the available CPUS 
    num_workers = str2double(getenv('SLURM_CPUS_PER_TASK'));
    
    % Initialize the parallel pool
    c=parcluster();
    
    % Create a temporary folder for the workers working on this job, 
    % in order not to conflict with other jobs.
    t=tempname();        
    mkdir(t);           
    c.JobStorageLocation=t;
    
    % start the parallel pool
    parpool(c,num_workers);
end
