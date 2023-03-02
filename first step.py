'''

main file
=========

'''
print("Welcome to Contact Directory Console App")
print()
def validate_mob(mn):
    if mn.isdigit() and len(mn)==10:
        return 1
    else:
        return 0
def create_contact():
    fp=open('data.txt','a')
    n=input("Enter Name:")
    mn=input("Enter Mobile Number:")
    res=validate_mob(mn)
    if res==1:
        a,b=searchmob(mn)
        if b==1:
            print("Number Already Exist")
        else:
          d=n+':'+mn+'\n'
          fp.write(d)
          fp.close()
          print("Contact Created Successfully!!")
    else:
        print("Please Enter Valid mobile number")

def display():
    fp=open('data.txt','r')
    d=fp.read()
    print("=================Contact Directory=================")
    print()
    print(d)
    print("---------------------------------------")

def searchmob(n):
    
    fp=open('data.txt','r')
    data=fp.readlines()
    for x in data:
            l=x.split(":")
            if int(n)==int(l[1]):
                #print("Contact Found:")
                #print(x)

                return x,1
            else:
                return '',0
        
def searchname():
    print("Seach Contact Number by Name:")
    ns=input("Enter Name:")
    fp=open('data.txt','r')
    data=fp.readlines()
    flag=0
    for x in data:
            l=x.split(":")
            if ns.upper()==l[0].upper():
                print(x)
                flag=1
            if flag==0:
                print("NOT FOUND!!!")
        
    

while True:
    print()
    print("1.Create Contact")
    print("2.Veiw Contact")
    print("3.Search By Name")
    print("4.Search By Mobile Number")
    print("5.Exit")
    ch=int(input("Enter Your Choice:"))

    if ch==1:
        create_contact()
        
    elif ch==2:
        display()
    elif ch==3:
        searchname()
    elif ch==4:
        ms=input("Enter Mobile Number to be search:")
        a,b=searchmob(ms)
        print(a)
        print(b)
        if b==1:
            print("Contact Found")
        else:
            print("NOT FOUND")
    elif ch==5:
        break
    else:
        print("-->Please Enter Valid Option!!!")
else:
    print("Thank You for  using application")
