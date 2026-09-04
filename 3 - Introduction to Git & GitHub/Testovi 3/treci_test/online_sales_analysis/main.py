from product import Product
from product_manager import ProductManager
from cart import Cart

product_manager = ProductManager()

product_manager.add_product(Product("Phone", 1000, 20))
product_manager.add_product(Product("Computer Screen", 300, 30))
product_manager.add_product(Product("Wireless Mouse", 50, 40))
product_manager.add_product(Product("Earbuds", 100, 10))
product_manager.add_product(Product("Playstation", 700, 20))

product_manager.display_products()

product_manager.total_value()

cart = Cart()

cart.add_to_cart(product_manager.products[0]) # Smartphone
cart.add_to_cart(product_manager.products[1]) # Monitor
cart.add_to_cart(product_manager.products[3]) # Headphones

cart.display_cart_info()
cart.total_cart_value()