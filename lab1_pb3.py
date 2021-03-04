def test():
    assert produs_rar([1, 0, 2, 0, 3], [1, 2, 0, 3, 1]) == 4
    assert produs_rar([0, 0, 0, 0, 1], [1, 1, 1, 0, 0]) == 0


def produs_rar(l1, l2):
    # complexitate: O(n)
    s = 0
    e1 = 0
    while e1 < len(l1):
        if l1[e1] == 0 or l2[e1] == 0:
            l1.pop(e1)
            l2.pop(e1)
            e1 -= 1
            if e1 == -1:
                e1 += 1
        else:
            e1 += 1

    for e1, e2 in zip(l1, l2):
        s += e1 * e2
    return s


test()
