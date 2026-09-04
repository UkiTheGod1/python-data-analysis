import mysql.connector
 
# Connecting to the MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="DbSb3272GlObEaBb",
    database="library"
)
 
# Creating a cursor
cursor = conn.cursor()
 
# SQL query to delete books published before 1950
sql_query = "DELETE FROM Book WHERE published < 1950"
 
# Executing the query
cursor.execute(sql_query)
conn.commit()  # Saving changes to the database
 
print("Old books have been deleted from the database.")
 
# Closing the connection
cursor.close()
conn.close()
print("Database connection closed.")