sales_data = [
    {'product': 'Smartphone', 'month': 'January', 'quantity': 150},
    {'product': 'Laptop', 'month': 'January', 'quantity': 80},
    {'product': 'Tablet', 'month': 'January', 'quantity': 50},
    {'product': 'Smartphone', 'month': 'February', 'quantity': 200},
    {'product': 'Laptop', 'month': 'February', 'quantity': 90},
    {'product': 'Tablet', 'month': 'February', 'quantity': 60},
    {'product': 'Smartphone', 'month': 'March', 'quantity': 250},
    {'product': 'Laptop', 'month': 'March', 'quantity': 100},
    {'product': 'Tablet', 'month': 'March', 'quantity': 70},
]

total_sales_by_product = {} # Pravimo novi prazan recnik za proizvode i mesece
total_sales_by_month = {}

for item in sales_data: # Iteriramo kroz sve recnike koji se nalaze u listi
    product = item['product'] # "item[product]" vraca vrednost, a ne kljuc, znaci "product" ce biti jednak 'Smartphone' ili 'Laptop'...
    month = item['month'] # Definisemo promenljive i stavljamo im vrednosti kljuceva u zagradi
    quantity = item['quantity']

    if product not in total_sales_by_product: # Ako se 'product' (Smartphone, Laptop, Tablet) ne nalazi u listi (a ne nalazi se), radi sledece:
        total_sales_by_product[product] = 0   # Stavlja ga u recnik i dodeljuje mu vrednost 0 (VREDNOSTI IZ LISTE POSTAJU KLJUCEVI!!!)
    total_sales_by_product[product] += quantity   # Ako ga vec ima u recniku (a dodali smo ga malopre) na vrednost 0 dodaje vrednosti quantity-a

    if month not in total_sales_by_month:     # Isti postupak samo za mesece
        total_sales_by_month[month] = 0
    total_sales_by_month[month] += quantity

print("Total sales by product:") # Printuje                 
for product, total in total_sales_by_product.items():   # "for x, y" - x je kljuc, a y je vrednost koja se nalazi u recniku (.items() je za sve
    print(f"- {product}: {total} units")                #                                                     a .keys() i .values() samo za jedno)

print("\nTotal sales by month:") # \n mislim da pravi prazan prostor pre neko krene da printuje
for month, total in total_sales_by_month.items():
    print(f"- {month}: {total} units")
