cene = [23.99, 19.50, 55.00, 48.75, 102.00, 33.40, 12.30]

cene_ispod50 = []

for cena in cene:
    if cena < 50:
        cene_ispod50.append(cena)

cene_ispod50.sort()
print(cene_ispod50)