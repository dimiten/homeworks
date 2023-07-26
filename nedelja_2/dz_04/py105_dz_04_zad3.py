"""
Napisati fuknciju koja pronalazi unikatne vrednosti u datoj listi tuplova, i ispisati ih na standardnom izlazu.
[(“h”, “g”, “l”, “k”), (“a”, “b”, “d”, “e”, “c”), (“j”, “i”, “y”), (“n”, “b”, “v”, “c”), (“x”, “z”)]
"""


def unikat_lista(lista_tuplova):
    temp_list = []
    for i in lista_tuplova:
        for j in i:
            if j not in temp_list:
                temp_list.append(j)
    return temp_list


lista = [("h", "g", "l", "k"), ("a", "b", "d", "e", "c"), ("j", "i", "y"), ("n", "b", "v", "c"), ("x", "z")]

print(unikat_lista(lista))

