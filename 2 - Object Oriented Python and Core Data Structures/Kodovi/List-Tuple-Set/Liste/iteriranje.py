products = ["Samsung Phone", "Laptop", "iPhone", "TV", "Headphones", "Camera", "Xiaomi Phone"]
x = input("Unesi svoj product: ")

for product in products:
    if x in product:
        print(product)