import mysql.connector as m

con = m.connect(
    host="enter your localhost",
    port="enter your port",
    user="enter your user",
    password="enter your password",
    database="enetr your database",
  
)

if(con.is_connected):
    print("Connected Successfully")
else:
    print("err in connection")

cursor=con.cursor()


sql=sql = "INSERT INTO unity(stu_name, stu_intrest, ph_no) VALUES(%s, %s, %s)"
stu_name=input("Enter Name :")
stu_intrest=input("Enter Intrest :")
ph_no=input("Enter phone no :")
t=(stu_name,stu_intrest,ph_no)

cursor.execute(sql,t)

con.commit()
print("Data Inserted")

