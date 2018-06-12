function parpool_parallel(n)
        % Try-catch expression that quits the Matlab session if your code crashes
        try
                % Initialize the parallel pool
                c=parcluster();
                t=tempname()
                mkdir(t)
                c.JobStorageLocation=t;
                parpool(c,n);
                % The actual program calls from matlab's example.
                % The path for r2017b
                addpath(strcat(matlabroot, '/examples/distcomp/main'));
                % The path for r2016b
                % addpath(strcat(matlabroot, '/examples/distcomp'));

                % simulate 10000 blackjack hands with 100 players
                tic;
                pctdemo_aux_parforbench(10000,100,n);
                toc
        catch error
                getReport(error)
                disp('Error occured');
                exit(0)
        end
end

