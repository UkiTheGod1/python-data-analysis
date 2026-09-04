class Product:  
    name = ""  
    price = 0.0 
    quantity = 0 
 
    # Define a method for applying a discount  
    def apply_discount(p):
        p.price *= 0.9
    def hello(self):
        print("Hello")
    # Mora da postoji parametar

p = Product()

p.price = 150

print(f"price = {p.price}")
p.apply_discount()
print(f"price = {p.price}")
p.hello()
