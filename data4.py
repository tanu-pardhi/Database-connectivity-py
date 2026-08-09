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

if con.is_connected():
    print("Connected")

cursor = con.cursor()

s = "select * from data where id=%s"

id = input("Enter ID: ")

t = (id,)

cursor.execute(s, t)

result = cursor.fetchone()

if result:
    print("Record Found:", result)
else:
    print("Record Not Found")

cursor.close()
con.close()