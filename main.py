from app.other import *
from app.ga import *
import numpy as np

if __name__ == '__main__':

    read_file(c.FILENAME)
    population = create_first_generation(c.POPULATION_SIZE)
    distances, fitness = calculate_fitness(population)
    best_fitness = np.min(distances)
    best_route_index = distances.index(best_fitness)
    best_route = population[best_route_index]
    for i in range(c.ITERATION):
        print(best_fitness)
        # print(best_route)
        children = []
        for i in range(c.POPULATION_SIZE):
            fitness1, fitness2 = rang(fitness)
            parent1, parent2 = get_parents(fitness, population, fitness1, fitness2)
            children.append(breed(parent1, parent2))
        children = mutate_population(children, 0.1)
        children_distances, children_fitness = calculate_fitness(children)
        population = next_generation(population, distances, children, children_distances, 0)
        distances, fitness = calculate_fitness(population)
        new_best_fitness = np.min(distances)
        if new_best_fitness > best_fitness:
            best_route_index = distances.index(new_best_fitness)
            best_route = population[best_route_index]
