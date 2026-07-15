import funct

while True:
    print("1. Add " + "\n" + "2. Search" + "\n" + "3. Update" + "\n" + "4. Delete" + "\n" + "5. Display")
    x=int(input("Enter choice : "))
    if x==1:
        while True:
            funct.add()
            ch=input("want to add more y/n  : ")
            if ch=="n" :
                break
    if x==2:
        while True:
            funct.search()
            chh=input("want to search more y/n  : ")
            if chh=="n" :
                break
    if x==3:
        while True:
            funct.update()
            chhh=input("want to update more y/n  : ")
            if chhh=="n" :
                break
    if x==4:
        while True:
            funct.delete()
            chhhh=input("want to delete more y/n  : ")
            if chhhh=="n" :
                break        
    if x==5:
         while True:
            funct.display()
            chhhhh=input("want to display more y/n  : ")
            if chhhhh=="n" :
                break 
    c=input("Want to continue program y/n  : ")
    if c=="n" :
        break