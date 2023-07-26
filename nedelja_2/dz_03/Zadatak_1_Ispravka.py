"""
Napisati program koji za svaki uneti broj na izlazu prikazuje delioce tog broja
koji su ujedno i prosti. Unos prestaje kada korisnik unese broj 0.
"""

"""
Komentar - Prvi zadatak - izbegavati mešanje engleskog i srpskog u imenovanju, kao npr is_prost(). 
Za unet prost broj bi takođe trebalo da da radi tako što štampa sam taj broj (on je sam svoj delilac i prost je)
"""


def prost_broj(neki_broj):
    prost = True
    for x in range(2, neki_broj):
        if neki_broj % x == 0:
            return False
    if prost:
        return True


broj = 1
while broj != 0:
    broj = int(input("Unesi broj: "))
    if broj == 1:
        print("1 nije prost broj, a sam je svoj delilac")
        continue
    for delioci in range(2, broj + 1):
        if broj % delioci == 0:
            if prost_broj(delioci):
                print(delioci)
