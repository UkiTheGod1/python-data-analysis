import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
 
df = pd.read_csv("small_online_store_data.csv")
 
plt.figure(figsize=(10, 5))
sns.histplot(df["price"], bins=15, color="skyblue", edgecolor="black")

plt.title("Distribution of Product Prices")
plt.xlabel("Price ($)")
plt.ylabel("Number of Products")
plt.grid(axis="y", linestyle="--", alpha = 0.5)
plt.tight_layout()
plt.show()

# Histogram je idealan kada želimo da vidimo tačnu raspodelu po binovima – precizno brojanje.