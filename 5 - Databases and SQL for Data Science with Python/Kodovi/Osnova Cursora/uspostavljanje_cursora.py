import mysql.connector
# 1. Creating a connection to the database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="DbSb3272GlObEaBb",
    database="library"
)
 
# 2. Creating a cursor to execute queries
cursor = conn.cursor()
 
print("Connection established successfully, and the cursor has been created.")