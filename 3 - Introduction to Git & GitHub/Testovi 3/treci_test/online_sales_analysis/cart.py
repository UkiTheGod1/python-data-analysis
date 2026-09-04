from product import Product

class Cart:
    def __init__(self):
        self.cart_items = []

    def add_to_cart(self, product):
        for item in self.cart_items:
            if item.name == product.name:
                item.update_quantity(item.quantity + 1)
                print(f"Product {product.name} quantity updated in cart.")
                return
        product.update_quantity(1)
        self.cart_items.append(product)
        print(f"Product {product.name} has been added to cart.")

    def total_cart_value(self):
        total = sum([product.price * product.quantity for product in self.cart_items])
        print(f"Total cart value is {total}$")

    def display_cart_info(self):
        print("Items in the cart:")
        for product in self.cart_items:
            product.display_info()