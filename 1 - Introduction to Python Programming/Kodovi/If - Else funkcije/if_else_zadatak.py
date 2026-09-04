# Napišimo program koji nam omogućava sledeće:

# unosimo broj preostalih zaliha, broj prodatih jedinica i informaciju o popustima;
# ako su zalihe niske i prodaja je veća od 200 jedinica, program predlaže hitnu narudžbinu;
# ako zalihe nisu niske, ali prodaja nije premašila 200 jedinica, program preporučuje dodatne promotivne akcije.

broj_preostalih_zaliha = int(input("Unesi broj preostalih zaliha: "))
broj_prodatih_jedinica = int(input("Unesi broj prodatih jedinica: "))
promocije = input("Da li ste iskoristili popust? - ")

if broj_preostalih_zaliha < 100 and broj_prodatih_jedinica > 200:
    print("Potrebna hitno naruciti nove zalihe")
else:
    print("Potrebno preporuciti dodatne promitivne akcije")

# Program ispisuje "Potrebno preporuciti dodatne promotivne akcije" iako je prodato puno jedinica, ako ima puno zaliha
# Nije definisano sta ce se desiti ako je samo jedan od uslova ispunjen
                             
