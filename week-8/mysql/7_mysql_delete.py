import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mypydb"
)

mycursor = mydb.cursor()
mycursor.execute("DELETE FROM customers WHERE name = 'John'")

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")
