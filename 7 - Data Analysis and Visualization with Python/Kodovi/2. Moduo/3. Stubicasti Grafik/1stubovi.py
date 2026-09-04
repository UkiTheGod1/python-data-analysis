import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
 
df = pd.read_csv("books.csv")
 
section_counts = df.groupby("section").agg(
    count=("section", "count")).reset_index().sort_values(by="count", ascending=False)
 
plt.figure(figsize=(8, 6))
sns.barplot(data=section_counts, x="count", y="section", hue="section", palette="pastel", legend=True)
 
plt.title("Books per section")
plt.xlabel("Number of books")
plt.ylabel("Section")
plt.tight_layout()
plt.show()