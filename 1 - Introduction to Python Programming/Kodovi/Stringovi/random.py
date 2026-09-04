#1. Promena i oblikovanje teksta

# pozdrav = "Dobrodošli na kurs"
# print(pozdrav.upper())  # Ispisuje: 'DOBRODOŠLI NA KURS'
# print(pozdrav.lower())  # Ispisuje: 'dobrodošli na kurs'
# print(pozdrav.lower().strip())  # Ispisuje: 'dobrodošli na kurs'

# 2. Pretraga i zamena teksta

# poruka = "Dobrodošli na kurs programiranja!"
# pozicija = poruka.find("kurs")
# print(f"Reč 'kurs' počinje na poziciji {pozicija}.") # Ispisuje: 'Reč 'kurs'
# zamena = poruka.replace("kurs", "cas")

# 3. Deljenje i spajanje reči

# poruka = "Danas je lep dan"
# reci = poruka.split()
# print(reci) # Ispisuje: ['Danas', 'je', 'lep', 'dan']
# spajanje = " ".join(poruka)
# print(reci) # Ispisuje spojenu poruku od liste

# 3.5 Podele liste na promenljive
# lista = ["Ker", "Macka", "Pas"]
# x, y, z = lista      -      Dodeljuje vrednosti iz liste promenljivima
# print(x)  ispisuje Ker
# print(y)  ispisuje Macka
# print(z)  ispisuje Pas

# 4. Računanje i analiza teksta
# tekst = "Python je zanimljiv i Python je popularan."
# broj_pojavljivanja = tekst.count("Python")
# duzina = len(tekst)
# print(f"Reč 'Python' se pojavljuje {broj_pojavljivanja} puta.")
# print(f"Dužina teksta je {duzina} karaktera.")

# 5. Provera sadržaja stringa

# kod = "12345"
# print(kod.isdigit())  # Ispisuje: True
 
# ime = "Marko"
# print(ime.isalpha())  # Ispisuje: True

# 6. Provera početka i kraja teksta

# tekst = "Dobro došli na kurs"
# print(tekst.startswith("Dobro"))  # Ispisuje: True
# print(tekst.endswith("kurs"))     # Ispisuje: True

# 7. Formatiranje teksta sa umetnutim vrednostima

# ime = "Marko"
# poruka = "Dobro došao, {}!".format(ime)
# print(poruka)  # Ispisuje: 'Dobro došao, Marko!'