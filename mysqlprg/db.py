import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "Shafeeq@7799",
    database = "elchap"
)

mycursor = db.cursor()

abc = []

a = mycursor.execute("select * from user")

abc.append(a)

print(abc)
