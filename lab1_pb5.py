"""
Pb5. Pentru un șir cu n elemente care conține valori din mulțimea {1, 2, ..., n - 1} astfel încât o
singură valoare se repetă de două ori, să se identifice acea valoare care se repetă.
De ex. în șirul [1,2,3,4,2] valoarea 2 apare de două ori.
"""


def val_duplicata(l1):
    # Complexitate: O(n)
    for index in range(len(l1)):
        if l1[abs(l1[index])] >= 0:
            l1[abs(l1[index])] *= -1
        else:
            return abs(l1[index])


def test():
    assert val_duplicata([1, 2, 3, 4, 2]) == 2
    assert val_duplicata([1, 2, 3, 4, 1, 5]) == 1
    assert val_duplicata([1, 2, 3, 4, 5, 6, 5, 8]) == 5
    assert val_duplicata([2, 1, 7, 4, 3, 6, 5, 7]) == 7


test()
