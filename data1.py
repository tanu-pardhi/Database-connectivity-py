import mysql.connector as m
con = m.connect(
host = input("Enter Host: ")
port = int(input("Enter Port: "))
user = input("Enter User: ")
password = input("Enter Password: ")
database = input("Enter Database: ")
charset="utf8"
)

if con.is_connected():
    print("Connected")

cursor = con.cursor()

s = "update data set name=%s where id=%s"

name = input("Enter Name: ")
id = input("Enter ID: ")

t = (name, id)

cursor.execute(s, t)

print("Data updated")

con.commit()

cursor.close()
con.close()