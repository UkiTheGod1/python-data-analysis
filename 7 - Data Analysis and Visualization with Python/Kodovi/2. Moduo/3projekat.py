import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("books.csv")

df_grouped = df.groupby("section").agg(
    count = ("title", "count"),
    sum = ("times_borrowed", "sum")
)

df_sorted = df_grouped.sort_values(by="sum", ascending=False)
df_sorted['copies_to_borrow_ratio'] = df_sorted['sum'] / df_sorted['count'] 
df_sorted = df_sorted.sort_values(by=['copies_to_borrow_ratio'], ascending=False).reset_index()


plt.figure(figsize=(12,8))
sns.barplot(data=df_sorted, x="sum", y='section', palette='magma')
plt.title("Title")
plt.xlabel("Borrowings per Section")
plt.ylabel("Library Section")
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()