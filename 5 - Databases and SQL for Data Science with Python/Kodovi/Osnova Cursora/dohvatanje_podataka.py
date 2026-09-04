import mysql.connector
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="DbSb3272GlObEaBb",
    database="library"
)

cursor = conn.cursor()

# Defining the SQL query
sql_query = """SELECT title, published  
               FROM Book 
               WHERE genre_id = (SELECT genre_id FROM Genre WHERE name = 'Fiction')"""
 
# Executing the query
cursor.execute(sql_query)  
 
# Fetching all results
books = cursor.fetchall()  
 
# Displaying results
for book in books:
    print(book)