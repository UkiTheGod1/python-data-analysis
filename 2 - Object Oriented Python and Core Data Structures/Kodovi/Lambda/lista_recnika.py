orders = [
    {'product': 'Laptop', 'quantity': 40, 'price': 500},
    {'product': 'Tablet', 'quantity': 220, 'price': 150},
    {'product': 'TV', 'quantity': 100, 'price': 700},
    {'product': 'PC', 'quantity': 20, 'price': 1200}

]
# Moze pomocu funkcija, ali je mnogo duze

# def calculate_total(orders):
#     for order in orders:
#         product = order['product']
#         quantity = order['quantity']
#         price = order['price']
#         total = quantity * price
#         print(f'{product} - {total}$')

calculate_total = lambda order: order['quantity'] * order['price']

# ovo sto je posle lambde uglavnom ide u zagradu kad pozivamo funkciju "calculate_total(order)"
for order in orders:
    total = calculate_total(order)
    print(f"{order['product']} - {total}$")