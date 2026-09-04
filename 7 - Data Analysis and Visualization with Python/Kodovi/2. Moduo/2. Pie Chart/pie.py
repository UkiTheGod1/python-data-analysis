import matplotlib.pyplot as plt
 
categories = ['Electronics', 'Clothing', 'Home', 'Books', 'Toys']
orders = [120, 90, 60, 80, 50]
 
plt.figure(figsize=(6, 6))
plt.pie(orders, labels=categories, autopct='%1.1f%%', startangle=90) # autopct='%1.1f%%' automatski prikazuje procente, startangle=90 okreće dijagram radi boljeg pregleda
plt.title("Share of Orders by Product Category")
plt.show()