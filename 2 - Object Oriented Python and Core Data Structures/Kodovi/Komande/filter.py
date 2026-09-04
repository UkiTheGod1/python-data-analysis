# Funkcija filter filtrira listu po odredjenom uslovu

# filter(uslov, lista)
# Primer:

lista = [0,1,2,3,4,5,6,7,8,9,10]
# moze se i koristiti list:
#               lista = list(range(0,10))

def filter_neparan(x):
    if x % 2 != 0:
        return x

filtrirana_lista = list(filter(filter_neparan, lista))
print(filtrirana_lista)

# Moze i sa lambda da ne pravimo bezveze funkciju nepotrebnu
filtrirana_lista = list(filter(lambda x: x % 2 != 0, lista))
print(filtrirana_lista)

# filter komanda je iterator tako da automatski prolazi kroz sve elemente navedene liste