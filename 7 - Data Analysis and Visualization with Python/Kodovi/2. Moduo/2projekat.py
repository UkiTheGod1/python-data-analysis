import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("online_store_ratings_through_years.csv")
df["date"] = pd.to_datetime(df["date"], errors='coerce')
df['year'] = df['date'].dt.year

df_grouped = df.groupby("year")["rating"].mean().reset_index()

plt.figure(figsize=(10,6))
sns.lineplot(data=df_grouped, x='year', y='rating', marker='o', color='red')
plt.title("Average Rating per Year")
plt.xlabel("Years")
plt.ylabel("Ratings")
plt.show()