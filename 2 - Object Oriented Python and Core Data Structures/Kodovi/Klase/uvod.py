class Product:
    name = ""
    price = 0.0
    quantity = 0

p = Product()
# Napravili praznu klasu i dodelili je promenljivoj

p.name = "Chocolate"
p.price = 56
p.quantity = 7
# Dodali smo joj vrednosti

print(f"{p.name}: price = {p.price}, quantity = {p.quantity}")
# Print time