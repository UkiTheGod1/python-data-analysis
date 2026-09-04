class Product:
    tax = 0.2
 
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
 
    def display_product_info(self):
        print(f"Product: {self.name}")
        print(f"Price per unit (with tax): {self.price * (1 + Product.tax)}")
        print(f"Quantity: {self.quantity}")
        print(f"Total price: {self.calculate_total_price()}")
 
    def calculate_total_price(self):
        return self.price * (1 + Product.tax) * self.quantity
    
    def update_price(self, new_price):
        self.price = new_price
        print(f"Product: {self.name}")
        print(f"New price per unit (with tax): {self.price * (1 + Product.tax)}")
        print(f"Quantity: {self.quantity}")
        print(f"New total price: {self.calculate_total_price()}")

p1 = Product("Kurac", 200, 10 )
p2 = Product("Kid", 150, 13)

p1.display_product_info()
p2.display_product_info()

p1.update_price(250)