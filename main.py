from utils.other import *
from utils.ga import *
import numpy as np

if __name__ == '__main__':

    read_file(c.FILENAME)

    population = create_first_generation(c.GENERATION_SIZE)
    distances, fitness = calculate_fitness(population)
    print(fitness)
    best_distance = np.min(distances)
    best_route_index = distances.index(best_distance)
    best_route = population[best_route_index]
    #sredjeno
    for i in range(c.ITERATION):
        print(best_distance)
        # print(best_route)
        children = []
        for i in range(c.GENERATION_SIZE):
            fitness1, fitness2 = rang(fitness)
            parent1, parent2 = get_parents(fitness, population, fitness1, fitness2)
            children.append(breed(parent1, parent2))
            # sredjen ovaj pod for

        children = mutate_population(children, 0.2)
        children_distances, children_fitness = calculate_fitness(children)
        population = next_generation(population, distances, children, children_distances, 0)
        distances, fitness = calculate_fitness(population)
        new_best_distance = np.min(distances)
        if new_best_distance < best_distance:
            best_distance = new_best_distance
            best_route_index = distances.index(new_best_distance)
            best_route = population[best_route_index]
