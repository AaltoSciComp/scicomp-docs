function int_parallel()
        try
                tic;
                A = rand(2000,2000);
                A = A + A.';
                B = pinv(A);
                max(max(B * A))
                toc
        catch error
                disp('Error occured');
                exit(0)
        end
end

