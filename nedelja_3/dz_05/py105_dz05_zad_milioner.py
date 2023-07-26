"""Napisati program za igranje kviza “Želite li da postanete milioner?
a. Napisati funkciju za unos podataka igraca
b. Napisati funkciju koja ce na osnovu broja pitanja iz liste pitanja (postoji jedinstvena lista za
pitanja od 1-5 (laksa), 6-10(srednja) i 11-15(teska)) random postaviti pitanje i odgovore igracu.
Nije dozvoljeno jednom igracu postaviti ista pitanja.
c. Napisati funkciju za pomoc pola pola
d. Napisati funkciju za pomoc zamena pitanja (nije dozvoljeno postaviti isto pitanje)
e. Napisati funkciju za pomoc pitaj publiku (Sto je teze pitanje, manja je sansa da publika da
tacan odgovor, svaki odgovor ima procentualno koliko je publike glasalo da je to tacan
odgovor)
f. Napisati funkciju za davanje odgovora (a, b, c, d, ODUSTAJEM)
g. Napisati funkciju koja ce na osnovu datog odgovora odrediti da li se igracu postavlja sledece
pitanje, ili se vraca na zagarantovanu sumu (5. pitanje, 10. pitanje)
h. Napisati funkciju koja ce na kraju igre prikazati koliko je novca osvojio takmicar
Objediniti sve ove funkcije i omoguciti igracu da igra."""


import random


def unos_podataka(takmicar_dict):
    ime_ = input("Vase ime: ")
    takmicar_dict["ime"] = ime_
    prezime_ = input("Vase prezime: ")
    takmicar_dict["prezime"] = prezime_
    return takmicar_dict


def postavljanje_pitanja(pitanja, takmicar_dict):
    trenutno_pitanje = takmicar_dict.get("trenutno_pitanje")
    if trenutno_pitanje <= 5:
        pitanje = pitanja.get("laka")
    elif trenutno_pitanje <= 10:
        pitanje = pitanja.get("srednja")
    else:
        pitanje = pitanja.get("teska")

    rand_faktor = random.randrange(len(pitanje))
    postavljeno_pitanje = pitanje.pop(rand_faktor)
    tacan_odgovor = postavljeno_pitanje.get("odgovori")[0].get("tekst")
    random.shuffle(postavljeno_pitanje.get("odgovori"))
    print(postavljeno_pitanje.get("pitanje"))
    print("a)", postavljeno_pitanje.get("odgovori")[0].get("tekst"))
    print("b)", postavljeno_pitanje.get("odgovori")[1].get("tekst"))
    print("c)", postavljeno_pitanje.get("odgovori")[2].get("tekst"))
    print("d)", postavljeno_pitanje.get("odgovori")[3].get("tekst"))
    return tacan_odgovor


def davanje_odgovora():
    print("Ako zelite da odustanete odgovorite: ODUSTANI")
    odgovor = input("Vas odgovor je: ")
    return odgovor


def provera_odgovora():
    odgovor = davanje_odgovora()
    if odgovor == postavljanje_pitanja(pitanja, takmicar):
        takmicar["osvojeni_novac"] = vrednost_pitanja.get(str(takmicar["trenutno_pitanje"])).get("vrednost")
        if vrednost_pitanja.get(str(takmicar["trenutno_pitanje"])).get("zagarantovana"):
            takmicar["zagarantovana_suma"] = vrednost_pitanja.get(str(takmicar["trenutno_pitanje"])).get("vrednost")
        takmicar["trenutno_pitanje"] += 1
        print("Tacan odgovor")
        return 1
    else:
        print("Kraj igre")
        print("Zagarantovana suma je: ", takmicar.get("zagarantovana_suma"))
        return 0





laka_pitanja = [
    {"pitanje": "Pitanje_1?",
     "odgovori": [{"tekst": "Odg1", "da_li_je_tacno": True}, {"tekst": "Odg2", "da_li_je_tacno": False},
                  {"tekst": "Odg3", "da_li_je_tacno": False}, {"tekst": "Odg4", "da_li_je_tacno": False}]},
    {"pitanje": "Pitanje_2?",
     "odgovori": [{"tekst": "Odg1", "da_li_je_tacno": True}, {"tekst": "Odg2", "da_li_je_tacno": False},
                  {"tekst": "Odg3", "da_li_je_tacno": False}, {"tekst": "Odg4", "da_li_je_tacno": False}]},
    {"pitanje": "Pitanje_3?",
     "odgovori": [{"tekst": "Odg1", "da_li_je_tacno": True}, {"tekst": "Odg2", "da_li_je_tacno": False},
                  {"tekst": "Odg3", "da_li_je_tacno": False}, {"tekst": "Odg4", "da_li_je_tacno": False}]},
    {"pitanje": "Pitanje_4?",
     "odgovori": [{"tekst": "Odg1", "da_li_je_tacno": True}, {"tekst": "Odg2", "da_li_je_tacno": False},
                  {"tekst": "Odg3", "da_li_je_tacno": False}, {"tekst": "Odg4", "da_li_je_tacno": False}]},
    {"pitanje": "Pitanje_5?",
     "odgovori": [{"tekst": "Odg1", "da_li_je_tacno": True}, {"tekst": "Odg2", "da_li_je_tacno": False},
                  {"tekst": "Odg3", "da_li_je_tacno": False}, {"tekst": "Odg4", "da_li_je_tacno": False}]},
    {"pitanje": "Pitanje_6?",
     "odgovori": [{"tekst": "Odg1", "da_li_je_tacno": True}, {"tekst": "Odg2", "da_li_je_tacno": False},
                  {"tekst": "Odg3", "da_li_je_tacno": False}, {"tekst": "Odg4", "da_li_je_tacno": False}]},
]
srednja_pitanja = [
    {"pitanje": "Pitanje_1?",
     "odgovori": [{"tekst": "Odg1", "da_li_je_tacno": True}, {"tekst": "Odg2", "da_li_je_tacno": False},
                  {"tekst": "Odg3", "da_li_je_tacno": False}, {"tekst": "Odg4", "da_li_je_tacno": False}]},
    {"pitanje": "Pitanje_2?",
     "odgovori": [{"tekst": "Odg1", "da_li_je_tacno": True}, {"tekst": "Odg2", "da_li_je_tacno": False},
                  {"tekst": "Odg3", "da_li_je_tacno": False}, {"tekst": "Odg4", "da_li_je_tacno": False}]},
    {"pitanje": "Pitanje_3?",
     "odgovori": [{"tekst": "Odg1", "da_li_je_tacno": True}, {"tekst": "Odg2", "da_li_je_tacno": False},
                  {"tekst": "Odg3", "da_li_je_tacno": False}, {"tekst": "Odg4", "da_li_je_tacno": False}]},
    {"pitanje": "Pitanje_4?",
     "odgovori": [{"tekst": "Odg1", "da_li_je_tacno": True}, {"tekst": "Odg2", "da_li_je_tacno": False},
                  {"tekst": "Odg3", "da_li_je_tacno": False}, {"tekst": "Odg4", "da_li_je_tacno": False}]},
    {"pitanje": "Pitanje_5?",
     "odgovori": [{"tekst": "Odg1", "da_li_je_tacno": True}, {"tekst": "Odg2", "da_li_je_tacno": False},
                  {"tekst": "Odg3", "da_li_je_tacno": False}, {"tekst": "Odg4", "da_li_je_tacno": False}]},
    {"pitanje": "Pitanje_6?",
     "odgovori": [{"tekst": "Odg1", "da_li_je_tacno": True}, {"tekst": "Odg2", "da_li_je_tacno": False},
                  {"tekst": "Odg3", "da_li_je_tacno": False}, {"tekst": "Odg4", "da_li_je_tacno": False}]},
]
teska_pitanja = [
    {"pitanje": "Pitanje_1?",
     "odgovori": [{"tekst": "Odg1", "da_li_je_tacno": True}, {"tekst": "Odg2", "da_li_je_tacno": False},
                  {"tekst": "Odg3", "da_li_je_tacno": False}, {"tekst": "Odg4", "da_li_je_tacno": False}]},
    {"pitanje": "Pitanje_2?",
     "odgovori": [{"tekst": "Odg1", "da_li_je_tacno": True}, {"tekst": "Odg2", "da_li_je_tacno": False},
                  {"tekst": "Odg3", "da_li_je_tacno": False}, {"tekst": "Odg4", "da_li_je_tacno": False}]},
    {"pitanje": "Pitanje_3?",
     "odgovori": [{"tekst": "Odg1", "da_li_je_tacno": True}, {"tekst": "Odg2", "da_li_je_tacno": False},
                  {"tekst": "Odg3", "da_li_je_tacno": False}, {"tekst": "Odg4", "da_li_je_tacno": False}]},
    {"pitanje": "Pitanje_4?",
     "odgovori": [{"tekst": "Odg1", "da_li_je_tacno": True}, {"tekst": "Odg2", "da_li_je_tacno": False},
                  {"tekst": "Odg3", "da_li_je_tacno": False}, {"tekst": "Odg4", "da_li_je_tacno": False}]},
    {"pitanje": "Pitanje_5?",
     "odgovori": [{"tekst": "Odg1", "da_li_je_tacno": True}, {"tekst": "Odg2", "da_li_je_tacno": False},
                  {"tekst": "Odg3", "da_li_je_tacno": False}, {"tekst": "Odg4", "da_li_je_tacno": False}]},
    {"pitanje": "Pitanje_6?",
     "odgovori": [{"tekst": "Odg1", "da_li_je_tacno": True}, {"tekst": "Odg2", "da_li_je_tacno": False},
                  {"tekst": "Odg3", "da_li_je_tacno": False}, {"tekst": "Odg4", "da_li_je_tacno": False}]},
]

pitanja = {"laka": laka_pitanja, "srednja": srednja_pitanja, "teska": teska_pitanja}

takmicar = {
    "ime": "",
    "prezime": "",
    "trenutno_pitanje": 1,
    "osvojeni_novac": 0,
    "zagarantovana_suma": 0,
    "pola-pola": False,
    "zamena_pitanja": False,
    "pitaj_publiku": False
}

vrednost_pitanja = {
    "1": {"vrednost": 1000, "zagarantovana": False},
    "2": {"vrednost": 2000, "zagarantovana": False},
    "3": {"vrednost": 3000, "zagarantovana": False},
    "4": {"vrednost": 4000, "zagarantovana": False},
    "5": {"vrednost": 5000, "zagarantovana": True},
    "6": {"vrednost": 10000, "zagarantovana": False},
    "7": {"vrednost": 20000, "zagarantovana": False},
    "8": {"vrednost": 40000, "zagarantovana": False},
    "9": {"vrednost": 80000, "zagarantovana": False},
    "10": {"vrednost": 160000, "zagarantovana": True},
    "11": {"vrednost": 320000, "zagarantovana": False},
    "12": {"vrednost": 640000, "zagarantovana": False},
    "13": {"vrednost": 1125000, "zagarantovana": False},
    "14": {"vrednost": 2500000, "zagarantovana": False},
    "15": {"vrednost": 5000000, "zagarantovana": True}
}

unos_podataka(takmicar_dict=takmicar)
while True:
    postavljanje_pitanja(pitanja=pitanja, takmicar_dict=takmicar)
    davanje_odgovora()
    provera_odgovora()
    print(takmicar)
