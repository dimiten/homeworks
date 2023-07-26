"""
Napisati funkcije koja kao argumente primaju dve liste, a vracaju listu koja predstavlja presek/razliku tih listi.
Primer razlike:
Lista1=[10,20,30,40]
Lista2=[10,30,50,70]
Izlazna_lista = [20,40,50,70]
Primer preseka:
Lista1=[10,20,30,40]
Lista2=[10,30,50,70]
Izlazna_lista = [10,30]
"""


def razlika_dve_liste(lista1, lista2):
    temp_list = []
    for i in lista1:
        if i not in lista2:
            temp_list.append(i)
    for j in lista2:
        if j not in lista1:
            temp_list.append(j)
    return temp_list


def presek_dve_liste(lista1, lista2):
    temp_list = []
    for i in lista1:
        if i in lista2:
            temp_list.append(i)
    return temp_list


prva_lista = [10, 20, 30, 40]
druga_lista = [10, 30, 50, 70]

print(f"Razlika dve liste je: {razlika_dve_liste(prva_lista, druga_lista)}")

print(f"Presek dve liste je : {presek_dve_liste(prva_lista, druga_lista)}")
