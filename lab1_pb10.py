"""
Pb 10.
Considerându-se o matrice cu n x m elemente binare (0 sau 1) sortate crescător pe linii, să se
identifice indexul liniei care conține cele mai multe elemente de 1.
De ex. în matricea
[[0,0,0,1,1],
[0,1,1,1,1],
[0,0,1,1,1]]
a doua linie conține cele mai multe elemente 1.

Complexitate : nlog(m)
"""

def cmm1(linie):
    #input: 
    st = 0
    dr = len(linie) - 1
    for index in range(len(linie)):
        while st <= dr:

            mij = int((st + dr) / 2)

            # mij este index-ul primului 1
            if linie[mij] == 1 and (mij == 0 or linie[mij - 1] == 0):
                return mij

                # primul 1 este la stanga mijlocului
            elif linie[mij] == 1:
                dr = mij - 1

            # primul 1 este la dreapta mijlocului
            else:
                st = mij + 1

            # 1 nu este pe linie
        return -1


def test():
    assert cmm1([0, 0, 0, 1, 1]) == 3
    assert cmm1([0, 0, 1, 1, 1]) == 2
    assert cmm1([0, 0, 0, 0, 1, 1, 1, 1]) == 4
    assert max_1([[0, 0, 0, 1, 1], [0, 1, 1, 1, 1], [0, 0, 1, 1, 1]]) == 2


def max_1(matrice):
    maxx = -2
    for linie in range(len(matrice)):
        if maxx < len(matrice[linie]) - cmm1(matrice[linie]):
            maxx = cmm1(matrice[linie])
    return maxx


test()
