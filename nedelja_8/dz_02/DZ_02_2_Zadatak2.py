"""Napisati program za izračunavanje i štampanje računa u piceriji. Svaka porudžbina sadrži samo jednu picu.

Pica može biti u veličinama S(500 RSD), M(650 RSD) ili L(770 RSD).
Svaki račun sadrži i stavku naknade za dostavu. Dostava košta 109 RSD.
U slučaju da su vremenski uslovi loši (izraziti verovatnoćom od 35%), uračunava se se dodatni iznos od 50 RSD).

Ukoliko je ukupan iznos računa iznad 800 RSD,
cena dostave se umanjuje za 20% (ovo umanjenje se ne odnosi na dodatak za loše vremenske uslove).
Napomena: Koristiti funkciju random() za implementaciju verovatnoće.
Prilagoditi zadatak sa picerijom tako da račun može da sadrži više pica."""

import random

pice = {
    "s": 500,
    "m": 650,
    "l": 770}

verovatnoca = random.randint(1, 100)

dodatni_iznos = 0
if verovatnoca <= 35:
    dodatni_iznos = 50
    print("Vreme je lose")
else:
    print("Vreme je dobro")

dostava = 109
ukupna_cena_pica = 0

while True:
    unos = input("Izaberite picu: s, m ili l: ")
    if unos in pice:
        unos = pice[unos]
    else:
        print("Nepostojeca velicina ili pogresan karakter")

    # print(unos)

    broj_pica = int(input("Izaberite broj pica: "))

    cena_pica = unos * broj_pica

    ukupna_cena_pica = ukupna_cena_pica + cena_pica

    pitanje = input("Da li zelite jos nesto?: ")

    if pitanje == "da":
        continue
    elif pitanje == "ne":
        break

if ukupna_cena_pica + dostava + dodatni_iznos > 800:
    cena_racuna = ukupna_cena_pica + dostava * 0.8 + dodatni_iznos
else:
    cena_racuna = ukupna_cena_pica + dostava * 0.8 + dodatni_iznos


print("Cena Vaseg racuna je {} dinara." .format(cena_racuna))
