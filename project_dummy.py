import mysql.connector as m 

con=m.connect(
    host="Enter your host",
    port='Enter your port number',
    user="Enter your root",
    password="Enter password",
    database="Enter your database",
    charset="utf8"
)

if(con.is_connected):
    print("Connected")

else:
    print("Error in connection")

cursor=con.cursor()
choice=1
choice2=1
while choice!=0:
 print("-----MENU-----")
 print("1.Insert Data")
 print("2.Show Data")
 print("3.Update Data")
 print("4.Delete Data")
 print("0.Exit")

 choice=int(input("Enter your Choice : "))

 if choice==1:
  
  id=input("Enter ID : ")
  name=input("Enter Name : ")
  mob=input("Enter mobile number : ")
 
  sql="insert into stud values(%s,%s,%s)"
  t=(id,name,mob)

  cursor.execute(sql,t)
  con.commit()
  print("Data Inserted ")


 elif choice==2:
   
    
    cursor.execute("select * from stud")
    r=cursor.fetchall()
    for i in r:
       print(i)
    

 elif choice==3:
        while choice2!=0:
            print("1.name")
            print("2.id")
            print("3.mobile no")
            choice2=int(input("Enter Choice : "))
            if choice2==1:
                print("Name")
                s="update stud set name=%s where id=%s"
                name=input("Enter Name : ")
                id=input("Enter Id : ")
                 
                t1=(name,id)
                cursor.execute(s,t1)
                con.commit()
                print("Data Inserted ")
                

            elif choice2==2:

                s="update stud set id=%s where name=%s"
                name=input("Enter name : ")
                id=input("Enter new ID : ")
                
                t2=(id,name)
                cursor.execute(s,t2)
                con.commit()
                print("Data Inserted")
                

            elif choice2==3:
               
                s="update stud set mob=%s where id=%s"
                id=input("Enter id : ")
                mob=input("Enter mob : ")
               
                t3=(mob,id)
                cursor.execute(s,t3)
                con.commit()
                print("Data Inserted")
                
            elif choice2==0:
                 print("Back")
 elif choice==4:
   
    s="delete from stud where id=%s"
    id=input("Enter Id : ")
    t4=(id,)
    cursor.execute(s,t4)
    print("Data Deleted ")
    con.commit()
    

 elif choice==0:
    con.close()
    cursor.close()
    print("Program Close")
    

else :
  print("Invalid Choice")
  