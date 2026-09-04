products_in_stock = {"Laptop", "Phone", "Headphones"}
products_on_sale = {"Phone", "Tablet", "Laptop"}

combined = products_in_stock | products_on_sale
print(combined)

intersection = products_in_stock & products_on_sale
print(intersection)

difference = products_in_stock - products_on_sale
print(difference)

