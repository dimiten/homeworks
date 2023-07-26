"""
Napisati funkciju koja od datih listi kreirati novu listu koja sadrzi parne elemente
prve i neparne elemente druge liste i sortirati ih u opadajucem redosledu.
[2,1,66,4,3,87] i [4, 4, 6, 99, 34, 3, 7, 10, -2, -10]
"""


def parni_prve_neparni_druge(lista1, lista2):
    temp_lista = []
    for i in lista1:
        if i % 2 == 0:
            temp_lista.append(i)
    for j in lista2:
        if j % 2 == 1:
            temp_lista.append(j)
    # temp_lista = [2, 66, 4, 99, 3, 7]
    temp_lista.sort(reverse=True)
    return temp_lista


prva_lista = [2, 1, 66, 4, 3, 87]
druga_lista = [4, 4, 6, 99, 34, 3, 7, 10, -2, -10]
print(parni_prve_neparni_druge(prva_lista, druga_lista))

