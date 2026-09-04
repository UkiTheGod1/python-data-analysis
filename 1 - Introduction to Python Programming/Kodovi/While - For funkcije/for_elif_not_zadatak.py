kupci = ['Sara', 'Tom', 'Lena', 'Marko', 'Ana']
lojalni_club = ['Tom', 'Lena', 'Ana']
premium_club = ['Ana', 'Sara']

for kupac in kupci:
    if kupac in premium_club and kupac in lojalni_club:
        print(f"Postovani/a {kupac}, vi ste lojalni kupac koji ima ekskluzivan pristup premium ponudi!")
    elif kupac in lojalni_club and kupac not in premium_club: # Mora se u oba uslova navesti KO pripada KOJOJ listi
        print(f"Dragi/a {kupac}, hvala na lojalnosti! Očekuje vas posebna ponuda.")
    elif kupac in premium_club and kupac not in lojalni_club:
        print(f"Dragi/a {kupac}, imate pristup nasoj premium ponudi!")
    else:
        print(f"Postovani/a {kupac}, dobrodosli!")