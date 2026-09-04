import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
 
df = pd.read_csv("books.csv")

df["published_century"] = ((df["year_published"] - 1) // 100 + 1).astype("Int64")
avg_rating_by_century = df.groupby("published_century")["rating"].mean().reset_index()

plt.figure(figsize=(10,6))
sns.lineplot(data=avg_rating_by_century, x='published_century', y='rating', marker='o')
plt.xlabel("Century of Publication")
plt.ylabel("Average Rating")
plt.grid(True)
plt.tight_layout()
plt.show()