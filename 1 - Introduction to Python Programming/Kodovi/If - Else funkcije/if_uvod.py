# Alex traži od korisnika da unese broj kupaca i informaciju o popustima
broj_kupaca = int(input("Unesite broj kupaca danas: "))
popust = input("Da li su kupci iskoristili popust (da/ne)? ")
 
# Provera uslova za preporuke prodajnom timu
if broj_kupaca > 100 and popust == "da":
    print("Prodaja je uspešna, zahvaljujući popustima!")
 
if broj_kupaca > 100 and popust == "ne":
    print("Prodaja je dobra, ali možete privući više kupaca uvođenjem popusta.")
 
if 50 <= broj_kupaca <= 100 and popust == "da":
    print("Prodaja je solidna, popusti su pomogli. Razmislite o povećanju popusta.")
 
if 50 <= broj_kupaca <= 100 and popust == "ne":
    print("Prodaja je solidna, ali može se poboljšati uvođenjem popusta.")
 
if broj_kupaca < 50 and popust == "da":
    print("Prodaja je slaba, iako su popusti ponuđeni. Razmotrite dodatne promocije.")
 
if broj_kupaca < 50 and popust == "ne":
    print("Prodaja je slaba. Uvedite hitne mere kao što su popusti ili posebne ponude.")