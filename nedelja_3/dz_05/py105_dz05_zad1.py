unet_string = "REG_OZNAKA    BOJA    TIP_VOZILA\n"\
              "NI-543-MM    siva    automobil\n"\
              "LE-345-KM    plava    kamion\n"\
              "BG-345-TT    bela    automobil\n"\
              "KG-365-KG    plava   automobil\n"\
              "SU-475-GM    bela    automobil\n"\
              "KG-845-YB    crna    autobus\n"\
              "NI-345-XD    bela    automobil\n"\
              "UE-134-NF    crna    automobil\n"\
              "AL-226-DF    bela     kamion"


def recnik(ulazni_string: str):
    lista1 = ulazni_string.split("\n")

    lista2 = []
    for element in lista1:
        lista2.append(element.split("   "))
    # print(lista2)

    lista_reg_oznaka = []
    for el in lista2:
        lista_reg_oznaka.append(el[0].strip())
    # print(lista_reg_oznaka)

    lista_boja = []
    for elem in lista2:
        lista_boja.append(elem[1].strip())
    lista_boja.remove(lista_boja[0])
    # print(lista_boja)

    lista_tipova = []
    for i in lista2:
        lista_tipova.append(i[2].strip())
    lista_tipova.remove(lista_tipova[0])
    # print(lista_tipova)

    lista_gradova_sa_dupl = []
    for index in range(1, len(lista_reg_oznaka)):
        lista_gradova_sa_dupl.append(lista_reg_oznaka[index][0:2])
    lista_gradova = []
    for item in lista_gradova_sa_dupl:
        if item not in lista_gradova:
            lista_gradova.append(item)
    # print(lista_gradova)

    tip_boja_lista = lista_tip_boja(lista_boja=lista_boja, lista_tipova=lista_tipova)

    krajnji_recnik = {
        "tip_vozila": {
            "automobil": str(round((lista_tipova.count("automobil") / (len(lista_tipova)) * 100), 2)) + "%",
            "kamion": str(round((lista_tipova.count("kamion") / (len(lista_tipova)) * 100), 2)) + "%",
            "autobus": str(round((lista_tipova.count("autobus") / (len(lista_tipova)) * 100), 2)) + "%"
        },
        "gradovi": lista_gradova,
        "boja_po_tipu": {
            "automobil": {
                "siva": tip_boja_lista.count(("automobil", "siva")),
                "bela": tip_boja_lista.count(("automobil", "bela")),
                "plava": tip_boja_lista.count(("automobil", "plava")),
                "crna": tip_boja_lista.count(("automobil", "crna"))
            },
            "kamion": {
                "bela": tip_boja_lista.count(("kamion", "bela")),
                "plava": tip_boja_lista.count(("kamion", "plava"))
            },
            "autobus": {
                "crna": tip_boja_lista.count(("autobus", "crna"))
            }
        }
    }

    return krajnji_recnik


def lista_tip_boja(lista_boja:list, lista_tipova:list):
    pomocna_lista = []
    for index in range(len(lista_tipova)):
        pomocna_lista.append((lista_tipova[index], lista_boja[index]))

    return pomocna_lista


print(recnik(unet_string))
