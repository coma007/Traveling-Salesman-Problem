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
    sum_distance = 0
    normalize_fitness = []
    fitness = []
    for population in generation:
        for i in range(len(population)-1):
            sum_distance += distance(population[i], population[i+1])
        fitness.append(1/sum_distance)
        total_fitness += 1/sum_distance
    for d in fitness:
        normalize_fitness.append(d/total_fitness)
    return normalize_fitness


def rang(fitness):
    fitness.sort()
    scores = {}
    for i in range(len(fitness)):
        scores[(i+1) * random.random()] = fitness[i]
    scores = sorted(scores.items())
    (s1, f1), (s2, f2) = scores[-1], scores[-2]
    return f1, f2

