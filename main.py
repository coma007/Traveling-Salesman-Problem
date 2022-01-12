from app.other import *
from app.ga import *
import numpy as np

if __name__ == '__main__':

    same_result = 0
    read_file(c.FILENAME)
    population = create_first_generation(c.POPULATION_SIZE)
    distances, fitness = calculate_fitness(population)
    best_distance = np.min(distances)
    best_route_index = distances.index(best_distance)
    best_route = population[best_route_index]
    for i in range(c.ITERATION):
        if same_result > c.ITERATION_STOP:
            break
        print(best_distance)
        # print(best_route)
        children = []
        for i in range(c.POPULATION_SIZE):
            fitness1, fitness2 = rang(fitness)
            parent1, parent2 = get_parents(fitness, population, fitness1, fitness2)
            children.append(breed(parent1, parent2))
        children = mutate_population(children, c.MUTATION_RATE)
        children_distances, children_fitness = calculate_fitness(children)
        population = next_generation(population, distances, children, children_distances, c.ELITISM_SIZE)
        distances, fitness = calculate_fitness(population)
        new_best_distance = np.min(distances)
        if new_best_distance < best_distance:
            best_distance = new_best_distance
            best_route_index = distances.index(new_best_distance)
            best_route = population[best_route_index]
            same_result = 0
        else:
            same_result += 1