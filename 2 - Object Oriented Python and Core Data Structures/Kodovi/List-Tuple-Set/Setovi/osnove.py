products_in_stock = {"Laptop", "Phone", "TV"}
products_in_stock.add("Headphones")
print(products_in_stock)  # {"Laptop", "Phone", "TV", "Headphones"}

products_in_stock2 = {"Laptop", "Phone", "TV", "Headphones"}
products_in_stock2.remove("TV")
print(products_in_stock2)  # {"Laptop", "Phone", "Headphones"}

products_in_stock3 = {"Laptop", "Phone", "TV", "Headphones"}
products_in_stock3.discard("Printer") # Does not raise an error even if "Printer" is not in the set
print(products_in_stock3) # {"Laptop", "Phone", "TV", "Headphones"}

products_on_sale = {"Phone", "Tablet", "Laptop"}
all_products = products_in_stock.union(products_on_sale)
print(all_products)  # {"Laptop", "Phone", "Headphones", "Tablet"}

products_in_stock = {"Laptop", "Phone", "TV"}
common_products = products_in_stock.intersection(products_on_sale)
print(common_products)  # Output: {"Phone", "Laptop"}

products_only_in_stock = products_in_stock.difference(products_on_sale)
print(products_only_in_stock)  # {"Headphones"}

customers = ["Emma", "John", "Emma", "Sophia", "John"]
unique_customers = set(customers)
print(unique_customers)  # Output: {"Emma", "John", "Sophia"}