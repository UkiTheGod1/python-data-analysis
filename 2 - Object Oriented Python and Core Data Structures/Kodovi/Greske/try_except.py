while True:
    try:
        x = int(input("Unesi broj neki: "))
        print(f"Tvoj broj je: {x}")
        break
    except Exception:
        print("Nije dobro nesto")

# ValueError: greška kada je vrednost argumenta funkcije neadekvatna, iako je tip ispravan;
# NameError: greška zbog pozivanja promenljive ili funkcije koja ne postoji;
# TypeError: greška usled korišćenja pogrešnog tipa podataka u operaciji;
# IndexError: greška prilikom pristupanja indeksu koji je van opsega sekvence;
# OverflowError nastaje prilikom izračunavanja realnog izraza kada je vrednost prevelika;
# ZeroDivisionError je greška zbog deljenja sa nulom;
# IOError: greška pri pokušaju ulazno-izlazne operacije (npr. čitanje nepostojeće datoteke)