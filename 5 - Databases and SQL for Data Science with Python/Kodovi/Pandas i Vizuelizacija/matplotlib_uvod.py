import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="DbSb3272GlObEaBb",
    database="library"
)

query = "SELECT book_id, title, published, genre_id FROM Book"
df_books = pd.read_sql(query, conn)
print(df_books.head())
conn.close()

plt.hist(df_books['published'], bins=10, color='skyblue', edgecolor='black') # Bins su brojevi stubova
plt.xlabel("Published Year")
plt.ylabel("Number of Books")
plt.title("Distribution of Books by Year")
plt.show()