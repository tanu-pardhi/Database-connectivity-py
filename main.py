import mysql.connector as m

con = m.connect(
    host="Enter your host",
    port=" Enter your port number",
    user="Enter your root",
    password="Enter your password",
    database="Enter your database",
  
)

if(con.is_connected):
    print("Connected Successfully")
else:
    print("err in connection")

cursor=con.cursor()

cursor.execute("insert into stu values('Nikhil','98564772'),('Amisha',56457657)")
print("Data Inserted")
con.commit()

