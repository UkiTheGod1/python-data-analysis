products = [
    {'name': 'Laptop', 'price': 85000, 'discount': True},
    {'name': 'Phone', 'price': 50000, 'discount': False},
    {'name': 'TV', 'price': 60000, 'discount': True},
    {'name': 'Camera', 'price': 25000, 'discount': False}
]

# Direktno sortiranje liste i samim tim azuriranje same liste
# products.sort(key=lambda product: product['discount'] = True)

# sorted() vraća novu listu i ne menja originalnu sekvencu.
# sort() menja postojeću listu, bez kreiranja nove

sorted_products = sorted(products, key = lambda product: product['price'])
print(sorted_products)

n = 0
for p in sorted_products:
    ime = p['name']
    cena = p['price']
    popust = p['discount']
    n += 1
    print(f'{n}. product is {ime} with a price of {cena} - discount: {popust}')