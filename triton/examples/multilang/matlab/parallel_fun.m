%First, we will initialize the parallel pool using our helper function.
initParPool()

% This is derived from the ga example from the mathworks website.
% Create a function to optimize
ras = @(x, y) 20 + x.^2 + y.^2 - 10*(cos(2*pi*x) + cos(2*pi*y));

% Create optimization variables x and y. Specify that the variables are bounded by .
x = optimvar("x","LowerBound",-100,"UpperBound",100);
y = optimvar("y","LowerBound",-100,"UpperBound",100);

% Create an optimization problem with the created function
prob = optimproblem("Objective",ras(x,y));

% create the options set
options1 = optimoptions("ga","PlotFcn","gaplotbestf");

rng default % For reproducibility
tic
% Solve the problem using ga as the solver.
[sol,fval] = solve(prob,"Solver","ga","Options",options1)
toc
% create new options with useParallel = true
options2 = optimoptions("ga","PlotFcn","gaplotbestf","UseParallel",true);
rng default % For reproducibility
tic
% Solve the problem using ga as the solver.
[sol2,fval2] = solve(prob,"Solver","ga","Options",options2)
toc
exit(0)
