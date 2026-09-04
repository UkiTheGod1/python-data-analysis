from sales_operation import *

sales = {

    "Laptop": 15,

    "Mouse": 150,

    "Keyboards": 85,

    "Monitor": 30,

    "USB Cables": 200
}

sales["Monitor"] += 5

# if "Web Camera" not in sales:
#     sales["Web Camera"] = 0    - pokušaćemo sa try-except:

try:
    print(f'Veb kamera je prodata {sales["Web Camera"]} puta') # Ako postoji, ispisuje koliko puta se prodala veb kamera
except KeyError:
    sales["Web Camera"] = 0                                    # Ako ne postoji, dodaje se u rečnik i dodeljuje vrednost 0

# Nisam siguran gde je još potrebno ubaciti try-except, jedino ovde imamo nedostajući ključ. Kod funkcija samo kod get_product_sales()...

print("Azuziran recnik glasi:",sales)
print("Ukupno proizvoda prodato:", total_sold(sales))
print("Proizvod koji se najvise prodao je", most_sold(sales)) 
print("Proizvod koji se najmanje prodao je", least_sold(sales))

print("Proizvodi koji su kriticni:", critical(sales))

validate_sales_data(sales)
get_product_sales(sales, 'LAPTOP') # Provera koliko puta je prodat Laptop, nezavisno od velicine slova
get_product_sales(sales, 'Tablet') # Provera koliko puta je prodat nepostajani proizvod - ispisuje grešku


# Zadatak nisam 100% shvatio i ima nekih stvari koje verovatno nisam uradio kako je zamisljeno, molim Vas, skrenite mi paznju sta nisam
# uradio kako je predvidjeno pre ocenjivanja.