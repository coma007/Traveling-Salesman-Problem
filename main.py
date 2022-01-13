from utils.genetic_algorithm.ga_main import *

__authors__ = "Nemanja Dutina - SV 27/2020, Milica Sladakovic SV 18/2020"
__project__ = "Problem putujuceg trgovca - Genetski algoritam"
__course__ = "Nelinearno programiranje i evolutivni algoritmi"


def read_file(filename):
    """
    Funkcija cita podatke iz fajla i unosi ih u listu jedinki.
    :param filename: Naziv fajla.
    :type filename: str
    """

    with open(filename, "r") as f:
        for line in f.readlines():
            data = line.split()
            param.CITIES.append(City(float(data[1]), float(data[2])))


if __name__ == '__main__':

    read_file("data_tsp.txt")
    best_route, best_distance = genetic_algorithm_work()
    print(f"\n\nNAJBOLJA RUTA: {best_route}\nDISTANCA: {best_distance}")
