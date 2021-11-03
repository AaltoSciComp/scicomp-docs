import pygad
import numpy as np
import os



function_inputs = np.array([4,-2,3.5,5,-11,-4.7])
desired_output = 44

def fitness_func(solution, solution_idx):
    output = np.sum(solution*function_inputs)
    fitness = 1.0 / np.abs(output - desired_output)
    return fitness

# define the parameters

fitness_function = fitness_func

num_generations = 200000
num_parents_mating = 4

sol_per_pop = 100
num_genes = len(function_inputs)

mutation_percent_genes = int(os.getenv('i'))

stop_criteria="saturate_50"

ga_instance = pygad.GA(num_generations=num_generations,
                       num_parents_mating=num_parents_mating,
                       fitness_func=fitness_function,
                       sol_per_pop=sol_per_pop,
                       num_genes=num_genes,
                       mutation_percent_genes=mutation_percent_genes,
                       stop_criteria=stop_criteria)

ga_instance.run()
solution, solution_fitness, solution_idx = ga_instance.best_solution()
print("Parameters of the best solution : {solution}".format(solution=solution))
print("Fitness value of the best solution = {solution_fitness}".format(solution_fitness=solution_fitness))
prediction = np.sum(np.array(function_inputs)*solution)
print("Predicted output based on the best solution : {prediction}".format(prediction=prediction))

