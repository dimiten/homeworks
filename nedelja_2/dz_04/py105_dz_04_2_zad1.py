"""
Napisati funkciju koja će prikazati sve podskupove unetog seta
Primer
Ulaz: {1, 2, 3}
Izlaz: {}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}
"""

from itertools import combinations


def sub_sets(set_):
    list_ = list(set_)
    sublist = []
    for i in range(len(set_) + 1):
        ans = combinations(list_, i)
        for elem in ans:
            sublist.append(set(elem))
    print(sublist)


some_set = {1, 2, 3}
sub_sets(some_set)
