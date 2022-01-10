from utils.other import *
from utils.classes.Generation import *
import random
from copy import deepcopy


class GeneticAlgorithm(object):

    def __init__(self, population_size):
        self._current_generation = None
        self._best_population = None
        self.__create_first_generation(population_size)

    def work(self):
        pass

    @property
    def current_generation(self):
        return self._current_generation

    def __create_first_generation(self, population_size):
        self._current_generation = Generation()
        for i in range(population_size):
            population = Population(deepcopy(c.POINTS))
            population.shuffle()
            population.add(population[0])
            self._current_generation.add(population)
        self._current_generation.best()
        self._best_population = self._current_generation.best

    def __rang_current_generation(self):
        populations = self._current_generation.populations
        populations.sort()
        scores = {}
        for i in range(len(populations)):
            scores[(i+1) * random.random()] = populations[i]
        scores = sorted(scores.items())
        (score_father, future_father), (score_mother, future_mother) = scores[-1], scores[-2]
        return future_father, future_mother

    def __breed(self, father, mother):
        new_population = Population()
        a = random.randint(0, len(father)-1)
        b = random.randint(0, len(mother)-1)

        start_gene = min(a, b)
        end_gene = max(a, b)

        for i in range(len(father)):
            if start_gene <= i <= end_gene:
                new_population.add(father[i])
            else:
                new_population.add(City(0, 0))
        for elem in mother:
            if elem not in new_population:
                i = new_population.index(City(0, 0))
                new_population[i] = elem

        return new_population
