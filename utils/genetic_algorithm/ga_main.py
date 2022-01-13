from utils.genetic_algorithm.ga_methods import *
import numpy as np

import utils.genetic_algorithm.ga_params as param


def genetic_algorithm_work():
    """
    Glavna funkcija genetskog algoritma.

    :return: Najbolja ruta i distanca na toj ruti.
    :rtype: (list[int], float)
    """

    current_generation = create_first_generation(param.GENERATION_SIZE, param.CITIES)
    current_gen_distances, current_gen_fitnesses = calculate_fitness(current_generation)

    best_distance = np.min(current_gen_distances)
    best_route_index = current_gen_distances.index(best_distance)
    best_route = current_generation[best_route_index]

    same_result = 0

    for i in range(param.TOTAL_ITERATIONS):

        print(f"Iteration: #{i}\nBest route: {list(param.CITIES.index(city) for city in best_route)}\nBest distance: {best_distance}\n")
        children = []

        if same_result > param.ITERATION_STOP:
            break

        for j in range(param.GENERATION_SIZE):
            future_parent1_fitness, fitness2 = rang(current_gen_fitnesses)
            parent1, parent2 = get_parents(current_gen_fitnesses, current_generation, future_parent1_fitness, fitness2)
            children.append(breed(parent1, parent2))

        children = mutate_generation(children, param.MUTATION_RATE)
        children_distances, children_fitness = calculate_fitness(children)

        current_generation = next_generation(current_generation, current_gen_distances, children, children_distances,
                                             param.ELITISM_SIZE)
        current_gen_distances, current_gen_fitnesses = calculate_fitness(current_generation)
        new_best_distance = np.min(current_gen_distances)

        if new_best_distance < best_distance:
            best_distance = new_best_distance
            best_route_index = current_gen_distances.index(new_best_distance)
            best_route = current_generation[best_route_index]
            same_result = 0
        else:
            same_result += 1

    return list(param.CITIES.index(city) for city in best_route), best_distance
