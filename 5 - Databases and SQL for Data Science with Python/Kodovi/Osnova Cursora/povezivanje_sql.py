import mysql.connector
 
# Creating a connection to the MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="DbSb3272GlObEaBb",
    database="library"
)
 
# Checking if the connection was successfully established
if(mydb == None):
    print("There is no connection to database.")
else:
    print("Connection to database is created.")