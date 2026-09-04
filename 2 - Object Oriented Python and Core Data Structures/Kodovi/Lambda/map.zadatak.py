products = [
    {'name': 'Laptop', 'price': 50000},
    {'name': 'Phone', 'price': 30000},
    {'name': 'Tablet', 'price': 20000}
]

products_with_tax = list(map(lambda product: {'name': product['name'], 'price': product['price'] * 1.2}, products))

for p in products_with_tax:
    print(f"Product {p['name']} has updated its price to {p['price']}$")