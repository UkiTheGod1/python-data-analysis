# Define the list of products, each product is a tuple: (product name, quantity, price per unit)
products = [
    ("Laptop", 10, 800.00),
    ("Smartphone", 25, 500.00),
    ("Headphones", 50, 30.00),
    ("Monitor", 15, 150.00),
    ("Keyboard", 40, 20.00),
    ("Mouse", 60, 15.00)
]

total_value = 0.0
product_no = 0

for product in products:
    id = product[0]
    quantity = product[1]
    value = product[2]

    total_product_value = value * quantity
    product_no += 1
    print(f"Ukupna vrednost prozivoda {id} je {total_product_value}")
    total_value += total_product_value

print(f"Ukupna vrednost svih proizvoda je {total_value}")