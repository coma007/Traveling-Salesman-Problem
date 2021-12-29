from app.other import *
from app.ga import *

if __name__ == '__main__':

    read_file(c.FILENAME)
    generation = create_first_generation(c.POPULATION_SIZE)
    fitness = calculate_fitness(generation)
    print(fitness)
    for i in range(c.POPULATION_SIZE):
        print(rang(fitness))
