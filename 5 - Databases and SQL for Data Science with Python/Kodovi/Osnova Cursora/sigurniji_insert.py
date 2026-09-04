import mysql.connector
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="DbSb3272GlObEaBb",
    database="library"
)
cursor = conn.cursor()
print("Connection established successfully, and the cursor has been created.")

firstname = input("Enter the author's first name: ").strip()
lastname = input("Enter the author's last name: ").strip()

sql_query = "INSERT INTO Author (firstname, lastname) VALUES (%s, %s)"
values = (firstname, lastname)

cursor.execute(sql_query, values)
conn.commit()

print(f"Author {firstname} {lastname} successfully added to the database.")
# Closing the database connection

cursor.close()
conn.close()
print("Database connection closed.")