import mysql.connector
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="DbSb3272GlObEaBb",
    database="movies"
)

query = """SELECT m.title, m.budget, g.genre_id, g.name AS genre_name
           FROM movie m
           JOIN genre g ON m.genre_id = g.genre_id"""
df_movies = pd.read_sql(query, conn)
print(df_movies)

df_grouped = df_movies.groupby("genre_name")["budget"].mean().sort_values(ascending=False)
print(df_grouped)
print(df_grouped.describe())

plt.figure(figsize=(12, 8))
sns.barplot(x=df_grouped.index, y=df_grouped.values, palette="viridis")
plt.xlabel("Genre name", fontsize=12)
plt.ylabel("Budget", fontsize=12)
plt.title("Average budget per Genre", fontsize=20)
plt.xticks(fontsize=8, rotation=15)
plt.yticks(fontsize=12)
plt.show()