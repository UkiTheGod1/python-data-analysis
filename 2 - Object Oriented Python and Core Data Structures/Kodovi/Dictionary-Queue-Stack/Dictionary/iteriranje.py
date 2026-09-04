cart = [
 
    {'item': 'Laptop', 'count': 5, 'price': 700},
 
    { 'item': 'Computer mouse', 'count': 10, 'price': 20},
 
    { 'item': 'Keyboard', 'count': 7, 'price': 30},
 
    { 'item': 'Мonitor', 'count': 3, 'price': 150},
 
    { 'item': 'Laptop', 'count': 2, 'price': 700},
 
    { 'item': 'Computer mouse', 'count': 5, 'price': 20},
 
]

total_income = 0
 
for stvar in cart:
 
    total_income += stvar['count'] * stvar['price']
 
print(f"Total income from sales: ${total_income}")