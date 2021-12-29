from app.other import *
from app.ga import *

if __name__ == '__main__':

    read_file(c.FILENAME)
    generation = create_first_generation(100)
    generation_fitness = calculate_fitness(generation)
    print(generation_fitness)
