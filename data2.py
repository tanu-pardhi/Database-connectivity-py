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

s = "delete from data where id=%s"

id = input("Enter ID : ")

t = (id,)

cursor.execute(s, t)

print("Data Deleted")

con.commit()

con.close()
cursor.close()