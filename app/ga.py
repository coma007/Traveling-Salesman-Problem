from app.other import *
import random
from copy import deepcopy


def create_first_generation(population_number):
    generation = []
    for i in range(population_number):
        population = deepcopy(c.POINTS)
        random.shuffle(population)
        population.append(population[0])
        generation.append(population)
    return generation


def calculate_fitness(generation):
    total_fitness = 0
    distances = []
    normalize_fitness = []
    fitness = []
    for population in generation:
        sum_distance = 0
        for i in range(len(population)-1):
            sum_distance += distance(population[i], population[i+1])
        distances.append(sum_distance)
        fitness.append(1/sum_distance)
        total_fitness += 1/sum_distance
    for d in fitness:
        normalize_fitness.append(d/total_fitness)
    return distances, normalize_fitness


def rang(fitness):
    fitness.sort()
    scores = {}
    for i in range(len(fitness)):
        scores[(i+1) * random.random()] = fitness[i]
    scores = sorted(scores.items())
    (s1, f1), (s2, f2) = scores[-1], scores[-2]
    return f1, f2


def get_parents(fitness, generation, fitness1, fitness2):
    # a, b = 0, 0
    # while a!=b:
    #     a = random.randint(0, len(generation))
    #     b = random.randint(0, len(generation))
    # parent1 = generation[a]
    # parent2 = generation[b]
    parent1 = generation[fitness.index(fitness1)]
    parent2 = generation[fitness.index(fitness2)]
    return parent1, parent2


def breed(parent1, parent2):
    child_part1 = []
    parent1 = parent1[:-1]
    parent2 = parent2[:-1]
    a = random.randint(0, len(parent1))
    b = random.randint(0, len(parent1))

    start_gene = min(a, b)
    end_gene = max(a, b)

    for i in range(len(parent1)):
        if start_gene <= i <= end_gene:
            child_part1.append(parent1[i])
        else:
            child_part1.append(Point(0, 0))
    # for i in range(start_gene, end_gene):
    #     child_part1.append(parent1[i])
    for elem in parent2:
        if elem not in child_part1:
            i = child_part1.index(Point(0, 0))
            child_part1[i] = elem

    return child_part1


def mutate(individual, mutation_rate):
    # for i in range(len(individual)):
    #     if random.random() < mutation_rate:
    #         swap_index = random.randint(0, len(individual)-1)
    #         individual[i], individual[swap_index] = individual[swap_index], individual[i]
    if random.random() < mutation_rate:
        swap_index1 = random.randint(0, len(individual) - 1)
        swap_index2 = random.randint(0, len(individual) - 1)
        individual[swap_index1], individual[swap_index2] = individual[swap_index2], individual[swap_index1]
    individual.append(individual[0])
    return individual


def mutate_population(population, mutate_rate):
    mutated_population = []
    population_for_mutation = deepcopy(population)
    for individual in population_for_mutation:
        mutated_population.append(mutate(individual, mutate_rate))
    return mutated_population


def next_generation(parents, parents_distances, children, children_distances, elite_size):
    mixed_population = {}
    for i in range(len(parents)):
        mixed_population[parents_distances[i]] = parents[i]
    for i in range(len(children)):
        mixed_population[children_distances[i]] = children[i]
    score = sorted(mixed_population.keys())
    next_gen = []
    for i in range(elite_size):
        if mixed_population[score[i]] in parents:
            next_gen.append(mixed_population[score[i]])
    i = 0
    children_distances_sorted = deepcopy(children_distances)
    children_distances_sorted.sort()
    while len(next_gen) < c.POPULATION_SIZE:
        next_gen.append(children[children_distances.index(children_distances_sorted[i])])
        i += 1
    return next_gen
