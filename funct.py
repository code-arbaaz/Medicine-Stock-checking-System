import mysql.connector
def add():
    con=mysql.connector.connect(host="localhost",user="root" ,password="",database="stock")
    if con.is_connected():
        print("Established sucessfully")
    else:
        print("not connected")
    cur=con.cursor()
    r=int(input("Serial no. : "))
    n=input("Name of medicine : ")
    man=input("Manufacturer : ")
    dm=input("Date of manufacture : ")
    de=input("Date of expiry : ")
    q=int(input("Quantity : "))
    c=int(input("Cost : "))   
    cur.execute("insert into medicine values('{}' , '{}' , '{}' , '{}' , {} , {} , {} )".format(n,man,dm,de,q,c,r))
    con.commit()
    cur.close()
    
def search():
    con=mysql.connector.connect(host="localhost",user="root" ,password="",database="stock")
    if con.is_connected():
        print("Established sucessfully")
    else:
        print("not connected")
    cur=con.cursor()
    s=int(input("enter serial no. : "))
    x="select * from medicine where serialno = %s"%(s,)
    cur.execute(x)
    data = cur.fetchall()
    for i in data :
        print("____________________________________")
        print("Serial no : ",i[6])
        print("Name of medicine : ",i[0])
        print("Manufacturer : ",i[1])
        print("Date of manufacture : ",i[2])
        print("Date of expiry : ",i[3])
        print("Quantity : ",i[4])
        print("Cost : ",i[5]) 
        con.close()
    
def update():
    con=mysql.connector.connect(host="localhost",user="root" ,password="",database="stock")
    if con.is_connected():
        print("Established sucessfully")
    else:
        print("not connected")
    cur=con.cursor()
    s=int(input("enter serial no. : "))
    x="select * from medicine where serialno = %s"%(s,)
    cur.execute(x)
    data = cur.fetchall()
    for i in data :
        print("_________________________________")
        print("Serial no : ",i[6])
        print("Name of medicine : ",i[0])
        print("Manufacturer : ",i[1])
        print("Date of manufacture : ",i[2])
        print("Date of expiry : ",i[3])
        print("Quantity : ",i[4])
        print("Cost : ",i[5]) 
    print("What u want to update : "  + "\n" + "1. Name" + "\n" + "2. manufacturer " + "\n" + "3. Date of manufacture " + "\n" + "4. Date of expiry " + "\n" + "5. Quantity " + "\n" + "6. Cost " )
    t=int(input("Enter choice : "))
    if t==1:
        n1=input("Enter new name : ")
        x="update medicine set name = '%s' where serialno =%s"%(n1,s)
        cur.execute(x)
        con.commit()
        print("Updated successfully !")
    if t==2:
        man1=input("Enter new manufacturer name : ")
        x="update medicine set manufacturer = '%s' where serialno =%s"%(man1,s)
        cur.execute(x)
        con.commit()
        print("Updated successfully !")
    if t==3:
        dm1=input("Enter new Date : ")
        x="update medicine set DOM = '%s' where serialno =%s"%(dm1,s)
        cur.execute(x)
        con.commit()
        print("Updated successfully !")
    if t==4:
        de1=input("Enter new Date : ")
        x="update medicine set DOE = '%s' where serialno =%s"%(de1,s)
        cur.execute(x)
        con.commit()
        print("Updated successfully !")
    if t==5:
        q1=input("Enter new Quantity : ")
        x="update medicine set DOM = %s where serialno =%s"%(q1,s)
        cur.execute(x)
        con.commit()
        print("Updated successfully !")
    if t==6:
        c1=input("Enter new cost : ")
        x="update medicine set Cost = %s where serialno =%s"%(c1,s)
        cur.execute(x)
        con.commit()
        print("Updated successfully !")      
    con.close()
    
def delete():
    con=mysql.connector.connect(host="localhost",user="root" ,password="",database="stock")
    if con.is_connected():
        print("Established sucessfully")
    else:
        print("not connected")
    cur=con.cursor()
    s=int(input("enter serial no. : "))
    x="select * from medicine where serialno = %s"%(s,)
    cur.execute(x)
    data = cur.fetchall()
    for i in data :
        print("____________________________")
        print("Serial no : ",i[6])
        print("Name of medicine : ",i[0])
        print("Manufacturer : ",i[1])
        print("Date of manufacture : ",i[2])
        print("Date of expiry : ",i[3])
        print("Quantity : ",i[4])
        print("Cost : ",i[5]) 
        h=input("Want to delete this record y/n : ")
        if h=="y":
            x="delete from medicine where serialno = %s"%(s,)
            cur.execute(x)
            con.commit()
            print("Record deleted successfully !")
        else:
            print("Record not deleted !")
    con.close()
    
def display():
    con=mysql.connector.connect(host="localhost",user="root" ,password="",database="stock")
    if con.is_connected():
        print("Established sucessfully")
    else:
        print("not connected")
    cur=con.cursor()
    print("Want to display  1. individual   2. all")
    s=int(input("Enter choice : "))
    if s==1:
        s=int(input("enter serial no. : "))
        x="select * from medicine where serialno = %s"%(s,)
        cur.execute(x)
        data = cur.fetchall()
        for i in data :
            print("________________________________")
            print("Serial no : ",i[6])
            print("Name of medicine : ",i[0])
            print("Manufacturer : ",i[1])
            print("Date of manufacture : ",i[2])
            print("Date of expiry : ",i[3])
            print("Quantity : ",i[4])
            print("Cost : ",i[5]) 
    if s==2:
        x="select * from medicine"
        cur.execute(x)
        data = cur.fetchall()
        for i in data :
            print("Serial no : ",i[6])
            print("Name of medicine : ",i[0])
            print("Manufacturer : ",i[1])
            print("Date of manufacture : ",i[2])
            print("Date of expiry : ",i[3])
            print("Quantity : ",i[4])
            print("Cost : ",i[5])
            print("_______________________________________")
    con.close()
