"""
Napisati funkciju koja će, na osnovu prosleđenog teksta, odrediti procenat učestalosti
pojavljivanja svakog jedinstvenog karaktera u tom tekstu
Primer
Ulaz: “say hello to my little friend”
Izlaz: {“a”: 3.45, “d”: 3.45, “e”: 10.35, “f”: 3.45, “h”: 3.45, “i”: 6.9, “l”:13.8, …, “ “: 17.24}
"""


def ucestalost_karaktera(tekst):
    temp_dict = {}
    for i in tekst:
        if i in temp_dict:
            temp_dict[i] = round(temp_dict[i] + round(float(1 / len(tekst) * 100), 2), 2)
        else:
            temp_dict[i] = round(float(1 / len(tekst) * 100), 2)
    return temp_dict


tekst = "say hello to my little friend"
print(ucestalost_karaktera(tekst))
