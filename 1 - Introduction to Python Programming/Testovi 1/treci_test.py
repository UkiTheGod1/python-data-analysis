while True:
    ukupan_broj_prozivoda = int(input("Unesi broj proizvoda: "))
    if ukupan_broj_prozivoda < 1 or ukupan_broj_prozivoda > 50:
        print("Greška: Nevalidan broj proizvoda")
        continue
    break

while True:
    cena_narudzbine = float(input("Unesi cenu narudžbine: "))
    if cena_narudzbine <= 0:
        print("Greška: Cena mora biti veća od 0.")
        continue
    break

while True:
    status_placanja = input("Unesi status plaćanja: ").lower()
    if status_placanja == "plaćeno":
        print(f"Broj proizvoda: {ukupan_broj_prozivoda}, cena: {cena_narudzbine}, status plaćanja: {status_placanja}")
        break
    elif status_placanja == "neplaćeno" or status_placanja == "na čekanju":
        print("Narudžbina nije plaćena, ne može biti obrađena.")
        continue
    else:
        print("Greška: Nepoznat status plaćanja.")
        continue
# Program se izvršava dok Alex ne unese validnu narudžbinu koja ispunjava SVE KRITERIJUME