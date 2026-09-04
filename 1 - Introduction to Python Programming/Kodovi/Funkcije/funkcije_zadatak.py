# Napišite funkciju pod nazivom preporuci_obucu, koja će na osnovu vremenskih uslova (sunce, kiša, sneg) vratiti preporuku za obuću. 
# Na primer, ako je vreme „kiša”, funkcija treba da preporuči gumene čizme.

def vreme(x):
    if x == "kisa":
        return "Ponesi gumene cizme!"
    elif x == "sunce":
        return "Obuci sandale!"
    elif x == "sneg":
        return "Obujte tople cizme!"
    else:
        return "Obuci sta hoces, vreme ne zahteva posebne mere"
    
trenutno_vreme = input("Kakvo je vreme danas? - ").lower()
print(vreme(trenutno_vreme))
