from product import Product
class ProductManager:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def display_products(self):
        print("List of all the products:")
        for product in self.products:
            product.display_info()
    
    def total_value(self):
        total = sum(product.price * product.quantity for product in self.products)
        print(f"Total value of all products: {total}$")

    def remove_product(self, product_name):
        for product in self.products:
            if product.name == product_name:
                self.products.remove(product)
                print(f"Product {product_name} has been removed.")
                return
        print(f"Product {product_name} is not found")
