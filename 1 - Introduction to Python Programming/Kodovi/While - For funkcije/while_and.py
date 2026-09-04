# Maksimalan broj kupona i vreme trajanja promocije u danima
maks_kupona = 100
vreme_trajanja = 7
 
# Trenutni status
iskorisceni_kuponi = 0
preostalo_dana = vreme_trajanja
while (iskorisceni_kuponi < maks_kupona) and (preostalo_dana > 0):
    # Simuliraj iskorišćenje kupona i protok vremena
    iskorisceni_kuponi += 10
    preostalo_dana -= 1
    print(f"Istrošeno kupona: {iskorisceni_kuponi}, Preostalo dana: {preostalo_dana}")
print("Promocija je završena.")