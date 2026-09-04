import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
 
df = pd.read_csv("online_store_order_items.csv")
 
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x="order_value", y="category", hue="category")
 
plt.title("Order Values Distribution Per Category")
plt.xlabel("Order Value (€)")
plt.ylabel("Category")
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()