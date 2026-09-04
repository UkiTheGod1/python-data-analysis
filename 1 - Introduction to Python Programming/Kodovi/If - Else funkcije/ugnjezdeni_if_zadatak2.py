# Pravila popusta

    # Redovni kupci:
        # iznos manji od 100 dolara: nema popusta;
        # iznos između 100 i 500 dolara: 5% popusta;
        # iznos veći od 500 dolara: 10% popusta.

    # Članovi kluba lojalnosti:
        # iznos manji od 100 dolara: 5% popusta;
        # iznos između 100 i 500 dolara: 10% popusta;
        # iznos veći od 500 dolara: 15% popusta.

iznos = int(input("Unesi iznos narudzbine: "))
kupac = input("Unesi vrstu kupca: ")

if kupac == "clan kluba lojalnosti":
    if iznos < 100:
        print("Dobijas 5% popusta")
    elif iznos <= 500:
        print("Dobijas 10% popusta")
    else:
        print("Dobijas 15% popusta")
else:
    if iznos < 100:
        print("Nema popusta")
    elif iznos <= 500:
        print("Dobijas 5% popusta")
    else:
        print("Dobijas 10% popusta")