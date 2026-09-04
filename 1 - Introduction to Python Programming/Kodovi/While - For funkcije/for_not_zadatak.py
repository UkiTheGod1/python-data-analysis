kupci = ["Marko", "Ana", "Lena", "Tom", "Iva"]
lojalni_kupci = ["Ana", "Tom", "Iva"]

for nelojalni in kupci:
    if nelojalni not in lojalni_kupci:    # moze "not nelojalni in" a moze i "nelojlni not in"
        print(f"Poštovani {nelojalni}, imamo specijalnu ponudu za vas da postanete lojalni član!")

# for x in y:
#   if x...:
# y je lista i ne koristi se kad smo jednom odredili njenu lokaciju