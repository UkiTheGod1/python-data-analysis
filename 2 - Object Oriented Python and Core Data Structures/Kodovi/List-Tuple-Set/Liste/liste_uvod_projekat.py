cene = [200, 150, 75, 60, 300, 500, 420, 600, 123, 400, 30, 60, 155, 210, 325]
budzet = int(input("Unesite svoj budzet kojim cete da kupujete: "))

moguce_cene = 0
nemoguce_cene = 0

for cena in cene:
    if cena <= budzet:
        moguce_cene += 1
    else:
        nemoguce_cene += 1

print(f"Proizvoda sa cenom koja odgovara vasem vudzetu ima {moguce_cene}, a proizvoda kojih ne mozete da priustite ima {nemoguce_cene}")
