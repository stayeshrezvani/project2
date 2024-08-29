#project

contact={}

def new() :  #براي مخاطب جديد
    name=input("please enter your name:")
    phonenumber=input("enter your phone number:")
    contact[name]=phonenumber
 
def delete():  # براي حذف
    name=input("enter your name for delet:")
    del contact[name]
    print("done")

def change():  #براي تغيير
    name=input("enter your name for change:")
    phonenumber=input("enter your phone number:")
    contact[name]=phonenumber
    print("done!")
    print(contact)
 
def show():   #براي نمايش همه 
    print(contact)

while True: # حلقه براي وارد بررسي
    x=input("enter:")
    if x=="out":
        print("Good Bye!")
        break
    elif x=="new":
        new()
    elif x=="delete":
        delete()
    elif x=="change":
        change()
    elif x=="show":
        show()
    else:
        print("invalid !")














    
        
