from utils.other import *
from utils.GeneticAlgortihm import *
import numpy as np

if __name__ == '__main__':

    read_file(c.FILENAME)
    gen_alg = GeneticAlgorithm(c.GENERATION_SIZE)
    gen_alg.work()

    # GeneticAlgorithm
    # generation = create_first_generation(c.POPULATION_SIZE)
    #
    # for population in generation:
    #     print(population)
    # father, mother = generation.rang()

