"""Napisati program koji za svaki uneti celi broj određuje da li uneti broj sadrži
više parnih ili neparnih cifara. Unos prekinuti nakon što korisnik unese broj
čije su sve cifre parne ili sve cifre neparne. Napomena: Ne koristiti operacije
nad stringovima, već brojevima!"""

broj_parnih = 0
broj_neparnih = 0
brojac = 0

while brojac != 1:
    broj = int(input("Unesi broj: "))

    while broj != 0:
        cifre = broj % 10
        broj = broj // 10
        #print(cifre)
        if cifre % 2 == 0:
            broj_parnih += 1
        else:
            broj_neparnih += 1

    if broj_parnih == 0:
        print("Sve cifre su neparne. Kraj programa.")
        brojac += 1
    elif broj_neparnih == 0:
        print("Sve cifre su parne. Kraj programa.")
        brojac += 1
    elif broj_parnih > broj_neparnih:
        print("Broj ima vise parnih cifara!")
    elif broj_parnih < broj_neparnih:
        print("Broj ima vise neparnih cifara!")
    elif broj_parnih == broj_neparnih:
        print("Broj ima isti broj parnih i neparnih cifara!")

    broj_parnih = 0
    broj_neparnih = 0














