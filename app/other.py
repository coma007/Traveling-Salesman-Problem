import constants as c
from app.classes.Point import *


def read_file(filename):

    with open(filename, "r") as f:
        for line in f.readlines():
            data = line.split()
            c.POINTS.append(Point(data[1], data[2]))
