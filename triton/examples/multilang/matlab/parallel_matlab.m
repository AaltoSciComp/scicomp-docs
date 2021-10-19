try
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
        parpool(c,num_workers);
    end
    % Create matrices to invert
    mat = rand(1000,1000,6);

    parfor i=1:size(mat,3)
    	invMats(:,:,i) = inv(mat(:,:,i))
    end
    % And now, we proceed to build the averages of each set of inverted matrices
    % each time leaving out one.
   
    parfor i=1:size(invMats,3)
    	usedelements = true(size(invMats,3),1)
    	usedelements(i) = false
    	res(:,:,i) = inv(mean(invMats(:,:,usedelements),3));
    end
    % end the program
    exit(0)
catch error
    getReport(error)
    disp('Error occured');
    exit(0)
end

