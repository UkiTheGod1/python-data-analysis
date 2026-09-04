products = [
    {'name': 'Laptop', 'price': 85000, 'discount': True},
    {'name': 'Phone', 'price': 50000, 'discount': False},
    {'name': 'TV', 'price': 60000, 'discount': True},
    {'name': 'Camera', 'price': 25000, 'discount': False}
]

products_on_sale = list(filter(lambda product: product['discount'] == True, products))

for p in products_on_sale:
    print(f'Product {p['name']} is on sale: {p['price']}$')