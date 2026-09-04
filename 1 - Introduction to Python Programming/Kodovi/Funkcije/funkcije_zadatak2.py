# Napišimo funkciju pod nazivom ukupno_vreme koja će:

# primiti listu sa satima provedenim na različitim zadacima;
# koristiti for petlju da sabere ukupno vreme provedeno na zadacima;
# vratiti poruku sa ukupnim brojem sati provedenih na zadacima.

zadaci = [2, 3, 1, 4, 2, 5, 1]  # Ova lista predstavlja sate provedene na različitim zadacima

def ukupno_vreme(x):
    x = 0
    for i in zadaci: # za svaku vrednost iz liste on ce je dodati na ukupno
        x += i
    return f"Ukupno vreme provedeno na zadacima je {x} sati."

# Primer korišćenja funkcije
print(ukupno_vreme(zadaci))