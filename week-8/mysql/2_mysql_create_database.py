import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE mypydb")
mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)
