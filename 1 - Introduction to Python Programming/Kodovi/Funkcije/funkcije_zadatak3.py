# Definišemo funkciju za izračunavanje popusta
def calculate_discount(x, y):
    new_price = x - (x * y) / 100 # Ovo je matematicki postupak za racunavanje procenta
    return new_price
 
# Poziv funkcije za primer kada je cena 500, a popust 10%
while True:
    cena = int(input("Unesi cenu prozivoda: "))
    if cena < 0:
        print("Ta cena je nemoguca, probajte opet: ")
        continue
    break

while True:
    popust = int(input("Unesi popust: "))
    if popust > 100 or popust < 0:
        print("Taj popust je nemoguc, probajte opet: ")
        continue
    break

print(calculate_discount(cena, popust))
