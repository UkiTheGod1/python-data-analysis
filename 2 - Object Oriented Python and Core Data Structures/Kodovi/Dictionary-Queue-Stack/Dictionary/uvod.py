order = {
 
    "customer": "John Smith",
 
    "product": "Laptop",
 
    "price": 75000,
 
    "date": "2024-10-15",
 
    "status": "delivered",
 
    "delivery_service": "DHL"
 
}

# x = ('laptop', 'smartphone', 'tablet')  # Option 1 - Tuple
 
# x = {'category': 'electronics', 'product_name': 'smartphone', 'price': 500, 'in_stock': True}  # Option 2 - Dictionary
 
# x = ['laptop', 'mouse', 'keyboard']  # Option 3 - List

print(order["customer"]) # - Printuje "John Smith"

order["status"] = "in transit" # - Zamenenjuje kljuc statusa sa "delivered" na "in transit"

print(order["status"]) # - Printuje "in transit" jer smo promenila na "in transit" sa "delivered"

order["estimated_time_of_arrival"] = "2024-10-18" # - Dodaje novu vrednost recniku koja ne postoji

print(order["estimated_time_of_arrival"]) # - Printuje tu vrednost 

del order["delivery_service"] # - Brise delivery service i kljuc i vrednost (logicno)

print(order)
print(" ")

values = order.values()
for k in values:
    print(k) # - Printuje vrednosti kljuceva
print(" ")

keys = order.keys()
for k in keys:
    print(k) # - Printuje samo kljuceve
print(" ")

for key, value in order.items():   # -  Iterira kroz ceo recnik
 
    print(f"{key}: {value}")

print(values)