def polozeni_predmeti_studenta(studenti_dict, student_indeks):
    student = studenti_dict.get(str(student_indeks))
    predmeti = student.get("predmeti").values()
    polozeni = []
    for predmet in predmeti:
        if int(predmet.get("ocena")) > 5:
            polozeni.append(predmet.get("naziv"))
    return polozeni
    # print(polozeni)


def srednja_ocena_studenta(studenti_dict, student_indeks):
    student = studenti_dict.get(str(student_indeks))
    predmeti = student.get("predmeti").values()
    suma = 0
    brojac = 0
    for predmet in predmeti:
        if int(predmet.get("ocena")) > 5:
            suma += int(predmet.get("ocena"))
            brojac += 1
    return round(float(suma / brojac), 2)
    # print(round(float(suma / brojac), 2))


def podaci_studenta_najvec_prosek(studenti_dict):
    global student_naj_prosek
    max_prosek = 0
    for key in studenti_dict:
        if srednja_ocena_studenta(studenti_dict, key) > max_prosek:
            max_prosek = srednja_ocena_studenta(studenti_dict, key)
            student_naj_prosek = key
    return studenti_dict.get(str(student_naj_prosek))


def podaci_studenta_najmanje_pol_ispita(studenti_dict):
    for key in studenti_dict:
        student = studenti_dict.get(key)
        predmeti = student.get("predmeti").values()
        nepol_predmeti = 0
        for predmet in predmeti:
            if predmet.get("ocena") == 5:
                nepol_predmeti += 1





studenti = {
    "501": {
        "ime": "Marko",
        "prezime": "Stankovic",
        "indeks": "501",
        "smer": "Elektrotehnika",
        "predmeti": {
            "MAT1": {"naziv": "Matematika 1", "ocena": 6},
            "MAT2": {"naziv": "Matematika 2", "ocena": 6},
            "INF": {"naziv": "Informatika", "ocena": 8},
            "ELK": {"naziv": "Elektronika", "ocena": 5},
            "ENG": {"naziv": "Engleski", "ocena": 9},
            "PR1": {"naziv": "Programiranje 1", "ocena": 7}
        }
    },
    "502": {
        "ime": "Stefan",
        "prezime": "Markovic",
        "indeks": "502",
        "smer": "Elektrotehnika",
        "predmeti": {
            "MAT1": {"naziv": "Matematika 1", "ocena": 8},
            "MAT2": {"naziv": "Matematika 2", "ocena": 9},
            "INF": {"naziv": "Informatika", "ocena": 7},
            "ELK": {"naziv": "Elektronika", "ocena": 9},
            "ENG": {"naziv": "Engleski", "ocena": 10},
            "PR1": {"naziv": "Programiranje 1", "ocena": 8}
        }
    },
    "503": {
        "ime": "Bogdan",
        "prezime": "Petrovic",
        "indeks": "503",
        "smer": "Elektrotehnika",
        "predmeti": {
            "MAT1": {"naziv": "Matematika 1", "ocena": 5},
            "MAT2": {"naziv": "Matematika 2", "ocena": 5},
            "INF": {"naziv": "Informatika", "ocena": 6},
            "ELK": {"naziv": "Elektronika", "ocena": 7},
            "ENG": {"naziv": "Engleski", "ocena": 8},
            "PR1": {"naziv": "Programiranje 1", "ocena": 6}
        }
    },
    "601": {
        "ime": "Dusan",
        "prezime": "Nikolic",
        "indeks": "601",
        "smer": "Masinstvo",
        "predmeti": {
            "MEH1": {"naziv": "Mehanika 1", "ocena": 6},
            "MEH2": {"naziv": "Mehanika 2", "ocena": 5},
            "ME1": {"naziv": "Masinski elementi 1", "ocena": 6},
            "ME2": {"naziv": "Masinski elementi 2", "ocena": 9},
            "OTP": {"naziv": "Otpornost materijala", "ocena": 9},
            "ING": {"naziv": "Inzenjerska grafika", "ocena": 7}
        }
    },
    "602": {
        "ime": "Nikola",
        "prezime": "Babic",
        "indeks": "602",
        "smer": "Masinstvo",
        "predmeti": {
            "MEH1": {"naziv": "Mehanika 1", "ocena": 9},
            "MEH2": {"naziv": "Mehanika 2", "ocena": 8},
            "ME1": {"naziv": "Masinski elementi 1", "ocena": 7},
            "ME2": {"naziv": "Masinski elementi 2", "ocena": 10},
            "OTP": {"naziv": "Otpornost materijala", "ocena": 9},
            "ING": {"naziv": "Inzenjerska grafika", "ocena": 10}
        }
    },
    "603": {
        "ime": "Nenad",
        "prezime": "Nedeljkovic",
        "indeks": "603",
        "smer": "Masinstvo",
        "predmeti": {
            "MEH1": {"naziv": "Mehanika 1", "ocena": 6},
            "MEH2": {"naziv": "Mehanika 2", "ocena": 7},
            "ME1": {"naziv": "Masinski elementi 1", "ocena": 6},
            "ME2": {"naziv": "Masinski elementi 2", "ocena": 6},
            "OTP": {"naziv": "Otpornost materijala", "ocena": 7},
            "ING": {"naziv": "Inzenjerska grafika", "ocena": 8}
        }
    },
}

# polozeni_predmeti_studenta(studenti, 503)

# srednja_ocena_studenta(studenti, 603)

# print(podaci_studenta_najvec_prosek(studenti))


print("a. svih položenih ispita određenog studenta\n"
      "b. srednje ocene određenog studenta\n"
      "c. podataka studenta/studenata sa navećom prosečnom ocenom\n"
      "d. podataka studenta/studenata sa najmanje položenih ispita\n"
      "e. svih studenta koji su položili sve ispite na predmetima koji su im dodeljeni\n"
      "f. raspodele studenata po smerovima, u procentima\n"
      "g. sve studente na odabranom smeru\n"
      "h. najboljeg studenta na odabranom smeru\n"
      "i. sve predmete koji nije položio niti jedan student\n"
      "j. predmeta sa najvećom prosečnom ocenom\n")

opcija = input("Izaberite opciju (slovo) od ponudjenih: ")

match opcija:
    case "a":
        indeks_studenta = input("Indeks studenta: ")
        print(polozeni_predmeti_studenta(studenti, indeks_studenta))
    case "b":
        indeks_studenta = input("Indeks studenta: ")
        print(srednja_ocena_studenta(studenti, indeks_studenta))
    case "c":
        print(podaci_studenta_najvec_prosek(studenti))
