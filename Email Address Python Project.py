def menu():
    print("Menu")
    print("-------------------------")
    print("1. Look up an email")
    print("2. Add a new name and email address")
    print("3. Change an existing email address")
    print("4. Delete a name and email address")
    print("5. Quit") 
    return 

def lookUpEmail(name,em):
    name = str(input("Enter a name: "))
    if name in em:
            print("Name: {}".format(name))
            print("Email: {}".format(email))
            print("")
    else:
        print("Name has not been found")

def addEmail(email):
    name = str(input("Enter a name: "))
    email = str(input("Enter an email address: "))
    em.append(name)
    print("Name and email have been added")
    print("")

def changeEmail(email):
    name = str(input("Enter name: "))
    if name not in email:
            print("name not found")
            return None
    email = str(input("Enter new email address"))
    em.append(name)
    print("")
    

def deleteEmail(email):
    name = str(input("Enter name: "))
    if name not in email:
        print("name not found")
        print("")
        return None
    del em[name]
    print("information deleted")
    print("")
    

def saveEmail(email):
    file = open("EmailAddresses.txt","r")
    names = list(em.keys())
    for i in range(len(names)):
        file.write(names[i] + " " + em[names[i]])
        if len(names)-i > 1:
            file.write("\n")
    print("information saved")
    

def read(email):
    file = em.read()
    for i in range(len(file)):
        ent = file[i].split(" ")
    return email

def main():
    email = open("EmailAddresses.txt")
    run = True
    while run:
        menu()
        opt = int(input("Enter the command you'd like to use: "))
        if opt == 1:
                  lookUpEmail(em)
        if opt == 2:
                  addEmail(em)
        if opt == 3:
                  changeEmail(em)
        if opt == 4:
                  deleteEmail(em)
        if opt == 5:
                  saveEmail(em)
                  run = False
main()
