from product import Product

class User:
    def __init__(self, name, username, phone, address):
        self.name = name
        self.username = username
        self.phone = phone
        self.address = address
        self.shopping_history = []

# U zadatku pise definisati "check_email" - smatram da je to greska i da se odnosi na Employee

    def total_spent(self):
        total = sum(product.price for product in self.shopping_history)
        print(f"User {self.name} has spent a total of {total}$")

    def add_product(self, product: Product):
        self.shopping_history.append(product)
        print(f'User {self.name} has bought {product.name}')

