import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mypydb"
)

mycursor = mydb.cursor()
mycursor.execute("UPDATE customers SET address = 'Canyon 123' WHERE name = 'John'")

mydb.commit()

print(mycursor.rowcount, "record(s) affected")
