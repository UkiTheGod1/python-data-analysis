import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="DbSb3272GlObEaBb",
    database="movies"
)

query = """SELECT c.country_id, c.country_name, AVG(m.box_office) as average_profit
        FROM Movie m
        JOIN Country c ON m.country_id = c.country_id
        GROUP BY c.country_id, c.country_name"""

df_movies = pd.read_sql(query, conn)
conn.close()

plt.figure(figsize=(10,6))
sns.barplot(x=df_movies["country_name"], y=df_movies["average_profit"], palette="plasma")
plt.xlabel("Country name", fontsize=14)
plt.ylabel("Box office", fontsize=14)
plt.title("Box office per country", fontsize=20)
plt.show()

# Preporuka - Ulagati u filmove iz Sjedinjenih Američkih Država je uvek sigurna opcija !