import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("ecommerce_orders_may.csv")
completed_orders = df[df["status"] == "Completed"]
completed_orders['total'] = completed_orders['price'] * completed_orders['quantity']

category_totals = completed_orders.groupby("category", as_index=False)["total"].sum()
category_totals = category_totals.sort_values(by="total", ascending=False)

plt.figure(figsize=(10,6))
sns.barplot(data=category_totals, x='category', y='total', hue="category", palette="Blues")
plt.xlabel("Categories")
plt.ylabel("Total Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("total_revenue_by_category.png")