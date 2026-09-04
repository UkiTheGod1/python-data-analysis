import pandas as pd
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="DbSb3272GlObEaBb",
    database="library"
)

query = "SELECT book_id, title, published, genre_id FROM Book"
df_books = pd.read_sql(query, conn) # Upit i SQL server

print(df_books.head())

print(df_books.describe())             # prikazuje neke statistike 
print(df_books['genre_id'].unique())   # prikazuje unikatne vrednosti

df_grouped = df_books.groupby("genre_id")["book_id"].count()   # grupise po zanru i prikazuje koliko knjiga pripada kojem zanru
print(df_grouped)

conn.close()