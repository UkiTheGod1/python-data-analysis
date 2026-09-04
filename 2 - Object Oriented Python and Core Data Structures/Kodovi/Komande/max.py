products = [
    ("Laptop", 10, 800.00),
    ("Smartphone", 25, 500.00),
    ("Headphones", 50, 30.00),
    ("Monitor", 15, 150.00),
    ("Keyboard", 40, 20.00),
    ("Mouse", 60, 15.00)
]

maksimal = max(products, key=lambda x: x[1]) 

# products - koja lista
# key=lambda - definise sledeci pojam
# x: x[1] - vraca x (celu torku), ali gleda samo "x[1]" (drugi item u torki koji je integer)

print(maksimal)