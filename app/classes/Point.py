from math import sqrt


class Point(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"(x, y) = ({self.x} ,{self.y})"


def distance(pt1, pt2):
    return sqrt((pt1.x + pt2.x)**2 + (pt1.y + pt2.y)**2)
