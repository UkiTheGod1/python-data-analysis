# Product list
products = ["Laptop", "Phone", "TV", "Headphones", "Camera"]
print("List before modification:")
print(products)
 
# Removing the product at position 3
removed_item = products.pop(3)
print("List after modification:")
print(products)
print("The product at position 3 was:", removed_item)

# pop(): Briše element na zadatom indeksu i vraća njegovu vrednost