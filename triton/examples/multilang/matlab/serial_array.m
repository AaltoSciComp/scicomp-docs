

% set the mutation rate
mutationRate = str2double(getenv('i'))/100;
opts = optimoptions('ga','MutationFcn', {@mutationuniform, mutationRate});

% Set population size and end criteria
opts.PopulationSize = 100;
opts.MaxStallGenerations = 50;
opts.MaxGenerations = 200000;

%set the range for all genes
opts.InitialPopulationRange = [-20;20];

% define number of variables (genes)
numberOfVariables = 6;

[x,Fval,exitFlag,Output] = ga(@fitness,numberOfVariables,[],[],[], ...
    [],[],[],[],opts);

output = [4,-2,3.5,5,-11,-4.7] * x'

function fit = fitness(x)
    output = [4,-2,3.5,5,-11,-4.7] * x';
    fit = abs(output - 44);
end

