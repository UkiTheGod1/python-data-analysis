import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
 
df = pd.read_csv("small_online_store_data.csv")
 
plt.figure(figsize=(10, 5))
sns.kdeplot(df["price"], fill=True, color="skyblue")
 
plt.title("Smoothed Distribution of Product Prices (KDE Only)")
plt.xlabel("Price ($)")
plt.ylabel("Density")
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()

# KDE kriva je naš izbor kada nam je važna šira slika – oblik, smer i energija podataka.