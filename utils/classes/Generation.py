from utils.classes.Population import *


class Generation(object):

    def __init__(self, populations=None):
        if populations is None:
            populations = []
        self._populations = populations
        self._total_fitness = 0
        self._best = None
        self.__calculate_total_fitness()
        self.__normalize_fitnesses()

    def __iter__(self):
        for population in self._populations:
            yield population

    def __getitem__(self, key):
        return self._populations[key]

    def __setitem__(self, key, value):
        self._populations[key] = value
        self.__calculate_total_fitness()
        self.__normalize_fitnesses()
        self.__find_best()

    def __delitem__(self, key):
        del self._populations[key]
        self.__calculate_total_fitness()
        self.__normalize_fitnesses()
        self.__find_best()

    def __contains__(self, value):
        return value in self._populations

    def add(self, new_population):
        self._populations.append(new_population)
        self.__calculate_total_fitness()
        self.__normalize_fitnesses()
        self.__find_best()

    def index(self, population):
        return self._populations.index(population)

    def __str__(self):
        return f"Generation with best population: {self._best}"

    @property
    def best(self):
        return self._best

    def __calculate_total_fitness(self):
        self._total_fitness = 0
        for population in self._populations:
            self._total_fitness += population.fitness

    def __normalize_fitnesses(self):
        for population in self._populations:
            population.normalized_fitness = population.fitness/self._total_fitness

    def __find_best(self):
        self._best = self._populations[0]
        for population in self._populations:
            if population.fitness > self._best.fitness:
                self._best = population

