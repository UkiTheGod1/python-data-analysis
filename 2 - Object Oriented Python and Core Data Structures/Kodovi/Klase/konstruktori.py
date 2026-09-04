class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def display_info(self):
        return f"Product: {self.name}, Price: {self.price} euros, Quantity: {self.quantity}"

p = Product("Chocolate", 56, 7)
print(p.display_info())