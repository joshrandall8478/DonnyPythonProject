def menu():
    print("Menu")
    print("--------------------")
    print("1. Look up an email")
    print("2. Add a new name and email address")
    print("3. Change an existing email address")
    print("4. Delete a name and email address")
    print("5. Quit") 
    return 

def lookUpEmail(email):
    name = str(input("Enter a name: "))
    if name in email:
            print("Name: {}".format(name))
            print("Email: {}".format(email))
            print("")
    else:
        print("Name has not been found")

def addEmail(email):
    name = str(input("Enter a name: "))
    email = str(input("Enter an email address: "))
    email.append({name: email})
    print("Name and email have been added")
    print("")

def changeEmail():
    name = str(input("Enter name: "))
    if name not in email:
            print("name not found")
            return None
    email = str(input("Enter new email address"))
    email.append({name: email})
    print("")
    

def deleteEmail(email):
    name = str(input("Enter name: ")
    if name not in email:
        print("name not found")
        print("")
        return None
    del email[name]
    print("information deleted")
    print("")
    

def saveEmail(email):
    file = open("EmailAddresses.txt","r")
    names = list(email.keys())
    for i in range(len(names)):
        file.write(names[i] + " " + email[names[i]])
        if len(names)-i > 1:
            file.write("\n")
    print("information saved")
    

def read(email):
    with open(file,'r') as file:
        file = file.read().split('\n')
        
    email = {}
    for i in range(len(file)):
        ent = file[i].split(" ")
        email.append({ent[0]: ent[1]})
    return email

def main():
    email = read("EmailAddresses.txt")
    run = true
    while run:
        menu()
        opt = int(input("Enter the command you'd like to use: ")
        if opt == 1:
                  lookupEmail(email)
        if opt == 2:
                  addEmail(email)
        if opt == 3:
                  changeEmail(email)
        if opt == 4:
                  deleteEmail(email)
        if opt == 5:
                  saveEmail(email)
                  run = False
main()
