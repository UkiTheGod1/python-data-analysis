import mysql.connector
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
 
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="DbSb3272GlObEaBb",
    database="library"
)
 
query = "SELECT book_id, title, published, genre_id FROM Book"
df_books = pd.read_sql(query, conn)
conn.close()

df_grouped = df_books.groupby("genre_id")["book_id"].count()
  
plt.figure(figsize=(10, 6)) # Velicina grafikona (10x6 incha)
sns.barplot(x=df_grouped.index, y=df_grouped.values, palette="viridis") # viridis je gradijent boja
 
plt.xlabel("Genre (ID)")
plt.ylabel("Number of Books")
plt.title("Number of Books per Genre")
plt.xticks(rotation=45)  # Rotating labels if there are many
plt.show()