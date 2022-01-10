import utils.constants as c
from utils.classes.City import *


def read_file(filename):

    with open(filename, "r") as f:
        for line in f.readlines():
            data = line.split()
            c.POINTS.append(City(float(data[1]), float(data[2])))
