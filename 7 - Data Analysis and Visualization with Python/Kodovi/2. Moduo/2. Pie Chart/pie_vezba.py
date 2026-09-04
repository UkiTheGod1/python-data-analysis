import matplotlib.pyplot as plt 

delivery_types = ['Standard', 'Express', 'Pickup']
orders = [180, 70, 50]

plt.figure(figsize=(6,6))
plt.pie(orders, labels=delivery_types, autopct='%.2f%%')
plt.title("Distribution of Orders by Delivery Type")
plt.show()
