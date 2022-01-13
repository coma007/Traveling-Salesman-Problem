import random
from copy import deepcopy

from utils.City import *


def create_first_generation(population_number, individuals):
    """
    Funkcija pravi prvu generaciju.

    :param population_number: Broj jedinki u populaciji.
    :type population_number: int
    :param individuals: Sve jedinke u sistemu.
    :type individuals: list[utils.City.City]
    :return: Prva generacija jedinki.
    :rtype: list[list[utils.City.City]]
    """
    generation = []
    for i in range(population_number):
        population = deepcopy(individuals)
        random.shuffle(population)
        population.append(population[0])
        generation.append(population)
    return generation


def calculate_fitness(population):
    """
    Funkcija racuna fitnes pojedinacnih jedinki u populaciji i ukupan fitnes populacije, te normalizuje fitnese pojedinacnih jedinki.

    :param population: Populacija.
    :type population: list[list[utils.City.City]]
    :return: Lista svih udaljenosti i lista svih fitnesa jedinki u populacija.
    :rtype: (list[float], list[float])
    """
    total_fitness = 0
    distances = []
    normalize_fitness = []
    fitness = []
    for population in population:
        sum_distance = 0
        for i in range(len(population) - 1):
            sum_distance += distance(population[i], population[i + 1])
        distances.append(sum_distance)
        fitness.append(1 / sum_distance)
        total_fitness += 1 / sum_distance
    for d in fitness:
        normalize_fitness.append(d / total_fitness)
    return distances, normalize_fitness


def rang(fitness):
    """
    Funkcija rangira jedinke prema fitnesu, a zatim vrsi ruletsku selekciju buducih roditelja.

    :param fitness: Lista svih fitnesa u populaciji.
    :type fitness: list[float]
    :return: Fitnesi buducih roditelja.
    :rtype: (float, float)
    """
    fitness_copy = deepcopy(fitness)
    fitness_copy.sort()
    scores = {}
    for i in range(len(fitness)):
        scores[(i + 1) * random.random()] = fitness_copy[i]
    scores = sorted(scores.items())
    (s1, f1), (s2, f2) = scores[-1], scores[-2]
    return f1, f2


def get_parents(fitness, population, fitness1, fitness2):
    """
    Funkcija dobavlja roditeljske populacije na osnovu njihovih fitnesa.

    :param fitness: Lista svih fitnesa u populaciji.
    :type fitness: list[float]
    :param population: Citava populacija.
    :type population: list[list[utils.City.City]]
    :param fitness1: Fitnes prvog roditelja.
    :type fitness1: float
    :param fitness2: Fitnes drugog roditelja.
    :type fitness2: float
    :return: Buduci roditelji.
    :rtype: (list[utils.City.City], list[utils.City.City])
    """
    parent1 = population[fitness.index(fitness1)]
    parent2 = population[fitness.index(fitness2)]
    return parent1, parent2


def breed(parent1, parent2):
    """
    Funkcija za ukrstanje dva roditelja, odnosno stvaranje djeteta.

    :param parent1: Prvi roditelj.
    :type parent1: list[utils.City.City]
    :param parent2: Drugi roditelj.
    :type parent2: list[utils.City.City]
    :return: Dijete.
    :rtype: list[utils.City.City]
    """
    child = []
    parent1 = parent1[:-1]
    parent2 = parent2[:-1]
    a = random.randint(0, len(parent1))
    b = random.randint(0, len(parent1))

    start_gene = min(a, b)
    end_gene = max(a, b)

    for i in range(len(parent1)):
        if start_gene <= i <= end_gene:
            child.append(parent1[i])
        else:
            child.append(City(0, 0))
    for elem in parent2:
        if elem not in child:
            i = child.index(City(0, 0))
            child[i] = elem

    return child


def mutate_individual(individual, mutation_rate):
    """
    Funkcija mutira jedinku.

    :param individual: Jedinka koja se mutira.
    :type individual: list[utils.City.City]
    :param mutation_rate: Stepen mutacije.
    :type mutation_rate: float
    :return: Mutirana jedinka.
    :rtype: list[utils.City.City]
    """
    if random.random() < mutation_rate:
        swap_index1 = random.randint(0, len(individual) - 1)
        swap_index2 = random.randint(0, len(individual) - 1)
        individual[swap_index1], individual[swap_index2] = individual[swap_index2], individual[swap_index1]
    individual.append(individual[0])
    return individual


def mutate_population(population, mutation_rate):
    """
    Funkcija mutira populaciju.

    :param population: Populacija koja se mutira.
    :type population: list[list[utils.City.City]]
    :param mutation_rate: Stepen mutacije.
    :type mutation_rate: float
    :return: Mutirana populacija.
    :rtype: list[list[utils.City.City]]
    """
    mutated_generation = []
    generation_for_mutation = deepcopy(population)
    for individual in generation_for_mutation:
        mutated_generation.append(mutate_individual(individual, mutation_rate))
    return mutated_generation


def next_generation(parents, parents_distances, children, children_distances, elite_size):
    """
    Funkcija kreira novu generaciju na osnovu populacije trenutne generacije i populacije dobijene ukrstanjima u trenutnoj generaciji.

    :param parents: Populacija trenutne generacije.
    :type parents: list[list[utils.City.City]]
    :param parents_distances: Lista svih udaljenosti unutar populacije trenutne generacije.
    :type parents_distances: list[float]
    :param children: Populacija dobijena ukrstanjem unutar jedinki iz trenutne generacije.
    :type children: list[list[utils.City.City]]
    :param children_distances: Lista svih udaljenosti unutar populacije dobijene ukrstanjem.
    :type children_distances: list[float]
    :param elite_size: Elitizam.
    :type elite_size: int
    :return: Nova generacija.
    :rtype: list[list[utils.City.City]]
    """
    mixed_generation = {}
    for i in range(len(parents)):
        mixed_generation[parents_distances[i]] = parents[i]
    for i in range(len(children)):
        mixed_generation[children_distances[i]] = children[i]
    score = sorted(mixed_generation.keys())
    next_gen = []
    for i in range(elite_size):
        if mixed_generation[score[i]] in parents:
            next_gen.append(mixed_generation[score[i]])
    i = 0
    children_distances_sorted = deepcopy(children_distances)
    children_distances_sorted.sort()
    while len(next_gen) < len(parents):
        next_gen.append(children[children_distances.index(children_distances_sorted[i])])
        i += 1
    return next_gen
