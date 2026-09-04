total_stock = 1000
sales = []
days = 7

for i in range(days):
    sale = int(input(f"Unesi broj prodatih artikala za dan {i+1}: "))
    sales.append(sale)

total_sales = sum(sales)
print(f"Ukupnan broj prodatih artikala je {total_sales}")

total_stock -= total_sales
print(f"Broj preostalih artikala je {total_stock}")