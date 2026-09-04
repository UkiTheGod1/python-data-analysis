import mysql.connector
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="DbSb3272GlObEaBb",
    database="library"
)
cursor = conn.cursor()
 
print("Connection established successfully, and the cursor has been created.")

sql_query = "INSERT INTO Author (firstname, lastname) VALUES ('Harper', 'Lee')"
cursor.execute(sql_query)  # Executes the SQL query
conn.commit()  # Saves changes to the database
print("Author added successfully.")