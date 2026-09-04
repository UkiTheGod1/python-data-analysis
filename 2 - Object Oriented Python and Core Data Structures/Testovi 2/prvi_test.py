sales = {

    "Laptop": 15,

    "Mouse": 150,

    "Keyboards": 85,

    "Monitor": 30,

    "USB Cables": 200
}

sales["Monitor"] += 5 # Dodavanje vrednosti pre racunanja ukupne vrednosti

keys = sales.keys()
values = sales.values()

total_sold = sum(values)

most_sold = max(sales, key=lambda item: sales[item]) # SLAMANJEEEEEE

least_sold = min(sales, key=lambda item: sales[item])

if "Web Camera" not in sales:
    sales["Web Camera"] = 0

print("Azuziran recnik glasi:",sales)
print("Ukupno proizvoda prodato:", total_sold)
print("Proizvod koji se najvise prodao je", most_sold) 
print("Proizvod koji se najmanje prodao je", least_sold)

def critical(sales):
    below_50 = [product for product, amount in sales.items() if amount < 50] # LIST COMPREHENSION
    return below_50

print("Proizvodi koji su kriticni:", critical(sales))

def negative_products(sales):
    negative = False
    for product, value in sales.items():
        if value < 0:
            print(f"Proizvod {product} ima negativnu vrednost {value}")
            negative = True
    if not negative:
        print("Svi proizvodi imaju pozitivnu vrednost")
    return negative

negative_products(sales)
