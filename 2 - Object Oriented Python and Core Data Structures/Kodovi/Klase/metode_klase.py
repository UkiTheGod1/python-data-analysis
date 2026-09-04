class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    @classmethod
    def create_from_input(cls):
        name = input("Name: ")
        price = int(input("Price: "))
        quantity = int(input("Quantity: "))
        return cls(name, price, quantity)
    
p1 = Product("Uros", 6, 10)
print(p1.name, p1.price, p1.quantity)
p2 = Product.create_from_input()
print(p2.name, p2.price, p2.quantity)