import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mypydb"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS customers (name VARCHAR(255), address VARCHAR(255))")
mycursor.execute("SHOW TABLES")

for x in mycursor:
    print(x)
