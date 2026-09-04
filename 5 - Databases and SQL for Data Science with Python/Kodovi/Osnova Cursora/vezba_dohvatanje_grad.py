import mysql.connector
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="DbSb3272GlObEaBb",
    database="library"
)

cursor = conn.cursor()

sql_query = """SELECT firstname, lastname, city_id
               FROM User
               WHERE city_id = (SELECT city_id FROM City WHERE name = 'Thompsonfurt')"""
 
cursor.execute(sql_query)  

users = cursor.fetchall()  

for user in users:
    print(user)