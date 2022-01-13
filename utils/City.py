from math import sqrt


class City(object):
    """
    Klasa City koja modeluje jedan grad.
    """

    def __init__(self, x, y):
        """
        Konstruktor klase City.

        :param x: x koordinata grada.
        :type x: float
        :param y: y koordinata grada.
        :type y: float
        """

        self.x = x
        self.y = y

    def __str__(self):
        return f"(x, y) = ({self.x} ,{self.y})"

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        return False


def distance(pt1, pt2):
    """
    Funkcija racuna udaljenost izmedju dvije tacke.

    :param pt1: Tacka 1
    :type pt1: utils.City.City
    :param pt2: Tacka 2
    :type pt2: utils.City.City
    :return: Udaljenost izmedju gradova.
    :rtype: float
    """
    return sqrt((pt1.x - pt2.x)**2 + (pt1.y - pt2.y)**2)
