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
    global student_najmanje_pol_ispita
    pol_ispiti = 200
    for key in studenti_dict:
        if len(polozeni_predmeti_studenta(studenti_dict, key)) < pol_ispiti:
            student_najmanje_pol_ispita = studenti_dict.get(key)
            pol_ispiti = len(polozeni_predmeti_studenta(studenti_dict, key))
    return student_najmanje_pol_ispita


def studenti_koji_polozili_sve_ispite(studenti_dict):
    lista_studenti_koji_polozili_sve_ispite = []
    for key in studenti_dict:
        polozio_sve_ispite = True
        predmeti = studenti_dict.get(key).get("predmeti").values()
        for predmet in predmeti:
            if predmet.get("ocena") < 6:
                polozio_sve_ispite = False
        if polozio_sve_ispite:
            lista_studenti_koji_polozili_sve_ispite.append(studenti_dict.get(key))

    print("Broj takvih studenata je: ", len(lista_studenti_koji_polozili_sve_ispite))
    return lista_studenti_koji_polozili_sve_ispite


def raspodela_studenata_po_smerovima(studenti_dict):
    broj_elektro = 0
    broj_masinstvo = 0
    broj_ukupno = 0
    for key in studenti_dict:
        smerovi = studenti_dict.get(key).get("smer")
        if smerovi == "Elektrotehnika":
            broj_elektro += 1
            broj_ukupno += 1
        elif smerovi == "Masinstvo":
            broj_masinstvo += 1
            broj_ukupno += 1
    procenat_elektro = round((broj_elektro / broj_ukupno * 100), 2)
    procenat_masinstvo = round((broj_masinstvo / broj_ukupno * 100), 2)
    raspodela_dict = {"Elektrotehnika": procenat_elektro, "Masinstvo": procenat_masinstvo}
    return raspodela_dict


def svi_studenti_na_odabranom_smeru(studenti_dict, odabrani_smer):
    for key in studenti_dict:
        student = studenti_dict.get(key)
        if student.get("smer") == odabrani_smer:
            print(student)


def najbolji_student_na_smeru(studenti_dict, odabrani_smer):
    studenti_na_smeru = {}
    for key in studenti_dict:
        if studenti_dict.get(key).get("smer") == odabrani_smer:
            studenti_na_smeru[key] = studenti_dict.get(key)
    # print(studenti_na_smeru)
    naj_student = podaci_studenta_najvec_prosek(studenti_na_smeru)
    return naj_student


def predmeti_koje_nije_polozio_nijedan_student(studenti_dict):
    nepol_predmeti_elektro = []
    broj_studenata_elektro = 0
    predmet_niko_nije_pol_elektro = []
    nepol_predmeti_masinstvo = []
    broj_studenata_masinstvo = 0
    predmet_niko_nije_pol_masinstvo = []
    for key in studenti_dict:
        if studenti_dict.get(key).get("smer") == "Elektrotehnika":
            predmeti = studenti_dict.get(key).get("predmeti").values()
            broj_studenata_elektro += 1
            for predmet in predmeti:
                if predmet.get("ocena") == 5:
                    nepol_predmeti_elektro.append(predmet.get("naziv"))
        if studenti_dict.get(key).get("smer") == "Masinstvo":
            predmeti = studenti_dict.get(key).get("predmeti").values()
            broj_studenata_masinstvo += 1
            for predmet in predmeti:
                if predmet.get("ocena") == 5:
                    nepol_predmeti_masinstvo.append(predmet.get("naziv"))
    for item in nepol_predmeti_elektro:
        if nepol_predmeti_elektro.count(item) == broj_studenata_elektro:
            predmet_niko_nije_pol_elektro.append(item)
    predmet_niko_nije_pol_elektro = list(set(predmet_niko_nije_pol_elektro))
    for item in nepol_predmeti_masinstvo:
        if nepol_predmeti_masinstvo.count(item) == broj_studenata_masinstvo:
            predmet_niko_nije_pol_masinstvo.append(item)
    predmet_niko_nije_pol_masinstvo = list(set(predmet_niko_nije_pol_masinstvo))
    predmet_niko_nije_pol = predmet_niko_nije_pol_elektro+ predmet_niko_nije_pol_masinstvo
    return predmet_niko_nije_pol


def predmet_sa_najvecom_prosecnom_ocenom(studenti_dict):
    pomocna_lista = []
    pomocna_lista_predmeta = []
    pomocna_lista_ocena = []
    for key in studenti_dict:
        student = studenti_dict.get(key)
        predmeti = student.get("predmeti").values()
        for predmet in predmeti:
            pomocna_lista.append(predmet)
    for items in pomocna_lista:
        pomocna_lista_predmeta.append(items.get("naziv"))
        pomocna_lista_ocena.append(items.get("ocena"))
    print(pomocna_lista_predmeta)
    print(pomocna_lista_ocena)



studenti = {
    "501": {
        "ime": "Marko",
        "prezime": "Stankovic",
        "indeks": "501",
        "smer": "Elektrotehnika",
        "predmeti": {
            "MAT1": {"naziv": "Matematika 1", "ocena": 8},
            "MAT2": {"naziv": "Matematika 2", "ocena": 6},
            "INF": {"naziv": "Informatika", "ocena": 10},
            "ELK": {"naziv": "Elektronika", "ocena": 5},
            "ENG": {"naziv": "Engleski", "ocena": 9},
            "PR1": {"naziv": "Programiranje 1", "ocena": 5}
        }
    },
    "502": {
        "ime": "Stefan",
        "prezime": "Markovic",
        "indeks": "502",
        "smer": "Elektrotehnika",
        "predmeti": {
            "MAT1": {"naziv": "Matematika 1", "ocena": 9},
            "MAT2": {"naziv": "Matematika 2", "ocena": 5},
            "INF": {"naziv": "Informatika", "ocena": 10},
            "ELK": {"naziv": "Elektronika", "ocena": 9},
            "ENG": {"naziv": "Engleski", "ocena": 9},
            "PR1": {"naziv": "Programiranje 1", "ocena": 9}
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
            "INF": {"naziv": "Informatika", "ocena": 10},
            "ELK": {"naziv": "Elektronika", "ocena": 9},
            "ENG": {"naziv": "Engleski", "ocena": 8},
            "PR1": {"naziv": "Programiranje 1", "ocena": 9}
        }
    },
    "601": {
        "ime": "Dusan",
        "prezime": "Nikolic",
        "indeks": "601",
        "smer": "Masinstvo",
        "predmeti": {
            "MEH1": {"naziv": "Mehanika 1", "ocena": 9},
            "MEH2": {"naziv": "Mehanika 2", "ocena": 5},
            "ME1": {"naziv": "Masinski elementi 1", "ocena": 9},
            "ME2": {"naziv": "Masinski elementi 2", "ocena": 9},
            "OTP": {"naziv": "Otpornost materijala", "ocena": 8},
            "ING": {"naziv": "Inzenjerska grafika", "ocena": 7}
        }
    },
    "602": {
        "ime": "Nikola",
        "prezime": "Babic",
        "indeks": "602",
        "smer": "Masinstvo",
        "predmeti": {
            "MEH1": {"naziv": "Mehanika 1", "ocena": 5},
            "MEH2": {"naziv": "Mehanika 2", "ocena": 5},
            "ME1": {"naziv": "Masinski elementi 1", "ocena": 7},
            "ME2": {"naziv": "Masinski elementi 2", "ocena": 5},
            "OTP": {"naziv": "Otpornost materijala", "ocena": 8},
            "ING": {"naziv": "Inzenjerska grafika", "ocena": 5}
        }
    },
    "603": {
        "ime": "Nenad",
        "prezime": "Nedeljkovic",
        "indeks": "603",
        "smer": "Masinstvo",
        "predmeti": {
            "MEH1": {"naziv": "Mehanika 1", "ocena": 6},
            "MEH2": {"naziv": "Mehanika 2", "ocena": 6},
            "ME1": {"naziv": "Masinski elementi 1", "ocena": 6},
            "ME2": {"naziv": "Masinski elementi 2", "ocena": 6},
            "OTP": {"naziv": "Otpornost materijala", "ocena": 8},
            "ING": {"naziv": "Inzenjerska grafika", "ocena": 8}
        }
    },
}


while True:
    print("Ponudjene opcije: \n"
          "a. svih položenih ispita određenog studenta\n"
          "b. srednje ocene određenog studenta\n"
          "c. podataka studenta/studenata sa navećom prosečnom ocenom\n"
          "d. podataka studenta/studenata sa najmanje položenih ispita\n"
          "e. svih studenta koji su položili sve ispite na predmetima koji su im dodeljeni\n"
          "f. raspodele studenata po smerovima, u procentima\n"
          "g. sve studente na odabranom smeru\n"
          "h. najboljeg studenta na odabranom smeru\n"
          "i. sve predmete koji nije položio niti jedan student\n"
          "j. predmeta sa najvećom prosečnom ocenom\n"
          "k. Kraj programa\n")
    opcija = input("Izaberite opciju (slovo) od ponudjenih: ")
    match opcija:
        case "a":
            indeks_studenta = input("Indeks studenta: ")
            print(f"{polozeni_predmeti_studenta(studenti, indeks_studenta)}\n")
        case "b":
            indeks_studenta = input("Indeks studenta: ")
            print(f"{srednja_ocena_studenta(studenti, indeks_studenta)}\n")
        case "c":
            print(f"{podaci_studenta_najvec_prosek(studenti)}\n")
        case "d":
            print(f"{podaci_studenta_najmanje_pol_ispita(studenti)}\n")
        case "e":
            print(f"{studenti_koji_polozili_sve_ispite(studenti)}\n")
        case "f":
            print(f"{raspodela_studenata_po_smerovima(studenti)}\n")
        case "g":
            smer = input("Unesite smer koji zelite: Elektrotehnika ili Masinstvo: ")
            svi_studenti_na_odabranom_smeru(studenti, smer)
        case "h":
            smer = input("Unesite smer koji zelite: Elektrotehnika ili Masinstvo: ")
            print(f"{najbolji_student_na_smeru(studenti, smer)}\n")
        case "i":
            print(f"{predmeti_koje_nije_polozio_nijedan_student(studenti)}\n")
        case "j":
            predmet_sa_najvecom_prosecnom_ocenom(studenti)
        case "k":
            print("Kraj programa")
            break
        case other:
            print("Slovo nije ponudjeno!!\n")
