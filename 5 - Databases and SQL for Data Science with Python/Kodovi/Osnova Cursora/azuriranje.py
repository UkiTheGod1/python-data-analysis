import mysql.connector
 
# Connecting to the MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="DbSb3272GlObEaBb",
    database="library"
)
 
# Creating a cursor to execute queries
cursor = conn.cursor()
 
# SQL query to update the publication year
sql_query = """UPDATE Book  
               SET published = 2025 
               WHERE title = 'To Kill a Mockingbird'"""
 
# Executing the query
cursor.execute(sql_query)
conn.commit()  # Saving changes to the database
 
print("Data successfully updated.")

# Moguci nacin
# sql_query = "UPDATE Book SET published = %s WHERE title = %s"
# values = (2025, "To Kill a Mockingbird")
# cursor.execute(sql_query, values)
# conn.commit() 


print("Data has been successfully updated.")
# Closing the connection
cursor.close()
conn.close()
print("Database connection closed.")