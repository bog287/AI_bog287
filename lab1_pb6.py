def elem_maj(l1):
    contor = 0
    candidat = 0
    aparitii = 0
    for index in range(len(l1)):
        if contor == 0:
            candidat = l1[index]
            contor = 1
        else:
            if l1 == candidat:
                contor += 1
            else:
                contor -= 1
    for index in range(len(l1)):
        if l1[index] == candidat:
            aparitii += 1

    if aparitii < int(len(l1) / 2 + 1):
        return -1
    else:
        return candidat


def test():
    assert elem_maj([2, 8, 7, 2, 2, 5, 2, 3, 1, 2, 2]) == 2
    assert elem_maj([3, 4, 3, 4, 3, 4, 3]) == 3
    assert elem_maj([3, 4, 4, 3, 3, 2, 3]) == 3


test()
