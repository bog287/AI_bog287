"""
Pb2.
Să se determine distanța Euclideană între două locații identificate prin perechi de numere.
De ex. distanța între (1,5) și (4,1) este 5.0.
"""

# import cmath.sqrt
from math import sqrt


def test_dist_euclid():
    #teste pt dist_euclid
    assert (dist_euclid(1, 5, 4, 1) == 5)
    assert (dist_euclid(4, 3, 0, 0) == 5)
    assert (dist_euclid(5, 12, 11, 4) == 10)


def dist_euclid(a_x, a_y, b_x, b_y):
    #O(n)
    rez = (sqrt((a_x - b_x) * (a_x - b_x) + (a_y - b_y)*(a_y - b_y)))
    return (rez)


def run():
    a_x = int(input("Introduceti x-ul primei locatii:"))
    a_y = int(input("Introduceti y-ul primei locatii:"))
    b_x = int(input("Introduceti x-ul celeilalte locatii:"))
    b_y = int(input("Introduceti y-ul celeilalte locattii:"))

    print(dist_euclid(a_x, a_y, b_x, b_y))


test_dist_euclid()
run()
