"""
Napisati program za enkripciju i dekripciju poruka. Na samom početku korisnik unosi
poruku i ključ (celobrojnu referentnu vrednost u opsegu od 1 do 5 koja se koristi u
procesu). Potom korisnik bira operaciju unošenjem reči “encrypt” ili “decrypt”. Program
na izlazu prikazuje obrađenu poruku.
● Enkripcija se vrši tako što se za svaki karakter vrši pomeranje unapred vrednosti
u Unicode tabeli za određeni broj vrednosti u zavisnosti od unešenog ključa.
● Dekripcija je inverzna operacija enkripciji - vrši se pomeranje unazad
Isprobati program sa različitim unosima. Testirati da li su operacije inverzne.
Hint: koristiti built-in funkcije za prevođenje karaktera u Unicode i obratno
"""
"""
Drugi zadatak je ok, ali se štampa nepoželjni karakter % na kraju u terminalu. 
Problem je sa korišćenjem end parametra print funkcije. Probaj da formiraš string pre štampanja. 
Provera ulaznih parametra je labava u slučaju da korisnik unese vrednost van opsega 1-5, string umesto broja i sl.
"""
# ord() - karakter u unicode indeks
# chr() - unicode indeks u karakter


def encrypt(tekst, broj):
    encrypted_text = ""
    for characters in tekst:
        encrypted_chars = chr(ord(characters) + broj)
        encrypted_text += encrypted_chars
    print(encrypted_text)


def decrypt(tekst, broj):
    decrypted_text = ""
    for characters in tekst:
        decrypted_chars = chr(ord(characters) - broj)
        decrypted_text += decrypted_chars
    print(decrypted_text)


poruka = input("Unesi poruku: ")

kljuc = 0
while kljuc not in range(1, 6):
    kljuc = input("Unesi kljuc (ceo broj od 1 do 5): ")
    while not kljuc.isnumeric():
        kljuc = input("Kljuc mora biti ceo broj od 1 do 5! Unesi novi kljuc: ")
    kljuc = int(kljuc)

operacija = ""
while operacija != "encrypt" and operacija != "decrypt":
    operacija = input("encrypt or decrypt: ")

if operacija == "encrypt":
    encrypt(poruka, kljuc)
else:
    decrypt(poruka, kljuc)





