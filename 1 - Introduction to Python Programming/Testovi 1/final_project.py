while True:
    ime_prezime = input("Unesite vaše ime i prezime: ")
    if " " not in ime_prezime or ime_prezime.replace(" ", "").isalpha() == False: # Proverava da li ima 2 reci i da li je tekst
        print("Ime nije dobro uneto. Pokušajte opet.")
        continue
    break

podeljeno_ime = ime_prezime.split()
ime, prezime = podeljeno_ime
print(f"Vaše ime je {ime}, a vaše prezime je {prezime}") # Samo provera promenljivih

while True:
    ukupan_broj_kupovina = int(input("Unesite ukupan broj obavljenih kupovina: "))
    if ukupan_broj_kupovina <= 0:
        print("Uneli ste neispravan broj kupovina. Pokušajte opet.")
        continue
    break

ukupan_iznos = 0
broj_skupih_kupovina = 0
for i in range(ukupan_broj_kupovina):
    iznos_kupovine = int(input("Unesite iznos kupovine u dinarima: "))
    ukupan_iznos += iznos_kupovine
    if iznos_kupovine > 10000:
        broj_skupih_kupovina += 1
print(f"Ukupan iznos svih kupovina je {ukupan_iznos} dinara.")
print(f"Broj kupovina sa iznosom većim od 10.000 dinara je {broj_skupih_kupovina}")

def status_korisnika(ukupan_iznos, ukupan_broj_kupovina):
    if ukupan_iznos > 100000 and ukupan_broj_kupovina > 10:
        status = "VIP"
    else:
        status = "STANDARD"
    return status

print(f"Vi ste {status_korisnika(ukupan_iznos, ukupan_broj_kupovina)} korisnik!")

if status_korisnika(ukupan_iznos, ukupan_broj_kupovina) == "VIP":
    popust = 10
else:
    popust = 5

cena_artikla = int(input("Unesi cenu novog artikla koji želite da kupite: "))

def konacna_cena(x, y):
    cena_sa_popustom = x - ((x * y) / 100)
    return cena_sa_popustom

print(f"Cena artikla sa popustom vašeg statusa je {konacna_cena(cena_artikla, popust)}")
