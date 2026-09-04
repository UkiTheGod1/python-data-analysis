import pandas as pd
import matplotlib.pyplot as plt
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="DbSb3272GlObEaBb",
    database="movies"
)

query = "SELECT budget, box_office FROM movie"
df_movies = pd.read_sql(query, conn)
conn.close()

df_grouped = df_movies.groupby("budget")

plt.figure(figsize=(10, 6))
plt.scatter(df_movies["budget"], df_movies["box_office"], color="purple", edgecolor="black")
plt.xlabel("Budget")
plt.ylabel("Box Office")
plt.title("Correlation between budget and box office")
plt.show()

correlation = df_movies[['budget', 'box_office']].corr().iloc[0,1] 
print(f"Pearson korelacija između budžeta i zarade: {correlation:.2f}")

# Pearson korelacija između budžeta i zarade: 0.80 - Jaka pozitivna veza (kao što vidimo iz grafika)