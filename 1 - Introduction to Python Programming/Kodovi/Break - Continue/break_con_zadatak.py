# ️Zadatak: Alex prati korisničke komentare i analizira ih na temelju pozitivnosti. 
# Zamislimo da ima listu komentara koji sadrže različite ocene. 
# Ona želi:
# da preskoči komentare sa ocenom manjom od 3, jer ih ne smatra dovoljno pozitivnim za dalju analizu (koristite continue);
# da prestane sa pregledom komentara čim naiđe na ocenu 5, jer bi taj komentar mogao biti odličan za izdvajanje kao primer za tim (koristite break).

ocene_komentara = [4, 2, 3, 5, 1, 3, 4]

for ocena in ocene_komentara:
    if ocena < 3:
        print("Ocena preskocena")
        continue

    if ocena == 5:
        print("Ova ocena je dobra, zaustavljamo se")
        break

    print(f"Ocena {ocena} je okej")
