"""
Napisati fuknciju koja prolazi kroz listu i proverava da li su svi elementi istog tipa unutar liste,
ako jesu, funkcija vraca True, ako nisu vraca False.
"""


def tip_elem_liste(lista):
    tip_elementa = type(lista[0])
    svi_istog_tipa = True
    for i in range(len(lista)):
        if type(lista[i]) != tip_elementa:
            svi_istog_tipa = False
            break
    if svi_istog_tipa:
        return True
    else:
        return False


lista1 = [1, 4, 7, 321, 56, "c"]
lista2 = ["a", 5, True, 'b']
print(tip_elem_liste(lista1))
print(tip_elem_liste(lista2))
