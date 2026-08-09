import mysql.connector as m

host = input("Enter Host: ")
port = int(input("Enter Port: "))
user = input("Enter User: ")
password = input("Enter Password: ")
database = input("Enter Database: ")

con = m.connect(
    host=host,
    port=port,
    user=user,
    password=password,
    database=database,
    charset="utf8"
)

if(con.is_connected):
    print("Connected")

cursor = con.cursor()

s = "select * from data"

cursor.execute(s)

result = cursor.fetchall()

for row in result:
    print(row)

cursor.close()
con.close()