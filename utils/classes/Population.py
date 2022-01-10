from utils.classes.City import *
import random


class Population(object):

    def __init__(self, members=None):
        if members is None:
            members = []
        self._members = members
        if members is not None:
            self._members.append(self._members[0])
        self._distance = 0
        self.__calculate_distance()
        self._fitness = 0
        self.__calculate_fitness()
        self._normalized_fitness = self._fitness

    def __iter__(self):
        for member in self._members:
            yield member

    def __getitem__(self, key):
        return self._members[key]

    def __setitem__(self, key, value):
        self._members[key] = value
        self.__calculate_distance()
        self.__calculate_fitness()

    def __delitem__(self, key):
        del self._members[key]
        self.__calculate_distance()
        self.__calculate_fitness()

    def __contains__(self, value):
        return value in self._members

    def add(self, new_member):
        self._members.append(new_member)
        self.__calculate_distance()
        self.__calculate_fitness()

    def index(self, member):
        return self._members.index(member)

    def __gt__(self, other):
        return self._normalized_fitness > other.normalized_fitness

    def __eq__(self, other):
        return self._normalized_fitness == other.normalized_fitness

    def __str__(self):
        return f"Population with fitness = {self._normalized_fitness} and distance = {self._distance}"

    @property
    def distance(self):
        return self._distance

    @property
    def fitness(self):
        return self._fitness

    @property
    def normalized_fitness(self):
        return self._normalized_fitness

    @normalized_fitness.setter
    def normalized_fitness(self, new_fitness):
        self._normalized_fitness = new_fitness

    def __calculate_distance(self):
        self._distance = 0
        for i in range(len(self._members)-1):
            self._distance += distance(self[i], self[i+1])

    def __calculate_fitness(self):
        self._fitness = 1/self._distance

    def shuffle(self):
        random.shuffle(self._members)
