customers = [
    {'name': 'Mark', 'spending': 75000},
    {'name': 'Anna', 'spending': 120000},
    {'name': 'John', 'spending': 50000},
    {'name': 'Eve', 'spending': 130000}
]

VIP = lambda customer: customer['spending'] >= 100000
VIP_lista = list(filter(VIP, customers))

for c in VIP_lista:
    name = c['name']
    spending = c['spending']
    print(f'Customer {name} is a VIP customer - Total spent: {spending}$')
