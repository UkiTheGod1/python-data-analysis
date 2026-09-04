import mysql.connector
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="DbSb3272GlObEaBb",
    database="library"
)

cursor = conn.cursor()

firstname = input("Enter the user's first name: ").strip()
lastname = input("Enter the user's last name: ").strip()
city_id = input("Enter the user's city id: ").strip()

sql_query = "INSERT INTO user (firstname, lastname, city_id) VALUES (%s, %s, %s)"
values = (firstname, lastname, city_id)

cursor.execute(sql_query, values) # Pokrece sql upit
conn.commit() # Samo sacuvava u bazu (server)

print(f"User {firstname} {lastname} {city_id} successfully added to the database.")

cursor.close()
conn.close()
