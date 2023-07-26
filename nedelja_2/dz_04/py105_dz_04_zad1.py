from itertools import combinations
"""
Napisati funkciju koja generise sub-liste iz prosledjene liste
Primer:
Lista = [10,20,30,40]
Sublist =  [[],[10],[20],[30],[40].[10,20],[10,30]...[10,20,30,40] ]
"""


def sub_lists(my_list):
    subs = []
    for i in range(len(my_list) + 1):
        ans = combinations(my_list, i)
        for elem in ans:
            subs.append(list(elem))
    print(subs)


lista = [10, 20, 30]
sub_lists(lista)

