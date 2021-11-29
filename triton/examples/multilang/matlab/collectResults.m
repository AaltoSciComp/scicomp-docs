function collectResults(maxMutationRate) 
   X=1:maxMutationRate
   Y=zeros(maxMutationRate,1);
   for index=1:maxMutationRate
      % read the output from the jobs
      filename = strcat( 'MutationJob', int2str( index ) );
      load( filename );

      Y(index)=output; 
   end 
   plot(X,Y,'b+:')

