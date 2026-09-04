import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("online_orders.csv")

category_count = df.groupby("product_category").agg(
    count = ("product_category", "count")
).sort_values(by="count", ascending=False) # .reset_index() je suvisan po meni

plt.figure(figsize=(10,6))
sns.barplot(data=category_count, x='count', y='product_category', hue='product_category', legend=True)

plt.title("Number of Orrders per Product category")
plt.xlabel("Order Count")
plt.ylabel("Product Category")
plt.show()
