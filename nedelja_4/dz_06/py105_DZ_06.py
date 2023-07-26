with open("inputfile.txt", "r") as f:
    lista_kasir_iznos = f.readlines()
# print(lista_kasir_iznos)

kasir_promet = {}
for index in range(len(lista_kasir_iznos)):
    if index % 2 == 0:
        pomoc_lista = lista_kasir_iznos[index].split(":")
        ime_prezime = pomoc_lista[1].strip()
        # kasir_promet[f"{ime_prezime}"] = 0
    else:
        pomoc_lista = lista_kasir_iznos[index].split(":")
        iznos = pomoc_lista[1].strip()
        # print(iznos)
        lista_iznosa = iznos.split(",")
        # print(lista_iznosa)
        suma = 0
        for el in lista_iznosa:
            suma += float(el)
        kasir_promet[f"{ime_prezime}"] = round(suma, 2)

kasir_promet = dict(sorted(kasir_promet.items(), key=lambda x: x[1], reverse=True))

print(kasir_promet)


for i, key in enumerate(kasir_promet):
    ime_prezime_rb = key.replace(" ", "_") + f"_{i+1}"
    # print(ime_prezime_rb)
    with open(f"{ime_prezime_rb}", "w") as fajl:
        fajl.write(f"{key}: {kasir_promet.get(key)}")
